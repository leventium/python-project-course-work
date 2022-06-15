# -*- coding: utf-8 -*-
"""
В этом скрипте содеражатся функции для создания и обработки дополнительных окон
Авторы: Фролов К.Д., Мирошниченко Л.И.
"""

from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Treeview
from tkinter.ttk import Scrollbar
import tkinter as tki
import tkinter.ttk as ttk
import os
import sys
import pandas as pd
import numpy as np
import Base as bd


def add_window():
    """
    Функция события нажатия на кнопу "Добавить", создаёт окно принимает 
    переменные и добовляет в базу.
    Автор: Мирошниченко Л.И.
    """
    def ok_button():
        """
        Функция события нажатия на кнопу "ОК", подтверждает изменения в базе.
        Автор: Мирошниченко Л.И.
        """
        imodel = model.get()
        icompany = firm.get()
        iengine = engine.get()
        ipower = int(power.get())
        ivolume = float(volume.get())
        itax = int(tax.get())
        iconsumption = float(rashod.get())
        iprice = int(price.get())
        icolour = colour.get()
        bd.addbd(imodel, icompany, iengine, ipower, ivolume,
                 itax, iconsumption, iprice, icolour)
        addwin.destroy()
    addwin = Tk()
    addwin.title("Добавить")
    addwin.geometry('200x250')
    addwin.resizable(width=False, height=False)

    modellbl = Label(addwin, text="Модель:")
    modellbl.grid(column=0, row=1)
    model = Entry(addwin, width=15)
    model.grid(column=3, row=1)

    firmlbl = Label(addwin, text="Фирма:")
    firmlbl.grid(column=0, row=2)
    firm = Entry(addwin, width=15)
    firm.grid(column=3, row=2)

    enginelbl = Label(addwin, text="Двигатель:")
    enginelbl.grid(column=0, row=3)
    engine = Entry(addwin, width=15)
    engine.grid(column=3, row=3)

    powerlbl = Label(addwin, text="Мощность:")
    powerlbl.grid(column=0, row=4)
    power = Entry(addwin, width=15)
    power.grid(column=3, row=4)

    volumelbl = Label(addwin, text="Объём:")
    volumelbl.grid(column=0, row=5)
    volume = Entry(addwin, width=15)
    volume.grid(column=3, row=5)

    taxlbl = Label(addwin, text="Налог:")
    taxlbl.grid(column=0, row=6)
    tax = Entry(addwin, width=15)
    tax.grid(column=3, row=6)

    rashodlbl = Label(addwin, text="Расход:")
    rashodlbl.grid(column=0, row=7)
    rashod = Entry(addwin, width=15)
    rashod.grid(column=3, row=7)

    pricelbl = Label(addwin, text="Цена:")
    pricelbl.grid(column=0, row=8)
    price = Entry(addwin, width=15)
    price.grid(column=3, row=8)

    colourlbl = Label(addwin, text="Цвет:")
    colourlbl.grid(column=0, row=9)
    colour = Entry(addwin, width=15)
    colour.grid(column=3, row=9)

    cancelbtn = Button(addwin, text="Отмена", command=addwin.destroy)
    cancelbtn.grid(column=0, row=10)

    okbtn = Button(addwin, text="OK", command=ok_button)
    okbtn.grid(column=2, row=10)


def del_window():
    """
    Функция события нажатия на кнопу "Удалить", принимает номер удаляемой 
    строки и удаляет её.
    Автор: Мирошниченко Л.И.
    """
    def ok_button():
        """
        Функция события нажатия на кнопу "ОК", подтверждает изменения в базе.
        Автор: Мирошниченко Л.И.
        """
        ind = int(delno.get())
        bd.delbd(ind)
        delwin.destroy()
    delwin = Tk()
    delwin.title("Удалить")
    delwin.geometry('200x70')
    delwin.resizable(width=False, height=False)

    delno = Entry(delwin, width=5)
    delno.grid(column=3, row=1)

    dellbl = Label(delwin, text="Номер удаляемой строки:")
    dellbl.grid(column=0, row=1)

    cancelbtn = Button(delwin, text="Отмена", command=delwin.destroy)
    cancelbtn.grid(column=0, row=2)

    okbtn = Button(delwin, text="OK", command=ok_button)
    okbtn.grid(column=3, row=2)


