from flask import Flask 

app=Flask(__name__)

@app.route('/')
def modification_one():
	return 'modified output'

app.run(port=5000)