from flask import Flask, redirect, url_for, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/')
def root():
    return (""" 
  <html>
   <body>
      
      <form action = "http://localhost:5000/submit" method = "post">
         <p>Write your masterpiece:</p>

         <p><textarea rows = "8" cols = "80" "text" name = "entry" > </textarea></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
      
   </body>
</html>
""")

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