def redact_window():
    """
    Функция события нажатия на кнопу "Редактировать", 
    принимает номер строки и новые параметры для неё.
    Автор: Мирошниченко Л.И.
    """
    def ok_button():
        """
        Функция события нажатия на кнопу "ОК", подтверждает изменения в базе.
        Автор: Мирошниченко Л.И.
        """
        redno = int(redactno.get())
        imodel = model.get()
        icompany = firm.get()
        iengine = engine.get()
        ipower = int(power.get())
        ivolume = float(volume.get())
        itax = int(tax.get())
        iconsumption = float(rashod.get())
        iprice = int(price.get())
        icolour = colour.get()
        bd.changebd(redno, imodel, icompany, iengine, ipower,
                    ivolume, itax, iconsumption, iprice, icolour)
        redactwin.destroy()
    redactwin = Tk()
    redactwin.title("Редактировать")
    redactwin.geometry('300x250')
    redactwin.resizable(width=False, height=False)

    redactnolbl = Label(redactwin, text="Редактировать номер:")
    redactnolbl.grid(column=0, row=0)
    redactno = Entry(redactwin, width=5)
    redactno.grid(column=3, row=0)

    modellbl = Label(redactwin, text="Модель:")
    modellbl.grid(column=0, row=1)
    model = Entry(redactwin, width=15)
    model.grid(column=3, row=1)

    firmlbl = Label(redactwin, text="Фирма:")
    firmlbl.grid(column=0, row=2)
    firm = Entry(redactwin, width=15)
    firm.grid(column=3, row=2)

    enginelbl = Label(redactwin, text="Двигатель:")
    enginelbl.grid(column=0, row=3)
    engine = Entry(redactwin, width=15)
    engine.grid(column=3, row=3)

    powerlbl = Label(redactwin, text="Мощность:")
    powerlbl.grid(column=0, row=4)
    power = Entry(redactwin, width=15)
    power.grid(column=3, row=4)

    volumelbl = Label(redactwin, text="Объём:")
    volumelbl.grid(column=0, row=5)
    volume = Entry(redactwin, width=15)
    volume.grid(column=3, row=5)

    taxlbl = Label(redactwin, text="Налог:")
    taxlbl.grid(column=0, row=6)
    tax = Entry(redactwin, width=15)
    tax.grid(column=3, row=6)

    rashodlbl = Label(redactwin, text="Расход:")
    rashodlbl.grid(column=0, row=7)
    rashod = Entry(redactwin, width=15)
    rashod.grid(column=3, row=7)

    pricelbl = Label(redactwin, text="Цена:")
    pricelbl.grid(column=0, row=8)
    price = Entry(redactwin, width=15)
    price.grid(column=3, row=8)

    colourlbl = Label(redactwin, text="Цвет:")
    colourlbl.grid(column=0, row=9)
    colour = Entry(redactwin, width=15)
    colour.grid(column=3, row=9)

    cancelbtn = Button(redactwin, text="Отмена", command=redactwin.destroy)
    cancelbtn.grid(column=0, row=10)

    okbtn = Button(redactwin, text="OK", command=ok_button)
    okbtn.grid(column=2, row=10)


