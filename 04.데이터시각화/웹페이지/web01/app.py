from flask import Flask, render_template, send_file
from io import BytesIO
import pandas as pd
df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv', index_col='지원번호')

import matplotlib.pyplot as plt

#한글설정
plt.rc('font', family = 'Malgun Gothic')
plt.rc('font', size = 10)
plt.rc('axes', unicode_minus = False )

app = Flask(__name__, template_folder='templates')

@app.route('/graph1') #학생별 키 막대그래프
def graph1():
    name = df['이름']
    height = df['키']

    plt.figure(figsize=(10, 5))
    plt.bar(name, height, color='pink', ec='purple')
    plt.ylim(150, 210)
    plt.xticks(name, rotation=45, size=10, color='purple')
    for idx, h in enumerate(height):
        plt.text(idx, h+1, h, ha='center', color='purple', size=10)
    
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph2')
def graph2(): #학생별 평균
    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)
    name = df['이름']
    avg = df['평균']

    plt.figure(figsize=(10, 5))
    plt.bar(name, avg, color='pink', ec='purple')
    plt.ylim(0, 100)
    plt.xticks(name, rotation=45, size=10, color='purple')
    for idx, h in enumerate(avg):
        plt.text(idx, h+1, f'{h:.2f}', ha='center', color='purple', size=10)
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph3')
def graph3(): #학교별 평균키
    group = df.groupby('학교')['키'].mean()
    labels = group.index
    values = group.values

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color='skyblue', ec='lightblue', hatch='..', width=0.5)
    plt.ylim(160, 200)
    plt.xticks(labels, rotation=45, size=10, color='darkblue')
    for idx, value in enumerate(values):
        plt.text(idx, value+1, f'{value:.2f}cm', ha='center', color='darkblue', size=10)
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph4')
def graph4(): #학교별 평균점수
    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)
    group = df.groupby('학교')['평균'].mean()
    label = group.index
    values = group.values

    plt.figure(figsize=(10, 5))
    plt.bar(label, values, color='skyblue', ec='lightblue', hatch='..', width=0.5)
    plt.ylim(0, 100)
    plt.xticks(label, rotation=45, size=10, color='darkblue')
    for idx, value in enumerate(values):
        plt.text(idx, value+1, f'{value:.2f}점', ha='center', color='darkblue', size=10)
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph5')
def graph5(): #SW특기별 학생수
    df['SW특기'] = df['SW특기'].str.capitalize()
    group = df.groupby('SW특기').size()

    labels = group.index
    values = group.values
    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color='skyblue', ec='lightblue', hatch='..', width=0.5)
    plt.ylim(0, 6)
    plt.xticks(labels, rotation=45, size=10, color='darkblue')
    for idx, value in enumerate(values):
        plt.text(idx, value+0.03, f'{value}명', ha='center', color='darkblue', size=10)
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/')
def index():
    return render_template('index.html', title='학생관리')

if __name__=='__main__':
    app.run(port=5001, debug=True)
