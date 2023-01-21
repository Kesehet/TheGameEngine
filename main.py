from flask import Flask, render_template, request


#This uses Flask to initialise the flask application, and designates the static folder as -  well, the static folder
app = Flask('app')
app.static_folder = 'static'


#This renders the homepage, the base request for the URL when no specific page is defined.
@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':      
      data = {}
      return render_template('index.html', data=data)

#this is the route for the play area ... we keep playArea.html until we are sure we want to make a release after which we can move this route to a different html template      
@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'GET':      
      data = {}
      return render_template('playArea.html', data=data)
      
#this runs the application
app.run(host='0.0.0.0', port=8080,debug=True)


