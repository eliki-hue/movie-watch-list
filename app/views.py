from multiprocessing.context import ForkProcess
from turtle import title
from flask import render_template
from app import app
from .requests import get_movies

# views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie

    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to the Best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies)


