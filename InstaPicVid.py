from ssl import Purpose
import instaloader
from instaloader import Post
from tkinter import *
import subprocess
from tkinter import ttk
import tkinter.messagebox
import urllib.request
import webbrowser


# Testing Purpose links

# https://www.instagram.com/gal_gadot/
# https://www.instagram.com/bollywoodbinge/
# https://www.instagram.com/reel/CWQQoTaJnhS/?utm_source=ig_web_copy_link
# https://www.instagram.com/tv/CWVlkM9tGvi/?utm_source=ig_web_copy_link
# https://www.instagram.com/p/CWVAGDuphAJ/?utm_source=ig_web_copy_link
# https://www.instagram.com/p/CWPy0FyqKir/?utm_source=ig_web_copy_link


root = Tk()

#Windows Title
root.title("InstaPicVid Downloader​")

#windows width=800 and height=500 fixed
root.geometry('800x500')

#windows resizable disable
root.resizable(width=False, height=False)

#windows icon set
p1 = PhotoImage(file = 'instagram_icon.png')

# Setting icon of master window
root.iconphoto(False, p1)

#variables
insta_Url= 'https://www.instagram.com/p/'
insta_Url1='https://www.instagram.com/tv/'
insta_Url_reel='https://www.instagram.com/reel/'
insta_ig='/?utm_source=ig_web_copy_link'
insta_Id=insta_Url[0:len(insta_Url)-2]
btColor= 'black'
borderWidth='0'
fontStyle=('', 11, 'bold')
fontStyle1=('', 15, 'bold')
fontSmall= ('', 8)
cursor="hand2"

#Checking internet connection status
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

#for webbrowser
def callback(event):
    webbrowser.open_new_tab(event)

#Function to download videos, photos ,reels and IGTV
def insta_pic_vid():
    def short(u1):

        char_to_replace = {str(insta_Url_reel): '',str(insta_Url): '',str(insta_Url1): '', str(insta_ig): ''}

        for key, value in char_to_replace.items():

            u1 = u1.replace(key, value)

        return u1

    def show1():

        #folder name
        target= 'Instagram'

        if connect() == True:
            try:
                
                url = inUrl.get()

                if url == '':
                    raise Exception

                elif url.find(insta_ig) != -1:
                    shorted_url = short(url)
                    print("first")
                    my_listbox.insert(END,"<< "+str(shorted_url))

                elif url.find(insta_Url) != -1:
                    shorted_url = url[28:len(url)-1]
                    print("2nd")
                    my_listbox.insert(END,"<< "+str(shorted_url))
                
                elif url.find(insta_Url_reel) != -1:
                    shorted_url = url[31:len(url)-1]
                    my_listbox.insert(END,"<< "+str(shorted_url))

                elif insta_Url1==url[0:len(url) - 12]:
                    shorted_url = url[29:len(url) - 1]
                    my_listbox.insert(END,"<< "+str(shorted_url))

                elif url.find(insta_ig) != -1:
                    shorted_url = short(url)
                    my_listbox.insert(END,"<< "+str(shorted_url))

                else:
                    shorted_url=url
                    my_listbox.insert(END,"<< "+str(shorted_url))
                
                #save_metadata=true, then Instaloader function also download post description()
                i = instaloader.Instaloader(save_metadata=False, post_metadata_txt_pattern='')
                post = Post.from_shortcode(i.context, shorted_url)
                i.download_post(post, target=target)

                #open downloaded path
                subprocess.Popen('explorer "{0}"'.format(target))

                tkinter.messagebox.showinfo("Downloading", "Downloading Successful")
            
            except Exception:

                tkinter.messagebox.showerror("Invalid Url","Input cannot be blanked and Inavid Url")

        else:
            tkinter.messagebox.showerror("Connection Status", "No Internet!\nPlease Connect to Internet")

    f2=Frame(bg="#ECE5F0")
    f2.place(x=0, y=0, width=800, height=500)

    input_url_label = ttk.Label(f2, text="Enter Post Link: ", background="#ECE5F0" ,  font=fontStyle)
    input_url_label.pack(fill='x', padx=200, pady=(20,5))

    inUrl = ttk.Entry(f2, font=(20), width=70)
    inUrl.pack(padx=200, ipady=5)

    b3 = Button(f2, text='Download', cursor=cursor, pady=5, borderwidth=borderWidth, relief="groove" , activebackground="blue", activeforeground="white",bg=btColor, fg='white', font=fontStyle1, command=show1)
    b3.pack(pady=10,padx=200, fill=X)

    input_url_history = ttk.Label(f2, text="Post Link History:", background="#ECE5F0" ,  font=fontStyle)
    input_url_history.pack(fill='x', padx=200, pady=(20,0))

    my_listbox = Listbox(f2, height=10, width=66)
    my_listbox.pack()

    label2 = Label(f2, text="Instruction: ", font=fontStyle, bd=5, fg="black", bg="#ECE5F0")
    label2.place(x=200, y=370)

    TEXT = "1. Copy Instagram Post Link and paste in the input field\n2. Download Photos, Video, Reels and IGTV"

    label2 = Label(f2, text=TEXT, font=('', 10), bd=5, fg="#cd486b", justify=LEFT, bg="#ECE5F0")
    label2.place(x=200, y=400)

    b4=Button(f2, text="Back", cursor=cursor, borderwidth=borderWidth, bg=btColor, activebackground="blue", activeforeground="white", fg='white', font=fontStyle1, command=home)
    b4.pack(anchor = "s", side = "right", padx=(0,20), pady=(0,15))
    
