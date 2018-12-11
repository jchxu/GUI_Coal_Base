# coding=utf-8
import pandas as pd

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