def prosmot_window():
    """
    Функция события нажатия на кнопу "Просмотр справочников", 
    принимает номер базы и отображает эту базу на экране.
    Автор: Мирошниченко Л.И.
    """
    global spar, tree_mini, scr_mini

    def ok_button():
        """
        Функция события нажатия на кнопу "ОК", 
        подтверждает выбранную базу и выводит её на экран.
        Автор: Мирошниченко Л.И.
        """
        global spar, tree_mini, scr_mini
        ind = chose.get()
        if ind == "Справочник 1":
            tree_mini.destroy()
            scr_mini.destroy()
            columns = ("#1", "#2", "#3")
            tree_mini = Treeview(spar, show="headings",
                                 columns=columns, height=12)
            tree_mini.heading("#1", text="Модель")
            tree_mini.heading("#2", text="Фирма")
            tree_mini.heading("#3", text="Цвет")

            tree_mini.column(column="#1", width=100)
            tree_mini.column(column="#2", width=100)
            tree_mini.column(column="#3", width=100)

            tree_mini.grid(column=1, row=0)
            scr_mini = Scrollbar(spar, orient=tki.VERTICAL,
                                 command=tree_mini.yview)
            tree_mini.configure(yscroll=scr_mini.set)
            scr_mini.grid(row=0, column=2, sticky=tki.N + tki.S)
            for idx, row in bd.base1.iterrows():
                tree_mini.insert("", tki.END, values=[
                                 row["Модель"], row["Фирма"], row["Цвет"]])
        elif ind == "Справочник 2":
            tree_mini.destroy()
            scr_mini.destroy()
            columns = ("#1", "#2", "#3")
            tree_mini = Treeview(spar, show="headings",
                                 columns=columns, height=12)
            tree_mini.heading("#1", text="Двигатель")
            tree_mini.heading("#2", text="Объём")
            tree_mini.heading("#3", text="Мощность")

            tree_mini.column(column="#1", width=100)
            tree_mini.column(column="#2", width=100)
            tree_mini.column(column="#3", width=100)

            tree_mini.grid(column=1, row=0)
            scr_mini = Scrollbar(spar, orient=tki.VERTICAL,
                                 command=tree_mini.yview)
            tree_mini.configure(yscroll=scr_mini.set)
            scr_mini.grid(row=0, column=2, sticky=tki.N + tki.S)
            for idx, row in bd.base2.iterrows():
                tree_mini.insert("",
                tki.END,
                values=[
                    row["Двигатель"],
                    row["Объем"],
                    row["Мощность"]
                ])
        elif ind == "Справочник 3":
            tree_mini.destroy()
            scr_mini.destroy()
            columns = ("#1", "#2")
            tree_mini = Treeview(spar, show="headings",
                                 columns=columns, height=12)
            tree_mini.heading("#1", text="Мощность")
            tree_mini.heading("#2", text="Расход")

            tree_mini.column(column="#1", width=150)
            tree_mini.column(column="#2", width=150)

            tree_mini.grid(column=1, row=0)
            scr_mini = Scrollbar(spar, orient=tki.VERTICAL,
                                 command=tree_mini.yview)
            tree_mini.configure(yscroll=scr_mini.set)
            scr_mini.grid(row=0, column=2, sticky=tki.N + tki.S)
            for idx, row in bd.base3.iterrows():
                tree_mini.insert("", tki.END, values=[
                                 row["Мощность"], row["Расход"]])
        elif ind == "Справочник 4":
            tree_mini.destroy()
            scr_mini.destroy()
            columns = ("#1", "#2", "#3", "#4")
            tree_mini = Treeview(spar, show="headings",
                                 columns=columns, height=12)
            tree_mini.heading("#1", text="Модель")
            tree_mini.heading("#2", text="Двигатель")
            tree_mini.heading("#3", text="Налог")
            tree_mini.heading("#4", text="Цена")

            tree_mini.column(column="#1", width=75)
            tree_mini.column(column="#2", width=75)
            tree_mini.column(column="#3", width=75)
            tree_mini.column(column="#4", width=75)

            tree_mini.grid(column=1, row=0)
            scr_mini = Scrollbar(spar, orient=tki.VERTICAL,
                                 command=tree_mini.yview)
            tree_mini.configure(yscroll=scr_mini.set)
            scr_mini.grid(row=0, column=2, sticky=tki.N + tki.S)
            for idx, row in bd.base4.iterrows():
                tree_mini.insert(
                    "",
                    tki.END,
                    values=[
                        row["Модель"],
                        row["Двигатель"],
                        row["Налог"],
                        row["Цена"]
                    ])

    prosmotwin = Tk()
    prosmotwin.title("Просмотр")
    prosmotwin.geometry('320x300')
    prosmotwin.resizable(width=False, height=False)

    chose = Combobox(prosmotwin)
    chose['values'] = ("Справочник 1", "Справочник 2",
                       "Справочник 3", "Справочник 4")
    chose.current(0)
    chose.grid(column=0, row=0)

    okbtn = Button(prosmotwin, text="OK", command=ok_button)
    okbtn.grid(column=1, row=0)

    spar = Frame(prosmotwin, bg="orange")
    spar.place(relx=0, rely=0.12, relwidth=1, relheight=0.88)

    columns = ("#1", "#2", "#3")
    tree_mini = Treeview(spar, show="headings", columns=columns, height=12)
    tree_mini.heading("#1", text="Модель")
    tree_mini.heading("#2", text="Фирма")
    tree_mini.heading("#3", text="Цвет")

    tree_mini.column(column="#1", width=100)
    tree_mini.column(column="#2", width=100)
    tree_mini.column(column="#3", width=100)

    tree_mini.grid(column=1, row=0)
    scr_mini = Scrollbar(spar, orient=tki.VERTICAL, command=tree_mini.yview)
    tree_mini.configure(yscroll=scr_mini.set)
    scr_mini.grid(row=0, column=2, sticky=tki.N + tki.S)
    for idx, row in bd.base1.iterrows():
        tree_mini.insert("", tki.END, values=[
                         row["Модель"], row["Фирма"], row["Цвет"]])


