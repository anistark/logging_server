import psutil
import os
import models
import json
from flask import Flask, render_template, Response
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('print_logs.html', data=models.read_logs())


@app.route('/stats')
def stats():
    process = psutil.Process(os.getpid())
    data = dict(
        cpu_times=psutil.cpu_times(),
        memory=process.memory_info(),
        disk_usage=psutil.disk_usage('/')
    )
    return render_template('stats.html', data=data)


@app.route('/stats_refresh')
def stats_refresh():
    process = psutil.Process(os.getpid())
    data = dict(
            cpu_times=psutil.cpu_times(),
            memory=process.memory_info(),
            disk_usage=psutil.disk_usage('/')
    )
    return json.dumps({'status':'OK','data':data})
