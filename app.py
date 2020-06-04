from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def minha_api():
    return jsonify({'nome':'Rafael'})

if __name__ == '__main__':
    app.run(debug=True)