def text_report():
    """
    Функция события нажатия на кнопу "Текстовый отчёт", принимает пункты
    и создаёт из базы отчёты номера котовых были выбраны.
    Автор: Мирошниченко Л.И.
    """
    global tree_rep, scr_rep

    def ok_button():
        """
        Функция события нажатия на кнопу "ОК", 
        подтверждает выбранную таблицу и выводит её на экран.
        Автор: Мирошниченко Л.И.
        """
        global tree_rep, scr_rep
        ind = chrep.get()
        if ind == "Таблица 1":
            tree_rep.destroy()
            scr_rep.destroy()
            columns = ("#1", "#2", "#3")
            tree_rep = Treeview(trep, show="headings",
                                columns=columns, height=12)
            tree_rep.heading("#1", text="Модель")
            tree_rep.heading("#2", text="Двигатель")
            tree_rep.heading("#3", text="Цена")

            tree_rep.column(column="#1", width=100)
            tree_rep.column(column="#2", width=100)
            tree_rep.column(column="#3", width=100)

            tree_rep.grid(column=1, row=0)
            scr_rep = Scrollbar(trep, orient=tki.VERTICAL,
                                command=tree_rep.yview)
            tree_rep.configure(yscroll=scr_rep.set)
            scr_rep.grid(row=0, column=2, sticky=tki.N + tki.S)
            for idx, row in bd.df1.iterrows():
                tree_rep.insert("", tki.END, values=[
                                row["Модель"], row["Двигатель"], row["Цена"]])

        elif ind == "Таблица 2":
            tree_rep.destroy()
            scr_rep.destroy()
            columns = ("#1", "#2")
            tree_rep = Treeview(trep, show="headings",
                                columns=columns, height=12)
            tree_rep.heading("#1", text="Двигатель")
            tree_rep.heading("#2", text="Мощность")

            tree_rep.column(column="#1", width=150)
            tree_rep.column(column="#2", width=150)

            tree_rep.grid(column=1, row=0)
            scr_rep = Scrollbar(trep, orient=tki.VERTICAL,
                                command=tree_rep.yview)
            tree_rep.configure(yscroll=scr_rep.set)
            scr_rep.grid(row=0, column=2, sticky=tki.N + tki.S)
            for idx, row in bd.df2.iterrows():
                tree_rep.insert("", tki.END, values=[
                                row["Двигатель"], row["Мощность"]])
        elif ind == "Таблица 3":
            tree_rep.destroy()
            scr_rep.destroy()
            columns = ("#1", "#2", "#3")
            tree_rep = Treeview(trep, show="headings",
                                columns=columns, height=12)
            tree_rep.heading("#1", text="Мощность")
            tree_rep.heading("#2", text="Объем")
            tree_rep.heading("#3", text="Налог")

            tree_rep.column(column="#1", width=100)
            tree_rep.column(column="#2", width=100)
            tree_rep.column(column="#3", width=100)

            tree_rep.grid(column=1, row=0)
            scr_rep = Scrollbar(trep, orient=tki.VERTICAL,
                                command=tree_rep.yview)
            tree_rep.configure(yscroll=scr_rep.set)
            scr_rep.grid(row=0, column=2, sticky=tki.N + tki.S)
            for idx, row in bd.df3.iterrows():
                tree_rep.insert("", tki.END, values=[
                                row["Мощность"], row["Объем"], row["Налог"]])
        """
        elif ind == "Таблица 4":
            tree_rep.destroy()
            scr_rep.destroy()
            columns = ("#1", "#2")
            tree_rep = Treeview(trep, show="headings", columns=columns, height=12)
            tree_rep.heading("#1", text="Двигатель")
            tree_rep.heading("#2", text="Мощность")
            
            #tree_rep.columns()
            
            tree_rep.grid(column=1, row=0)
            scr_rep = Scrollbar(trep, orient=tki.VERTICAL, command=tree_rep.yview)
            tree_rep.configure(yscroll=scr_rep.set)
            scr_rep.grid(row=0, column=2, sticky=tki.N + tki.S)
            for idx, row in bd.tabl1.iterrows():
                tree_rep.insert("", tki.END, 
                    values=[row["Двигатель"], row["Мощность"]])
        """

    txrep = Tk()
    txrep.title("Текстовый отчёт")
    txrep.geometry('320x300')
    txrep.resizable(width=False, height=False)
    bd.report()

    chrep = Combobox(txrep)
    chrep['values'] = ("Таблица 1", "Таблица 2", "Таблица 3",
                       "Таблица 4", "Таблица 5", "Таблица 6")
    chrep.current(0)
    chrep.grid(column=0, row=0)

    okbtn = Button(txrep, text="OK", command=ok_button)
    okbtn.grid(column=1, row=0)

    trep = Frame(txrep, bg="orange")
    trep.place(relx=0, rely=0.12, relwidth=1, relheight=0.88)

    columns = ("#1", "#2", "#3")
    tree_rep = Treeview(trep, show="headings", columns=columns, height=12)
    tree_rep.heading("#1", text="Модель")
    tree_rep.heading("#2", text="Двигатель")
    tree_rep.heading("#3", text="Цена")

    tree_rep.column(column="#1", width=100)
    tree_rep.column(column="#2", width=100)
    tree_rep.column(column="#3", width=100)

    tree_rep.grid(column=1, row=0)
    scr_rep = Scrollbar(trep, orient=tki.VERTICAL, command=tree_rep.yview)
    tree_rep.configure(yscroll=scr_rep.set)
    scr_rep.grid(row=0, column=2, sticky=tki.N + tki.S)
    for idx, row in bd.df1.iterrows():
        tree_rep.insert("", tki.END, values=[
                        row["Модель"], row["Двигатель"], row["Цена"]])


