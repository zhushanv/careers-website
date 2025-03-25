
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Scientist',
    'location': 'Bangalore, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id':2,
    'title': 'Frontend Developer',
    'location': 'Mumbai, India', 
    'salary': 'Rs. 12,00,000'
  },
  {
    'id':3,
    'title': 'Backend Engineer',
    'location': 'Delhi, India',
    'salary': 'Rs. 14,00,000'
  },
  {
    'id':4,
    'title': 'Machine Learning Engineer',
    'location': 'Hyderabad, India',
    'salary': 'Rs. 18,00,000'
  }
]

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
