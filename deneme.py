import dropbox
from dropbox.files import FolderMetadata


def printListFilesRecursive():
    dbx = dropbox.Dropbox('sl.BENlRODhPbb-OJRmNUvOQGgGHvTGVlDOlWtXP7P7jXDkoiYFoKDIB6Sb_l18XzZGw4jVTJ9YRIChyj3UuyuCFZBIHiVvuR-mm_o6sri7d_dcvEnAbsKfs9Dbtbm0Z_sy_uOyf-Iu')

    # Use recursive=True for scan recursive folder.
    for entry in dbx.files_list_folder('', recursive=True).entries:
        # Use instance FileMetadata for get more information of entry
        if isinstance(entry, dropbox.files.FileMetadata):
            print(entry.path_display)


if __name__ == '__main__':
    printListFilesRecursive()