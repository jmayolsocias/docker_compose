from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   
    return jsonify(hello='world') # Returns HTTP Response with {"hello": "world"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
