# -*- coding: utf-8 -*-

import pymssql
import tkinter as tk
import re
r1=re.compile(r'.*')
import tkinter.messagebox
import tkinter.messagebox as messagebox
from tkinter import StringVar

#sql服务器名，这里(127.0.0.1)是本地数据库IP
serverName = 'localhost'
#登陆用户名和密码
userName = 'sa'
passWord = '123456'
#建立连接并获取cursor
con = pymssql.connect(serverName , userName , passWord, "BookShop")

def  click_query_author(data,root):
    if str(data).startswith('张'):
        cur1 = con.cursor()
        # 执行sql语句
        cur1.execute('exec Query_Book_Author @Bauthor=张嘉佳')
        data1=cur1.fetchall()
        r=data1[0]
        for a in r:
            a1=tk.Label(root, text=a)
            a1.pack()

    elif str(data).startswith('林汉'):
        cur2 = con.cursor()
        # 执行sql语句
        cur2.execute('exec Query_Book_Author @Bauthor=林汉达')
        data2=cur2.fetchall()
        s=data2[0]
        for b in s:
            b1=tk.Label(root, text=b)
            b1.pack()

    elif str(data).startswith('谷'):
        cur3 = con.cursor()
        # 执行sql语句
        cur3.execute('exec Query_Book_Author @Bauthor=谷崎润一郎')
        data3=cur3.fetchall()
        t=data3[0]
        for c in t:
            c1=tk.Label(root, text=c)
            c1.pack()

    elif str(data).startswith('叶'):
        cur4 = con.cursor()
        # 执行sql语句
        cur4.execute('exec Query_Book_Author @Bauthor=叶楚桥')
        data4=cur4.fetchall()
        u=data4[0]
        for d in u:
            d1=tk.Label(root, text=d)
            d1.pack()

    elif str(data).startswith('林海'):
        cur5 = con.cursor()
        # 执行sql语句
        cur5.execute('exec Query_Book_Author @Bauthor=林海英')
        data5 = cur5.fetchall()
        v = data5[0]
        for e in v:
            e1 = tk.Label(root, text=e)
            e1.pack()

    elif str(data).startswith('丹'):
        cur6 = con.cursor()
        # 执行sql语句
        cur6.execute('exec Query_Book_Author @Bauthor=丹尼尔笛福')
        data6=cur6.fetchall()
        w=data6[0]
        for f in w:
            f1=tk.Label(root, text=f)
            f1.pack()

    elif str(data).startswith('蕾'):
        cur7 = con.cursor()
        # 执行sql语句
        cur7.execute('exec Query_Book_Author @Bauthor=蕾切尔卡斯克')
        data7 = cur7.fetchall()
        x = data7[0]
        for g in x:
            g1 = tk.Label(root, text=g)
            g1.pack()
def  click_query_bname(data,root):
    if str(data).startswith('鲁'):
        cur1 = con.cursor()
        # 执行sql语句
        cur1.execute('exec Query_Book_BName @Bname=鲁冰逊漂流记')
        data1=cur1.fetchall()
        r=data1[0]
        for a in r:
            a1=tk.Label(root, text=a)
            a1.pack()

    elif str(data).startswith('上'):
        cur2 = con.cursor()
        # 执行sql语句
        cur2.execute('exec Query_Book_BName @Bname=上下五千年')
        data2=cur2.fetchall()
        s=data2[0]
        for b in s:
            b1=tk.Label(root, text=b)
            b1.pack()

    elif str(data).startswith('桃'):
        cur3 = con.cursor()
        # 执行sql语句
        cur3.execute('exec Query_Book_BName @Bname=桃李春风一杯酒')
        data3=cur3.fetchall()
        t=data3[0]
        for c in t:
            c1=tk.Label(root, text=c)
            c1.pack()

    elif str(data).startswith('春'):
        cur4 = con.cursor()
        # 执行sql语句
        cur4.execute('exec Query_Book_BName @Bname=春琴抄')
        data4=cur4.fetchall()
        u=data4[0]
        for d in u:
            d1=tk.Label(root, text=d)
            d1.pack()

    elif str(data).startswith('成'):
        cur5 = con.cursor()
        # 执行sql语句
        cur5.execute('exec Query_Book_BName @Bname=成为母亲')
        data5 = cur5.fetchall()
        v = data5[0]
        for e in v:
            e1 = tk.Label(root, text=e)
            e1.pack()

    elif str(data).startswith('从'):
        cur6 = con.cursor()
        # 执行sql语句
        cur6.execute('exec Query_Book_BName @Bname=从你的全世界路过')
        data6=cur6.fetchall()
        w=data6[0]
        for f in w:
            f1=tk.Label(root, text=f)
            f1.pack()

    elif str(data).startswith('城'):
        cur7 = con.cursor()
        # 执行sql语句
        cur7.execute('exec Query_Book_BName @Bname=城南旧事')
        data7 = cur7.fetchall()
        x = data7[0]
        for g in x:
            g1 = tk.Label(root, text=g)
            g1.pack()
