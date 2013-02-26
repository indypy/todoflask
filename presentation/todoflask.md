% Todo-be-do-be-do with Flask
% Pradeep Gowda -- @btbytes
% Feb 28, 2013

# Flask

  * Created by Armin Ronacher
  * Started out as an April fool's joke
  * 

# Flask Origins

# When to Flask?

  * Think Hip.
  * Think App vs Application
  * Think standalone Service
  * Think web apps interacting over HTTP vs lib calls.



# Hello world

~~~~{.python}
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run()
~~~~

# A more 'complete' webapp

~~~~{.python}
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
~~~~

----

Where `index.html` is:

~~~~{.html}

~~~~



----

### 3...

----
  
### 2...

---

### Get on with it
  
----

## EEK! A hoo-man

----

I am a machine, you insensitive clod!

----

What now?

----
