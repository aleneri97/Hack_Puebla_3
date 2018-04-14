from flask import Flask, redirect, url_for, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/input')
def input():
     return (""" 
  <!DOCTYPE html>
<html lang="en">
<head>
  <!-- TODO: subir div.mood-->
  <!-- TODO: ponerle diferentes íconos a cada mood -->
  <!-- TODO: hacer texto mood más opaco -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title>T.Beat</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="css/main.css">

</head>
<body>
    <header>
        <h1>T·Beat</h1>
        <p>Lorem Ipsum Dolore</p>
    </header>
    <div class="main">
        <div class="box">
            <p class="text">¿Cómo te sientes?</p>
            <div class="mood-box">
                <div class="mood">
                    <img src="images/happy.jpg" alt="" class="img-responsive">
                </div>
                <div class="mood">
                    <img src="images/happy.jpg" alt="" class="img-responsive">
                </div>
                <div class="mood mood-active">
                    <img src="images/happy.jpg" alt="" class="img-responsive">
                </div>
                <div class="mood">
                    <img src="images/happy.jpg" alt="" class="img-responsive">
                </div>
                <div class="mood">
                    <img src="images/happy.jpg" alt="" class="img-responsive">
                </div>
                <div class="mood">
                    <img src="images/happy.jpg" alt="" class="img-responsive">
                </div>
            </div>
        </div>
        <textarea placeholder="Escribe tu canción..." name="" id="" cols="20" rows="3"></textarea>
        <span class="btn-send">
            <i class="fa fa-paper-plane-o" aria-hidden="true"></i>
        </span>
    </div>


    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
    crossorigin="anonymous"></script>
</body>
</html>
""")


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