from flask import Flask

app = Flask(__name__)

@app.route('/')
def minha_api():
    return 'Olá'

if __name__ == '__main__':
    app.run(debug=True)