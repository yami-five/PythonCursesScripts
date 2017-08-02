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

def SetLenght(DirectoryList):
    if len(DirectoryList)>15: return 15
    elif len(DirectoryList)<=15: return len(DirectoryList)
    else: print("you fucked up")

def ShowWhatDirectoryContains(DirectoryList,Shift):
    pad = curses.newpad(20, 40)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    Lenght=SetLenght(DirectoryList)
    for x in range(0,Lenght):
        if DirectoryList[x+Shift]=="..":
            pad.addstr(x, 0, DirectoryList[x+Shift])
        if DirectoryList[x+Shift]!=".." and len(DirectoryList[x])>24:
            pad.addstr(x, 0, DirectoryList[x+Shift][0:20]+"...")
        if DirectoryList[x+Shift]!=".." and len(DirectoryList[x])<=24:
            pad.addstr(x, 0, DirectoryList[x+Shift])
        else: print("you fucked up")
    pad.addstr(18,0,"Press Ctrl+x for exit")
    pad.refresh(0, 0, 0, 0, 19, 39)

os.system("mode con cols=40 lines=20")
stdscr=curses.initscr()
ItemNumber=0
Lenght=14
Shift=0
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
    # # Page Up 339
    # elif key == 339:
    #     Shift, ItemNumber, Lenght=ScrollListUp(DirectoryList,ItemNumber,PartitionList,ColumnNumber,Lenght,Shift)
    # # Page Down 338
    # elif key == 338:
    #     Shift, ItemNumber, Lenght=ScrollListDown(DirectoryList,ItemNumber,PartitionList,ColumnNumber,Lenght,Shift)

else: print(key)
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()