# -*- coding: utf-8 -*-
"""
В этом скрипте содеражатся главная функция и функции её обработки
Авторы: Фролов К.Д., Мирошниченко Л.И.
"""

#from tkinter import *
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
sys.path.insert(0,"/home/leon/Documents/Docs/Work/")
import Base as bd
import win_functions as wf


def take_ini():
    """
    Функция производящая парсинг файла settings.ini.
    Автор: Мирошниченко Л.И.
    """
    global buttonStyle
    global labelStyle
    global entryStyle
    with open("./data/settings.ini", "r") as f:
        for i in f:
            j = i.split(sep=" = ")
            if j[0] == "buttonStyle":
                buttonStyle = eval(j[1])
            elif j[0] == "labelStyle":
                labelStyle = eval(j[1])
            elif j[0] == "entryStyle":
                entryStyle = eval(j[1])


def refresh():
    """
    Функция события нажатия на кнопу "Обновить", обновляет таблицу на экране.
    Автор: Мирошниченко Л.И.
    """
    global showbase
    global tree
    global scr
    tree.destroy()
    scr.destroy()
    columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10")
    tree = Treeview(showbase, show="headings", columns=columns, height=25)
    tree.heading("#1", text="№")
    tree.heading("#2", text="Модель")
    tree.heading("#3", text="Фирма")
    tree.heading("#4", text="Двигатель")
    tree.heading("#5", text="Мощность")
    tree.heading("#6", text="Объем")
    tree.heading("#7", text="Налог")
    tree.heading("#8", text="Расход")
    tree.heading("#9", text="Цена")
    tree.heading("#10", text="Цвет")
    
    tree.column(column="#1", width=50)
    tree.column(column="#2", width=100)
    tree.column(column="#3", width=100)
    tree.column(column="#4", width=100)
    tree.column(column="#5", width=100)
    tree.column(column="#6", width=100)
    tree.column(column="#7", width=100)
    tree.column(column="#8", width=100)
    tree.column(column="#9", width=100)
    tree.column(column="#10", width=100)
    
    tree.grid(column=1, row=0)
    bd.convert()
    scr = Scrollbar(showbase, orient=tki.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scr.set)
    scr.grid(row=0, column=2, sticky=tki.N + tki.S)
    for idx, row in bd.data.iterrows():
        tree.insert(
            "",
            tki.END,
            values=[
                row["Index"],
                row["Модель"],
                row["Фирма"],
                row["Двигатель"],
                row["Мощность"],
                row["Объем"],
                row["Налог"],
                row["Расход"],
                row["Цена"],
                row["Цвет"]
            ]
        )


os.chdir("/home/leon/Documents/Docs/Work")

buttonStyle = dict()
labelStyle = dict()
entryStyle = dict()
take_ini()

root = Tk()
root.title("Main")
root.geometry('970x585')
root.resizable(width=False, height=False)

bd.base1 = pd.DataFrame()
bd.base2 = pd.DataFrame()
bd.base3 = pd.DataFrame()
bd.base4 = pd.DataFrame()
bd.data = pd.DataFrame()

bd.readbd(
    './data/base1.csv',
    './data/base2.csv',
    './data/base3.csv',
    './data/base4.csv'
)
bd.convert()


dobavit = Button(root, text="Добавить", command=wf.add_window)
dobavit.grid(column=0, row=0)

udalit = Button(root, text="Удалить", command=wf.del_window)
udalit.grid(column=1, row=0)

redact = Button(root, text="Редактировать", command=wf.redact_window)
redact.grid(column=2, row=0)

prosmot = Button(
    root, text="Просмотр\n справочников", command=wf.prosmot_window)
prosmot.grid(column=3, row=0)

texto = Button(root, text="Текстовый\n отчёт", command=wf.text_report)
texto.grid(column=4, row=0)

grafo = Button(root, text="Графический\n отчёт", command=wf.graf_report)
grafo.grid(column=5, row=0)

sohr = Button(root, text="Сохранить", command=wf.save_window)
sohr.grid(column=6, row=0)

refbtn = Button(root, text="Обновить\n таблицу", command=refresh)
refbtn.grid(column=7, row=0)

showbase = Frame(root, bg="orange")
showbase.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10")
tree = Treeview(showbase, show="headings", columns=columns, height=25)
tree.heading("#1", text="№")
tree.heading("#2", text="Модель")
tree.heading("#3", text="Фирма")
tree.heading("#4", text="Двигатель")
tree.heading("#5", text="Мощность")
tree.heading("#6", text="Объем")
tree.heading("#7", text="Налог")
tree.heading("#8", text="Расход")
tree.heading("#9", text="Цена")
tree.heading("#10", text="Цвет")

tree.column(column="#1", width=50)
tree.column(column="#2", width=100)
tree.column(column="#3", width=100)
tree.column(column="#4", width=100)
tree.column(column="#5", width=100)
tree.column(column="#6", width=100)
tree.column(column="#7", width=100)
tree.column(column="#8", width=100)
tree.column(column="#9", width=100)
tree.column(column="#10", width=100)

tree.grid(column=1, row=0)
scr = Scrollbar(showbase, orient=tki.VERTICAL, command=tree.yview)
tree.configure(yscroll=scr.set)
scr.grid(row=0, column=2, sticky=tki.N + tki.S)
for idx, row in bd.data.iterrows():
    tree.insert(
        "",
        tki.END,
        values=[
            row["Index"],
            row["Модель"],
            row["Фирма"],
            row["Двигатель"],
            row["Мощность"],
            row["Объем"],
            row["Налог"],
            row["Расход"],
            row["Цена"],
            row["Цвет"]
        ]
    )

root.mainloop()