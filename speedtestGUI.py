from tkinter import *
import subprocess


def speed ():
    #subprocess code
    ret_text=subprocess.check_output("speedtest-cli",shell=True,universal_newlines=True)
    #show result
    lbl.config(text=ret_text)
    #retart button 
    btn.config(text="reSTART")


#root tkinter
win=Tk()
#title
win.title("speed test internet :)")


#label click
lbl=Label(win,text="click on Button for start and wait a few moments",bg="grey",font=40,border=300)
lbl.pack()
#button start
btn=Button(win,text='START',font="40",border=10,command=speed,height=3,width=60)
btn.pack()
#label info
lblload=Label(win,text="After clicking start ")
lblload.pack()
Label(win,text=" wait a few moments ").pack()
Label(win,text="(depends on your internet speed)").pack()



#isze frame
win.geometry("730x950")
#size off
win.resizable(height = False, width = False)
win.mainloop()


#thanks for visit :)

