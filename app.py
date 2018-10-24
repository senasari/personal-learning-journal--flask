from flask import Flask, render_template, request, redirect, url_for

import forms
import models


DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'lf;ksd;flkajsd'


@app.route('/')
@app.route('/entries', methods=('GET', 'POST'))
def index():
    posts = models.Post.select().limit(100)
    return render_template('index.html', stream=posts)


@app.route('/details')
def details():
    posts = models.Post.select().limit(100)
    return render_template('detail.html', stream=posts)


@app.route('/entries/edit')
def edit():
    form = forms.PostForm()
    posts = models.Post.select()
    # TODO: for editing is there any special method in databases/peewee?
    return render_template('edit.html', stream=posts)  # send the post/posts for giving the input a default value.

# models.Post


@app.route('/entries/add', methods=('GET', 'POST'))
def add():
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.create(
            # todo: 1. i can create new posts from console with string
            # todo: 2. i can not create a new post within this method even with string
            title=form.title.data,
            date=form.date.data,
            timespent=form.timespent.data,
            content=form.content.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT, host=HOST)
    # my_input = input('What do you want the title to be?')
    # models.Post.create(
    #     title=my_input,
    #     date="2018-10-10",
    #     timespent="3",
    #     content="some content",
    #     resources="it doesnt matter"
    # )
    # for post in models.Post.select():
    #     print(post.title)

