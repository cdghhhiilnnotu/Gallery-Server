import pyodbc, json
from helpers.mutils import *

class MultimediaDB:

    def __init__(self, server_name="Duong-NT027\SQLEXPRESS", database_name="MultimediaApp"):
        self.conn = pyodbc.connect("Driver={SQL Server};"
                      f"Server={server_name};"
                      f"Database={database_name};"
                      "Trusted_Connection=yes;")
        self.cursor = self.conn.cursor()
        self.db_json = self.get_json_db()

    def get_json_videos(self):
        self.cursor.execute('SELECT * FROM Videos')
        video_list = self.cursor.fetchall()
        video_json = listDict(video_list, ['video_id', 'video_name', 'view_count', 'upload_date', 'download_count', 'video_url', 'theme_url', 'video_description'])
        return video_json

    def get_json_images(self):
        self.cursor.execute('SELECT * FROM Images')
        images_list = self.cursor.fetchall()
        images_json = listDict(images_list, ['image_id', 'image_name', 'view_count', 'upload_date', 'download_count', 'image_url', 'theme_url', 'image_description'])
        return images_json

    def get_json_audios(self):
        self.cursor.execute('SELECT * FROM Audios')
        audios_list = self.cursor.fetchall()
        audios_json = listDict(audios_list, ['audio_id', 'audio_name', 'view_count', 'upload_date', 'download_count', 'audio_url', 'theme_url', 'audio_description'])
        return audios_json
    
    def get_json_db(self):
        db_json = {}
        db_json['audios'] = self.get_json_audios()
        db_json['images'] = self.get_json_images()
        db_json['videos'] = self.get_json_videos()
        json_object = json.dumps(db_json, indent=4)
 
        # Writing to sample.json
        with open("api1.json", "w") as outfile:
            outfile.write(json_object)
        return db_json


