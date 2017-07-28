import os
import curses
os.system("mode con cols=100 lines=50")
stdscr=curses.initscr()
stdscr.refresh()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
directorylist=os.listdir()
##for x in directorylist:
##    print(x)
pad = curses.newpad(100, 50)
for x in range(0,len(directorylist)-1):
        pad.addstr(x,0,directorylist[x])
pad.addstr(40,0,"Press Ctrl+x for exit")
pad.refresh( 0,0, 5,5, 49,99)
while True:
    key=stdscr.getch()
    if key==24:
        break
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
