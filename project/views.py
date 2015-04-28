from project import app
from flask import request

print("views.func")

@app.route('/<path:msg>/')
@app.route('/msg')
@app.route('/')
def index(msg="message"):
    print(msg)
    print(request.args)
    return "Hello  " + msg


# @app.route('/')
# def index2():
#     return "Hello world"

    # user = {'nickname': 'Miguel'}  # fake user
    # posts = [  # fake array of posts
    #     {
    #         'author': {'nickname': 'John'}, 
    #         'body': 'Beautiful day in Portland!' 
    #     },
    #     {
    #         'author': {'nickname': 'Susan'}, 
    #         'body': 'The Avengers movie was so cool!' 
    #     }
    # ]
    # return render_template("index.html",
    #                        title='Home',
    #                        user=user,
    #                        posts=posts)