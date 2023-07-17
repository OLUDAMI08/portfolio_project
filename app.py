from flask import Flask, render_template, jsonify, request
from database import engine
from sqlalchemy import text
from database import load_job_from_db, jobs_load_from_db, add_application_to_db

app = Flask(__name__)


@app.route('/')
def home():
    jobs = jobs_load_from_db()
    return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
    JOBS = jobs_load_from_db()
    return jsonify(JOBS)


@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    return render_template('jobpage.html', job=job)


@app.route('/job/<id>/apply', methods=['post'])
def apply_job_by_id(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html', data=data, job=job)


if __name__ == '__main__':
    app.run(debug=False, port=8000)
