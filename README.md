# SERVER FOR GALLERY ANDROID APP
# GITHUB: https://github.com/cdghhhiilnnotu/Gallery-Android

## Android Gallery App Data Structure at src/
  ### Images:
    * Folder: Images/
    * File Format: Supported image formats (e.g., JPEG, PNG, GIF)
  ### Videos:
    * Folder: Videos/
    * File Format: Supported video formats (e.g., MP4, MOV, AVI)
    * Themes:
      ** Folder: themes/
      ** File Format: Supported image formats (e.g., JPEG, PNG, GIF)
  ### Audio:
    * Folder: Audios/
    * File Format: Supported audio formats (e.g., MP3, WAV, AAC)
    * Themes:
      ** Folder: themes/
      ** File Format: Supported image formats (e.g., JPEG, PNG, GIF)
  ### Note:
    * The folder structure may vary depending on the theme of the Gallery (e.g., dogs, cats, animals, music, etc.).
    * In this example, the theme is sports.

## Including servermain File for Launching Server on PythonAnywhere:
  ### Functionality:
    * Server Creation: Utilizes Flask to create a server.
    * Data Acquisition: Reads api.json file to retrieve and pass data.
    * GET API Methods: Provides GET API methods for images, videos, audio, and aggregation.
    * POST File Methods: Includes POST file methods and APIs for files (currently non-functional).
    * File Access: Enables access to files within the src directory (requires creating this directory structure in PythonAnywhere).
  ### Additional Notes:
    * The servermain file likely contains the main server code for the application.
    * The api.json file is likely a JSON-formatted file that stores data for the API.
    * The GET API methods provide endpoints for retrieving data from the server.
    * The POST file methods are intended for uploading and managing files on the server.
    * The file access functionality allows the server to access and process files stored in the src directory on PythonAnywhere.

## SQLs Folder:
  ### Functionality:
    * Database Table Creation: Establishes the necessary tables in the database.
    * Data Initialization: Populates the database with initial data from the src/ directory.
    * Database Tables: Includes three tables: Images, Videos, and Audios.
    * Table Structure: Each table consists of the following columns:
      ** id: Unique identifier for each record
      ** name: Name of the image, video, or audio file
      ** view: Number of views for the file
      ** download_count: Number of times the file has been downloaded
      ** url: URL of the file
      ** theme_url: URL of the theme image for the file (if applicable)
      ** description: Description of the file
  ### Additional Notes:
    * The SQLs folder likely contains SQL scripts or code for managing the database.
    * The data initialization process involves inserting data from the src/ directory into the corresponding tables in the database.
    * The table structure defines the attributes and data types for each field in the database tables.

## Database Connection in SQL Server:
  ### Functionality:
    * Database Connection through dbmain.py: Establishes a connection to the SQL Server database using the dbmain.py file.
    * Data Conversion to JSON: Converts retrieved data from the database into JSON format.
  ### Additional Notes:
    * The dbmain.py file likely contains functions or code for connecting to and interacting with the SQL Server database.
    * The data conversion process involves transforming the data structures retrieved from the database into a JSON format suitable for consumption by web applications or APIs.
  ### Other Files and Functionality:
    * Media File Name Editing: Certain files handle operations related to modifying the filenames of media files within the src directory.
    * Image Compression: Functionality for compressing images likely exists to optimize file size and storage.
    * Request Testing: Mechanisms for testing and validating various requests are likely implemented.

## Repository as a Media File Server:
  * The repository functions not only as a code storage location but also serves as a media file server. 
  * This suggests that the repository contains both source code files and media assets (e.g., images, videos, audio) for the associated application or project.
