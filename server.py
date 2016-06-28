import models
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('print_logs.html', data=models.read_logs())


@app.route('/stats')
def stats():
    return render_template('stats.html', data=models.get_stats())
