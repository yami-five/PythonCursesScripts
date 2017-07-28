import os
import curses
def ShowWhatDirectoryContains():
        directorylist=os.listdir()
        pad = curses.newpad(100, 50)
        for x in range(0,len(directorylist)-1):
                pad.addstr(x,0,directorylist[x])
        pad.addstr(40,0,"Press Ctrl+x for exit")
        pad.refresh( 0,0, 5,5, 49,99)
        
os.system("mode con cols=100 lines=50")
stdscr=curses.initscr()
stdscr.refresh()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
ShowWhatDirectoryContains()

while True:
    key=stdscr.getch()
    if key==24: break
    elif key==120:
        os.chdir("folder")
        ShowWhatDirectoryContains()
    else: print(key)
        
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
