from tkinter import *
from tkinter.filedialog import *
import  win32ui
# root = Tk()
# fd=LoadFileDialog(root)
# Filename=fd.go()
# print(Filename)
dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName() # 获取选择的文件名称
print (filename)