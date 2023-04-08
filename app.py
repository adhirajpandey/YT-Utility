from flask import Flask, render_template, request, jsonify
from functions import html2csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/watch-later')
def wl():
    return render_template('wl.html')

@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        postdata = request.get_json(force=True)
        input_html = postdata['user_html']

        res = html2csv(input_html)

        a = "asas"

        d = {"ans": res}
        
        return jsonify(d)
        

@app.route('/subscription')
def subs():
    return render_template('subs.html')

if __name__ == '__main__':
    app.run(debug=True)
