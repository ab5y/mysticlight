from flask import Flask, request, session, g, redirect, url_for, \
				abort, render_template, flash

# Configuation
# USERNAME = 'admin'
# PASSWORD = 'default'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def hello():
	print 'Reaches here'
	return render_template('home.html')

if __name__ == '__main__':
	app.run()