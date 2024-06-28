USE master;

DROP DATABASE MultimediaApp;

CREATE DATABASE MultimediaApp;

USE MultimediaApp;

CREATE TABLE Videos (
    video_id VARCHAR(20) PRIMARY KEY,
    video_name NVARCHAR(255) NOT NULL,
    view_count INT,
    upload_date DATETIMEOFFSET NOT NULL,
    download_count INT,
    video_url VARCHAR(255),
	theme_url VARCHAR(255),
    video_description NVARCHAR(2000)
);


CREATE TABLE Images (
    image_id VARCHAR(20) PRIMARY KEY,
    image_name NVARCHAR(255) NOT NULL,
    view_count INT,
    upload_date DATETIMEOFFSET NOT NULL,
    download_count INT,
    image_url VARCHAR(255),
	theme_url VARCHAR(255),
    image_description NVARCHAR(2000)
);

CREATE TABLE Audios (
    audio_id VARCHAR(20) PRIMARY KEY,
    audio_name NVARCHAR(255) NOT NULL,
    view_count INT,
    upload_date DATETIMEOFFSET NOT NULL,
    download_count INT,
    audio_url VARCHAR(255),
	theme_url VARCHAR(255),
    audio_description NVARCHAR(2000)
);



