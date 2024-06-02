from flask import Flask, jsonify
from dbmain import *
from mutils import *

app = Flask(__name__)
db = MultimediaDB()

# GET ROUTE
@app.route('/', methods=['GET'])
def get_db():
    return jsonify(db.db_json)

@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify(db.db_json['videos'])

@app.route('/images', methods=['GET'])
def get_images():
    return jsonify(db.db_json['images'])

@app.route('/audios', methods=['GET'])
def get_audios():
    return jsonify(db.db_json['audios'])



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)