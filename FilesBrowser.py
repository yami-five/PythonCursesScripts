import os
import curses
def ShowWhatDirectoryContains():
        directorylist=os.listdir()
        pad = curses.newpad(100, 50)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        for x in range(0,len(directorylist)):
                if x>0: pad.addstr(x,0,directorylist[x-1])
                else: pad.addstr(x,0,"..",curses.color_pair(1))
        pad.addstr(40,0,"Press Ctrl+x for exit")
        pad.refresh( 0,0, 5,5, 49,99)
        
def UpperItem(ItemNumber):
        directorylist=os.listdir()
        if ItemNumber<0: ItemNumber=(len(directorylist)-1)
        print(ItemNumber)
        pad = curses.newpad(100, 50)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        for x in range(0,len(directorylist)):
                if x>0:
                        if x==ItemNumber:
                                pad.addstr(x,0,directorylist[x-1],curses.color_pair(1))
                        else: pad.addstr(x,0,directorylist[x-1])
                else:
                        if x==ItemNumber:
                                pad.addstr(x,0,"..",curses.color_pair(1))
                        else: pad.addstr(x,0,"..")
        pad.addstr(40,0,"Press Ctrl+x for exit")
        pad.refresh( 0,0, 5,5, 49,99)
        return ItemNumber

def LowerItem(ItemNumber):
       directorylist=os.listdir()
       if ItemNumber>(len(directorylist)-1): ItemNumber=0
       print(ItemNumber)
       pad = curses.newpad(100, 50)
       curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
       for x in range(0,len(directorylist)):
               if x>0:
                       if x==ItemNumber:
                               pad.addstr(x,0,directorylist[x-1],curses.color_pair(1))
                       else: pad.addstr(x,0,directorylist[x-1])
               else:
                       if x==ItemNumber:
                               pad.addstr(x,0,"..",curses.color_pair(1))
                       else: pad.addstr(x,0,"..")
       pad.addstr(40,0,"Press Ctrl+x for exit")
       pad.refresh( 0,0, 5,5, 49,99)
       return ItemNumber

os.system("mode con cols=100 lines=50")
stdscr=curses.initscr()
ItemNumber=0
curses.start_color()
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
    elif key==258:
            ItemNumber=ItemNumber+1
            ItemNumber=LowerItem(ItemNumber)
    elif key==259:
            ItemNumber=ItemNumber-1
            ItemNumber=UpperItem(ItemNumber)
    else: print(key)


        
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
