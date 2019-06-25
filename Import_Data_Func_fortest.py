# coding=utf-8
import pandas as pd
import numpy as np
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
#def read_data(self,datafiles):     #GUI程序用
def read_data(datafiles):           #测试程序用
    dflist = []
    for i in range(len(datafiles)):
        datafile = datafiles[i]
        if (datafile.split('.')[-1] == 'xls') or (datafile.split('.')[-1] == 'xlsx'):
            print('读取Excel文件:', datafile)                         #测试程序用
            #self.textEdit.append('读取Excel数据文件:%s' % datafile)   #GUI程序用
            df = pd.read_excel(datafile)
            dflist.append(df)
        elif (datafile.split('.')[-1] == 'csv'):
            print('读取CSV文件:', datafile)                       #测试程序用
            #self.textEdit.append('读取CSV数据文件:%s' % datafile) #GUI程序用
            file = open(datafile)
            df = pd.read_csv(file)
            dflist.append(df)
            file.close()
    dfs = pd.concat(dflist, ignore_index=True)
    return dfs

### 获取基础煤种的原始数据
def get_Base_coal(dfs):
    base_dfs = pd.DataFrame
    namelist = dfs['煤名称'].tolist()
    yearlist = dfs['年份'].tolist()
    unique_name = list(set(namelist))
    # 获取每个煤名称对应的年份
    name_year = {}
    for item in unique_name:
        name_year[item] = []
    for i in range(len(namelist)):
        name_year[namelist[i]].append(int(yearlist[i]))
    # 获取次数并判断是否属于基础煤种
    base_name = []
    base_year = {}
    for item in unique_name:
        years = name_year[item]
        years.sort()
        # 获取三个时间段内使用的年数
        list1996 = []
        list2009 = []
        list2015 = []
        for yy in years:
            if (yy >= 1996): list1996.append(yy)
            if (yy >= 2009): list2009.append(yy)
            if (yy >= 2015): list2015.append(yy)
        # 判断是否基础煤种，并记录使用年份
        if (len(set(list1996)) >= 16):
            base_name.append(item)
            base_year[item] = 1996
        elif (len(set(list2009)) >= 8):
            base_name.append(item)
            base_year[item] = 2009
        elif (len(set(list2015)) >= 4):
            base_name.append(item)
            base_year[item] = 2015

    # 根据基础煤种名称和使用年份，获取基础煤种原始数据
    dflist = []
    for item in base_name:
        df_name = dfs[(dfs['煤名称'] == item) & (dfs['年份'] >= base_year[item])]
        dflist.append(df_name)
    base_dfs = pd.concat(dflist, ignore_index=True)
    return base_dfs

### 获取经典煤种数据
def get_Classic_coal(dfs):
    classic_dfs = pd.DataFrame
    dflist = []
    df1 = dfs[(dfs['年份'] >= 1999) & (dfs['年份'] <= 2002)]    # 1999-2002年间用的煤种

    dfs_level = init_level(dfs)
    df2 = dfs_level[(dfs_level['煤质分级'] == '中等')]    # 煤质分级为特等的煤种
    print(df2)

    return classic_dfs


### 根据煤种和硫分数据，判断硫分分级
def get_S_level(coal_kind,coal_Std):
    if coal_kind == '焦煤':
        if (coal_Std < 0.4):  return ('特低')
        elif (0.4 <= coal_Std < 0.6):  return ('低')
        elif (0.6 <= coal_Std < 1):  return ('中')
        elif (1 <= coal_Std <= 1.5):  return ('高')
        elif (coal_Std > 1.5):  return ('特高')
    elif (coal_kind == '肥煤') or (coal_kind == '1/3焦煤'):
        if (coal_Std < 0.4):  return ('特低')
        elif (0.4 <= coal_Std < 0.7):  return ('低')
        elif (0.7 <= coal_Std < 1.2):  return ('中')
        elif (1.2 <= coal_Std <= 1.8):  return ('高')
        elif (coal_Std > 1.8):  return ('特高')
    elif (coal_kind == '气煤'):
        if (coal_Std < 0.4):  return ('特低')
        elif (0.4 <= coal_Std < 0.6):  return ('低')
        elif (0.6 <= coal_Std < 0.7):  return ('中')
        elif (0.7 <= coal_Std <= 0.9):  return ('高')
        elif (coal_Std > 0.9):  return ('特高')
    elif (coal_kind == '瘦煤'):
        if (coal_Std < 0.4):  return ('特低')
        elif (0.4 <= coal_Std < 0.6):  return ('低')
        elif (0.6 <= coal_Std < 0.8):  return ('中')
        elif (0.8 <= coal_Std <= 1.2):  return ('高')
        elif (coal_Std > 1.2):  return ('特高')
    else:
        return ('煤种未知')

