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

def ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift,PartitionList,Column):
    pad = curses.newpad(20, 40)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    Lenght=SetLenght(DirectoryList,Shift)
    for x in range(0+Shift,Lenght):
        print(DirectoryList[x])
        if DirectoryList[x]=="..":
            if x-Shift==ItemNumber and Column==0:
                pad.addstr(x-Shift, 0, DirectoryList[x], curses.color_pair(1))
                ItemName=DirectoryList[x]
            else: pad.addstr(x-Shift, 0, DirectoryList[x])
        elif DirectoryList[x]!=".." and len(DirectoryList[x])>24:
            if x-Shift==ItemNumber and Column==0:
                pad.addstr(x-Shift, 0, DirectoryList[x][0:20]+"...", curses.color_pair(1))
                ItemName=DirectoryList[x]
            else: pad.addstr(x-Shift, 0, DirectoryList[x][0:20]+"...")
        elif DirectoryList[x]!=".." and len(DirectoryList[x])<=24:
            if x-Shift==ItemNumber and Column==0:
                pad.addstr(x-Shift, 0, DirectoryList[x], curses.color_pair(1))
                ItemName=DirectoryList[x]
            else: pad.addstr(x-Shift, 0, DirectoryList[x])
        else: print("you fucked up:2")
    for x in range(0,len(PartitionList)):
            if x==ItemNumber and Column==1:
                pad.addstr(x, 30, PartitionList[x], curses.color_pair(1))
            else: pad.addstr(x, 30, PartitionList[x])
    string=("Shift="+str(Shift))
    pad.addstr(18,0,string)
    pad.addstr(19,0,"Esc=exit | Ctrl+C=copy | Ctrl+X=cut")
    pad.refresh(0, 0, 0, 0, 19, 39)

def ScrollListUp(DirectoryList,Shift,Column):
    Shift-=15
    if Shift+0<0 and Column==0: Shift=0
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift,PartitionList,Column)
    return [Shift, 0]

def ScrollListDown(DirectoryList,Shift,Column):
    Shift+=15
    if len(DirectoryList)<15 and Column==0: Shift-=15
    elif Shift+len(DirectoryList)>len(DirectoryList):
        Shift=len(DirectoryList)-Shift
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift,PartitionList,Column)
    return [Shift, 0]

def LowerItem(DirectoryList,ItemNumber,Column):
    ItemNumber+=1
    if ItemNumber>14 and len(DirectoryList)>15 and Column==0:
        ItemNumber=0
    elif len(DirectoryList)<=15 and ItemNumber>(len(DirectoryList)-1) and Column==0:
        ItemNumber=0
    elif Column==1 and ItemNumber<0:
        ItemNumber=(len(PartitionList)-1)
    elif Column==1 and ItemNumber>len(PartitionList)-1:
        ItemNumber=0
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift,PartitionList,Column)
    return ItemNumber

def UpperItem(DirectoryList,ItemNumber,Column):
    ItemNumber-=1
    if ItemNumber<0 and len(DirectoryList)<15 and Column==0:
        ItemNumber=len(DirectoryList)-1
    elif ItemNumber <0 and len(DirectoryList)>=15 and Column==0:
        ItemNumber=14
    elif Column==1 and ItemNumber<0:
        ItemNumber=len(PartitionList)-1
    elif Column==1 and ItemNumber>len(PartitionList):
        ItemNumber=0
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift,PartitionList,Column)
    return ItemNumber

def ChangeDirectory(ItemNumber,DirectoryList,Shift,Column):
    if Column==0:
        if os.path.isdir(DirectoryList[ItemNumber+Shift]) and os.access(DirectoryList[ItemNumber+Shift], os.R_OK)==True:
            os.chdir(DirectoryList[ItemNumber+Shift])
            DirectoryList=SetDirectoryList()
            Shift=0
            ItemNumber=0
    elif Column==1:
        os.chdir(PartitionList[ItemNumber])
        DirectoryList = SetDirectoryList()
        Shift = 0
        ItemNumber = 0
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift,PartitionList,Column)
    return [ItemNumber, DirectoryList, Shift]

def SwitchColumn(DirectoryList,Shift,PartitionList,Column):
    if Column==1:Column=0
    elif Column==0:Column=1
    else: print("you fucked up:3")
    ShowWhatDirectoryContains(DirectoryList,0,Shift,PartitionList,Column)
    return [Column,0]


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
Column=0
DirectoryList=SetDirectoryList()
ShowWhatDirectoryContains(DirectoryList,ItemNumber,Shift,PartitionList,Column)

while True:
    key=stdscr.getch()
    #Esc
    if key==27: break
    #Up_Arrow
    elif key==258:
        ItemNumber=LowerItem(DirectoryList,ItemNumber,Column)
    #Down_Arrow
    elif key==259:
        ItemNumber=UpperItem(DirectoryList,ItemNumber,Column)
    #Left_Arrow
    elif key==260:
        Column,ItemNumber=SwitchColumn(DirectoryList,Shift,PartitionList,Column)
    #Right_Arrow
    elif key==261:
        Column,ItemNumber=SwitchColumn(DirectoryList,Shift,PartitionList,Column)
    #Enter
    elif key==10:
        ItemNumber, DirectoryList, Shift=ChangeDirectory(ItemNumber,DirectoryList,Shift,Column)
    # Page Up 339
    elif key == 339:
        Shift, ItemNumber=ScrollListUp(DirectoryList,Shift,Column)
    # Page Down 338
    elif key == 338:
        Shift, ItemNumber=ScrollListDown(DirectoryList,Shift,Column)
    # Ctrl+Z
    # Ctrl+X
    # Ctrl+C
    # Ctrl+V
    else: print(key)

curses.nocbreak()
stdscr.keypad(False)
curses.endwin()