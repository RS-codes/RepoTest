from flask import Flask 

app=Flask(__name__)

@app.route('/')
def hello_world():
	return 'Tested OK'

app.run(port=5000)