### 根据煤种和灰分数据，判断灰分分级
def get_Ash_level(coal_kind,coal_Ad):
    if (coal_kind == '焦煤') or (coal_kind == '瘦煤'):
        if (coal_Ad < 8):  return ('特低')
        elif (8 <= coal_Ad < 9):  return ('低')
        elif (9 <= coal_Ad < 10):  return ('中')
        elif (10 <= coal_Ad <= 11.5):  return ('高')
        elif (coal_Ad > 11.5):  return ('特高')
    elif (coal_kind == '肥煤'):
        if (coal_Ad < 7):  return ('特低')
        elif (7 <= coal_Ad < 9):  return ('低')
        elif (9 <= coal_Ad < 10):  return ('中')
        elif (10 <= coal_Ad <= 11.5):  return ('高')
        elif (coal_Ad > 11.5):  return ('特高')
    elif (coal_kind == '1/3焦煤'):
        if (coal_Ad < 5):  return ('特低')
        elif (5 <= coal_Ad < 7):  return ('低')
        elif (7 <= coal_Ad < 8):  return ('中')
        elif (8 <= coal_Ad <= 10):  return ('高')
        elif (coal_Ad > 10):  return ('特高')
    elif (coal_kind == '气煤'):
        if (coal_Ad < 6):  return ('特低')
        elif (6 <= coal_Ad < 7):  return ('低')
        elif (7 <= coal_Ad < 8):  return ('中')
        elif (8 <= coal_Ad <= 9):  return ('高')
        elif (coal_Ad > 9):  return ('特高')
    else:
        return ('煤种未知')

### 根据煤种和CSR数据，判断热强度分级
def get_HotStrength_level(coal_kind,coal_CSR):
    if (coal_kind == '焦煤') or (coal_kind == '肥煤'):
        if (coal_CSR < 60):  return ('C级')
        elif (60 <= coal_CSR < 70):  return ('B级')
        elif (coal_CSR >= 70):  return ('A级')
    elif (coal_kind == '1/3焦煤'):
        if (coal_CSR < 52):  return ('C级')
        elif (52 <= coal_CSR < 60):  return ('B级')
        elif (coal_CSR >= 60):  return ('A级')
    elif (coal_kind == '气煤') or (coal_kind == '瘦煤'):
        if (coal_CSR < 40):  return ('C级')
        elif (40 <= coal_CSR < 50):  return ('B级')
        elif (coal_CSR >= 50):  return ('A级')
    else:
        return ('煤种未知')

