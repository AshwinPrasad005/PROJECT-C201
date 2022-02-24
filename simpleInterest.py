from tkinter import *
window=Tk()

window.title('Simple Interest')
window.geometry("600x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = float(principalEntry.get())
    r = float(rateEntry.get())
    t = float(timeEntry.get())
    i = (p*r*t)/100
    interest = round(i)

    result_label.destroy()

    messageLabel=Label(result_frame, text="Interest on Rs."+str(p)+" at the rate of"+str(r)+" for"+str(t)+" years is"+str(interest), bg="lightcyan", font=("Calibri", 12), width=55 )
    messageLabel.place(x=10, y=40)
    messageLabel.pack()

appLabel=Label(window, text="Simple Interest", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
appLabel.place(x=50, y=20)

principalLabel=Label(window, text="Enter Principal", fg = "black", bg = "lightcyan" , font=("Calibri", 12))
principalLabel.place(x=20, y =140)

principalEntry=Entry(window, text="", bd=2, width=15)
principalEntry.place(x=200, y=142)

rateLabel=Label(window, text="Enter Rate of Interest", fg = "black", bg = "lightcyan" , font=("Calibri", 12))
rateLabel.place(x=20 ,y=185)

rateEntry=Entry(window, text="", bd=2, width=15)
rateEntry.place(x=200, y=187)

timeLabel=Label(window, text="Enter Time", fg = "black", bg = "lightcyan" , font=("Calibri", 12))
timeLabel.place(x=20 ,y=230)

timeEntry=Entry(window, text="", bd=2, width=15)
timeEntry.place(x=200, y=232)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan", bd = 4, command=calculate_interest)
calculate_button.place(x=20,y=275)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=100)
result_frame.place(x=20,y=325)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=5,y=20)
result_label.pack()

window.mainloop()