from flask import Flask, request, jsonify, send_file
import json

# UPLOAD_FOLDER = 'mysite/src/images/'
with open('mysite/api.json', 'r') as file:
    data = json.load(file)

app = Flask(__name__)
json_db = data

# GET ROUTE
@app.route('/', methods=['GET'])
def get_db():
    return jsonify(json_db)

@app.route('/images', methods=['GET'])
def get_images():
    return jsonify(json_db["images"])

@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify(json_db["videos"])

@app.route('/audios', methods=['GET'])
def get_audios():
    return jsonify(json_db["audios"])

@app.route('/images/upload', methods=['POST'])
def upload_images():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    file.save('mysite/src/images/' + file.filename)
    return jsonify({'message': 'File successfully uploaded'}), 201

@app.route('/videos/upload', methods=['POST'])
def upload_videos():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    file.save('mysite/src/videos/' + file.filename)
    return jsonify({'message': 'File successfully uploaded'}), 201

@app.route('/audios/upload', methods=['POST'])
def upload_audios():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    file.save('mysite/src/audios/' + file.filename)
    return jsonify({'message': 'File successfully uploaded'}), 201

@app.route('/images/api', methods=['POST'])
def post_image():
    data["images"].append(request.form)

    json_object = json.dumps(request.form['file'], indent=4)
    with open("mysite/api1.json", "w") as outfile:
            outfile.write(json_object)

    return jsonify({'message': 'Updated API'}), 201

# GET ROUTE
@app.route('/images/<file_name>')
def get_image(file_name):
    image_path = f'src/images/{file_name}'
    return send_file(image_path, mimetype='image/jpeg')


# GET ROUTE
@app.route('/audios/<file_name>')
def get_audio(file_name):
    audio_path = f'src/audios/{file_name}'
    return send_file(audio_path, mimetype='audio/mp3')


# GET ROUTE
@app.route('/videos/<file_name>')
def get_video(file_name):
    video_path = f'src/videos/{file_name}'
    return send_file(video_path, mimetype='video/mp4')