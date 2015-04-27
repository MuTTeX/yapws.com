from project import app
from flask import request


@app.route('/<path:msg>/')
# @app.route('/index')
def index(msg):
    print(msg)
    print(request.args)
    return "Hello world"

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