### 根据挥发分、基质流动度、全膨胀数据，判断硬煤分类
def get_Hard_level(coal_Vd,coal_lgMF,coal_TD):
    coal_MF = 10**coal_lgMF
    if 30 <= coal_Vd < 33:  #高档硬A
        if (coal_MF >= 15000) and (coal_TD >= 200): return ('硬煤')
        elif (coal_MF >= 15000) or (coal_TD >= 200): return ('半硬优')
        elif (coal_MF < 1000) and (coal_TD < 50): return ('软煤')
        elif (coal_MF < 1000) or (coal_TD < 50): return ('半软')
        else: return ('半硬')
    elif 33 <= coal_Vd < 36:  #高档硬B
        if (10000 <= coal_MF < 15000) and (175 <= coal_TD < 200): return ('硬煤')
        elif (10000 <= coal_MF < 15000) or (175 <= coal_TD < 200): return ('半硬优')
        elif (coal_MF < 1000) and (coal_TD < 50): return ('软煤')
        elif (coal_MF < 1000) or (coal_TD < 50): return ('半软')
        else: return ('半硬')
    elif 36 <= coal_Vd:  #高档硬C
        if (2500 <= coal_MF < 10000) and (50 <= coal_TD < 175): return ('硬煤')
        elif (2500 <= coal_MF < 10000) or (50 <= coal_TD < 175): return ('半硬优')
        elif (coal_MF < 1000) and (coal_TD < 50): return ('软煤')
        elif (coal_MF < 1000) or (coal_TD < 50): return ('半软')
        else: return ('半硬')
    elif 27 <= coal_Vd < 30:  #中档硬A
        if (7500 <= coal_MF) and (175 <= coal_TD): return ('硬煤')
        elif (7500 <= coal_MF) or (175 <= coal_TD): return ('半硬优')
        elif (coal_MF < 90) and (coal_TD < 50): return ('软煤')
        elif (coal_MF < 90) or (coal_TD < 50): return ('半软')
        else: return ('半硬')
    elif 24 <= coal_Vd < 27:  #中档硬B
        if (2500 <= coal_MF < 7500) and (150 <= coal_TD < 175): return ('硬煤')
        elif (2500 <= coal_MF < 7500) or (150 <= coal_TD < 175): return ('半硬优')
        elif (coal_MF < 90) and (coal_TD < 50): return ('软煤')
        elif (coal_MF < 90) or (coal_TD < 50): return ('半软')
        else: return ('半硬')
    elif 22 <= coal_Vd < 24:  #中档硬C
        if (300 <= coal_MF < 2500) and (50 <= coal_TD < 150): return ('硬煤')
        elif (300 <= coal_MF < 2500) or (50 <= coal_TD < 150): return ('半硬优')
        elif (coal_MF < 90) and (coal_TD < 50): return ('软煤')
        elif (coal_MF < 90) or (coal_TD < 50): return ('半软')
        else: return ('半硬')
    elif 18 <= coal_Vd < 22:  #低档硬A
        if (300 <= coal_MF) and (75 <= coal_TD): return ('硬煤')
        elif (300 <= coal_MF) or (75 <= coal_TD): return ('半硬优')
        elif (coal_MF < 10) and (coal_TD < 25): return ('软煤')
        elif (coal_MF < 10) or (coal_TD < 25): return ('半软')
        else: return ('半硬')
    elif 15 <= coal_Vd < 18:  #低档硬B
        if (100 <= coal_MF < 300) and (50 <= coal_TD < 100): return ('硬煤')
        elif (100 <= coal_MF < 300) or (50 <= coal_TD < 100): return ('半硬优')
        elif (coal_MF < 10) and (coal_TD < 25): return ('软煤')
        elif (coal_MF < 10) or (coal_TD < 25): return ('半软')
        else: return ('半硬')
    elif coal_Vd < 15:  #低档硬C
        if (coal_MF < 100) and (coal_TD < 50): return ('硬煤')
        elif (coal_MF < 100) or (coal_TD < 50): return ('半硬优')
        elif (coal_MF < 10) and (coal_TD < 25): return ('软煤')
        elif (coal_MF < 10) or (coal_TD < 25): return ('半软')
        else: return ('半硬')

### 根据大小关系、分数范围给指标打分
def get_score(flag,lowvalue,highvalue,value):
    low_cutoff = lowvalue + (highvalue-lowvalue)/4
    high_cutoff = highvalue - (highvalue-lowvalue)/4
    if (flag == 'small'):
        if (value <= low_cutoff): return 100
        elif (value <= high_cutoff): return 70
        elif (value > high_cutoff): return 40
    elif (flag == 'big'):
        if (value >= high_cutoff): return 100
        elif (value >= low_cutoff): return 70
        elif (value < low_cutoff): return 40

