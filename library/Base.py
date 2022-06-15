"""
В этом скрипте содеражатся функции для работы с базой данных
Авторы: Фролов К.Д., Мирошниченко Л.И., Анисимов М.А.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


def readbd(fname1, fname2, fname3, fname4):
    """
    Функция считывает базу данных из файла с именами fname1, fname2, 
    fname3, fname4 и записывает ее в оперативную память 
    fname1, fname2, fname3, fname4 - имена файлов с базой данных
    base1, base2, base3, base4 - база данных в четырех справочниках
    Автор: Фролов К.Д.
    """
    global base1, base2, base3, base4
    base1 = pd.read_csv(fname1, delimiter=',',
                        names=['Модель', 'Фирма', 'Цвет'])
    base2 = pd.read_csv(fname2, delimiter=',',
                        names=['Двигатель', 'Объем', 'Мощность'])
    base3 = pd.read_csv(fname3, delimiter=',',
                        names=['Мощность', 'Расход'])
    base4 = pd.read_csv(fname4, delimiter=',',
                        names=['Модель', 'Двигатель', 'Налог', 'Цена'])


def savebd(fname1, fname2, fname3, fname4):
    """
    Функция сохраняет базу данных в четырех справочниках base1, base2, 
    base3, base4 в файлы с именами fname1, fname2, fname3, fname4
    fname1, fname2, fname3, fname4 - имена фaйлов с базой данных
    base1, base2, base3, base4 - база данных в четырех справочниках
    Автор: Фролов К.Д.
    """
    global base1, base2, base3, base4
    base1.to_csv(fname1, index=False)
    base2.to_csv(fname2, index=False)
    base3.to_csv(fname3, index=False)
    base4.to_csv(fname4, index=False)


def delbd(ind):
    """
    Функция удаляет конкретную автомобиль по номеру в списке
    base1, base2, base3, base4 - база данных в четырех справочниках
    ind - индекс автомобиля
    Автор: Фролов К.Д.
    """
    global base1, base2, base3, base4
    mod = base4.loc[ind, 'Модель']
    fl = 0
    for i in range(len(base4.index)):
        if (base4.loc[i, 'Модель'] == mod) and (fl == 1):
            fl = 2
        elif (base4.loc[i, 'Модель'] == mod) and (fl == 0):
            fl = 1
    if fl == 1:
        for i in range(len(base1.index)):
            if base1.loc[i, 'Модель'] == mod:
                base1.drop(index=[i], inplace=True)
        base1 = base1.reset_index(drop=True)
    mod = base4.loc[ind, 'Двигатель']
    fl = 0
    for i in range(len(base4.index)):
        if (base4.loc[i, 'Двигатель'] == mod) and (fl == 1):
            fl = 2
        elif (base4.loc[i, 'Двигатель'] == mod) and (fl == 0):
            fl = 1
    if fl == 1:
        for i in range(len(base2.index)):
            if base2.loc[i, 'Двигатель'] == mod:
                poww = base2.loc[i, 'Мощность']
        fl = 0
        for i in range(len(base2.index)):
            if (base2.loc[i, 'Мощность'] == poww) and (fl == 1):
                fl = 2
            elif (base2.loc[i, 'Мощность'] == poww) and (fl == 0):
                fl = 1
        if fl == 1:
            for i in range(len(base3.index)):
                if base3.loc[i, 'Мощность'] == poww:
                    base3.drop(index=[i], inplace=True)
            base3 = base3.reset_index(drop=True)
        for i in range(len(base2.index)):
            if base2.loc[i, 'Двигатель'] == mod:
                base2.drop(index=[i], inplace=True)
        base2 = base2.reset_index(drop=True)
    base4.drop(index=[ind], inplace=True)
    base4 = base4.reset_index(drop=True)


def addbd(
    model,
    company,
    engine,
    power,
    volume,
    tax,
    consumption,
    price,
    colour
    ):
    """
    Функция добавляет автомобиль в базу данных base1, base2, base2, base3 
    с названием model, от произваодителя company, с двигателем engi с 
    мощностью power, объемом volume, налогом tax, расходом consumption, 
    ценой price и цветом colour.

    base1, base2, base3, base4 - база данных в четырех справочниках
    model - нaзвание модели автомобиля
    company - нaзвание фирмы-производителя
    engine - нaзвание двигателя
    power - мощность двигателя
    volume - объем двигателя
    tax - налог на автомобиль
    consumption - расход топлива
    price - цена автомобиля
    colour - цвет автомобиля
    Автор: Фролов К.Д.
    """
    global base1, base2, base3, base4
    data4 = {'Модель': model,
             'Двигатель': engine,
             'Налог': tax,
             'Цена': price
             }
    base4 = base4.append(data4, ignore_index=True)
    fl = False
    for i in range(len(base1.index)):
        if base1.loc[i, 'Модель'] == model:
            fl = True
    if fl == False:
        data1 = {
            'Модель': model,
            'Фирма': company,
            'Цвет': colour}
        base1 = base1.append(data1, ignore_index=True)
    fl = False
    for i in range(len(base2.index)):
        if base2.loc[i, 'Двигатель'] == engine:
            fl = True
    if fl == False:
        data2 = {
            'Двигатель': engine,
            'Объем': volume,
            'Мощность': power}
        base2 = base2.append(data2, ignore_index=True)
        for i in range(len(base3.index)):
            if base3.loc[i, 'Мощность'] == power:
                fl = True
        data3 = {
            'Мощность': power,
            'Расход': consumption}
        if fl == False:
            base3 = base3.append(data3, ignore_index=True)


def changebd(
    ind,
    model,
    company,
    engine,
    power,
    volume,
    tax,
    consumption,
    price,
    colour
):
    """
    Функция изменяет конкретный автомобиль с индексом ind в базе данных 
    base1, base2, base3, base4

    base1, base2, base3, base4 - база данных в четырех справочниках
    model - новое название модели автомобиля
    company - новое название фирмы-производителя
    engine - новое название двигателя
    power - новая мощность двигателя
    volume - новый объем двигателя
    tax - новый налог на автомобиль
    consumption - новый расход топлива
    price - новая цена автомобиля
    colour - новый цвет автомобиля
    Автор: Фролов К.Д.
    """
    global base1, base2, base3, base4
    mod = base4.loc[ind, 'Модель']
    eng = base4.loc[ind, 'Двигатель']
    k = 0
    q = 0
    for i in range(len(base4.index)):
        if base4.loc[i, 'Модель'] == mod:
            k += 1
    for i in range(len(base4.index)):
        if base4.loc[i, 'Двигатель'] == eng:
            q += 1
    data1 = {
        'Модель': model,
        'Фирма': company,
        'Цвет': colour}
    data11 = [model, company, colour]
    fl = False
    for i in range(len(base1.index)):
        if base1.loc[i, 'Модель'] == model:
            fl = True
    if k > 1:
        base1 = base1.append(data1, ignore_index=True)
    else:
        for i in range(len(base1.index)):
            if base1.loc[i, 'Модель'] == mod:
                ind1 = i
        if fl == False:
            base1.loc[ind1] = data11
        else:
            base1.drop(index=[ind1], inplace=True)
            base1 = base1.reset_index(drop=True)

    data3 = {
        'Мощность': power,
        'Расход': consumption}
    data33 = [power, consumption]
    data2 = {
        'Двигатель': engine,
        'Объем': volume,
        'Мощность': power}
    data22 = [engine, volume, power]
    fll = False
    for i in range(len(base2.index)):
        if base2.loc[i, 'Двигатель'] == engine:
            fll = True
    if q < 2:
        for i in range(len(base2.index)):
            if base2.loc[i, 'Двигатель'] == eng:
                ind1 = i
        poww = base2.loc[ind1, 'Мощность']
        k = 0
        for i in range(len(base2.index)):
            if base2.loc[i, 'Мощность'] == poww:
                k = k+1
        fl = False
        for i in range(len(base3.index)):
            if base3.loc[i, 'Мощность'] == power:
                fl = True
        if k > 1:
            base3 = base3.append(data3, ignore_index=True)
        else:
            for i in range(len(base3.index)):
                if base3.loc[i, 'Мощность'] == poww:
                    ind2 = i
            if fl == False:
                base3.loc[ind2] = data33
            else:
                base3.drop(index=[ind2], inplace=True)
                base3 = base3.reset_index(drop=True)
        if fll == False:
            base2.loc[ind1] = data22
        else:
            base2.drop(index=[ind1], inplace=True)
            base2 = base2.reset_index(drop=True)
    else:
        if fl == False:
            base2 = base2.append(data2, ignore_index=True)
        if fll == False:
            base3 = base3.append(data3, ignore_index=True)
    data4 = [model, engine, tax, price]
    fl = False
    for i in range(len(base4.index)):
        if (base4.loc[i, 'Модель'] == model) and (base4.loc[i, 'Двигатель'] == engine):
            fl = True
    if fl == False:
        base4.loc[ind] = data4
    else:
        base4.drop(index=[ind], inplace=True)
        base4 = base4.reset_index(drop=True)


def convert():
    """
    Функция преобразует четыре справочника base1, base2, base3, base4 в одну таблицу data
    base1, base2, base3, base4 - база данных в четырех справочниках
    data - база данных в одной таблице
    Автор: Фролов К.Д.
    """
    global data
    data = base4.copy(deep=True)
    header_list = ['Index', 'Модель', 'Фирма', 'Двигатель',
                   'Мощность', 'Объем', 'Налог', 'Расход', 'Цена', 'Цвет']
    data = data.reindex(columns=header_list)
    data['Index'] = base4.index

    for i in range(len(data.index)):
        for j in range(len(base1.index)):
            if data.loc[i, 'Модель'] == base1.loc[j, 'Модель']:
                data.loc[i, 'Фирма'] = base1.loc[j, 'Фирма']
                data.loc[i, 'Цвет'] = base1.loc[j, 'Цвет']
        for j in range(len(base2.index)):
            if data.loc[i, 'Двигатель'] == base2.loc[j, 'Двигатель']:
                poww = base2.loc[j, 'Мощность']
                data.loc[i, 'Объем'] = base2.loc[j, 'Объем']
                data.loc[i, 'Мощность'] = base2.loc[j, 'Мощность']
        for j in range(len(base3.index)):
            if base3.loc[j, 'Мощность'] == poww:
                data.loc[i, 'Расход'] = base3.loc[j, 'Расход']


def report():
    """
    Функция создающая 6 таблиц формата exel из базы данных.

    Returns
    -------
    None.

    Авторы: Фролов К.Д., Анисимов М.А.
    """
    global data
    global df1, df2, df3, tabl1, tabl2, tabl3

    df1 = pd.DataFrame(data)
    df1 = df1.drop(['Фирма', 'Мощность', 'Объем',
                   'Налог', 'Расход', 'Цвет'], axis=1)
    with pd.ExcelWriter('./output/report1.xlsx') as writer:
        df1.to_excel(writer)

    df2 = pd.DataFrame(data)
    df2 = df2.drop(['Модель', 'Фирма', 'Объем', 'Налог',
                   'Расход', 'Цена', 'Цвет'], axis=1)
    with pd.ExcelWriter('./output/report2.xlsx') as writer:
        df2.to_excel(writer)

    df3 = pd.DataFrame(data)
    df3 = df3.drop(['Модель', 'Фирма', 'Двигатель',
                   'Расход', 'Цвет', 'Цена'], axis=1)
    with pd.ExcelWriter('./output/report3.xlsx') as writer:
        df3.to_excel(writer)

    tabl1 = pd.pivot_table(data, index='Двигатель', values='Мощность')
    with pd.ExcelWriter('./output/report4.xlsx') as writer:
        tabl1.to_excel(writer)

    tabl2 = pd.pivot_table(data, index='Двигатель', values='Расход')
    with pd.ExcelWriter('./output/report5.xlsx') as writer:
        tabl1.to_excel(writer)

    tabl3 = pd.pivot_table(data, index='Двигатель', values='Объем')
    with pd.ExcelWriter('./output/report6.xlsx') as writer:
        tabl1.to_excel(writer)


def build_plot(ind1, ind2, ind3, ind4):
    """
    Функция принимающая выбор пользователя и выводящая в папку запрашиваемые графики.

    Parameters
    ----------
    ind1 : int - 0 или 1, является индикатором выбора 1 флажка
    ind2 : int - 0 или 1, является индикатором выбора 2 флажка
    ind3 : int - 0 или 1, является индикатором выбора 3 флажка
    ind4 : int - 0 или 1, является индикатором выбора 4 флажка

    Returns
    -------
    None.

    Автор: Анисимов М.А.
    """
    global data
    if ind1 == 1:
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.set_title('Цвета автомобилей')
        ax.set_xlabel('Цвет')
        ax.set_ylabel('Количество автомобилей')
        ax.hist(df['Цвет'],)
        plt.savefig('./graphics/graph1.png')
    if ind2 == 1:
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.set_title('Объём и расход')
        ax.set_xlabel('Объем')
        ax.set_ylabel('Расход')
        ax.bar(df['Объем'], df['Расход'], width=0.5)
        plt.savefig('./graphics/graph2.png')
    if ind3 == 1:
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.set_title('Объём и мощность')
        ax.set_xlabel('Объем')
        ax.set_ylabel('Мощность')
        ax.bar(df['Объем'], df['Мощность'], width=0.5)
        plt.savefig('./graphics/graph3.png')
    if ind4 == 1:
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax = sns.boxplot(df['Модель'], df['Расход'])
        plt.savefig('./graphics/graph4.png')
