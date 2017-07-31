import os
import curses
import wmi
def ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber):
        DirectoryList=os.listdir()
        pad = curses.newpad(20, 80)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
        if len(os.getcwd())>3:
            if len(DirectoryList)>13: NumberOfElements=13
            else: NumberOfElements=len(DirectoryList)+1
            for x in range(0,NumberOfElements):
                if x>0:
                    if len(DirectoryList[x-1])>24:
                        ItemName=DirectoryList[x-1][0:20]+"..."
                    else: ItemName=DirectoryList[x-1]

                    if x==ItemNumber and ColumnNumber==0:
                        pad.addstr(x,0,ItemName,curses.color_pair(1))
                    else: pad.addstr(x,0,ItemName)
                else:
                    if x==ItemNumber and ColumnNumber==0:
                        pad.addstr(x,0,"..",curses.color_pair(1))
                    else: pad.addstr(x,0,"..")
        else:
            if len(DirectoryList)>13: NumberOfElements=13
            else: NumberOfElements=len(DirectoryList)
            for x in range(0,NumberOfElements):
                if len(DirectoryList[x])>24:
                    ItemName=DirectoryList[x][0:20]+"..."
                else: ItemName=DirectoryList[x]

                if x==ItemNumber and ColumnNumber==0:
                    pad.addstr(x,0,ItemName,curses.color_pair(1))
                else: pad.addstr(x,0,ItemName)
        for x in range (0,len(PartitionList)):
            if x==ItemNumber and ColumnNumber==1:
                pad.addstr(x,30,PartitionList[x],curses.color_pair(1))
            else:
                pad.addstr(x,30,PartitionList[x])
        pad.addstr(15,0,"Press Ctrl+x for exit")
        pad.refresh( 0,0, 2,5, 19,39)

def UpperItem(ItemNumber,PartitionList,ColumnNumber):
        DirectoryList=os.listdir()
        if ColumnNumber==0:
            if len(os.getcwd())>3:
                if ItemNumber<0: ItemNumber=(len(DirectoryList))
            else:
                if ItemNumber<0: ItemNumber=(len(DirectoryList)-1)
        elif ColumnNumber==1:
            if ItemNumber < 0: ItemNumber = (len(PartitionList)-1)
        else: print("you fucked up")
        print(ItemNumber)
        ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber)
        return ItemNumber

def LowerItem(ItemNumber,PartitionList,ColumnNumber):
    DirectoryList=os.listdir()
    if ColumnNumber==0:
        if len(os.getcwd())>3:
            if ItemNumber>(len(DirectoryList)): ItemNumber=0
        else:
            if ItemNumber>(len(DirectoryList)-1): ItemNumber=0
        print(ItemNumber)
    elif ColumnNumber==1:
        if ItemNumber > (len(PartitionList)-1): ItemNumber = 0
    else: print("you fucked up")
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber)
    return ItemNumber

def ChangeDirectory(ItemNumber,PartitionList,ColumnNumber):
    DirectoryList=os.listdir()
    if ColumnNumber==0:
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
    elif ColumnNumber==1:
        os.chdir(PartitionList[ItemNumber])
        ItemNumber=0
        ColumnNumber=0
    else:
        print("you fucked up")
    ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber)
    return [ColumnNumber,ItemNumber]

def SwitchColumn(ItemNumber,PartitionList,KeyNumber,ColumnNumber):
    if KeyNumber==260:
        print("Left")
        if ColumnNumber==0: ColumnNumber=1
        elif ColumnNumber==1: ColumnNumber=0
        else: print("you fucked up")
    if KeyNumber==261:
        print("Right")
        if ColumnNumber==0: ColumnNumber=1
        elif ColumnNumber==1: ColumnNumber=0
        else: print("you fucked up")
    else: print("you fucked up")
    return ColumnNumber

os.system("mode con cols=80 lines=20")
stdscr=curses.initscr()
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
DirectoryList=os.listdir()
ColumnNumber=0
ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber)

while True:
    key=stdscr.getch()
    #Ctrl+x
    if key==24: break
    #Up_Arrow
    elif key==258:
        ItemNumber=ItemNumber+1
        ItemNumber=LowerItem(ItemNumber,PartitionList,ColumnNumber)
    #Down_Arrow
    elif key==259:
        ItemNumber=ItemNumber-1
        ItemNumber=UpperItem(ItemNumber,PartitionList,ColumnNumber)
    #Left_Arrow
    elif key==260:
        ColumnNumber=SwitchColumn(ItemNumber,PartitionList,key,ColumnNumber)
        ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber)
    #Right_Arrow
    elif key==261:
        ColumnNumber=SwitchColumn(ItemNumber,PartitionList,key,ColumnNumber)
        ShowWhatDirectoryContains(DirectoryList,ItemNumber,PartitionList,ColumnNumber)
    #Enter
    elif key==10:
        ColumnNumber,ItemNumber=ChangeDirectory(ItemNumber,PartitionList,ColumnNumber)
        ItemNumber=0
    else: print(key)

curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
