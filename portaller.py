import bottle, os
from bottle import template, static_file

app = application = bottle.Bottle()
copyright = '2015'

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@app.route('/')
def index():
	return template('index', dict(error = None, year = copyright))


@app.route('/beta')
def index():
	return template('beta', dict(error = None, year = copyright))


@app.route('/setup')
def index():
	return template('setup', dict(error = None, year = copyright))

@app.route('/status')
def index():
	snipid = '/var/tmp/sniproxy.pid'
	check = os.path.isfile(snipid)
	sni = ''
	if check == True:
		with open(snipid, 'r') as fl:
			sni = fl.readline()
	else:
		sni = 'proxy dead'

	la = os.popen("uptime | awk -F'[a-z]:' '{ print $2}'").read()

	with open("./connections.txt", 'r') as fl:
		connections = fl.readline()

	return template('status', dict(error = None, year = copyright, sni = sni, la = la, connections = connections))
