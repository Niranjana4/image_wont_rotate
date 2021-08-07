from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import ttk
root=Tk()
root.geometry("600x600")
root.configure(background="black")


label_image=Label(root,highlightthickness=5,borderwidth=2,relief=SOLID)
img_path=""
def open_image():
    global img_path
    img_path=filedialog.askopenfilename(title="open text file",filetypes=(("Image files", "*.jpg"),))
    print(img_path)
    im=Image.open(img_path)
    img=ImageTk.PhotoImage(im)
    label_image["image"]=img
    img.close()

def rotate():
    global img_path
    im=Image.open(img_path)
    rotate_img=ImageTk.PhotoImage(im.rotate(180))
    label_image["image"]=rotate_img
    rotate_img.close()

btn=Button(root,text="open image",command=open_image)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

btn=Button(root,text="rotate image",command=rotate)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)


label_image.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()

