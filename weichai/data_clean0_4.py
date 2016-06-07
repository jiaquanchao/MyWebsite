import matplotlib.pyplot as plt
import csv
import numpy as np
import os, os.path

def csv2array(filename):
    with open(filename) as f:
        f_csv = csv.reader(f)
        # headers = next(f_csv)
        List = []
        # data_array = np.array
        for row in f_csv:
            List.append(row)
        data_array = np.vstack(List)
    arrayname = data_array
    return arrayname
    # print(data_array)

fileload = '/home/jax/Downloads/test2/xlsone/csvtest.csv'
data_tem = csv2array(fileload)
#['0采样时间' '1扭矩' '2角度' '3螺栓' '4最大扭矩']

# print(data_array[0])
print(len(data_tem))
data_tem[0] = 0
print(data_tem[0])
# L = list(data_array[:, 1])
# print(L)
# data_array_tem = []
num_array_tem = []
niuju_array_tem = []
data_array_tem1 = []
data_array_tem2 = []
data_array = []
niuju_array = []
Niuju = []
for i in np.arange(len(data_tem)):
    num_array_tem.append(float(data_tem[i][3]))
    niuju_array_tem.append(float(data_tem[i][1]))

data_array_tem = np.transpose(np.vstack((num_array_tem, niuju_array_tem)))
print(data_array_tem)

# for ii in np.arange(14):
#     data_array_tem1 = []
#     for i in np.arange(len(data_array_tem)-1):
#         if (data_array_tem[i][1] < 20) or (data_array_tem[i+1][1] - data_array_tem[i][1] < -5) and (data_array_tem[i][0] == ii+1):
#             data_array_tem1.append(0)
#         elseif(data_array_tem[i][0] == ii+1):
#             data_array_tem1.append(data_array_tem[i][1])
#     data_array.append(data_array_tem1)
for ii in np.arange(14):
    data_array_tem1 = []
    for i in np.arange(len(data_array_tem)-1):
        if data_array_tem[i][0] == ii+1:
            data_array_tem1.append(data_array_tem[i][1])
    data_array.append(data_array_tem1)

print(data_array)
a = 10
for ii in np.arange(14):
    L = list(data_array[ii])
    data_array_tem1 = []
    # print(data_array_tem[6][1])
    for i in np.arange(len(L))[1::]:
        f = 0
        if (L[i] < 40) or (L[i] - L[i-1] < -a):
            data_array_tem1.append(0)
        else:
            data_array_tem1.append(L[i])
    data_array_tem2 = []
    for v in np.arange(len(data_array_tem1)):
        if data_array_tem1[v] != 0:
            data_array_tem2.append(data_array_tem1[v])

    # for i in np.arange(len(data_array_tem1))[1::]:
    #     if data_array_tem1[i] - data_array_tem1[i-1] < -a:
    #         data_array_tem2.append(0)
    #     else:
    #         data_array_tem2.append(data_array_tem1[i])

    data_array_tem1 = []
    for i in np.arange(len(data_array_tem2))[1::]:
        if data_array_tem2[i] - data_array_tem2[i-1] < -a:
            data_array_tem1.append(0)
        else:
            data_array_tem1.append(data_array_tem2[i])
    data_array_tem2 = []
    for v in np.arange(len(data_array_tem1)):
        if data_array_tem1[v] != 0:
            data_array_tem2.append(data_array_tem1[v])

    data_array_tem1 = []
    for i in np.arange(len(data_array_tem2))[1::]:
        if data_array_tem2[i] - data_array_tem2[i-1] < -a:
            data_array_tem1.append(0)
        else:
            data_array_tem1.append(data_array_tem2[i])
    data_array_tem2 = []
    for v in np.arange(len(data_array_tem1)):
        if data_array_tem1[v] != 0:
            data_array_tem2.append(data_array_tem1[v])

    data_array_tem1 = []
    for i in np.arange(len(data_array_tem2))[1::]:
        if data_array_tem2[i] - data_array_tem2[i-1] < -a:
            data_array_tem1.append(0)
        else:
            data_array_tem1.append(data_array_tem2[i])
    data_array_tem2 = []
    for v in np.arange(len(data_array_tem1)):
        if data_array_tem1[v] != 0:
            data_array_tem2.append(data_array_tem1[v])

    data_array_tem1 = []
    for i in np.arange(len(data_array_tem2))[1::]:
        if data_array_tem2[i] - data_array_tem2[i-1] < -a:
            data_array_tem1.append(0)
        else:
            data_array_tem1.append(data_array_tem2[i])
    data_array_tem2 = []
    for v in np.arange(len(data_array_tem1)):
        if data_array_tem1[v] != 0:
            data_array_tem2.append(data_array_tem1[v])

    data_array_tem1 = []
    for i in np.arange(len(data_array_tem2))[1::]:
        if data_array_tem2[i] - data_array_tem2[i-1] < -a:
            data_array_tem1.append(0)
        else:
            data_array_tem1.append(data_array_tem2[i])
    data_array_tem2 = []
    for v in np.arange(len(data_array_tem1)):
        if data_array_tem1[v] != 0:
            data_array_tem2.append(data_array_tem1[v])

    data_array_tem1 = []
    for i in np.arange(len(data_array_tem2))[1::]:
        if data_array_tem2[i] - data_array_tem2[i-1] < -a:
            data_array_tem1.append(0)
        else:
            data_array_tem1.append(data_array_tem2[i])
    data_array_tem2 = []
    for v in np.arange(len(data_array_tem1)):
        if data_array_tem1[v] != 0:
            data_array_tem2.append(data_array_tem1[v])

    # data_array_tem2 = []
    # for i in np.arange(len(data_array_tem1))[1::]:
    #     if data_array_tem1[i] - data_array_tem1[i-1] < -a:
    #         data_array_tem2.append(0)
    #     else:
    #         data_array_tem2.append(data_array_tem1[i])

    data_array_tem1 = []
    for i in np.arange(len(data_array_tem2))[1::]:
        if data_array_tem2[i] - data_array_tem2[i-1] < -a:
            data_array_tem1.append(0)
        else:
            data_array_tem1.append(data_array_tem2[i])

    # data_array_tem2 = []
    # for i in np.arange(len(data_array_tem1))[1::]:
    #     if data_array_tem1[i] - data_array_tem1[i-1] < -a:
    #         data_array_tem2.append(0)
    #     else:
    #         data_array_tem2.append(data_array_tem1[i])

    niuju_array.append(data_array_tem1)
    # for
    # print(L[0])
    Niuju_tem = []
    print(niuju_array)
    for v in np.arange(len(niuju_array[ii])):
        if niuju_array[ii][v] != 0:
            Niuju_tem.append(niuju_array[ii][v])
    Niuju.append(Niuju_tem)
    print(len(Niuju), len(data_array))
    print(Niuju[ii])

for i in np.arange(14):
    if i == 5:
        continue
    x = range(len(Niuju[i]))
    plt.plot(x, Niuju[i])
plt.show()

with open('/home/jax/Downloads/test2/xlsone/csv1.csv', mode='w', newline='') as wf:
    # headers = ['采样时间', '扭矩', '角度', '螺栓', '最大扭矩']
    rows = Niuju
    writer = csv.writer(wf)
    # writer.writerow(headers)
    for i in range(len(rows)):
        rowss = np.array(rows[i])
        # writer.writerow(rowss)
        # writer.writerow(rows[i])
        for ii in range(len(rowss)):
            writer.writerow(rowss[ii])
