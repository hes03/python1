from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__, template_folder='temp', static_folder='static')

#감독배우장르추천
@app.route('/soup/data')
def sim_recommend2():
    title = request.args['title']
    df = pd.read_csv('data/movie/tmdb_5000_movies.csv')
    idx = df[df['title']==title].index[0]

    cosine_sim = pickle.load(open('data/movie/cosine_sim2.pickle', 'rb'))
    sim = cosine_sim[idx]

    title_sim = list(enumerate(sim))
    title_sim = sorted(title_sim, key=lambda x:x[1], reverse=True)
    title_sim = title_sim[1:11]
    index = [x[0] for x in title_sim]
    
    from tmdbv3api import Movie, TMDb
    tmdb = TMDb()
    tmdb.api_key='c668cda4cf75bf267ef2aeffa2da0341'
    tmdb.language='ko-KR'
    movie = Movie()

    df = df.loc[index, 'id']
    details = []
    for id in df:
        detail = movie.details(id)
        ko_title = detail['title']
        poster = 'https://image.tmdb.org/t/p/w500' + detail['poster_path']
        soup = detail['soup']
        data = {'title':ko_title, 'poster':poster, 'soup':soup}
        details.append(data)
    return details

#줄거리추천
@app.route('/overview/data')
def sim_recommend():
    title = request.args['title']
    df = pd.read_csv('data/movie/movies.csv')
    idx=df[df['title']==title].index[0]

    cosine_sim = pickle.load(open('data/movie/cosine_sim.pickle', 'rb'))
    sim = cosine_sim[idx]

    sim = list(enumerate(sim))
    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    sim = sim[1:13]
    index = [x[0] for x in sim]
    
    from tmdbv3api import Movie, TMDb
    tmdb = TMDb()
    tmdb.api_key='c668cda4cf75bf267ef2aeffa2da0341'
    tmdb.language='ko-KR'
    movie = Movie()

    df = df.loc[index, 'id']
    details = []
    for id in df:
        detail = movie.details(id)
        ko_title = detail['title']
        poster = 'https://image.tmdb.org/t/p/w500' + detail['poster_path']
        overview = detail['overview']
        data = {'title':ko_title, 'poster':poster, 'overview':overview}
        details.append(data)
    return details

@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='영화추천')

@app.route('/overview')
def overview():
    return render_template('index.html', pageName='overview.html', title='줄거리추천')

@app.route('/soup')
def soup():
    return render_template('index.html', pageName='soup.html', title='감독/배우/장르 추천')

if __name__=='__main__':
    app.run(port=5000, debug=True)
