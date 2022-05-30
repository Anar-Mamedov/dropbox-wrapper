import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError
from psutil import users

# Dropbox uygulamasını kurma ve Token alma

DROPBOX_ACCESS_TOKEN = 'sl.BIjZ_BNoRGpRsJqED8oMWz7Mp9D3AIf4AnkXwDY4bRvnSyTqwgNn-X8xiN683JJ0zhXqnAZ4p9-mX67Gq-axFSbsRkVx43e6hdgjSDp5aZqUGSf8GWqt4LfzJ6uvQU6Iord5Xb8'


# Dropbox API'sine Bağlanma


def dropbox_connect():
    """Create a connection to Dropbox."""

    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx


# Dropbox'tan dosya indirme


def dropbox_download_file(dropbox_file_path, local_file_path):
    """Download a file from Dropbox to the local machine."""

    try:

        dbx = dropbox_connect()

        with open(local_file_path, 'wb') as f:

            metadata, result = dbx.files_download(path=dropbox_file_path)
            f.write(result.content)

    except Exception as e:
        print('Error downloading file from Dropbox: ' + str(e))


dropbox_download_file("/Documents/projeno_12.txt", "/Users/anarmammadov/Desktop/projeno_12.txt")