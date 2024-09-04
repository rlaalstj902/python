#code10-03.py

from tkinter import *
window = Tk()

label1 = Label(window, text = "COOKBOK~~Python을",bg="rose quartz")
label2 = Label(window, text = "열심히", font = ("궁서체", 30),
               fg = "black",bg="rose quartz")
label3 = Label(window, text = "공부 중입니다.", bg = "serenity",
               width = 20, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()