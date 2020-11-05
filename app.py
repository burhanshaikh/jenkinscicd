from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Hello World2.0 from Python Flask!'

app.run(host='0.0.0.0', port=5000)
