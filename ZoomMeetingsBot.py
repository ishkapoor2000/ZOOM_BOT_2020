"""
Created on Mon Nov  2 13:39:14 2020
@author: ISH KAPOOR
"""

from subprocess import call
import pyautogui as pg
import time
import pandas as pd
from datetime import datetime

join_icon = 'C:/Users/ISH KAPOOR/Desktop/PYTHONprojects/PYTHON-regularWorks/ZoomMeetingsBot/join_icon.png'
unchecked_icon = 'C:/Users/ISH KAPOOR/Desktop/PYTHONprojects/PYTHON-regularWorks/ZoomMeetingsBot/unchecked_icon.png'
final_join_icon = 'C:/Users/ISH KAPOOR/Desktop/PYTHONprojects/PYTHON-regularWorks/ZoomMeetingsBot/final_join_icon.png'

def sign_in(meeting_id, pswd):

    call(["C:/Users/ISH KAPOOR/AppData/Roaming/Zoom/bin/Zoom.exe"])
    time.sleep(14)
    join_button = pg.locateCenterOnScreen(join_icon)
    pg.moveTo(join_button)
    pg.click()
    time.sleep(14)
    print("Clicked on Join Button.")

    for m in meeting_id:
        pg.write(m)
    print("Written Meeting ID")

    unchecked_button = pg.locateAllOnScreen(unchecked_icon)
    for btn in unchecked_button:
        pg.moveTo(btn)
        pg.click()
    time.sleep(14)
    print("Clicked on Unchecked Buttons.")

    final_join_button = pg.locateCenterOnScreen(final_join_icon)
    pg.moveTo(final_join_button)
    pg.click()
    time.sleep(14)
    print("Clicked on Final Join Button.")

    for p in pswd:
        pg.write(p)
    print("Written password.")
    time.sleep(14)
    print("Donw waiting 14 sec after writing the password.")
    pg.press('enter')

df = pd.read_csv('zoommeeting_log.csv')

def execute():

    while True:

        now = datetime.now().strftime("%H:%M")
        day = datetime.now().strftime("%A")
        if day in str(df['day']):
            if now in str(df['timings']):
                row = df.loc[df['timings'] == now]
                m_id = str(row.iloc[0, 1])
                m_psw = str(row.iloc[0, 2])
                sign_in(m_id, m_psw)
                time.sleep(40)
                print('Signed in!')