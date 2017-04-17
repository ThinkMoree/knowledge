__author__ = 'Yu'
"""
@app.route() is a decorator, default it only response GET
it binds a function with an url, you can access the function with the url
if the url in route is suffixed by /, if your web url is not suffixed by /,
web browser will redirect to. eg:
@app.route('/hello/'), in web: http://127.0.0.1:5000/hello, it will be redirected to
http://127.0.0.1:5000/hello/
but if the url in route is not suffixed by /, if your web url is suffixed by /,
web browser will not redirect.
eg:
@app.route('/hello'), in web: http://127.0.0.1:5000/hello/,
Error occurs: 404 Not Found.
"""
from flask import Flask, url_for
app = Flask(__name__)
@app.route("/hello")
def hello_world():
    return "hello world"

@app.route("/<username>")
def say_hello(username):
    return "Hi," + username

@app.route("/<int:variable>")
def variable_func(variable):
    return "Result:%d" %(variable*variable)

"""
make url with url_for()
"""
@app.route("/")
def index():
    pass

@app.route("/login")
def login():
    pass

@app.route("/user/<username>")
def profile(username):
    pass

if __name__ == "__main__":
    #app.run()
    #app.run('xx.xx.xx.xx')
    #app.run(debug=True)
    with app.test_request_context():
        print url_for("index")
        print url_for("login")
        print url_for("login", next="/")
        print url_for("profile", username="zhang yu")