def  click_query_isbn(data,root):
    if str(data).startswith('A'):
        cur1 = con.cursor()
        # 执行sql语句
        cur1.execute('exec Query_Book_ISBN @ISBN=A00001')
        data1=cur1.fetchall()
        r=data1[0]
        for a in r:
            a1=tk.Label(root, text=a)
            a1.pack()

    elif str(data).startswith('B'):
        cur2 = con.cursor()
        # 执行sql语句
        cur2.execute('exec Query_Book_ISBN @ISBN=B00001')
        data2=cur2.fetchall()
        s=data2[0]
        for b in s:
            b1=tk.Label(root, text=b)
            b1.pack()

    elif str(data).startswith('C00002'):
        cur3 = con.cursor()
        # 执行sql语句
        cur3.execute('exec Query_Book_ISBN @ISBN=C00002')
        data3=cur3.fetchall()
        t=data3[0]
        for c in t:
            c1=tk.Label(root, text=c)
            c1.pack()

    elif str(data).startswith('D'):
        cur4 = con.cursor()
        # 执行sql语句
        cur4.execute('exec Query_Book_ISBN @ISBN=D00001')
        data4=cur4.fetchall()
        u=data4[0]
        for d in u:
            d1=tk.Label(root, text=d)
            d1.pack()

    elif str(data).startswith('E'):
        cur5 = con.cursor()
        # 执行sql语句
        cur5.execute('exec Query_Book_ISBN @ISBN=E00001')
        data5 = cur5.fetchall()
        v = data5[0]
        for e in v:
            e1 = tk.Label(root, text=e)
            e1.pack()

    elif str(data).startswith('F'):
        cur6 = con.cursor()
        # 执行sql语句
        cur6.execute('exec Query_Book_ISBN @ISBN=F00001')
        data6=cur6.fetchall()
        w=data6[0]
        for f in w:
            f1=tk.Label(root, text=f)
            f1.pack()

    elif str(data).startswith('C00001'):
        cur7 = con.cursor()
        # 执行sql语句
        cur7.execute('exec Query_Book_ISBN @ISBN=C00001')
        data7 = cur7.fetchall()
        x = data7[0]
        for g in x:
            g1 = tk.Label(root, text=g)
            g1.pack()
