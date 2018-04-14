T-Beat is a web application that allows users to write a text input, which is then analyzed
using the TextBlob library to find the overall sentiment of the message. This information
alongside the text itself is used to generate a custom song to properly express any given
range of emotions. The given emotion of the piece can be guessed by the application or it
can be suggested by the user.

The following instalation guide assumes a windows environment:

intstall python-midi from https://github.com/vishnubob/python-midi
in console, run tbeat.py ["text"] [sentiment]

create a virtual environment with
pip install virtualenv
venv\Scripts\activate

install flask inside a virtual environment with
pip install flask 

Finally run the application with 
python RESTApi.py
The app should be running in your local host with port 5000.
