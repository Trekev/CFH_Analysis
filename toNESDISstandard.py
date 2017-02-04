import os
import pandas as pd

os.chdir('Upload')


def from_GRAW(filename=None):
    for i in os.listdir(os.getcwd()):
        if 'UPP_RAW' in i:
            filename = i
            print(filename)
        if filename==None:
            return('Cannot find GRAW file')

    df = pd.read_csv(filename, header=1, skiprows=[2], sep='\s+')
    l = list(df.index)
    for i in l:
        if 'Trop' in df.loc[i,'Time']:
            df = df.loc[:(i-1)]
            break
    df[['Time']] = df[['Time']].apply(pd.to_numeric)
    df['Time'] /=60
    df['Long.'] = round(df['Long.'],6)
    df = df.drop(['Geopot'], axis=1)
    df = df[['P','T','Dewp.','Hu','Wd','Ws','Alt','Lat.','Long.','Time']]

    print(filename)
    name = ('79000'+'_'+filename[0:7]+'_'+filename[8:12]+'_GRAW_WALL_01.txt')
    df.to_csv(name, sep='\t',index=False)

    return(df)

def from_LMG(filename=None):
    for i in os.listdir(os.getcwd()):
        if '.rtso' in i:
            filename = i
            print(filename)
        if filename==None:
            return('Cannot find GRAW file')

    fp = open(filename)
    for i, line in enumerate(fp):
        if i == 2:
            date = line[6:8]+line[9:11]+line[12:16]
            time = line[24:26]+line[27:29]
            print(date,time)
        elif i > 4:
            break
    fp.close()

    df = pd.read_csv(filename, header=None, skiprows=11, skip_blank_lines=False, sep='\s+', names=['Time','Press','Temp','RH','Alt','Dewp','Dir'])

    #df[['Time']] = df[['Time']].apply(pd.to_numeric)
    #df['Time'] /=60

    #df = df[['P','T','Dewp.','Hu','Wd','Ws','Alt','Lat.','Long.','Time']]

    print(filename)
    name = ('73000'+'_'+date+'_'+time+'_LMG6_WALL_01.txt')
    df.to_csv(name, sep='\t',index=False)

    return(df)

print(from_LMG())