# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:22:53 2018

@author: Anshuman_Mahapatra
"""
import pyautogui
print(pyautogui.position())

##Moving Mouse
pyautogui.moveTo(10, 10, duration=20)

##Mouse click
pyautogui.click(button='left')

pyautogui.click(button='right')

pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)

pyautogui.alert('I AM IN DANGER')
pyautogui.confirm('AM FINE')