def  click_query_brnumber(data,root):
    if str(data).startswith('171'):
        cur1 = con.cursor()
        # 执行sql语句
        cur1.execute('exec Query_Book_Author @Bauthor=鲁冰逊漂流记')
        data1=cur1.fetchall()
        r=data1[0]
        for a in r:
            a1=tk.Label(root, text=a)
            a1.pack()

    elif str(data).startswith('上'):
        cur2 = con.cursor()
        # 执行sql语句
        cur2.execute('exec Query_Bookreader_BR# @Bauthor=1711216')
        data2=cur2.fetchall()
        s=data2[0]
        for b in s:
            b1=tk.Label(root, text=b)
            b1.pack()

    elif str(data).startswith('1759115'):
        cur3 = con.cursor()
        # 执行sql语句
        cur3.execute('exec Query_Bookreader_BR# @BR#=1759115')
        data3=cur3.fetchall()
        t=data3[0]
        for c in t:
            c1=tk.Label(root, text=c)
            c1.pack()

    elif str(data).startswith('1759116'):
        cur4 = con.cursor()
        # 执行sql语句
        cur4.execute('exec Query_Bookreader_BR# @BR#=1759116')
        data4=cur4.fetchall()
        u=data4[0]
        for d in u:
            d1=tk.Label(root, text=d)
            d1.pack()

    elif str(data).startswith('1759117'):
        cur5 = con.cursor()
        # 执行sql语句
        cur5.execute('exec Query_Bookreader_BR# @BR#=1759117')
        data5 = cur5.fetchall()
        v = data5[0]
        for e in v:
            e1 = tk.Label(root, text=e)
            e1.pack()

    elif str(data).startswith('1759119'):
        cur6 = con.cursor()
        # 执行sql语句
        cur6.execute('exec Query_Bookreader_BR# @BR#=1759119')
        data6=cur6.fetchall()
        w=data6[0]
        for f in w:
            f1=tk.Label(root, text=f)
            f1.pack()

    elif str(data).startswith('1759140'):
        cur7 = con.cursor()
        # 执行sql语句
        cur7.execute('exec Query_Bookreader_BR# @BR#=1759140')
        data7 = cur7.fetchall()
        x = data7[0]
        for g in x:
            g1 = tk.Label(root, text=g)
            g1.pack()
def  click_query_brname(data,root):
    if str(data).startswith('鲁'):
        cur1 = con.cursor()
        # 执行sql语句
        cur1.execute('exec Query_Bookreader_BRname @BRname=鲁冰逊漂流记')
        data1=cur1.fetchall()
        r=data1[0]
        for a in r:
            a1=tk.Label(root, text=a)
            a1.pack()

    elif str(data).startswith('蔡'):
        cur2 = con.cursor()
        # 执行sql语句
        cur2.execute('exec Query_Bookreader_BRname @BRname=蔡佳泉')
        data2=cur2.fetchall()
        s=data2[0]
        for b in s:
            b1=tk.Label(root, text=b)
            b1.pack()

    elif str(data).startswith('岑'):
        cur3 = con.cursor()
        # 执行sql语句
        cur3.execute('exec Query_Bookreader_BRname @BRname=岑拓望')
        data3=cur3.fetchall()
        t=data3[0]
        for c in t:
            c1=tk.Label(root, text=c)
            c1.pack()

    elif str(data).startswith('钟'):
        cur4 = con.cursor()
        # 执行sql语句
        cur4.execute('exec Query_Bookreader_BRname @BRname=钟宇航')
        data4=cur4.fetchall()
        u=data4[0]
        for d in u:
            d1=tk.Label(root, text=d)
            d1.pack()

    elif str(data).startswith('何'):
        cur5 = con.cursor()
        # 执行sql语句
        cur5.execute('exec Query_Bookreader_BRname @BRname=何昌霖')
        data5 = cur5.fetchall()
        v = data5[0]
        for e in v:
            e1 = tk.Label(root, text=e)
            e1.pack()

    elif str(data).startswith('乔伯'):
        cur6 = con.cursor()
        # 执行sql语句
        cur6.execute('exec Query_Bookreader_BRname @BRname=乔伯昱')
        data6=cur6.fetchall()
        w=data6[0]
        for f in w:
            f1=tk.Label(root, text=f)
            f1.pack()

    elif str(data).startswith('贺'):
        cur7 = con.cursor()
        # 执行sql语句
        cur7.execute('exec Query_Bookreader_BRname @BRname=贺依凡')
        data7 = cur7.fetchall()
        x = data7[0]
        for g in x:
            g1 = tk.Label(root, text=g)
            g1.pack()

