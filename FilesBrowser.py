import os
import curses
def ShowWhatDirectoryContains(DirectoryList,ItemNumber):
        DirectoryList=os.listdir()
        pad = curses.newpad(20, 40)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        if len(os.getcwd())>3:
               if len(DirectoryList)>13: NumberOfElements=13
               else: NumberOfElements=len(DirectoryList)+1
               for x in range(0,NumberOfElements):
                       if x>0:
                               if len(DirectoryList[x-1])>24:
                                       ItemName=DirectoryList[x-1][0:20]+"..."
                               else: ItemName=DirectoryList[x-1]

                               if x==ItemNumber:
                                       pad.addstr(x,0,ItemName,curses.color_pair(1))
                               else: pad.addstr(x,0,ItemName)
                       else:
                               if x==ItemNumber:
                                       pad.addstr(x,0,"..",curses.color_pair(1))
                               else: pad.addstr(x,0,"..")
        else:
               if len(DirectoryList)>13: NumberOfElements=13
               else: NumberOfElements=len(DirectoryList)
               for x in range(0,NumberOfElements):
                       if len(DirectoryList[x])>24:
                               ItemName=DirectoryList[x][0:20]+"..."
                       else: ItemName=DirectoryList[x]
                       
                       if x==ItemNumber:
                               pad.addstr(x,0,ItemName,curses.color_pair(1))
                       else: pad.addstr(x,0,ItemName)
        pad.addstr(15,0,"Press Ctrl+x for exit")
        pad.refresh( 0,0, 2,5, 19,39)
        
def UpperItem(ItemNumber):
        DirectoryList=os.listdir()
        if len(os.getcwd())>3:
                if ItemNumber<0: ItemNumber=(len(DirectoryList))
        else:
                if ItemNumber<0: ItemNumber=(len(DirectoryList)-1)
        print(ItemNumber)
        ShowWhatDirectoryContains(DirectoryList,ItemNumber)
        return ItemNumber

def LowerItem(ItemNumber):
       DirectoryList=os.listdir()
       if len(os.getcwd())>3:
               if ItemNumber>(len(DirectoryList)): ItemNumber=0
       else:
               if ItemNumber>(len(DirectoryList)-1): ItemNumber=0
       print(ItemNumber)
       ShowWhatDirectoryContains(DirectoryList,ItemNumber)
       return ItemNumber

def ChangeDirectory(ItemNumber):
        DirectoryList=os.listdir()
        if ItemNumber==0 and len(os.getcwd())>3:
                os.chdir("..")
                ItemNumber=0
        else:
                if "." in DirectoryList[ItemNumber-1]:
                        print("It's file")
                else:
                        if len(os.getcwd())>3:
                                os.chdir(DirectoryList[ItemNumber-1])
                        else:
                                os.chdir(DirectoryList[ItemNumber])
                        ItemNumber=0
        ShowWhatDirectoryContains(DirectoryList,ItemNumber)
        return ItemNumber

os.system("mode con cols=40 lines=20")
stdscr=curses.initscr()
ItemNumber=0
curses.start_color()
stdscr.refresh()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
DirectoryList=os.listdir()
ShowWhatDirectoryContains(DirectoryList,ItemNumber)

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
            ItemNumber=ChangeDirectory(ItemNumber)  
    else: print(key)

curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
