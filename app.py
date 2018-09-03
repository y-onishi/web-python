from flask import Flask, render_template
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def hello_world():
    return render_template('index.html',message = 'A')

#    render_template('index.html', message = 'A')
#    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
