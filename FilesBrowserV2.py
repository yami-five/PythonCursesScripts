import os
import curses
import wmi

def SetDirectoryList():
    List=[]
    Buff=os.listdir()
    if len(os.getcwd())>3:
        List.append("..")
    DirectoryList=List+Buff
    DirectoryList=list(DirectoryList)
    return DirectoryList

def SetLenght(DirectoryList,Shift):
    if len(DirectoryList)>15: return 15+Shift
    elif len(DirectoryList)<=15: return len(DirectoryList)
    else: print("you fucked up")

def ShowWhatDirectoryContains(DirectoryList,Shift):
    pad = curses.newpad(20, 40)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    Lenght=SetLenght(DirectoryList,Shift)
    for x in range(0+Shift,Lenght):
        if DirectoryList[x]=="..":
            pad.addstr(x-Shift, 0, DirectoryList[x])
        if DirectoryList[x]!=".." and len(DirectoryList[x])>24:
            pad.addstr(x-Shift, 0, DirectoryList[x][0:20]+"...")
        if DirectoryList[x]!=".." and len(DirectoryList[x])<=24:
            pad.addstr(x-Shift, 0, DirectoryList[x])
        else: print("you fucked up")
    pad.addstr(18,0,"Press Ctrl+x for exit")
    pad.refresh(0, 0, 1, 0, 19, 39)

def ScrollListUp(DirectoryList,ItemNumber,Shift):
    Shift-=15
    if Shift+0<0:
        Shift=0
    else: ItemNumber=0
    print("Shift=",Shift)
    ShowWhatDirectoryContains(DirectoryList,Shift)
    return [Shift, ItemNumber]

def ScrollListDown(DirectoryList,ItemNumber,Shift):
    Shift+=15
    if Shift+len(DirectoryList)>len(DirectoryList):
        Shift=len(DirectoryList)-Shift
        print("here")
    else: ItemNumber=0
    print("Shift=",Shift)
    ShowWhatDirectoryContains(DirectoryList,Shift)
    return [Shift, ItemNumber]

os.system("mode con cols=40 lines=20")
stdscr=curses.initscr()
Shift=0
ItemNumber=0
curses.start_color()
stdscr.refresh()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
PartitionList=[]
c=wmi.WMI()
for disk in c.Win32_LogicalDisk(DriveType=3):
    PartitionList.append(disk.name)
ColumnNumber=0
DirectoryList=SetDirectoryList()
ShowWhatDirectoryContains(DirectoryList,Shift)
print("len=",len(DirectoryList))

while True:
    key=stdscr.getch()
    #Ctrl+x
    if key==24: break
    # #Up_Arrow
    # elif key==258:
    #     ItemNumber=ItemNumber+1
    #     ItemNumber=LowerItem(ItemNumber,PartitionList,ColumnNumber)
    # #Down_Arrow
    # elif key==259:
    #     ItemNumber=ItemNumber-1
    #     ItemNumber=UpperItem(ItemNumber,PartitionList,ColumnNumber)
    # #Left_Arrow
    # elif key==260:
    #     ColumnNumber=SwitchColumn(ItemNumber,PartitionList,key,ColumnNumber)
    #     ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber,Lenght,Shift)
    # #Right_Arrow
    # elif key==261:
    #     ColumnNumber=SwitchColumn(ItemNumber,PartitionList,key,ColumnNumber)
    #     ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber,Lenght,Shift)
    # #Enter
    # elif key==10:
    #     ColumnNumber,ItemNumber,Shift=ChangeDirectory(ItemNumber,PartitionList,ColumnNumber,Lenght,Shift)
    # Page Up 339
    elif key == 339:
        Shift, ItemNumber=ScrollListUp(DirectoryList,ItemNumber,Shift)
    # Page Down 338
    elif key == 338:
        Shift, ItemNumber=ScrollListDown(DirectoryList,ItemNumber,Shift)
    else: print(key)

else: print(key)
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()