def qurey_author():
    window = tk.Tk()  # 创建窗口
    window.title("读者")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,
             text='欢迎使用图书管理系统',  # 文本
             bg='green',  # 字体的背景颜色
             font=('Arial', 12),  # 字体和大小
             width=30, height=2  # 字体所占的宽度和高度
             )
    k.pack()  # 固定
    # 以上是窗口的主体

    menubar = tk.Menu(window)  # 在窗口上添加菜单栏
    filemenu = tk.Menu(menubar, tearoff=0)  # filemenu放在menu中
    submenu = tk.Menu(filemenu, tearoff=0)  # submenu放在filemenu中
    menubar.add_cascade(label='嘿嘿嘿', menu=filemenu)  # add_cascade用来创建下拉栏，filemenu命名为File
    filemenu.add_cascade(label='小组成员', menu=submenu)
    submenu.add_cascade(label='钟宇航')
    submenu.add_cascade(label='岑拓望')
    submenu.add_cascade(label='蔡佳泉')
    submenu.add_cascade(label='何昌霖')
    submenu.add_cascade(label='乔伯昱')
    submenu.add_cascade(label='贺依凡')
    filemenu.add_command(label='退出', command=quit)  # add_command用来创建命令栏，不可有子项
    window.config(menu=menubar)  # 创建完毕

    # 在`window`上创建一个`frame`
    frm = tk.Frame(window)
    frm.pack()
    # 在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`
    frm_l = tk.Frame(frm)
    frm_r = tk.Frame(frm)
    # 这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
    frm_l.pack(side='left')
    frm_r.pack(side='right')

    tk.Label(frm_l, text='请输入作者名字:').pack()

    var1 = StringVar()
    e = tk.Entry(window,textvariable=var1)
    e.pack()
    e.get()
    type(e.get())

    b = tk.Button(window, text='查询', width=14, height=1, command=lambda: click_query_author(e.get(),window))
    b.pack()

    # 提交修改
    con.commit()

    window.mainloop()  # 结束（不停循环刷新）
def qurey_bname():
    window = tk.Tk()  # 创建窗口
    window.title("读者")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,
             text='欢迎使用图书管理系统',  # 文本
             bg='green',  # 字体的背景颜色
             font=('Arial', 12),  # 字体和大小
             width=30, height=2  # 字体所占的宽度和高度
             )
    k.pack()  # 固定
    # 以上是窗口的主体

    menubar = tk.Menu(window)  # 在窗口上添加菜单栏
    filemenu = tk.Menu(menubar, tearoff=0)  # filemenu放在menu中
    submenu = tk.Menu(filemenu, tearoff=0)  # submenu放在filemenu中
    menubar.add_cascade(label='嘿嘿嘿', menu=filemenu)  # add_cascade用来创建下拉栏，filemenu命名为File
    filemenu.add_cascade(label='小组成员', menu=submenu)
    submenu.add_cascade(label='钟宇航')
    submenu.add_cascade(label='岑拓望')
    submenu.add_cascade(label='蔡佳泉')
    submenu.add_cascade(label='何昌霖')
    submenu.add_cascade(label='乔伯昱')
    submenu.add_cascade(label='贺依凡')
    filemenu.add_command(label='退出', command=quit)  # add_command用来创建命令栏，不可有子项
    window.config(menu=menubar)  # 创建完毕

    # 在`window`上创建一个`frame`
    frm = tk.Frame(window)
    frm.pack()
    # 在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`
    frm_l = tk.Frame(frm)
    frm_r = tk.Frame(frm)
    # 这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
    frm_l.pack(side='left')
    frm_r.pack(side='right')

    tk.Label(frm_l, text='请输入书名:').pack()

    var1 = StringVar()
    e = tk.Entry(window,textvariable=var1)
    e.pack()
    e.get()
    type(e.get())

    b11 = tk.Button(window, text='查询', width=14, height=1, command=lambda: click_query_bname(e.get(),window))
    b11.pack()

    # 提交修改
    con.commit()

    window.mainloop()  # 结束（不停循环刷新）
