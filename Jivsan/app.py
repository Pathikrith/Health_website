from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/booking')
def booking():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
