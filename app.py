from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text
from database import load_job_from_db, jobs_load_from_db

app = Flask(__name__)


    


@app.route('/')
def home():
    jobs = jobs_load_from_db()
    return render_template('home.html', jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    JOBS = jobs_load_from_db()
    return jsonify(JOBS)

@app.route('/api/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    return jsonify(job)


if __name__ == '__main__':
    app.run(debug=True)