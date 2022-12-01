from tkinter import *
from pytube import YouTube as yt


root = Tk()
root.geometry("550x250")
root.resizable(0, False)
root.title("Yt downloader")

label_1 = Label(root, text="Downloade videos here ", font="san-serif").pack()
link = StringVar()
label_2 = Label(root, text="ENTER YOUR URL BELOW", font='san-serif').pack()
Entry(root, width=60, textvariable=link).place(x=30, y=80)




def download():
    save_path = "/home/sandy/Desktop"
    url = yt(str(link.get()))
    video = url.streams.first()
    video.download(save_path)
    label_3 = Label(root, text="Downlloaded", font="san-serif 15").pack()
    print(url)


btn = Button(root, text="DOWNLOAD", font="san-serif", bg="green", padx=2, command="download").place(x=230, y=150)
root.mainloop()


