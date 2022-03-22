import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError


# Dropbox uygulamasını kurma ve Token alma

DROPBOX_ACCESS_TOKEN = 'sl.BERmUAWHUCBduRQ15CRkYaXHggMeNdP85vb7Ur5U0o3LbVGDJHcub1sfXplqd9l3GRb9omDhKI-bLBqQ0NISyxeIXWHJ0pMtqip1u9wfl1bk1XKgY5FPK4fJ4CdfxT7D6KueGl4'



# Dropbox API'sine Bağlanma


def dropbox_connect():
    """Create a connection to Dropbox."""

    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx


# Dropbox klasöründeki dosyaların listesini alma


def dropbox_list_files(path):
    """Return a Pandas dataframe of files in a given Dropbox folder path in the Apps directory.
    """

    dbx = dropbox_connect()

    try:
        files = dbx.files_list_folder(path).entries
        files_list = []
        for file in files:
            if isinstance(file, dropbox.files.FileMetadata):
                metadata = {
                    'name': file.name,
                    'path_display': file.path_display,
                    'client_modified': file.client_modified,
                    'server_modified': file.server_modified
                }
                files_list.append(metadata)

        df = pd.DataFrame.from_records(files_list)
        return df.sort_values(by='server_modified', ascending=False)

    except Exception as e:
        print('Error getting list of files from Dropbox: ' + str(e))



dropbox_list_files('sl.BERmUAWHUCBduRQ15CRkYaXHggMeNdP85vb7Ur5U0o3LbVGDJHcub1sfXplqd9l3GRb9omDhKI-bLBqQ0NISyxeIXWHJ0pMtqip1u9wfl1bk1XKgY5FPK4fJ4CdfxT7D6KueGl4')