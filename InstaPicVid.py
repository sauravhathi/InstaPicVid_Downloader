import instaloader
from instaloader import Post
from tkinter import *
import subprocess
from tkinter import ttk
import tkinter.messagebox
import urllib.request

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

root = Tk()

#Windows Title
root.title("Instagram Images/Videos Downloader")

#windows width=800 and height=500 fixed
root.geometry('800x500')

#windows resizable disable
root.resizable(width=False, height=False)

#windows icon set
p1 = PhotoImage(file = 'instagram_icon.png')

# Setting icon of master window
root.iconphoto(False, p1)


# def tru():
#     directory = "./download_post"
#     files_in_directory = os.listdir(directory)
#     filtered_files = [file for file in files_in_directory if file.endswith((".txt", ".xz"))]
#     for file in filtered_files:
#         path_to_file = os.path.join(directory, file)
#         os.remove(path_to_file)

#variables
insta_Url= 'https://www.instagram.com/p/'
insta_Url1='https://www.instagram.com/tv/'
insta_Id='https://www.instagram.com/'
btColor= 'black'
borderWidth='0'
fontStyle=('', 10, 'bold')
fontStyle1=('', 13, 'bold')
fontSmall= ('', 8)
cursor="hand2"


# https://www.instagram.com/p/CUNM_lzvKrD/

#Function to download images and videos(Reels)
def insta_pic_vid():

    def show1():

        #folder name
        target= 'download_post'

        if connect() == True:
            try:
                url = input_field.get()
                if insta_Url==url[0:len(url) - 12]:
                    my_listbox.insert(END,"<< "+str(url))
                    shorted_url = url[28:len(url) - 1]

                elif insta_Url1==url[0:len(url) - 12]:
                    my_listbox.insert(END,"<< "+str(url))
                    shorted_url = url[29:len(url) - 1]
                
                #save_metadata=true, then Instaloader function also download post description()
                i = instaloader.Instaloader(save_metadata=False, post_metadata_txt_pattern='')
                post = Post.from_shortcode(i.context, shorted_url)
                i.download_post(post, target=target)

                #open downloaded path
                subprocess.Popen('explorer "{0}"'.format(target))
                # tru()

                tkinter.messagebox.showinfo("Downloading", "Downloading Successful")
            
            except Exception:
                url=input_field.get()
                if url == "" or insta_Url != url[0:len(url) - 12]:
                    tkinter.messagebox.showerror("Invalid Url","Input cannot be blanked and Inavid Url")

        else:
            tkinter.messagebox.showerror("Connection Status", "No Internet!\nPlease Connect to Internet")

    f2=Frame(bg="#ECE5F0")
    f2.place(x=0, y=0, width=800, height=500)

    input_url = ttk.Label(f2, text="Enter Post Url:", background="#ECE5F0" ,  font=fontStyle)
    input_url.pack(fill='x', padx=200)

    input_field = ttk.Entry(f2, font=(20), width=70)
    input_field.pack(padx=200)


    b3 = Button(f2, text='Download', cursor=cursor, borderwidth=borderWidth, relief="groove" , activebackground="blue", activeforeground="white",bg=btColor, fg='white', font=fontStyle1, command=show1)
    b3.pack(pady=10)

    input_url = ttk.Label(f2, text="Url History:", background="#ECE5F0" ,  font=fontStyle)
    input_url.pack(fill='x', padx=200)

    my_listbox = Listbox(f2, height=20, width=66)
    my_listbox.pack()

    b4=Button(f2, text="Back", cursor=cursor, borderwidth=borderWidth, bg=btColor, activebackground="blue", activeforeground="white", fg='white', font=fontStyle1, command=home)
    b4.pack(side=RIGHT, padx=20)
    
#Function to download unsta user's profile picture
def insta_profile_image():

    def show2():
        if connect() == True:

            url1 = input_field1.get()

            try:

                if url1=="":
                    raise Exception

                elif len(url1) > 26 and url1.find(insta_Id, 0, 26) == 0:
                    temp=url1.replace(insta_Id,"")
                    shorted_url1=temp[0:-1]
                    my_listbox1.insert(END,"<< "+str(shorted_url1))

                else:
                    shorted_url1=url1
                    my_listbox1.insert(END,"<< "+str(url1))
                

                #save_metadata=true, then Instaloader function also download post description()
                j = instaloader.Instaloader(save_metadata=False, post_metadata_txt_pattern='')
                j.download_profile(shorted_url1, profile_pic_only=True)

                #open downloaded path
                subprocess.Popen('explorer "{0}"'.format(shorted_url1))
                
                # tru()
                tkinter.messagebox.showinfo("Downloading", "Downloading Successful")
            
            except Exception:
                tkinter.messagebox.showerror("Blanked","Input cannot be blanked and Inavid Url")

        else:
            tkinter.messagebox.showerror("Connection Status", "No Internet!\nPlease Connect to Internet")

    f3=Frame(bg="#ECE5F0")
    f3.place(x=0, y=0, width=800, height=500)

    input_url = ttk.Label(f3, text="Enter Username:", background="#ECE5F0" ,  font=fontStyle)
    input_url.pack(fill='x', padx=200)


    input_field1 = ttk.Entry(f3, font=(20), width=70)
    input_field1.pack(padx=200)


    b5 = Button(f3, text='Download', cursor=cursor, relief="groove" , borderwidth=borderWidth, activebackground="blue", activeforeground="white", bg=btColor, fg='white', font=fontStyle1, command=show2)
    b5.pack(pady=10)

    input_url = ttk.Label(f3, text="Url History:", background="#ECE5F0" ,  font=fontStyle)
    input_url.pack(fill='x', padx=200)

    my_listbox1 = Listbox(f3, height=20, width=66)
    my_listbox1.pack()

    b6=Button(f3, text="Back", cursor=cursor, borderwidth=borderWidth, bg=btColor, activebackground="blue", activeforeground="white", fg='white', font=fontStyle1, command=home)
    b6.pack(side=RIGHT, padx=20)

#Home Page Function
def home():
    f1=Frame(bg="#ECE5F0")
    f1.place(width=800, height=500)

    des=ttk.Label(f1, background="#ECE5F0" , text="Download Instagram Video, Photos, DP, Stories, IGTV & Reels", anchor=CENTER, font=('', 15, 'bold'),)
    des.pack(fill='x', pady=130)

    fB3=('', 15, 'bold')

    b1=Button(f1, text="Picture & Video", cursor=cursor, width=20, bg=btColor, activebackground="blue", activeforeground="white", borderwidth=borderWidth, fg='white', font=fB3, command=insta_pic_vid)
    b1.place(x=125, y=200)

    b2=Button(f1, text="Profile Picture", cursor=cursor, width=20, bg=btColor, activebackground="blue", activeforeground="white", borderwidth=borderWidth, fg='white', font=fB3, command=insta_profile_image)
    b2.place(x=410, y=200)

    version=ttk.Label(f1, text="Version: 1.0.0", background="#ECE5F0" ,  font=fontSmall)
    version.pack(anchor = "s", side = "left")

    qut=ttk.Label(f1, text="Download Instagram Video, Photos, DP, Stories, IGTV & Reels", background="#ECE5F0" , anchor=CENTER, font=fontSmall)
    qut.pack(anchor = "s", side = "right")


#home function call
home()

#root. mainloop() is a method on the main window which we execute when we want to run our application
root.mainloop()
