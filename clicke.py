from tkinter import *
import pyautogui as pag
from pyautogui import *

#list of keys supported by pyautogui
supportedKeys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~','accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome','browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete','divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20','f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja','kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack','nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn','pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator','shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen','command', 'option', 'optionleft', 'optionright']

#initialize
keyboardApp = Tk()
keyboardApp.title('Click-E')
keyboardApp.geometry('813x250+550+370')

#making an entry
entry = Entry(keyboardApp, width = 85)
entry.grid(row = 0, column = 0, columnspan = 12)

#input
inputedKeys = []
def select(value):
    entry.insert('end',value + ' + ')
    inputedKeys.append(value)

#hold / click
def spam():
    while True:
        for ele in inputedKeys:
            pag.press(ele)
    inputedKeys.clear()
def hold():
    for ele in inputedKeys:
        pag.keyDown(ele)
    inputedKeys.clear()

spamClick = Button(keyboardApp, text = 'Spam', width = 5, relief = 'ridge', padx = 4, pady = 4, command = spam).grid(column = 12, row = 0)
hold = Button(keyboardApp, text = 'Hold', width = 5, relief = 'ridge', padx = 4, pady = 4, command = hold).grid(column = 13, row = 0)

#keyboard creation
keys = ['`','1','2','3','4','5','6','7','8','9','-','=','backspace',
		'tab','q','w','e','r','t','y','u','i','o','p','[',']','\\',
		'capslock','a','s','d','f','g','h','j','k','l',';','\'','enter',
		'shiftleft','z','x','c','v','b','n','m',',','.','.','/','shiftright',
		'controlleft', 'altleft', 'space', 'altright', 'controlright']

varRow = 2
varCol = 0
for key in keys:
    command = lambda x=key: select(x)
    #special keys
    if key == 'space':
	    space = Button(keyboardApp, text = 'Space', width = 50, relief = 'ridge', padx = 4, pady = 4, command = command).grid(row = 6, column = 2, columnspan = 7)
    elif key == 'altright':
        altr = Button(keyboardApp, text = 'rAlt', width = 5, relief = 'ridge', padx = 4, pady = 4, command = command).grid(row = 6, column = 9)
    elif key == 'altleft':
        altl = Button(keyboardApp, text = 'lAlt', width = 5, relief = 'ridge', padx = 4, pady = 4, command = command).grid(row = 6, column = 1)
    elif key == 'controlright':
        controlr = Button(keyboardApp, text = 'rCtrl', width = 5, relief = 'ridge', padx = 4, pady = 4, command = command).grid(row = 6, column = 10)
    elif key == 'controlleft':
        controll = Button(keyboardApp, text = 'lCtrl', width = 5, relief = 'ridge', padx = 4, pady = 4, command = command).grid(row = 6, column = 0)
    elif key == 'shiftright':
        shiftr = Button(keyboardApp, text = 'rShift', width = 5, relief = 'ridge', padx = 4, pady = 4, command = command).grid(row = 5, column = 12)
    elif key == 'shiftleft':
        shiftl = Button(keyboardApp, text = 'rSlhift', width = 5, relief = 'ridge', padx = 4, pady = 4, command = command).grid(row = 5, column = 0)
    #normal characters
    else:
	notSpecial = Button(keyboardApp, text = key, width = 5, relief = 'ridge', padx = 4, pady = 4, command = command).grid(row = varRow, column = varCol)
    
    #this makes sure the 'keyboard' isn't a straight line
    varCol += 1
    if varCol > 12 and varRow == 2:
        varCol = 0
        varRow += 1
    if varCol > 13 and varRow == 3:
        varCol = 0
        varRow += 1
    if varCol > 12 and varRow == 4:
        varCol = 0
        varRow += 1

keyboardApp.mainloop()
