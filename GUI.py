"""
Created on Fri Nov  6 19:48:47 2020
@author: ISH KAPOOR
"""
import tkinter as tk
import csv
import ZoomMeetingsBot

filename = "zoommeeting_log.csv"
csv_rows = []

root = tk.Tk()
root.title("ZoomMeetingLogger")
root.geometry("640x600")

entry_1 = tk.Entry(root, width = 40, bg = "black", fg = "lime green", borderwidth = 5, justify = tk.CENTER)
entry_1.place(x = 250, y = 20)

entry_2 = tk.Entry(root, width = 40, bg = "black", fg = "lime green", borderwidth = 5, justify = tk.CENTER)
entry_2.place(x = 250, y = 70)

entry_3 = tk.Entry(root, width = 40, bg = "black", fg = "lime green", borderwidth = 5, justify = tk.CENTER)
entry_3.place(x = 250, y = 120)

entry_4 = tk.Entry(root, width = 40, bg = "black", fg = "lime green", borderwidth = 5, justify = tk.CENTER)
entry_4.place(x = 250, y = 170)

def loadData():

    entryLabel_1 = tk.Label(root, text = entry_1.get(), justify = tk.CENTER)
    entryLabel_1.place(x = 280, y = 360)

    entryLabel_2 = tk.Label(root, text = entry_2.get(), justify = tk.CENTER)
    entryLabel_2.place(x = 280, y = 400)

    entryLabel_3 = tk.Label(root, text = entry_3.get(), justify = tk.CENTER)
    entryLabel_3.place(x = 280, y = 440)

    entryLabel_4 = tk.Label(root, text = entry_4.get(), justify = tk.CENTER)
    entryLabel_4.place(x = 280, y = 480)

    e1 = entry_1.get()
    e2 = entry_2.get()
    e3 = entry_3.get()
    e4 = entry_4.get()

    csv_rows.append(e4)
    csv_rows.append(e1)
    csv_rows.append(e2)
    csv_rows.append(e3)

    with open(filename, 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(csv_rows)

    csv_rows.clear()

Label_1 = tk.Label(root, text = "Zoom Meeting ID:",
    font = ("arial black", 10, "bold"), fg = "steelblue").place(x = 0, y = 20)
Label_2 = tk.Label(root, text = "Zoom Meeting Password:",
    font = ("arial black", 10, "bold"), fg = "steelblue").place(x = 0, y = 70)
Label_3 = tk.Label(root, text = "Days of Meeting:",
    font = ("arial black", 10, "bold"), fg = "steelblue").place(x = 0, y = 120)
Label_4 = tk.Label(root, text = "Zoom Meeting Time:",
    font = ("arial black", 10, "bold"), fg = "steelblue").place(x = 0, y = 170)

loadButton = tk.Button(root, text = "Load", command = loadData)
loadButton.place(x = 300, y = 300)

executeButton = tk.Button(root, text = "Start")#, command = ZoomMeetingsBot.execute())
executeButton.place(x = 300, y = 250)

root.mainloop()