def qurey_isbn():
    window = tk.Tk()  # 创建窗口
    window.title("读者")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,
             text='欢迎使用图书管理系统',  # 文本
             bg='green',  # 字体的背景颜色
             font=('Arial', 12),  # 字体和大小
             width=30, height=2  # 字体所占的宽度和高度
             )
    k.pack()  # 固定
    # 以上是窗口的主体

    menubar = tk.Menu(window)  # 在窗口上添加菜单栏
    filemenu = tk.Menu(menubar, tearoff=0)  # filemenu放在menu中
    submenu = tk.Menu(filemenu, tearoff=0)  # submenu放在filemenu中
    menubar.add_cascade(label='嘿嘿嘿', menu=filemenu)  # add_cascade用来创建下拉栏，filemenu命名为File
    filemenu.add_cascade(label='小组成员', menu=submenu)
    submenu.add_cascade(label='钟宇航')
    submenu.add_cascade(label='岑拓望')
    submenu.add_cascade(label='蔡佳泉')
    submenu.add_cascade(label='何昌霖')
    submenu.add_cascade(label='乔伯昱')
    submenu.add_cascade(label='贺依凡')
    filemenu.add_command(label='退出', command=quit)  # add_command用来创建命令栏，不可有子项
    window.config(menu=menubar)  # 创建完毕

    # 在`window`上创建一个`frame`
    frm = tk.Frame(window)
    frm.pack()
    # 在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`
    frm_l = tk.Frame(frm)
    frm_r = tk.Frame(frm)
    # 这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
    frm_l.pack(side='left')
    frm_r.pack(side='right')

    tk.Label(frm_l, text='请输入ISBN:').pack()

    var1 = StringVar()
    e = tk.Entry(window,textvariable=var1)
    e.pack()
    e.get()
    type(e.get())

    b = tk.Button(window, text='查询', width=14, height=1, command=lambda: click_query_isbn(e.get(),window))
    b.pack()

    # 提交修改
    con.commit()

    window.mainloop()  # 结束（不停循环刷新）
def qurey_brnumber():
    window = tk.Tk()  # 创建窗口
    window.title("读者")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,
             text='欢迎使用图书管理系统',  # 文本
             bg='green',  # 字体的背景颜色
             font=('Arial', 12),  # 字体和大小
             width=30, height=2  # 字体所占的宽度和高度
             )
    k.pack()  # 固定
    # 以上是窗口的主体

    menubar = tk.Menu(window)  # 在窗口上添加菜单栏
    filemenu = tk.Menu(menubar, tearoff=0)  # filemenu放在menu中
    submenu = tk.Menu(filemenu, tearoff=0)  # submenu放在filemenu中
    menubar.add_cascade(label='嘿嘿嘿', menu=filemenu)  # add_cascade用来创建下拉栏，filemenu命名为File
    filemenu.add_cascade(label='小组成员', menu=submenu)
    submenu.add_cascade(label='钟宇航')
    submenu.add_cascade(label='岑拓望')
    submenu.add_cascade(label='蔡佳泉')
    submenu.add_cascade(label='何昌霖')
    submenu.add_cascade(label='乔伯昱')
    submenu.add_cascade(label='贺依凡')
    filemenu.add_command(label='退出', command=quit)  # add_command用来创建命令栏，不可有子项
    window.config(menu=menubar)  # 创建完毕

    # 在`window`上创建一个`frame`
    frm = tk.Frame(window)
    frm.pack()
    # 在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`
    frm_l = tk.Frame(frm)
    frm_r = tk.Frame(frm)
    # 这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
    frm_l.pack(side='left')
    frm_r.pack(side='right')

    tk.Label(frm_l, text='请输入您的编号:').pack()

    var1 = StringVar()
    e = tk.Entry(window,textvariable=var1)
    e.pack()
    e.get()
    type(e.get())

    b = tk.Button(window, text='查询', width=14, height=1, command=lambda: click_query_brnumber(e.get(),window))
    b.pack()

    # 提交修改
    con.commit()

    window.mainloop()  # 结束（不停循环刷新）
