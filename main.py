import audiograph

from tkinter import *
import tkinter.font as tkfont

def run():
    
    def reload_image():
        image_path = "files/tempfile.png"
        image = PhotoImage(file=image_path)
        image_label.configure(image=image)
        image_label.image = image

    def handle():
        audiograph.generate_sound_and_graph(.5, int(text_box.get()))
        reload_image()

    root = Tk()
    root.title("Sine Waves")
    root.geometry("700x630")
    root.iconbitmap("files/icon.ico")
    root.configure(bg="black")

    dejavu_sans = tkfont.Font(family="files/DejaVu Sans", size=12)

    image = PhotoImage(file="files/tempfile.png")
    image_label = Label(root, image=image, bg="black")
    image_label.pack(pady=10)

    text_box = Entry(root, bg="black", fg="white", font=(dejavu_sans), justify="center", textvariable='12')
    text_box.pack(padx=275, pady=5)

    button = Button(root, text="▶️", bg="black", fg="white", font=(dejavu_sans))
    button.pack(pady=5)

    button.bind("<Button-1>", lambda event: handle())

    root.mainloop()

run()
