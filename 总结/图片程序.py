def pin():
    print('wqeqwwqe')



from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
window = Tk()   #创建一个窗口
window.title('爱你吆')   #定义窗口标题
window.geometry('400x400+800+200')   #定义窗口大小    窗口显示位置
# window.protocol('WM_DELETE_WINDOW', pin)  #摧毁窗口，引到另一个函数命令
window.protocol('WM_DELETE_WINDOW')
##############
label = Label(window, text='hey,小姐姐', font=("微软雅黑", 15))
# text 窗口文本  font 设置字体   fg设置字体颜色
label.grid(row=10, column=10)  # 网格布局   显示位置
################# 人
window=mainloop()