#Function to download unsta user's profile picture
def insta_profile_image():

    def show2():
        if connect() == True:

            url1 = inUrl1.get()

            try:

                if url1=="":
                    raise Exception

                elif len(url1) > 26 and url1.find(insta_Id, 0, 26) == 0:
                    temp=url1.replace(insta_Id,"")
                    shorted_url=temp[0:-1]
                    my_listbox1.insert(END,"<< "+str(shorted_url))

                else:
                    shorted_url=url1
                    my_listbox1.insert(END,"<< "+str(shorted_url))
                

                #save_metadata=true, then Instaloader function also download post description()
                j = instaloader.Instaloader(save_metadata=False)
                j.download_profile(shorted_url, profile_pic_only=True)

                #open downloaded path
                subprocess.Popen('explorer "{0}"'.format(shorted_url))
                
                # tru()
                tkinter.messagebox.showinfo("Downloading", "Downloading Successful")
            
            except Exception:
                tkinter.messagebox.showerror("Blanked","Input cannot be blanked and Inavid Url")

        else:
            tkinter.messagebox.showerror("Connection Status", "No Internet!\nPlease Connect to Internet")

    f3=Frame(bg="#ECE5F0")
    f3.place(x=0, y=0, width=800, height=500)

    input_url_label1 = ttk.Label(f3, text="Enter Username:", background="#ECE5F0" ,  font=fontStyle)
    input_url_label1.pack(fill='x', padx=200, pady=(20,5))

    inUrl1 = ttk.Entry(f3, font=(20), width=70)
    inUrl1.pack(padx=200, ipady=5)

    b5 = Button(f3, text='Download', cursor=cursor, pady=5, borderwidth=borderWidth, relief="groove" , activebackground="blue", activeforeground="white",bg=btColor, fg='white', font=fontStyle1, command=show2)
    b5.pack(pady=10,padx=200, fill=X)

    input_url_history1 = ttk.Label(f3, text="Username History:", background="#ECE5F0" ,  font=fontStyle)
    input_url_history1.pack(fill='x', padx=200, pady=(20,0))

    my_listbox1 = Listbox(f3, height=10, width=66)
    my_listbox1.pack()

    instruction = Label(f3, text="Instruction: ", font=fontStyle, bd=5, fg="black", bg="#ECE5F0")
    instruction.place(x=200, y=370)

    TEXT = "1. You just any Public Instagram account profile URL\n    or Link Address in the input field\n2. Download Profile Picture or DP"

    instruction_Con = Label(f3, text=TEXT, font=('', 10), bd=5, fg="#cd486b", justify=LEFT, bg="#ECE5F0")
    instruction_Con.place(x=200, y=400)

    b6=Button(f3, text="Back", cursor=cursor, borderwidth=borderWidth, bg=btColor, activebackground="blue", activeforeground="white", fg='white', font=fontStyle1, command=home)
    b6.pack(anchor = "s", side = "right", padx=(0,20), pady=(0,15))

