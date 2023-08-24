import tkinter as tk 
from tkinter import ttk 
from tkinter import *
from library import returnLecture , lectureTime 
from datetime import datetime

class LectureBoard:
    window_color = "#101010" 
    frame_color = "#101010" 
    window_font = "Helvetica" 
    border_color = "#C0C0C0" 
    fg_color = "#F5F5F5" # text color

    def __init__(self):
        self.window = tk.Tk() 
        self.window.geometry("530x480") # widthxheight
        self.window.title("Lecture Model") 
        self.window.configure(bg=self.window_color)

        img= PhotoImage(file='bg_image.png', master= self.window)
        img_label= Label(self.window,image=img, borderwidth=0, highlightbackground="black")
        img_label.place(x=0, y=0)

        self.frame = tk.Frame(height = 410, width = 470, bg = self.frame_color, borderwidth=5, highlightbackground=self.border_color, highlightthickness=2)
        self.frame.place(x=30, y=35)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TCombobox',
                                background="#C0C0C0",
                                fieldbackground=self.frame_color,
                                
                                foreground="white",
                                darkcolor="#C0C0C0",
                                selectbackground=self.frame_color,
                                lightcolor="#C0C0C0"
                                )


        self.options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
        
        
        self.DayComboBox = ttk.Combobox(values=self.options, justify='center',font=(self.window_font, "16"), width=10)   
        self.DayComboBox.bind("<<ComboboxSelected>>", self.selection_changed) 
        self.DayComboBox.place(x=50, y=55)
          

        self.theoryLecture_Label = tk.Label(text="Theory lectures", borderwidth=2, highlightbackground=self.border_color, highlightthickness=2,justify="center", font=(self.window_font, "16"), width=35, bg=self.frame_color, fg=self.fg_color)
        self.theoryLecture_Label.place(x=50, y=100)  

        curr_lecture_time = f"{lectureTime[1][0]} - {lectureTime[1][1]}"
        self.lectureOneLabel = tk.Label(text=curr_lecture_time, borderwidth=2, highlightbackground=self.border_color, highlightthickness=2,justify="center", font=(self.window_font, "12"), width=11, bg=self.frame_color, fg=self.fg_color)
        self.lectureOneLabel.place(x=70, y=150)

        self.lectureOneValue = tk.Entry(width=22,justify="center", font=(self.window_font,'14'), bg=self.frame_color, borderwidth=0, highlightbackground=self.border_color, highlightthickness=2) 
        self.lectureOneValue.insert(0,"lecture 1") 
        self.lectureOneValue.place(x=218, y=150) 
        self.lectureOneValue.configure(fg="gray") 

        curr_lecture_time = f"{lectureTime[2][0]} - {lectureTime[2][1]}"
        self.lectureTwoLabel = tk.Label(text=curr_lecture_time, borderwidth=2, highlightbackground=self.border_color, highlightthickness=2,justify="center", font=(self.window_font, "12"), width=11, bg=self.frame_color, fg=self.fg_color)
        self.lectureTwoLabel.place(x=70, y=190)

        self.lectureTwoValue = tk.Entry(width=22,justify="center", font=(self.window_font,'14'), bg=self.frame_color, borderwidth=0, highlightbackground=self.border_color, highlightthickness=2) 
        self.lectureTwoValue.insert(0,"lecture 2") 
        self.lectureTwoValue.place(x=218, y=190) 
        self.lectureTwoValue.configure(fg="gray")

        curr_lecture_time = f"{lectureTime[3][0]} - {lectureTime[3][1]}"
        self.lectureThreeLabel = tk.Label(text=curr_lecture_time, borderwidth=2, highlightbackground=self.border_color, highlightthickness=2,justify="center", font=(self.window_font, "12"), width=11, bg=self.frame_color, fg=self.fg_color)
        self.lectureThreeLabel.place(x=70, y=230)

        self.lectureThreeValue = tk.Entry(width=22,justify="center", font=(self.window_font,'14'), bg=self.frame_color, borderwidth=0, highlightbackground=self.border_color, highlightthickness=2) 
        self.lectureThreeValue.insert(0,"lecture 3") 
        self.lectureThreeValue.place(x=218, y=230) 
        self.lectureThreeValue.configure(fg="gray")

        curr_lecture_time = f"{lectureTime[4][0]} - {lectureTime[4][1]}"
        self.lectureFourLabel = tk.Label(text=curr_lecture_time, borderwidth=2, highlightbackground=self.border_color, highlightthickness=2,justify="center", font=(self.window_font, "12"), width=11, bg=self.frame_color, fg=self.fg_color)
        self.lectureFourLabel.place(x=70, y=270)

        self.lectureFourValue = tk.Entry(width=22,justify="center", font=(self.window_font,'14'), bg=self.frame_color, borderwidth=0, highlightbackground=self.border_color, highlightthickness=2) 
        self.lectureFourValue.insert(0,"lecture 4") 
        self.lectureFourValue.place(x=218, y=270) 
        self.lectureFourValue.configure(fg="gray")


        self.labPractical_Label = tk.Label(text="Lab Practical", borderwidth=2, highlightbackground=self.border_color, highlightthickness=2,justify="center", font=(self.window_font, "16"), width=35, bg=self.frame_color, fg=self.fg_color)
        self.labPractical_Label.place(x=50, y=330)  

        curr_lecture_time = f"{lectureTime[5][0]} - {lectureTime[5][1]}"
        self.labPracticalOneLabel = tk.Label(text=curr_lecture_time, borderwidth=2, highlightbackground=self.border_color, highlightthickness=2,justify="center", font=(self.window_font, "12"), width=11, bg=self.frame_color, fg=self.fg_color)
        self.labPracticalOneLabel.place(x=70, y=380) 

        self.labPracticalOneValue = tk.Entry(width=22,justify="center", font=(self.window_font,'14'), bg=self.frame_color, borderwidth=0, highlightbackground=self.border_color, highlightthickness=2) 
        self.labPracticalOneValue.insert(0,"practical") 
        self.labPracticalOneValue.place(x=218, y=380) 
        self.labPracticalOneValue.configure(fg="gray")

        self.DayComboBox.set(datetime.today().strftime("%A"))
        self.selected_day = self.dayToDayNo(self.DayComboBox.get())
        self.updateFields() 
        self.window.mainloop() 
    
    def updateFields(self):
        self.selected_day = self.dayToDayNo(self.DayComboBox.get())
        
        lectures = returnLecture(self.selected_day) 
        # 0     1   2   3   4 
        #l1     l2  l3  l4  pr1
        # f"{lecture1[0]}  {lecture1[1]}        
        # self.lectureFourValue.insert(0,"lecture 4")
        self.lectureOneValue.delete(0, END) 
        self.lectureOneValue.insert(0, f"{lectures[0][0]}  {lectures[0][1]}") 

        self.lectureTwoValue.delete(0, END) 
        self.lectureTwoValue.insert(0, f"{lectures[1][0]}  {lectures[1][1]}") 

        self.lectureThreeValue.delete(0, END) 
        self.lectureThreeValue.insert(0, f"{lectures[2][0]}  {lectures[2][1]}") 

        self.lectureFourValue.delete(0, END) 
        self.lectureFourValue.insert(0, f"{lectures[3][0]}  {lectures[3][1]}") 

        self.labPracticalOneValue.delete(0, END) 
        self.labPracticalOneValue.insert(0, f"{lectures[4][0]}  {lectures[4][1]}") 
        

    def selection_changed(self, event):
        self.updateFields() 


    def dayToDayNo(self, day): 
        match (day.lower()):
            case "monday":
                return 0
            case "tuesday":
                return 1
            case "wednesday":
                return 2 
            case "thursday":
                return 3
            case "friday":
                return 4
            case "saturday":
                return 5
            case "sunday":
                return 6
            case _ :        # default case
                return -1



if __name__ == "__main__":
    LectureBoard()  