from tkinter import *

root = Tk()

root.title("BMI Calculator By @SmashedFrenzy16")

root.geometry("600x400")

def execute():

    global weight

    weight = float(weight_e.get())

def execute2():

    global height

    height = float(height_e.get())

def execute3():

    bmi = (weight/(pow(height, 2))) * 703

    blank_label2 = Label(root, text="")

    blank_label2.pack()

    result = Label(root, text=str(bmi))

    result.pack()

title_label = Label(
            root, fg="black", text="BMI Calculator", font=("Arial", 48))

title_label.pack()

blank_label = Label(root, text="")

blank_label.pack()

weight_e = Entry(root, width=100, borderwidth=5)

weight_e.pack()

weight_e.insert(0, "Enter in your weight (lb)")

weight_button = Button(root, text="Enter", command=execute)

weight_button.pack()

height_e = Entry(root, width=100, borderwidth=5)

height_e.pack()

height_e.insert(0, "Enter in your height (in)")

height_button = Button(root, text="Enter", command=execute2)

height_button.pack()

result_button = Button(root, text="Get Result", command=execute3)

result_button.pack()

root.mainloop()