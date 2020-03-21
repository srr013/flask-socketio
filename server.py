from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
	app.logger.debug("Application started")
	return render_template('index.html')

@socketio.on('connect_event')
def log_message(msg):
	app.logger.warn("message %s" % msg)













if __name__ == '__main__':
    socketio.run(app)