### 根据若干指标计算煤质分级
def get_CoalQuality_level(coal_kind,coal_CRI,coal_CSR,coal_DI,coal_Y,coal_G,coal_TD,coal_lgMF,coal_Ad,coal_Std,coal_Vd,coal_Pd,coal_K2O):
    if (coal_kind == '焦煤'):
        score_CRI = get_score('small',15.7,30.3,coal_CRI)
        score_CSR = get_score('big',56.6,74.0,coal_CSR)
        score_DI = get_score('big',79.6,87.7,coal_DI)
        score_Y = get_score('big',11.8,17.7,coal_Y)
        score_G = get_score('big',72.3,86.0,coal_G)
        score_TD = get_score('big',27.4,104.0,coal_TD)
        score_lgMF = get_score('big',1.37,3.25,coal_lgMF)
        score_Ad = get_score('small',8.88,10.97,coal_Ad)
        score_Std = get_score('small',0.39,1.22,coal_Std)
        score_Vd = get_score('small',17.4,25.2,coal_Vd)
        score_Pd = get_score('small',0.008,0.076,coal_Pd)
        score_K2O = get_score('small',0.73,2.52,coal_K2O)
    elif (coal_kind == '肥煤'):
        score_CRI = get_score('small',13.8,27.5,coal_CRI)
        score_CSR = get_score('big',53.0,75.0,coal_CSR)
        score_DI = get_score('big',81.4,86.0,coal_DI)
        score_Y = get_score('big',23.0,27.0,coal_Y)
        score_G = get_score('big',86.0,94.0,coal_G)
        score_TD = get_score('big',142.0,266.0,coal_TD)
        score_lgMF = get_score('big',3.3,4.4,coal_lgMF)
        score_Ad = get_score('small',7.0,11.8,coal_Ad)
        score_Std = get_score('small',0.30,2.30,coal_Std)
        score_Vd = get_score('small',23.0,30.0,coal_Vd)
        score_Pd = get_score('small',0.009,0.063,coal_Pd)
        score_K2O = get_score('small',0.53,2.85,coal_K2O)
    elif (coal_kind == '1/3焦煤'):
        score_CRI = get_score('small',17.5,28.6,coal_CRI)
        score_CSR = get_score('big',52.0,71.2,coal_CSR)
        score_DI = get_score('big',70.0,84.8,coal_DI)
        score_Y = get_score('big',16.0,24.0,coal_Y)
        score_G = get_score('big',80.0,92.5,coal_G)
        score_TD = get_score('big',92.0,237.0,coal_TD)
        score_lgMF = get_score('big',2.05,4.68,coal_lgMF)
        score_Ad = get_score('small',3.40,9.85,coal_Ad)
        score_Std = get_score('small',0.41,2.15,coal_Std)
        score_Vd = get_score('small',26.0,39.0,coal_Vd)
        score_Pd = get_score('small',0.003,0.045,coal_Pd)
        score_K2O = get_score('small',0.72,3.54,coal_K2O)
    elif (coal_kind == '气煤'):
        score_CRI = get_score('small',32.0,56.5,coal_CRI)
        score_CSR = get_score('big',21.0,52.0,coal_CSR)
        score_DI = get_score('big',57.0,83.0,coal_DI)
        score_Y = get_score('big',10.7,16.0,coal_Y)
        score_G = get_score('big',61.0,87.0,coal_G)
        score_TD = get_score('big',4.0,115.0,coal_TD)
        score_lgMF = get_score('big',1.13,3.76,coal_lgMF)
        score_Ad = get_score('small',6.80,9.00,coal_Ad)
        score_Std = get_score('small',0.26,0.70,coal_Std)
        score_Vd = get_score('small',32.0,36.5,coal_Vd)
        score_Pd = get_score('small',0.005,0.042,coal_Pd)
        score_K2O = get_score('small',0.95,3.57,coal_K2O)
    elif (coal_kind == '瘦煤'):
        score_CRI = get_score('small',24.0,28.0,coal_CRI)
        score_CSR = get_score('big',30.0,37.0,coal_CSR)
        score_DI = get_score('big',40.0,59.0,coal_DI)
        score_Y = get_score('big',5.0,7.0,coal_Y)
        score_G = get_score('big',29.0,56.0,coal_G)
        score_TD = get_score('big',2.0,2.0,coal_TD)
        score_lgMF = get_score('big',0,0.3,coal_lgMF)
        score_Ad = get_score('small',9.5,11.5,coal_Ad)
        score_Std = get_score('small',0.37,0.85,coal_Std)
        score_Vd = get_score('small',14.2,15.2,coal_Vd)
        score_Pd = get_score('small',0.002,0.043,coal_Pd)
        score_K2O = get_score('small',0.65,1.74,coal_K2O)
    mean_score = np.mean([score_CRI,score_CSR,score_DI,score_Y,score_G,score_TD,score_lgMF,score_Ad,score_Std,score_Vd,score_Pd,score_K2O])
    if (mean_score > 80): return '优质'
    elif (60 <= mean_score <= 80): return '中等'
    elif (mean_score < 60): return '一般'

