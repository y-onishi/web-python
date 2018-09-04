from flask import Flask, render_template
from dbsetting import LinkRecord, session
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def hello_world():
    articles = session.query(LinkRecord).all()
    return render_template('index.html',articles = articles)

if __name__ == '__main__':
    app.run()
