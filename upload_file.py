import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError


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




# Dropbox'a dosya yükleme


def dropbox_upload_file(local_path, local_file, dropbox_file_path):
    """Upload a file from the local machine to a path in the Dropbox app directory.

    Args:
        local_path (str): The path to the local file.
        local_file (str): The name of the local file.
        dropbox_file_path (str): The path to the file in the Dropbox app directory.

    Example:
        dropbox_upload_file('.', 'test.csv', '/stuff/test.csv')

    Returns:
        meta: The Dropbox file metadata.
    """

    try:
        dbx = dropbox_connect()

        local_file_path = pathlib.Path(local_path) / local_file

        with local_file_path.open("rb") as f:

            meta = dbx.files_upload(f.read(), dropbox_file_path, mode=dropbox.files.WriteMode("overwrite"))

            return meta
    except Exception as e:
        print('Error uploading file to Dropbox: ' + str(e))

dropbox_upload_file('/Users/anarmammadov/Desktop/', 'projeno_12.txt', '/Documents/projeno_12.txt')