### 更新煤质分级指标（5个指标中有4个是最好的，煤质分级更新为特等）
def update_CoalQuality_level(S_level,Ash_level,HotStrength_level,Hard_level,CoalQuality_level):
    count = 0
    if (S_level == '特低') or (S_level == '低'): count += 1
    if (Ash_level == '特低') or (Ash_level == '低'): count += 1
    if (HotStrength_level == 'A级') : count += 1
    if (Hard_level == '硬煤') or (Hard_level == '半硬优'): count += 1
    if (CoalQuality_level == '优质') : count += 1
    if (count >= 4): return '特等'
    else: return CoalQuality_level

### 根据时间段对数据进行分段平均
#def mean_by_year(self,dfs):    #GUI程序用
def mean_by_yearregion(dfs):          #测试程序用
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
    print('已根据年份时间段对各煤种进行指标数据平均')                   #测试程序用
    #self.textEdit.append('已根据年份时间段对各煤种进行指标数据平均')   #GUI程序用
    return dfs_mean_yearrange

### 根据年份对数据进行平均
#def mean_by_year(self,dfs):    #GUI程序用
def mean_by_year(dfs):          #测试程序用
    cols = dfs.columns.tolist()
    dfs_mean_year = pd.DataFrame(columns=cols)
    for item in ['序号', '煤种', '煤名称', '年份', '国家', '产地']:
        if item in cols:
            cols.remove(item)
    years = list(set(dfs['年份'].tolist()))
    years.sort()
    for i in range(len(years)):
        dfs_year = dfs[(dfs.年份 == years[i])]
        names = list(set(dfs_year['煤名称'].tolist()))
        coal_kind, coal_country, coal_place = {}, {}, {}
        already_names = []
        for index, row in dfs_year.iterrows():
            if (row.煤名称 in names) and (row.煤名称 not in already_names):
                coal_kind[row.煤名称] = row.煤种
                coal_country[row.煤名称] = row.国家
                coal_place[row.煤名称] = row.产地
                already_names.append(row.煤名称)
        dfs_yearGM = dfs_year.loc[:,cols].groupby(dfs_year['煤名称']).mean()
        initnum = len(dfs_mean_year.index)
        for nameindex in range(len(names)):
            for col in cols:
                dfs_mean_year.loc[initnum+nameindex, '序号'] = initnum+nameindex+1
                dfs_mean_year.loc[initnum+nameindex, '煤种'] = coal_kind[names[nameindex]]
                dfs_mean_year.loc[initnum+nameindex, '煤名称'] = names[nameindex]
                dfs_mean_year.loc[initnum+nameindex, '年份'] = years[i]
                dfs_mean_year.loc[initnum+nameindex, '国家'] = coal_country[names[nameindex]]
                dfs_mean_year.loc[initnum+nameindex, '产地'] = coal_place[names[nameindex]]
                if (names[nameindex] in dfs_yearGM.index) and (col in dfs_yearGM.columns):
                    dfs_mean_year.loc[initnum+nameindex,col] = dfs_yearGM.loc[names[nameindex],col]
    print('已根据年份对各煤种进行指标数据平均')  # 测试程序用
    #self.textEdit.append('已根据年份对各煤种进行指标数据平均')   #GUI程序用
    return dfs_mean_year

    #    if len(dfs_year.index) > 0:
    #        names = list(set(dfs_yearrange['煤名称'].tolist()))
    #        coal_kind,coal_country,coal_place = {},{},{}
    #        already_names = []
    #        for index,row in dfs_yearrange.iterrows():
    #            if (row.煤名称 in names) and (row.煤名称 not in already_names):
    #                coal_kind[row.煤名称] = row.煤种
    #                coal_country[row.煤名称] = row.国家
    #                coal_place[row.煤名称] = row.产地
    #                already_names.append(row.煤名称)
    #        dfs_yearrangeGM = dfs_yearrange.loc[:,cols].groupby(dfs_yearrange['煤名称']).mean()
    #        initnum = len(dfs_mean_yearrange.index)
    #        for nameindex in range(len(names)):
    #            for col in cols:
    #                dfs_mean_yearrange.loc[initnum+nameindex, '序号'] = initnum+nameindex+1
    #                dfs_mean_yearrange.loc[initnum+nameindex, '煤种'] = coal_kind[names[nameindex]]
    #                dfs_mean_yearrange.loc[initnum+nameindex, '煤名称'] = names[nameindex]
    #                dfs_mean_yearrange.loc[initnum+nameindex, '年份'] = year_range[i]
    #                dfs_mean_yearrange.loc[initnum+nameindex, '国家'] = coal_country[names[nameindex]]
    #                dfs_mean_yearrange.loc[initnum+nameindex, '产地'] = coal_place[names[nameindex]]
    #                if (names[nameindex] in dfs_yearrangeGM.index) and (col in dfs_yearrangeGM.columns):
    #                    dfs_mean_yearrange.loc[initnum+nameindex,col] = dfs_yearrangeGM.loc[names[nameindex],col]
    #print('已根据年份时间段对各煤种进行指标数据平均')                   #测试程序用
    ##self.textEdit.append('已根据年份时间段对各煤种进行指标数据平均')   #GUI程序用
    #return dfs_mean_yearrange

