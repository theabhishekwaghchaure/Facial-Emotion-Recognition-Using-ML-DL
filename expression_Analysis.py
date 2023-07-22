import tkinter as tk 
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
import emotion_1 as validate


global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Facial Emotion Recognition ")

# 430
#######lbl = tk.Label(root, text="Diabetic Retinopathy Detection System", font=('times', 35,' bold '), height=1, width=30,bg="seashell2",fg="indian red")
########lbl.place(x=350, y=5)
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('red_yellow_emoji_faces_hd_emoji.jpg')
image2 = image2.resize((1600, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Facial Emotion Recognition", font=("Times New Roman", 35, 'bold'),
                    background="black", fg="white",height=1)
label_l1.place(x=500, y=25)

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)

def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T,  font=("bold", 25), bg='pink', fg='black')
    result_label.place(x=380, y=150)
#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



def lecture_evaluation():
        # from subprocess import call
        # call(['python','detection_emotion_practice.py'])
        validate.upload()

def prediction_emotion():
    #clear_img()
    #update_label("Model Training Start...............")

    start = time.time()

    result = validate.files_count()
    #validate.files_count()
    end = time.time()
    #print("---" + result)
    ET = "Execution Time: {0:.4} seconds \n".format(end - start)

    msg = "Model Training Completed.." + '\n' + str(result) + '\n'+ ET

    update_label(msg)


#################################################################################################################
def window():
    root.destroy()



button3 = tk.Button(root, text="Find Evaluation",command=lecture_evaluation,height=1,width=15,font=('times', 25, ' bold '), bg="brown4", fg="white")
button3.place(x=50, y=180)

button4 = tk.Button(root, text="Prediction",command=prediction_emotion,  height=1,width=15, bg="brown4", fg="white",font=('times', 25, ' bold '))
button4.place(x=50, y=280)

exit = tk.Button(root, text="Exit", command=window, height=1,width=15, font=('times',25, ' bold '), bg="red",fg="white")
exit.place(x=50, y=480)

root.mainloop()