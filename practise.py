from tkinter import *
import sqlite3

root = Tk()
root.title("Student login Application")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d") % (width, height, x, y)
root.resizable(0, 0)

#===================METHODS========================
def Database():
    global conn, cursor
    conn = sqlite3.connect('pythontut.db')














