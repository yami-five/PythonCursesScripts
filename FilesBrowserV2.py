import os
import curses
import wmi
import sys

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
    else: print("you fucked up:1")

def ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift):
    pad = curses.newpad(20, 40)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    Lenght=SetLenght(DirectoryList,Shift)
    for x in range(0+Shift,Lenght):
        print(DirectoryList[x])
        if DirectoryList[x]=="..":
            if x-Shift==ItemNumber:
                pad.addstr(x-Shift, 0, DirectoryList[x], curses.color_pair(1))
                ItemName=DirectoryList[x]
            else: pad.addstr(x-Shift, 0, DirectoryList[x])
        elif DirectoryList[x]!=".." and len(DirectoryList[x])>24:
            if x-Shift==ItemNumber:
                pad.addstr(x-Shift, 0, DirectoryList[x][0:20]+"...", curses.color_pair(1))
                ItemName=DirectoryList[x]
            else: pad.addstr(x-Shift, 0, DirectoryList[x][0:20]+"...")
        elif DirectoryList[x]!=".." and len(DirectoryList[x])<=24:
            if x-Shift==ItemNumber:
                pad.addstr(x-Shift, 0, DirectoryList[x], curses.color_pair(1))
                ItemName=DirectoryList[x]
            else: pad.addstr(x-Shift, 0, DirectoryList[x])
        else: print("you fucked up:2")
    pad.addstr(18,0,"Press Ctrl+x for exit")
    pad.refresh(0, 0, 1, 0, 19, 39)

def ScrollListUp(DirectoryList,Shift):
    Shift-=15
    if Shift+0<0: Shift=0
    ShowWhatDirectoryContains(DirectoryList,0,Shift)
    return [Shift, 0]

def ScrollListDown(DirectoryList,Shift):
    Shift+=15
    if Shift+len(DirectoryList)>len(DirectoryList):
        Shift=len(DirectoryList)-Shift
    ShowWhatDirectoryContains(DirectoryList,0,Shift)
    return [Shift, 0]

def LowerItem(DirectoryList,ItemNumber):
    ItemNumber+=1
    if ItemNumber>14 and len(DirectoryList)>15:
        ItemNumber=0
    elif len(DirectoryList)<=15 and ItemNumber>len(DirectoryList)-1:
        ItemNumber=0
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift)
    return ItemNumber

def UpperItem(DirectoryList,ItemNumber):
    ItemNumber-=1
    if ItemNumber<0 and len(DirectoryList)<15:
        ItemNumber=len(DirectoryList)-1
    elif ItemNumber <0 and len(DirectoryList)>=15:
        ItemNumber=14
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift)
    return ItemNumber

def ChangeDirectory(ItemNumber,DirectoryList,Shift):
    if os.path.isdir(DirectoryList[ItemNumber+Shift]):
        os.chdir(DirectoryList[ItemNumber+Shift])
        DirectoryList=SetDirectoryList()
        Shift=0
        ItemNumber=0
        ShowWhatDirectoryContains(DirectoryList, ItemNumber, Shift)
    return [ItemNumber, DirectoryList, Shift]


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
ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift)

while True:
    key=stdscr.getch()
    #Ctrl+x
    if key==24: break
    #Up_Arrow
    elif key==258:
        ItemNumber=LowerItem(DirectoryList,ItemNumber)
    #Down_Arrow
    elif key==259:
        ItemNumber=UpperItem(DirectoryList,ItemNumber)
    # #Left_Arrow
    # elif key==260:
    #     ColumnNumber=SwitchColumn(ItemNumber,PartitionList,key,ColumnNumber)
    #     ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber,Lenght,Shift)
    # #Right_Arrow
    # elif key==261:
    #     ColumnNumber=SwitchColumn(ItemNumber,PartitionList,key,ColumnNumber)
    #     ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber,Lenght,Shift)
    #Enter
    elif key==10:
        ItemNumber, DirectoryList, Shift=ChangeDirectory(ItemNumber,DirectoryList,Shift)
    # Page Up 339
    elif key == 339:
        Shift, ItemNumber=ScrollListUp(DirectoryList,Shift)
    # Page Down 338
    elif key == 338:
        Shift, ItemNumber=ScrollListDown(DirectoryList,Shift)
    else: print(key)

curses.nocbreak()
stdscr.keypad(False)
curses.endwin()