### 根据数据对煤质、热强度、硬煤分类、灰分、硫分进行分级，并插入各自数据中
#def init_level(self,dfs):  #GUI程序用
def init_level(dfs):        #测试程序用
    colnum = len(dfs.index)
    new_indexs = ['煤质分级','热强度分级','硬煤分类','灰分分级','硫分分级']
    dfs = pd.concat([dfs,pd.DataFrame(columns=new_indexs)], sort=False)
    print('根据各指标进行煤质、热强度、硬煤分类、灰分、硫分分级')                  #测试程序用
    #self.textEdit.append('根据各指标进行煤质、热强度、硬煤分类、灰分、硫分分级')  #GUI程序用
    for index,row in dfs.iterrows():
        dfs.loc[index,'硫分分级'] = get_S_level(row.煤种,row.Std)
        dfs.loc[index,'灰分分级'] = get_Ash_level(row.煤种,row.Ad)
        dfs.loc[index,'热强度分级'] = get_HotStrength_level(row.煤种,row.CSR)
        dfs.loc[index,'硬煤分类'] = get_Hard_level(row.Vd,row.lgMF,row.TD)
        dfs.loc[index,'煤质分级'] = get_CoalQuality_level(row.煤种,row.CRI,row.CSR,row.DI150_15,row.Y,row.G,row.TD,row.lgMF,row.Ad,row.Std,row.Vd,row.Pd,row.K2O_Na2O)
        dfs.loc[index,'煤质分级'] = update_CoalQuality_level(row.硫分分级,row.灰分分级,row.热强度分级,row.硬煤分类,dfs.loc[index,'煤质分级'])
        #report_progress(index, len(dfs.index))
    #report_progress_done()
    return dfs