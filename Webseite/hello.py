from flask import jsonify, Flask, request, render_template
import json
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/postchange', methods=['POST', 'GET'])
def postchange():
    data = request.json
    print(data)

    data = json.dumps(data)
    
    with open('./changes.txt', 'w') as currentfile:
        currentfile.write(data)
    
    return data

if __name__ == '__main__':
    app.run(debug=True,port=5000)