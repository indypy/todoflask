from todoflask import *

create_all()

# add an user
u1 = auth.User(username='admin', admin=True, active=True)
u1.email = 'pradeep@btbytes.com'
u1.set_password('secret')
u1.save()

#add another user
u2 = auth.User(username='pgowda', admin=True, active=True)
u2.email = 'pgowda@cs.iupui.edu'
u2.set_password('jaguars')
u2.save()

'''
# add a task
task1 = Task(task="Eat breakfast",  user=u1.id, due=datetime.date(2013,03,01))
task1.save()

# add 'nther task
task2 = Task(task='submit interim project report', user=u2.id, due=datetime.date(2013,04,02))
task2.save()

# Add tags
tag1 = Tag(tag='foo')
tag1.save()
#tag_dup = Tag(tag='foo')
#tag_dup.save()
tag2 = Tag(tag='bar')
tag2.save()
tag3 = Tag(tag='school')
tag3.save()


# add tags to the task
tt1 = TaskTag(task=task1.id, tag=tag1.id)
tt1.save()
tt2 = TaskTag(task=task1.id, tag=tag2.id)
tt2.save()
tt3 = TaskTag(task=task2.id, tag=tag3.id)
tt3.save()

# Query
## Tasks 
print '> tags of task1'
for tg in task1.tags:
	print tg.tag

## User tasks
print '> tasks belonging to user admin'
for ts in task1._user_tasks(u1):
	print ts.task

print '> tasks belonging to user pgowda'
for ts in task1._user_tasks(u2):
	print ts.task
	

## User tags
print '> tags belonging to the user admin'
for tg in tag1._user_tags(u1):
	print tg.tag

'''

