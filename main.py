from flask import Flask, redirect, request, render_template_string
nm = '''
<!DOCTYPE html>
<html>
<head>
    <title>Text Entry Form</title>
</head>
<body>
    <h1>Text Entry Form</h1>
    <form action="https://url-shortr.chingsang.repl.co/api" method="post">
        <label for="text">Enter real url:</label>
        <input type="text" name="text" id="text">
				<input type="hidden" name="current_url" value="{{ request.url }}">
        <input type="submit" value="Submit">
    </form>
</body>
</html>

'''
app = Flask('app')
dict = {'yt':'https://www.youtube.com'}
@app.route('/')
def hello_world():
  return 'Hello, World! main page of url shortener,<br> to generate new url shortening go to url.com/your url, then create by pasting your url on it , and share your url'


@app.route('/api', methods=['POST'])
def text_entry():
	# Read the text data from the request body
	text = request.form['text']
	# Do something with the text data
	current_url = request.form['current_url']
	k = current_url.split('.co/')
	#print('current url:',current_url)
	dict[k[1]] = text
	#print('successfully inserted value ',str(dict[k[1]]),' to ',str(text))
	# Return a response
	return redirect(dict[k[1]])

@app.route('/<new_name>')
def router(new_name):
	if new_name in dict:
		return redirect(dict[new_name])
	else:
		rendered = render_template_string(nm)
		return rendered

app.run(host='0.0.0.0', port=8080)
