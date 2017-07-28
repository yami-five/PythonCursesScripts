import os
import curses
def ShowWhatDirectoryContains():
        directorylist=os.listdir()
        pad = curses.newpad(100, 50)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        if len(os.getcwd())>3: 
               for x in range(0,len(directorylist)+1):
                       if x>0:
                               if x==ItemNumber:
                                       pad.addstr(x,0,directorylist[x-1],curses.color_pair(1))
                               else: pad.addstr(x,0,directorylist[x-1])
                       else:
                               if x==ItemNumber:
                                       pad.addstr(x,0,"..",curses.color_pair(1))
                               else: pad.addstr(x,0,"..")
        else:
               for x in range(0,len(directorylist)):
                       if x==ItemNumber:
                               pad.addstr(x,0,directorylist[x],curses.color_pair(1))
                       else: pad.addstr(x,0,directorylist[x])
        pad.addstr(40,0,"Press Ctrl+x for exit")
        pad.refresh( 0,0, 5,5, 49,99)
        
def UpperItem(ItemNumber):
        directorylist=os.listdir()
        if len(os.getcwd())>3:
                if ItemNumber<0: ItemNumber=(len(directorylist))
        else:
                if ItemNumber<0: ItemNumber=(len(directorylist)-1)
        print(ItemNumber)
        pad = curses.newpad(100, 50)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        if len(os.getcwd())>3: 
               for x in range(0,len(directorylist)+1):
                       if x>0:
                               if x==ItemNumber:
                                       pad.addstr(x,0,directorylist[x-1],curses.color_pair(1))
                               else: pad.addstr(x,0,directorylist[x-1])
                       else:
                               if x==ItemNumber:
                                       pad.addstr(x,0,"..",curses.color_pair(1))
                               else: pad.addstr(x,0,"..")
        else:
               for x in range(0,len(directorylist)):
                       if x==ItemNumber:
                               pad.addstr(x,0,directorylist[x],curses.color_pair(1))
                       else: pad.addstr(x,0,directorylist[x])
        pad.addstr(40,0,"Press Ctrl+x for exit")
        pad.refresh( 0,0, 5,5, 49,99)
        return ItemNumber

def LowerItem(ItemNumber):
       directorylist=os.listdir()
       if len(os.getcwd())>3:
               if ItemNumber>(len(directorylist)): ItemNumber=0
       else:
               if ItemNumber>(len(directorylist)-1): ItemNumber=0
       print(ItemNumber)
       pad = curses.newpad(100, 50)
       curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
       if len(os.getcwd())>3: 
               for x in range(0,len(directorylist)+1):
                       if x>0:
                               if x==ItemNumber:
                                       pad.addstr(x,0,directorylist[x-1],curses.color_pair(1))
                               else: pad.addstr(x,0,directorylist[x-1])
                       else:
                               if x==ItemNumber:
                                       pad.addstr(x,0,"..",curses.color_pair(1))
                               else: pad.addstr(x,0,"..")
       else:
               for x in range(0,len(directorylist)):
                       if x==ItemNumber:
                               pad.addstr(x,0,directorylist[x],curses.color_pair(1))
                       else: pad.addstr(x,0,directorylist[x])
       pad.addstr(40,0,"Press Ctrl+x for exit")
       pad.refresh( 0,0, 5,5, 49,99)
       return ItemNumber

def ChangeDirectory(ItemNumber):
        directorylist=os.listdir()
        if ItemNumber==0 and len(os.getcwd())>3: os.chdir("..")
        else:
                if "." in directorylist[ItemNumber]:
                        print("It's file")
                else: os.chdir(directorylist[ItemNumber])
        ShowWhatDirectoryContains()

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
    elif key==258:
            ItemNumber=ItemNumber+1
            ItemNumber=LowerItem(ItemNumber)
    elif key==259:
            ItemNumber=ItemNumber-1
            ItemNumber=UpperItem(ItemNumber)
    elif key==10:
            ChangeDirectory(ItemNumber)  
    else: print(key)

curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
