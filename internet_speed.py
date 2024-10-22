from tkinter import *
import speedtest

def speedcheck():
    loading_label = Label(sp, text="Loading...", font=("Times New Roman", 30, "bold"), bg="Black", fg="White")
    loading_label.place(x=60, y=460, height=50, width=380)
    sp.update()  

    speed_test = speedtest.Speedtest()
    speed_test.get_servers()
    down = str(round(speed_test.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(speed_test.upload() / (10 ** 6), 3)) + " Mbps"
    
    loading_label.place_forget()  
    lab_Down.config(text=down)
    lab_Up.config(text=up)

def on_enter(event):
    event.widget.config(bg='DarkOrange', fg='Black')

def on_leave(event):
    event.widget.config(bg='Red', fg='White')

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="Black")

title_lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="Black", fg="White")
title_lab.place(x=60, y=40, height=50, width=380)

download_label = Label(sp, text="Download Speed", font=("Times New Roman", 30, "bold"), bg="Black", fg="White")
download_label.place(x=60, y=130, height=50, width=380)

lab_Down = Label(sp, text="00", font=("Times New Roman", 30, "bold"), bg="Black", fg="White")
lab_Down.place(x=60, y=200, height=50, width=380)

upload_label = Label(sp, text="Upload Speed", font=("Times New Roman", 30, "bold"), bg="Black", fg="White")
upload_label.place(x=60, y=290, height=50, width=380)

lab_Up = Label(sp, text="00", font=("Times New Roman", 30, "bold"), bg="Black", fg="White")
lab_Up.place(x=60, y=360, height=50, width=380)

check_speed_button = Button(sp, text="Check Speed", font=("Times New Roman", 30, "bold"), relief=RAISED, bg="Red", command=speedcheck)
check_speed_button.place(x=60, y=460, height=50, width=380)


check_speed_button.bind("<Enter>", on_enter)
check_speed_button.bind("<Leave>", on_leave)

sp.mainloop()
