from tkinter import *
import tkinter as tk
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
from user_panel import FilePanel
import webbrowser

root=Tk()
root.geometry("600x400")
root.title("DropBox Giriş")

APP_KEY = "g1otg87k4rv07zy"
APP_SECRET = "bvs1puw0vb425w0"
auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
Text_Area=StringVar()

def dropbox_link():
    
    authorize_url = auth_flow.start()
    webbrowser.open_new(authorize_url)
def dropbox_login():
    auth_code=Text_Area.get()
    try:
        oauth_result = auth_flow.finish(auth_code)
    except Exception as e:
        print('Error: %s' % (e,))
        exit(1)

    with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
        #dbx.users_get_current_account()
        print("Successfully set up client!")
        FilePanel(root,dbx)

button_link=Button(root,text="Open to get authorization code",command=dropbox_link,bg="green")
button_link.pack(anchor=CENTER,pady=20)


Input=Entry(root,textvariable=Text_Area,width=20)
Input.pack(anchor=CENTER,pady=2)

button_login=Button(root,text="Login",command=dropbox_login,bg="green")
button_login.pack(anchor=CENTER,pady=10)


root.mainloop()