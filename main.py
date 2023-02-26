from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'
@app.route('/new')
def funcs():
	#api endpoint to get a list of products rebranded again and again 
app.run(host='0.0.0.0', port=8080)