def qurey_brname():
    window = tk.Tk()  # 创建窗口
    window.title("读者")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,
             text='欢迎使用图书管理系统',  # 文本
             bg='green',  # 字体的背景颜色
             font=('Arial', 12),  # 字体和大小
             width=30, height=2  # 字体所占的宽度和高度
             )
    k.pack()  # 固定
    # 以上是窗口的主体

    menubar = tk.Menu(window)  # 在窗口上添加菜单栏
    filemenu = tk.Menu(menubar, tearoff=0)  # filemenu放在menu中
    submenu = tk.Menu(filemenu, tearoff=0)  # submenu放在filemenu中
    menubar.add_cascade(label='嘿嘿嘿', menu=filemenu)  # add_cascade用来创建下拉栏，filemenu命名为File
    filemenu.add_cascade(label='小组成员', menu=submenu)
    submenu.add_cascade(label='钟宇航')
    submenu.add_cascade(label='岑拓望')
    submenu.add_cascade(label='蔡佳泉')
    submenu.add_cascade(label='何昌霖')
    submenu.add_cascade(label='乔伯昱')
    submenu.add_cascade(label='贺依凡')
    filemenu.add_command(label='退出', command=quit)  # add_command用来创建命令栏，不可有子项
    window.config(menu=menubar)  # 创建完毕

    # 在`window`上创建一个`frame`
    frm = tk.Frame(window)
    frm.pack()
    # 在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`
    frm_l = tk.Frame(frm)
    frm_r = tk.Frame(frm)
    # 这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
    frm_l.pack(side='left')
    frm_r.pack(side='right')

    tk.Label(frm_l, text='请输入您的姓名:').pack()

    var1 = StringVar()
    e = tk.Entry(window,textvariable=var1)
    e.pack()
    e.get()
    type(e.get())

    b = tk.Button(window, text='查询', width=14, height=1, command=lambda: click_query_brname(e.get(),window))
    b.pack()

    # 提交修改
    con.commit()

    window.mainloop()  # 结束（不停循环刷新）
# 五个存储过程

def reader():
    window = tk.Tk()  # 创建窗口
    window.title("读者")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,text='欢迎使用图书管理系统',  # 文本
             bg='green',  # 字体的背景颜色
             font=('Arial', 12),  # 字体和大小
             width=30, height=2  # 字体所占的宽度和高度
             )
    k.pack()  # 固定
    # 以上是窗口的主体

    menubar = tk.Menu(window)  # 在窗口上添加菜单栏
    filemenu = tk.Menu(menubar, tearoff=0)  # filemenu放在menu中
    submenu = tk.Menu(filemenu, tearoff=0)  # submenu放在filemenu中
    menubar.add_cascade(label='嘿嘿嘿', menu=filemenu)  # add_cascade用来创建下拉栏，filemenu命名为File
    filemenu.add_cascade(label='小组成员', menu=submenu)
    submenu.add_cascade(label='钟宇航')
    submenu.add_cascade(label='岑拓望')
    submenu.add_cascade(label='蔡佳泉')
    submenu.add_cascade(label='何昌霖')
    submenu.add_cascade(label='乔伯昱')
    submenu.add_cascade(label='贺依凡')
    filemenu.add_command(label='退出', command=quit)  # add_command用来创建命令栏，不可有子项
    window.config(menu=menubar)  # 创建完毕

    tk.Label(window, text='图书信息:').pack()

    b1 = tk.Button(window,text = '通过作者查询',width = 14 , height = 1,command=qurey_author)
    b1.pack()

    b2 = tk.Button(window, text='通过书名查询', width=14, height=1,command=qurey_bname)
    b2.pack()

    b3 = tk.Button(window, text='通过ISBN查询', width=14, height=1,command=qurey_isbn)
    b3.pack()

    tk.Label(window, text='读者信息:').pack()

    b4 = tk.Button(window, text='通过编号查询', width=14, height=1,command=qurey_brnumber)
    b4.pack()

    b5 = tk.Button(window, text='通过姓名查询', width=14, height=1,command=qurey_brname)
    b5.pack()

    window.mainloop()  # 结束（不停循环刷新）
