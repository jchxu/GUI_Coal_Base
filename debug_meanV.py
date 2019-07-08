# conding=utf-8
import sys,os,re
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

file = open('原始数据.csv')
df = pd.read_csv(file, encoding='utf-8')
df = df.reset_index(drop=True)

df1 = df[df.煤种 == '焦煤'].reset_index(drop=True)
yearlist = list(set(df1.年份.tolist()))
Slist = []
for year in yearlist:
    tempdf = df1[df1.年份 == year]
    del tempdf['煤名称']
    del tempdf['国家']
    del tempdf['产地']
    tempdfmean = tempdf.mean()
    #tempdfmean.煤种 = '焦煤'
    #tempdfmean.年份 = year
    print(year+"---"*50)
    print(tempdf)
    print(tempdfmean)
    print(type(tempdfmean))

    Slist.append(tempdfmean)
df2 = pd.DataFrame(Slist)
print(df2)



#df2 = df1.groupby(df.年份)
#for name,group in df2:
#    print(name)
#    print(group)
#df3 = df2.mean()
#namelist = df3.columns.tolist()
#if not ('年份' in namelist):
#    df3 = pd.concat([df3, pd.DataFrame(columns='年6份')])
#for index,row in df3.iterrows():
#    row.年6份 = str(index)[0:4]
#print(df3)
#df4 = df3.reset_index(drop=True)
#print(df4)