def graf_report():
    """
    Функция события нажатия на кнопу "Графический отчёт", принимает пункты
    и создаёт из базы отчёты номера котовых были выбраны.
    Автор: Мирошниченко Л.И.
    """
    def ok_button():
        """
        Функция события нажатия на кнопу "OK", принимает 
        выбранные пункты и выводит таблицы.
        Автор: Мирошниченко Л.И.
        """
        try:
            g11 = int(chk1.state()[0] == 'selected')
        except:
            g11 = 0

        try:
            g12 = int(chk1.state()[1] == 'selected')
        except:
            g12 = 0

        g1 = g11 or g12

        try:
            g21 = int(chk2.state()[0] == 'selected')
        except:
            g21 = 0

        try:
            g22 = int(chk2.state()[1] == 'selected')
        except:
            g22 = 0

        g2 = g21 or g22

        try:
            g31 = int(chk3.state()[0] == 'selected')
        except:
            g31 = 0

        try:
            g32 = int(chk3.state()[1] == 'selected')
        except:
            g32 = 0

        g3 = g31 or g32

        try:
            g41 = int(chk4.state()[0] == 'selected')
        except:
            g41 = 0

        try:
            g42 = int(chk4.state()[1] == 'selected')
        except:
            g42 = 0

        g4 = g41 or g42
        bd.build_plot(g1, g2, g3, g4)
        gfrep.destroy()

    gfrep = Tk()
    gfrep.title("Графический отчёт")
    gfrep.geometry('200x115')
    gfrep.resizable(width=False, height=False)

    chk1 = Checkbutton(gfrep, text="График 1")
    chk1.grid(column=0, row=0)

    chk2 = Checkbutton(gfrep, text="График 2")
    chk2.grid(column=0, row=1)

    chk3 = Checkbutton(gfrep, text="График 3")
    chk3.grid(column=0, row=2)

    chk4 = Checkbutton(gfrep, text="График 4")
    chk4.grid(column=0, row=3)

    cancel = Button(gfrep, text="Отмена", command=gfrep.destroy)
    cancel.grid(column=0, row=4)

    okbtn = Button(gfrep, text="OK", command=ok_button)
    okbtn.grid(column=1, row=4)


def save_window():
    """
    Функция события нажатия на кнопу "Сохранить", принимает путь к папке
    и сохраняет все базы по указанному пути.
    Автор: Мирошниченко Л.И.
    """
    def ok_button():
        """
        Функция события нажатия на кнопу "ОК", принимает указаные параметры
        и производит сохранение.
        Автор: Мирошниченко Л.И.
        """
        do_you_ktw = folder.get()
        do_you_ktw = do_you_ktw.replace('\\', '/')
        bd.savebd(do_you_ktw + "/base1.csv", do_you_ktw + "/base2.csv",
                  do_you_ktw + "/base3.csv", do_you_ktw + "/base4.csv")
        savewin.destroy()
    savewin = Tk()
    savewin.title("Сохранить")
    savewin.geometry('300x100')
    savewin.resizable(width=False, height=False)

    textlbl = Label(savewin, text="Выберите папку для сохраниния")
    textlbl.grid(column=0, row=0)

    folder = Entry(savewin, width=45)
    folder.grid(column=0, row=1)

    cancel = Button(savewin, text="Отмена", command=savewin.destroy)
    cancel.grid(column=0, row=2)

    okbtn = Button(savewin, text="OK", command=ok_button)
    okbtn.grid(column=1, row=2)