from flask import Flask, jsonify, json
from dbmain import *

app = Flask(__name__)
db = MultimediaDB()
json_db = json.load(open('api.json'))

# GET ROUTE
@app.route('/', methods=['GET'])
def get_db():
    return jsonify(json_db)

@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify(json_db['videos'])

@app.route('/images', methods=['GET'])
def get_images():
    return jsonify(json_db['images'])

@app.route('/audios', methods=['GET'])
def get_audios():
    return jsonify(json_db['audios'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)