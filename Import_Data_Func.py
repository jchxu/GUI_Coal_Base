# coding=utf-8
import pandas as pd

### 逐个读取excel/csv数据文件
def read_data(datafiles):
    dflist = []
    for i in range(len(datafiles)):
        datafile = datafiles[i]
        if (datafile.split('.')[-1] == 'xls') or (datafile.split('.')[-1] == 'xlsx'):
            print('读取Excel文件:', datafile)
            #self.textEdit.append('读取Excel数据文件:%s' % datafile)
            df = pd.read_excel(datafile)
            dflist.append(df)
        elif (datafile.split('.')[-1] == 'csv'):
            print('读取CSV文件:', datafile)
            #self.textEdit.append('读取CSV数据文件:%s' % datafile)
            file = open(datafile)
            df = pd.read_csv(file)
            dflist.append(df)
            file.close()
    dfs = pd.concat(dflist, ignore_index=True)
    return dfs

### 根据煤种和硫分数据，判断硫分分级
def get_S_level(coal_kind,coal_Std):
    if coal_kind == '焦煤':
        if (coal_Std < 0.4):  return ('特低')
        elif (0.4 <= coal_Std) and (coal_Std < 0.6):  return ('低')
        elif (0.6 <= coal_Std) and (coal_Std < 1):  return ('中')
        elif (1 <= coal_Std) and (coal_Std <= 1.5):  return ('高')
        elif (coal_Std > 1.5):  return ('特高')
        else :  return ('硫分超出范围')
    elif (coal_kind == '肥煤') or (coal_kind == '1/3焦煤'):
        if (coal_Std < 0.4):  return ('特低')
        elif (0.4 <= coal_Std) and (coal_Std < 0.7):  return ('低')
        elif (0.7 <= coal_Std) and (coal_Std < 1.2):  return ('中')
        elif (1.2 <= coal_Std) and (coal_Std <= 1.8):  return ('高')
        elif (coal_Std > 1.8):  return ('特高')
        else :  return ('硫分超出范围')
    elif (coal_kind == '气煤'):
        if (coal_Std < 0.4):  return ('特低')
        elif (0.4 <= coal_Std) and (coal_Std < 0.6):  return ('低')
        elif (0.6 <= coal_Std) and (coal_Std < 0.7):  return ('中')
        elif (0.7 <= coal_Std) and (coal_Std <= 0.9):  return ('高')
        elif (coal_Std > 0.9):  return ('特高')
        else :  return ('硫分超出范围')
    elif (coal_kind == '瘦煤'):
        if (coal_Std < 0.4):  return ('特低')
        elif (0.4 <= coal_Std) and (coal_Std < 0.6):  return ('低')
        elif (0.6 <= coal_Std) and (coal_Std < 0.8):  return ('中')
        elif (0.8 <= coal_Std) and (coal_Std <= 1.2):  return ('高')
        elif (coal_Std > 1.2):  return ('特高')
        else :  return ('硫分超出范围')
    else:
        return ('煤种未知')

### 根据煤种和灰分数据，判断灰分分级
def get_Ash_level(coal_kind,coal_Ad):
    if (coal_kind == '焦煤') or (coal_kind == '瘦煤'):
        if (coal_Ad < 8):  return ('特低')
        elif (8 <= coal_Ad) and (coal_Ad < 9):  return ('低')
        elif (9 <= coal_Ad) and (coal_Ad < 10):  return ('中')
        elif (10 <= coal_Ad) and (coal_Ad <= 11.5):  return ('高')
        elif (coal_Ad > 11.5):  return ('特高')
        else :  return ('灰分超出范围')
    elif (coal_kind == '肥煤'):
        if (coal_Ad < 7):  return ('特低')
        elif (7 <= coal_Ad) and (coal_Ad < 9):  return ('低')
        elif (9 <= coal_Ad) and (coal_Ad < 10):  return ('中')
        elif (10 <= coal_Ad) and (coal_Ad <= 11.5):  return ('高')
        elif (coal_Ad > 11.5):  return ('特高')
        else :  return ('灰分超出范围')
    elif (coal_kind == '1/3焦煤'):
        if (coal_Ad < 5):  return ('特低')
        elif (5 <= coal_Ad) and (coal_Ad < 7):  return ('低')
        elif (7 <= coal_Ad) and (coal_Ad < 8):  return ('中')
        elif (8 <= coal_Ad) and (coal_Ad <= 10):  return ('高')
        elif (coal_Ad > 10):  return ('特高')
        else :  return ('灰分超出范围')
    elif (coal_kind == '气煤'):
        if (coal_Ad < 6):  return ('特低')
        elif (6 <= coal_Ad) and (coal_Ad < 7):  return ('低')
        elif (7 <= coal_Ad) and (coal_Ad < 8):  return ('中')
        elif (8 <= coal_Ad) and (coal_Ad <= 9):  return ('高')
        elif (coal_Ad > 9):  return ('特高')
        else :  return ('灰分超出范围')
    else:
        return ('煤种未知')

### 根据煤种和CSR数据，判断热强度分级
def get_HotStrength_level(coal_kind,coal_CSR):
    if (coal_kind == '焦煤') or (coal_kind == '肥煤'):
        if (coal_CSR < 60):  return ('C级')
        elif (60 <= coal_CSR) and (coal_CSR < 70):  return ('B级')
        elif (coal_CSR >= 70):  return ('A级')
        else :  return ('CSR超出范围')
    elif (coal_kind == '1/3焦煤'):
        if (coal_CSR < 52):  return ('C级')
        elif (52 <= coal_CSR) and (coal_CSR < 60):  return ('B级')
        elif (coal_CSR >= 60):  return ('A级')
        else :  return ('CSR超出范围')
    elif (coal_kind == '气煤') or (coal_kind == '瘦煤'):
        if (coal_CSR < 40):  return ('C级')
        elif (40 <= coal_CSR) and (coal_CSR < 50):  return ('B级')
        elif (coal_CSR >= 50):  return ('A级')
        else :  return ('CSR超出范围')
    else:
        return ('煤种未知')

### 根据挥发分、基质流动度、全膨胀数据，判断硬煤分类
def get_Hard_level(coal_Vd,coal_lgMF,coal_TD):
    MF = 10**coal_lgMF


### 根据时间段对数据进行分段平均
def mean_by_year(dfs):
    year_range = ['1985-1990','1991-1995','1996-1998','1999-2002','2003-2005','2006-2010','2011-2015','2016至今']
    for i in range(len(year_range)):
        if (i != len(year_range)-1):
            year_start = int(year_range[i].split('-')[0])
            year_end = int(year_range[i].split('-')[1])
            dfs_i = dfs[(dfs.年份 >= year_start) & (dfs.年份 <= year_end)]
            if len(dfs_i.index) > 0:
                print(year_range[i])
                print(dfs_i)
                print(dfs_i.mean())
                print(dfs_i.mean()['Ad'])

    return dfs


### 根据数据对煤质、热强度、硬煤分类、灰分、硫分进行分级，并插入各自数据中
def init_level(dfs):
    colnum = len(dfs.index)
    new_indexs = ['煤质分级','热强度分级','硬煤分类','灰分分级','硫分分级']
    dfs = pd.concat([dfs,pd.DataFrame(columns=new_indexs)])#, sort=False)
    for index,row in dfs.iterrows():
        dfs.loc[index,'硫分分级'] = get_S_level(row.煤种,row.Std)
        dfs.loc[index,'灰分分级'] = get_Ash_level(row.煤种,row.Ad)
        dfs.loc[index,'热强度分级'] = get_HotStrength_level(row.煤种,row.CSR)

    return dfs