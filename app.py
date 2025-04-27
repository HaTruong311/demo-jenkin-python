from flask import Flask
from controllers import controller_bp

app = Flask(__name__)

# Register the controller blueprint
app.register_blueprint(controller_bp)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
