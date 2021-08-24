from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    current_year = datetime.now().year
    return render_template('index.html',  current_year=current_year)


@app.route('/dashboard')
def dashboard():
    current_year = datetime.now().year
    return render_template('dashboard.html', current_year=current_year)


if __name__ == '__main__':
    app.run(debug=True)