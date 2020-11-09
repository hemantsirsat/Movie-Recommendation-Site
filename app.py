from flask import Flask, render_template, request, redirect, url_for, session
from scripts.recommend import Recommend
import sys

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        movie_user_like = request.form['movie_user_like']
        session['movie'] = movie_user_like
        return redirect(url_for('movie'))
    return render_template("home.html")

@app.route('/similar_movie',methods=['POST','GET'])
def movie():
    similar_movies = Recommend
    names = similar_movies.show_similar_movies(session['movie'])
    if request.method == 'POST':
        session.clear()
        i=0
        return redirect(url_for('index'))
    return render_template('movie.html',movies = similar_movies.show_similar_movies(session['movie']))

if __name__=='__main__':
    app.run(debug=True,port=5000)