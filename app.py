from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' :1,
        'title': 'Data analyst',
        'location' : 'Lagos',
        'salary' : '#200 000'
    },
      {
        'id' :2,
        'title': 'Excel analyst',
        'location' : 'Abuja',
        'salary' : '#300 000'
    },
      {
        'id' :3,
        'title': 'Fronttend developer',
        'location' : 'Edo',
        'salary' : '#400 000'
    },
      {
        'id' :4,
        'title': 'Backend developer',
        'location' : 'Lagos',
       
    },
      {
        'id' :5,
        'title': 'Devops engineer',
        'location' : 'Lagos',
        'salary' : '#2 000 000'
    }
    
]


@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)