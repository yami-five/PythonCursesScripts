import curses
import os
def ShowList(lenght,list,num,shift):
    pad.clear()
    if num>lenght-1:num=0
    elif num<0:num=lenght-1
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    for x in range(0, lenght):
        if x==num:
            pad.addstr(x, 0, alphabet[x+shift], curses.color_pair(1))
        else:
            pad.addstr(x, 0, alphabet[x+shift])
    pad.refresh(0, 0, 0, 0, 19, 39)
    return num
os.system("mode con cols=40 lines=20")
stdscr = curses.initscr()
curses.start_color()
pad = curses.newpad(20, 40)
stdscr.refresh()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
alphabet = ['a']
counter = 97
while(alphabet[-1] != 'z'):
    counter += 1
    alphabet.append(chr(counter))
lenght = 15
num=0
shift=0
ShowList(lenght,alphabet,num,shift)
while True:
    key=stdscr.getch()
    #Ctrl+x
    if key==24: break
    #Space 32
    #Up_Arrow
    elif key==259:
        num-=1
        num=ShowList(lenght,alphabet,num,shift)
    #Down_Arrow
    elif key==258:
        num+=1
        num=ShowList(lenght,alphabet,num,shift)
    #Page Up 339
    elif key==339:
        shift-=15
        if shift<0:
            shift=0
        else:
            num=0
        if lenght+shift<len(alphabet):
            lenght=15
        ShowList(lenght, alphabet, num, shift)
    #Page Down 338
    elif key==338:
        shift+=15
        if shift>len(alphabet):
            shift-=15
        else:
            num=0
        if lenght+shift>len(alphabet):
            lenght=lenght-((lenght+shift)-len(alphabet))
        ShowList(lenght, alphabet, num, shift)
    else: print(key)
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()