def insta_stories():

    def show3():
        USERNAME=username_inUrl2.get()
        PASSWORD=password_inUrl2.get()
        TARGET="stories"

        if connect() == True:

            url2 = inUrl2.get()

            try:

                if USERNAME=="" and PASSWORD=="" and url2=="" :
                    raise Exception

                elif len(url2) > 26 and url2.find(insta_Id, 0, 26) == 0:
                    temp=url2.replace(insta_Id,"")
                    shorted_url=temp[0:-1]
                    my_listbox2.insert(END,"<< "+str(shorted_url))

                else:
                    shorted_url=url2
                    my_listbox2.insert(END,"<< "+str(shorted_url))

                s = instaloader.Instaloader(save_metadata=False)
                s.login(USERNAME, PASSWORD)
                profile = s.check_profile_id(shorted_url)
                #save_metadata=true, then Instaloader function also download post description()
                for story in s.get_stories(userids=str(profile.userid)):
                    for item in story.get_items():
                        s.download_storyitem(item, TARGET)
                #open downloaded path
                subprocess.Popen('explorer "{0}"'.format(TARGET))
                
                # tru()
                tkinter.messagebox.showinfo("Downloading", "Downloading Successful")
            
            except Exception:
                tkinter.messagebox.showerror("Blanked","Input cannot be blanked and Inavid Url")

        else:
            tkinter.messagebox.showerror("Connection Status", "No Internet!\nPlease Connect to Internet")

    f4=Frame(bg="#ECE5F0")
    f4.place(x=0, y=0, width=800, height=500)

    username = ttk.Label(f4, text="Username:", background="#ECE5F0" ,  font=fontStyle)
    username.pack(fill='x', padx=200, pady=(10,5))
    username_inUrl2 = ttk.Entry(f4, font=(20), width=70)
    username_inUrl2.pack(padx=200, ipady=5)

    password = ttk.Label(f4, text="Password:", background="#ECE5F0" ,  font=fontStyle)
    password.pack(fill='x', padx=200, pady=(5,5))
    password_inUrl2 = ttk.Entry(f4, font=(20), width=70)
    password_inUrl2.pack(padx=200, ipady=5)

    input_url_label4 = ttk.Label(f4, text="Profile Username:", background="#ECE5F0" ,  font=fontStyle)
    input_url_label4.pack(fill='x', padx=200, pady=(5,5))
    inUrl2 = ttk.Entry(f4, font=(20), width=70)
    inUrl2.pack(padx=200, ipady=5)

    b6 = Button(f4, text='Download', cursor=cursor, pady=5, borderwidth=borderWidth, relief="groove" , activebackground="blue", activeforeground="white",bg=btColor, fg='white', font=fontStyle1, command=show3)
    b6.pack(pady=10,padx=200, fill=X)

    input_url_history2 = ttk.Label(f4, text="Stories History:", background="#ECE5F0" ,  font=fontStyle)
    input_url_history2.pack(fill='x', padx=200)

    my_listbox2 = Listbox(f4, height=5, width=66)
    my_listbox2.pack()

    instruction = Label(f4, text="Instruction: ", font=fontStyle, bd=5, fg="black", bg="#ECE5F0")
    instruction.place(x=200, y=380)

    TEXT = "1. Enter USERNAME, PASSWORD and Public Instagram\n   account profile URL or Link Address\n2. Download any public profile Stories"

    instruction_Con = Label(f4, text=TEXT, font=('', 10), bd=5, fg="#cd486b", justify=LEFT, bg="#ECE5F0")
    instruction_Con.place(x=200, y=420)

    b7=Button(f4, text="Back", cursor=cursor, borderwidth=borderWidth, bg=btColor, activebackground="blue", activeforeground="white", fg='white', font=fontStyle1, command=home)
    b7.pack(anchor = "s", side = "right", padx=(0,20), pady=(0,15))
#Home Page Function
def home():
    f1=Frame(bg="#ECE5F0")

    des=ttk.Label(f1, background="#ECE5F0" , text="Download Instagram Video, Photos, DP, Stories, IGTV & Reels", anchor=CENTER, font=('Arial Bold', 18))

    fB3=('', 15, 'bold')

    b1=Button(f1, text="Photos", cursor=cursor, width=20, pady=10, bg=btColor, activebackground="blue", activeforeground="white", borderwidth=borderWidth, fg='white', font=fB3, command=insta_pic_vid)

    b2=Button(f1, text="Profile Picture", cursor=cursor, width=20, pady=10, bg=btColor, activebackground="blue", activeforeground="white", borderwidth=borderWidth, fg='white', font=fB3, command=insta_profile_image)

    
    b3=Button(f1, text="Videos", cursor=cursor, width=20, pady=10, bg=btColor, activebackground="blue", activeforeground="white", borderwidth=borderWidth, fg='white', font=fB3, command=insta_pic_vid)

    b4=Button(f1, text="Stories", cursor=cursor, width=20, pady=10, bg=btColor, activebackground="blue", activeforeground="white", borderwidth=borderWidth, fg='white', font=fB3, command=insta_stories)

    lbl = Label(f1, text="Github",background="#ECE5F0", fg='red', highlightthickness=2,highlightbackground = "red", font=('', 20, 'bold'), cursor=cursor)
    lbl.bind("<Button>", lambda e: callback("https://github.com/sauravhathi"))

    version=ttk.Label(f1, text="Version: 1.0.0", background="#ECE5F0" ,  font=fontSmall)

    qut=ttk.Label(f1, text="Download Instagram Video, Photos, DP, Stories, IGTV & Reels", background="#ECE5F0" , anchor=CENTER, font=fontSmall)

    #home page widget method
    des.pack(fill='x', pady=(80,0))
    b1.place(x=125, y=160)
    b2.place(x=410, y=160)
    b3.place(x=125, y=260)
    b4.place(x=410, y=260)
    lbl.place(x=340, y=380)
    version.pack(anchor = "s", side = "left")
    qut.pack(anchor = "s", side = "right")
    f1.place(width=800, height=500)
    

#home function call
home()

#root. mainloop() is a method on the main window which we execute when we want to run our application
root.mainloop()