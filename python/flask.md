Flask is a microframework for web development in Python.


```python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

```
Now let's understand what's happening here:
    We import our Flask dependency
    We create an instance of a Flask App. The argument passed into the Flask instantiator (__name__) evaluates to a string that "names" the Flask App. When run from the command line, __name__ == "__main__". You can set the first argument to whatever you want.
    We set up a route / on our App that executes the hello() function immediately below it when that route is visited. Note that the function must return a string or a rendered template.

