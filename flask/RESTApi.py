from flask import Flask, redirect, url_for, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/input')
def input():
     return (render_template('/frontend/index.html'))


@app.route('/')
def root():
    return redirect('input')

@app.route('/submit',methods = ['POST'])
def submit():
    if request.method == 'POST':
      text = request.form['entry']
      sentiment = TextBlob(text).sentiment.polarity
      return redirect(url_for('show', name = sentiment))
  

@app.route('/show/<name>', methods = ['GET'])
def show(name):
    nm = request.args.get('entry')
    return redirect(url_for('success', name = name))

if __name__ == '__main__':
   app.run(debug = True)