# 读者子窗口
def manager():
    window = tk.Tk()  # 创建窗口
    window.title("管理员")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,
             text='欢迎使用图书管理系统',  # 文本
             bg='green',  # 字体的背景颜色
             font=('Arial', 12),  # 字体和大小
             width=30, height=2  # 字体所占的宽度和高度
             )
    k.pack()  # 固定
    # 以上是窗口的主体

    menubar = tk.Menu(window)  # 在窗口上添加菜单栏
    filemenu = tk.Menu(menubar, tearoff=0)  # filemenu放在menu中
    submenu = tk.Menu(filemenu, tearoff=0)  # submenu放在filemenu中
    menubar.add_cascade(label='嘿嘿嘿', menu=filemenu)  # add_cascade用来创建下拉栏，filemenu命名为File
    filemenu.add_cascade(label='小组成员', menu=submenu)
    submenu.add_cascade(label='钟宇航')
    submenu.add_cascade(label='岑拓望')
    submenu.add_cascade(label='蔡佳泉')
    submenu.add_cascade(label='何昌霖')
    submenu.add_cascade(label='乔伯昱')
    submenu.add_cascade(label='贺依凡')
    filemenu.add_command(label='退出', command=quit)  # add_command用来创建命令栏，不可有子项
    window.config(menu=menubar)  # 创建完毕

    tk.Label(window, text='请选择功能:').pack()

    b1 = tk.Button(window,text = '借阅图书',width = 14 , height = 1,)
    b1.pack()

    b2 = tk.Button(window, text='归还图书', width=14, height=1, )
    b2.pack()

    b3 = tk.Button(window, text='购买图书', width=14, height=1, )
    b3.pack()

    b3 = tk.Button(window, text='注销图书', width=14, height=1, )
    b3.pack()

    b4 = tk.Button(window, text='征订图书', width=14, height=1, )
    b4.pack()

    b4 = tk.Button(window, text='管理图书信息', width=14, height=1, )
    b4.pack()

    b4 = tk.Button(window, text='管理读者信息', width=14, height=1, )
    b4.pack()

    window.mainloop()  # 结束（不停循环刷新）
# 管理员子窗口
def quie():
    root = tk()
    root.quit()

def main():
    window = tk.Tk()  # 创建窗口
    window.title("图书管理系统")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,
            text='欢迎使用图书管理系统',  # 文本
            bg='green',  # 字体的背景颜色
            font=('Arial', 12),  # 字体和大小
            width=30, height=2  # 字体所占的宽度和高度
            )
    k.pack()  # 固定
    # 以上是窗口的主体

    menubar = tk.Menu(window)  # 在窗口上添加菜单栏
    filemenu = tk.Menu(menubar, tearoff=0)  # filemenu放在menu中
    submenu = tk.Menu(filemenu, tearoff=0)  # submenu放在filemenu中
    menubar.add_cascade(label='嘿嘿嘿', menu=filemenu)  # add_cascade用来创建下拉栏，filemenu命名为File
    filemenu.add_cascade(label='小组成员', menu=submenu)
    submenu.add_cascade(label='钟宇航')
    submenu.add_cascade(label='岑拓望')
    submenu.add_cascade(label='蔡佳泉')
    submenu.add_cascade(label='何昌霖')
    submenu.add_cascade(label='乔伯昱')
    submenu.add_cascade(label='贺依凡')
    filemenu.add_command(label='退出',command=quit)  # add_command用来创建命令栏，不可有子项
    window.config(menu=menubar)  # 创建完毕

    tk.Label(window, text='请选择你的身份:').pack()

    # 在`window`上创建一个`frame`
    frm = tk.Frame(window)
    frm.pack()
    # 在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`
    frm_l = tk.Frame(frm)
    frm_r = tk.Frame(frm)
    # 这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
    frm_l.pack(side='left')
    frm_r.pack(side='right')

    b1 = tk.Button(frm_l,text='读者',width=14, height=1,command=reader)
    b1.pack()

    b2 = tk.Button(frm_r,text='管理员',width=14, height=1,command=manager)
    b2.pack()

    window.mainloop()  # 结束（不停循环刷新）
# 主窗口
if __name__ == '__main__':
    main()

# tk.messagebox.showinfo(title=' ', message=' ')  # 提示信息对话窗
# tk.messagebox.showwarning(title=' ', message=' ')  # 提出警告对话窗
# tk.messagebox.showerror(title=' ', message=' ')  # 提出错误对话窗
# tk.messagebox.askquestion(title=' ', message=' ')  # 询问选择对话窗

# conn.close()

