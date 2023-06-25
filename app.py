from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def jobs_load_from_db():
    with engine.connect() as conn:
      query = text('SELECT * FROM jobs')
      results = conn.execute(query)

      jobs = []
      for row in results.all():
        row_dict = row._asdict()
        jobs.append(row_dict)
      return(jobs)
    


@app.route('/')
def home():
    jobs = jobs_load_from_db()
    return render_template('home.html', jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)