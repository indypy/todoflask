import datetime
from flask import Flask, flash, redirect, request, render_template, url_for
import peewee as pw
import wtforms as wt
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from utils import slugify

DATABASE = {
    'name': 'test.db',
    'engine': 'peewee.SqliteDatabase',
}

DEBUG = True
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)
db = Database(app)
auth = Auth(app, db)

# Models
User = auth.get_user_model()


class Task(db.Model):
    task = pw.TextField()
    user = pw.ForeignKeyField(User)
    created = pw.DateTimeField(default=datetime.datetime.now)
    due = pw.DateField()

    @property
    def tags(self):
        return Tag.select().join(TaskTag).join(Task).where(Task.id == self.id)


class Tag(db.Model):
    tag = pw.TextField(unique=True)


class TaskTag(db.Model):
    task = pw.ForeignKeyField(Task)
    tag = pw.ForeignKeyField(Tag)


# Forms
class TaskForm(wt.Form):
    task = wt.TextField([wt.validators.Required()])
    tags = wt.TextField()
    due = wt.DateField()


# Queries
def user_tasks():
    return Task.select().join(User).where(User.id == auth.get_logged_in_user())


def user_tagged_tasks(tag):
    tagged_tasks = TaskTag.select().join(Tag).where(Tag.tag == tag)
    #XXX:Join jiu jitsu fail.
    tasks = Task.select().join(User).where(
        (User.id == auth.get_logged_in_user()) &
        (Task.id << [t.task for t in tagged_tasks]))
    return tasks


# Views
@app.route("/", methods=['GET'])
@auth.login_required
def home():
    sortby = request.args.get('sortby', 'due')
    if sortby == 'title':
        todos = user_tasks().order_by(Task.task)
    else:
        todos = user_tasks().order_by(Task.due)
    return render_template('todo.html', todos=todos)


@app.route('/add', methods=['POST'])
@auth.login_required
def add_task():
    form = TaskForm(request.form)
    if form.validate():
        tags = [slugify(t) for t in form.tags.data.split(' ')]
        new_task = Task(task=form.task.data,
                        user=auth.get_logged_in_user(),
                        due=form.due.data
                        )
        new_task.save()
        for t in tags:
            try:
                new_tag = Tag.get(tag=t)
            except:
                new_tag = Tag(tag=t)
                new_tag.save()
            tasktag = TaskTag(task=new_task.id, tag=new_tag.id)
            tasktag.save()
        flash("New Task: %s" % (new_task.task))
    else:
        flash("Derp!")
    return redirect(url_for('home'))


@app.route('/del', methods=['POST'])
@auth.login_required
def delete_task():
    tskid = request.form['task']
    #XXX: delete only those tasks belonging to the user
    tskobj = Task.get(Task.id == tskid)
    tskobj.delete_instance()
    query = TaskTag.delete().where(TaskTag.task == tskid)
    query.execute()
    flash("Task deleted.")
    return redirect(url_for('home'))


@app.route("/tag/<tag>", methods=['GET'])
def tag(tag):
    todos = user_tagged_tasks(tag)
    flash("Tasks labeled %s" % (tag, ))
    return render_template('todo.html', todos=todos)


def create_all():
    '''create all the tables'''
    auth.User.create_table(fail_silently=True)
    Task.create_table(fail_silently=True)
    Tag.create_table(fail_silently=True)
    TaskTag.create_table(fail_silently=True)


if __name__ == '__main__':
    create_all()
    app.run(port=5005)
