# coding=utf-8
import pandas as pd
import sys

### 进度条相关
def report_progress(progress, total):
    ratio = progress / float(total)
    percentage = round(ratio * 100)
    length = 80
    percentnums = round(length*ratio)
    buf = '\r[%s%s] %d%%' % (('>'*percentnums),('-'*(length-percentnums)), percentage)
    sys.stdout.write(buf)
    sys.stdout.flush()
def report_progress_done():
    sys.stdout.write('\n')

### 逐个读取excel/csv数据文件
#def read_data(self,datafiles):
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
#def mean_by_year(self,dfs):
def mean_by_year(dfs):
    year_range = ['1985-1990','1991-1995','1996-1998','1999-2002','2003-2005','2006-2010','2011-2015','2016至今']
    cols = dfs.columns.tolist()
    dfs_mean_yearrange = pd.DataFrame(columns=cols)
    for item in ['序号', '煤种', '煤名称', '年份', '国家', '产地']:
        if item in cols:
            cols.remove(item)
    for i in range(len(year_range)):
        if (i != len(year_range)-1):
            year_start = int(year_range[i].split('-')[0])
            year_end = int(year_range[i].split('-')[1])
            dfs_yearrange = dfs[(dfs.年份 >= year_start) & (dfs.年份 <= year_end)]
        else:
            year_start = int(year_range[i][:4])
            dfs_yearrange = dfs[(dfs.年份 >= year_start)]
        if len(dfs_yearrange.index) > 0:
            names = list(set(dfs_yearrange['煤名称'].tolist()))
            coal_kind,coal_country,coal_place = {},{},{}
            already_names = []
            for index,row in dfs_yearrange.iterrows():
                if (row.煤名称 in names) and (row.煤名称 not in already_names):
                    coal_kind[row.煤名称] = row.煤种
                    coal_country[row.煤名称] = row.国家
                    coal_place[row.煤名称] = row.产地
                    already_names.append(row.煤名称)
            dfs_yearrangeGM = dfs_yearrange.loc[:,cols].groupby(dfs_yearrange['煤名称']).mean()
            initnum = len(dfs_mean_yearrange.index)
            for nameindex in range(len(names)):
                for col in cols:
                    dfs_mean_yearrange.loc[initnum+nameindex, '序号'] = initnum+nameindex+1
                    dfs_mean_yearrange.loc[initnum+nameindex, '煤种'] = coal_kind[names[nameindex]]
                    dfs_mean_yearrange.loc[initnum+nameindex, '煤名称'] = names[nameindex]
                    dfs_mean_yearrange.loc[initnum+nameindex, '年份'] = year_range[i]
                    dfs_mean_yearrange.loc[initnum+nameindex, '国家'] = coal_country[names[nameindex]]
                    dfs_mean_yearrange.loc[initnum+nameindex, '产地'] = coal_place[names[nameindex]]
                    if (names[nameindex] in dfs_yearrangeGM.index) and (col in dfs_yearrangeGM.columns):
                        dfs_mean_yearrange.loc[initnum+nameindex,col] = dfs_yearrangeGM.loc[names[nameindex],col]
    print('已根据年份时间段对各煤种进行指标数据平均')
    #self.textEdit.append('已根据年份时间段对各煤种进行指标数据平均')
    return dfs_mean_yearrange

### 根据数据对煤质、热强度、硬煤分类、灰分、硫分进行分级，并插入各自数据中
#def init_level(self,dfs):
def init_level(dfs):
    colnum = len(dfs.index)
    new_indexs = ['煤质分级','热强度分级','硬煤分类','灰分分级','硫分分级']
    dfs = pd.concat([dfs,pd.DataFrame(columns=new_indexs)])#, sort=False)
    print('根据各指标进行煤质、热强度、硬煤分类、灰分、硫分分级')
    #self.textEdit.append('根据各指标进行煤质、热强度、硬煤分类、灰分、硫分分级')
    for index,row in dfs.iterrows():
        dfs.loc[index,'硫分分级'] = get_S_level(row.煤种,row.Std)
        dfs.loc[index,'灰分分级'] = get_Ash_level(row.煤种,row.Ad)
        dfs.loc[index,'热强度分级'] = get_HotStrength_level(row.煤种,row.CSR)
        #report_progress(index, len(dfs.index))
    #report_progress_done()
    return dfs