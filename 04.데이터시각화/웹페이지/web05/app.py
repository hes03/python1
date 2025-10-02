from flask import Flask, render_template, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
plt.rc('font', family = 'Malgun Gothic')
plt.rc('font', size = 10)
plt.rc('axes', unicode_minus = False )

app = Flask(__name__, template_folder='temp')

@app.route('/')
def health():
    return render_template('health.html')

@app.route('/health/graph')
def health_graph():
    plt.rc('font', size = 6)
    df = pd.read_csv('c:/python/04.데이터시각화/프로젝트/06.행정구역/인구수별 공공의료기관수.csv')
    word = request.args['word']
    filt = df['시도군구'].str.contains(word)
    df = df[filt]
    if len(df)>10:
        df = df[:10]

    #plt.figure(figsize=(13, 8))
    plt.title('지역별 공공의료기관 수', size=15)
    plt.barh(df['시도군구'], df['count'])
    # for idx, c in enumerate(df['count']):
    #         plt.text(c+0.2, idx, c, va='center')
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/health/data')
def health_data():
    page = int(request.args['page'])
    size = int(request.args['size'])
    word = request.args['word']

    df = pd.read_csv('c:/python/04.데이터시각화/프로젝트/06.행정구역/인구수별 공공의료기관수.csv')
    filt = df['시도군구'].str.contains(word)
    df = df[filt]

    start = (page-1) * size
    end = page * size
    df2 = df[start:end]

    count = len(df)
    table = df2.to_html(index=True, classes='table table-striped table-bordered table-hover')
    
    data = {'count':count, 'table':table}
    return data

if __name__=='__main__':
    app.run(port=5001, debug=True)