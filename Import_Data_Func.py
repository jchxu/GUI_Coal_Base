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


### 根据数据对煤质、热强度、硬煤分类、灰分、硫分进行分级，并插入各自数据中
def init_level(dfs):
    colnum = len(dfs.index)
    new_indexs = ['煤质分级','热强度分级','硬煤分类','灰分分级','硫分分级']
    dfs = pd.concat([dfs,pd.DataFrame(columns=new_indexs)],sort=False)
    for index,row in dfs.iterrows():
        dfs.loc[index,'硫分分级'] = get_S_level(row.煤种,row.Std)

    return dfs