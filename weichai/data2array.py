import os, os.path
from array import array

import numpy as np
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt
# from openpyxl.compat import file



def read_xls(path, filename):
    # path = "/home/jax/Downloads/test2/xlsone/"
    data = os.listdir(path)
    # num = len(data)
    num = 1
    List = []
    list = []

    for i in range(num):
        xls_file = pd.ExcelFile(path+data[i])
        table = xls_file.parse('Report result')
        print('====================', data[i], '===================')
        state = ['采样时间', '扭矩', '角度', '螺栓', '最大扭矩']
        table_tem = table.reindex(columns=state)
        for i in np.arange(14):
           table_tem_1 = table_tem[table_tem['螺栓'] == (i+1)]
           table_new = table_tem_1.sort_index(by='采样时间')
           # x = table_new['最大扭矩'].head(1).values[0]
           # print(table_new['扭矩'])
           # print('===========', i+1, '================')
           # print(x)
           # print(type(x))
           # list.append(x)
           list.append(table_new)
           # table_tem_1 = []
           # table_new = []
        # print(listOfa)
        List.extend(list)

# '/home/jax/Downloads/test2/xlsone/csvtest.csv'
    with open(filename, mode='w', newline='') as wf:
        headers = ['采样时间', '扭矩', '角度', '螺栓', '最大扭矩']
        rows = List
        writer = csv.writer(wf)
        writer.writerow(headers)
        # print(type(rows))
        # # print(rows[0])
        # print(len(rows))
        # print(len(rows[1]))
        # rowsss = np.array(List[2])
        # print(len(rowsss))
        for i in range(len(List)):
            rowss = np.array(List[i])
            for ii in range(len(List[i])):
                writer.writerow(rowss[ii])

    data_all = np.array(List)
    
if __name__ == '__main__':
    read_xls()