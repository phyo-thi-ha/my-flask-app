from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, This is free python hosting by Phyo Thiha!'

if __name__ == '__main__':
    app.run()