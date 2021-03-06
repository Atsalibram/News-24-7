from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello World'
    title = 'Home - Welcome to the best News Review Website online'
    return render_template('index.html',message = message)

# views
@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    message = 'Hello World'
    return render_template('news.html',id = news_id)