# import the module and all specifications
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
import pandas as pd
from tkinter import filedialog
import pathlib
import dropbox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from dropbox.exceptions import AuthError
import shutil
import io
# create the window and set geometry and title

class FilePanel(Toplevel):
    def __init__(self, master,dbx):
        super().__init__(master = master)
        print(dbx.users_get_current_account())
        #DROPBOX_ACCESS_TOKEN = 'sl.BJ3MNybjz-E9DAQQI-g_4F08dcZ7LLVpYRrDHny4MNJYp3mRSooWG45nkRMmOz0iJUwfC9TYqx2GymhDUTJzlf6Vwdnis0VgH2zC4TBBApYKwED8zz40URECDcXYs39EVIkfPoDpXRIU'
        root=self
        #root=Tk()
        root.geometry("600x400")
        root.title("DropBox'ta Dosya İşlemleri")
        
       # creating the commanding
# function of the button

        
        
        # Dropbox'tan dosya indirme
        def folder_path():
            if os.name=='posix':
                desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
            if os.name=='nt':
                desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            dropbox_folder='dropbox'
            filepath=os.path.join(desktop, dropbox_folder)
            if os.path.exists(filepath):
                return filepath
            else:
                os.makedirs(filepath)
                return filepath
        def temp_path():
            if os.name=='posix':
                desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
            if os.name=='nt':
                desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            dropbox_folder='temp'
            filepath=os.path.join(desktop, dropbox_folder)
            if os.path.exists(filepath):
                return filepath
            else:
                os.makedirs(filepath)
                return filepath
        def dropbox_list_files():    
            try:
                files = dbx.files_list_folder("/Documents").entries
        
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
                if len(files_list)!=0:
                    df = pd.DataFrame.from_records(files_list)
                    return df.sort_values(by='server_modified', ascending=False)
                else:
                    print("No file in dropbox")
        
            except Exception as e:
                print('Error getting list of files from Dropbox: ' + str(e))
        
        
        def dropbox_upload_file(key,local_path, dropbox_file_path):
        
            try:
                key = str.encode(key)
                cipher = AES.new(key, AES.MODE_CBC)
                file = open(local_path, 'rb').read()
                cipher_text = cipher.encrypt(pad(file, AES.block_size))
                
                with open(local_path, 'wb') as kfile:
                    kfile.write(cipher.iv)
                    kfile.write(cipher_text)
                
                local_file_path = pathlib.Path(local_path) / local_path
        
                with local_file_path.open("rb") as f:
        
                    dbx.files_upload(f.read(), dropbox_file_path, mode=dropbox.files.WriteMode("overwrite"))
                return "Dosya Başarıyla Yüklendi"
            except Exception as e:
                print('Error uploading file to Dropbox: ' + str(e))
        T = Text(root, height = 13, width = 80)
        T.place(x=15,y=5)
        
        def getRespondForList():
            T.delete("1.0","end")
            Fact = dropbox_list_files()
            T.insert(tk.END, Fact)
        
        
        
        def getRespondForUpload():
            filepath = filedialog.askopenfilename()
            file = open(filepath, 'r')
            file.close()
            dst=os.path.join(folder_path(),os.path.basename(filepath))
            dst_temp=os.path.join(temp_path(),os.path.basename(filepath))
            if not filepath==dst:
                shutil.copy(filepath, dst)
            shutil.copy(filepath, dst_temp)
            print(dropbox_upload_file("1F61ECB5ED5D6BAF8D7A7068B28DCC8E",dst_temp, '/Documents/'+str(os.path.basename(filepath))))
            os.remove(dst_temp)
        
        
        # set the string variable
        Text_Area=StringVar()
        
        label1 = Label(root,text="İndirilecek Dosyanın Adı")
        label1.place(x=270,y=185)
        # creating the text area
        # we will set the text variable in this
        
        # create a button
        button=Button(root,text="Dosya Yükle",command=getRespondForUpload)
        button.place(x=150,y=210)
        button=Button(root,text="Dosya Listele",command=getRespondForList)
        button.place(x=20,y=210)
        Input=Entry(root,textvariable=Text_Area,width=20)
        Input.place(x=270,y=213)
        
        def dropbox_download_file():
            """Download a file from Dropbox to the local machine."""
            filepath=os.path.join(folder_path(),Input.get())
            try:
                with open(filepath, 'wb') as f:
        
                    metadata, result = dbx.files_download(path="/Documents/"+Input.get())
                    f.write(result.content)
        
                key = str.encode("1F61ECB5ED5D6BAF8D7A7068B28DCC8E")
                with open(filepath, 'rb') as c_text:
                    iv = c_text.read(16)
                    ct = c_text.read()
                cipher = AES.new(key, AES.MODE_CBC, iv)
                pt = unpad(cipher.decrypt(ct), AES.block_size)
                file = open(filepath, 'wb')
                file.write(pt)
                file.close()
        
            except Exception as e:
                print('Error downloading file from Dropbox: ' + str(e))
        button=Button(root,text="Dosya İndir",command=dropbox_download_file)
        button.place(x=470,y=210)

#root.mainloop()


