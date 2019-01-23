import numpy as np
import pandas as pd
import os

#from grf file get data
def get_data(filename):
    df = pd.read_table(filename)
# def get_data():
#     df = pd.read_table('data/02_052A.grf')
    t = df.loc[df['DPLOT v1.6'].str.contains(r'\s+[0]$')].index.tolist()
    arr = df.values
    data_class = int(df.iat[1, 0])
    data_name = []
    normalised_x = []
    normalised_y = []
    for i in range(data_class):
        data_x = []
        data_y = []
        data_name.append(df.iat[int(t[i])+1,0])
        if i == 0:
            x1 = df[3:int(t[i])].values
            for j in range(x1.shape[0]):
                data_x.append(''.join(x1[j]).split(',')[0])
                data_y.append(''.join(x1[j]).split(',')[1])
        else:
            x2 = df[int(t[i-1])+3:int(t[i])].values
            for k in range(x2.shape[0]):
                data_x.append(''.join(x2[k]).split(',')[0])
                data_y.append(''.join(x2[k]).split(',')[1])
        normalised_x.append(np.array(data_x))
        normalised_y.append(np.array(data_y))
#     print('2222',normalised_x,"333",normalised_y)
    data_class = str(df.iat[t[-1]+5, 0])
    if "Pressure" in data_class:
        data_class = 'Pressure'
    else:
        data_class = 'Impulses'
    title = df.iat[t[-1]+3,0].replace("(","").replace(")","")
    N = title.split(', ')[0].split(' = ')[1]
    lL = title.split(', ')[1].split(' = ')[1]
    hH = title.split(', ')[2].split(' = ')[1]
    LH = title.split(', ')[3].split(' = ')[1]
    return data_class, N, lL, hH, LH, np.array(data_name),np.array(normalised_x),np.array(normalised_y)

if __name__=='__main__':
    for dirName, subdirList, fileList in os.walk('./data'):
        x_pressure = []
        x_impulses = []
        print('Found directory: %s' % dirName)
        for fname in fileList:
            x = []
            y = []
            filename = str(dirName + '/' + fname)
            data_class, N, lL, hH, LH, data_name, normalised_x, normalised_y = get_data(filename)
            if data_class == 'Pressure':
                for i in range(len(data_name)):
                    train = []
                    for j in range(len(normalised_x[i])):
                        train.append([N, lL, hH, LH, data_name[i], normalised_x[i][j]])
                    train = np.array(train).reshape(-1, 6)
                    x.append(train)
                x = np.array(x).reshape(-1,6)
                y = np.array(normalised_y).reshape(-1,1)
                x_pressure.append(np.c_[x, y])
            else:
                for i in range(len(data_name)):
                    train = []
                    for j in range(len(normalised_x[i])):
                        train.append([N, lL, hH, LH, data_name[i], normalised_x[i][j]])
                    train = np.array(train).reshape(-1, 6)
                    x.append(train)
                x = np.array(x).reshape(-1,6)
                y = np.array(normalised_y).reshape(-1,1)
                x_impulses.append(np.c_[x, y])
        x_pressure = np.array(x_pressure).reshape(-1, 7)
        x_impulses = np.array(x_impulses).reshape(-1, 7)
        data_pressure = pd.DataFrame(x_pressure, columns=["N", "lL", "hH", "LH", "data_name", "x", "y"])
        data_impulses = pd.DataFrame(x_impulses, columns=["N", "lL", "hH", "LH", "data_name", "x", "y"])
        data_pressure.to_csv("pressure_data.csv", index=False)
        print('Save Pressure Data Success!')
        data_impulses.to_csv("impulses_data.csv", index=False)
        print('Save Impulses Data Success!')