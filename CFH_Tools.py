import pandas as pd
import os
import matplotlib.pyplot as plt


class CFH(object):


    def __init__(self, datarate=None,filename=None, compareTo=None):
        self.filename = filename
        self.datarate = datarate

        if self.filename is None:
            path = 'C:/PythonProjects/CFH_Analysis/Upload'
            os.chdir(path)
            for i in os.listdir(os.getcwd()):
                if ".dat" in i:
                    print("Identified an unprocessed CFH file")
                    self.filename=str(i)
                    break
        if compareTo is not None:
            for i in compareTo:
                for j in os.listdir(os.getcwd()):
                    if i in j:
                        fNameA = str(j)
                        self.importOther(fNameA)

        df = pd.read_csv(self.filename,header=242, skiprows=[243], skip_blank_lines=False, na_values=999.9)

        df.columns = df.columns.str.strip()
        df['Time'] = round(df['Time']*60)
        if self.datarate is None: self.datarate=[df.loc[1,'Time']-df.loc[0,'Time']]
        df.index = df['Time']

        fp = open(self.filename)
        for i, line in enumerate(fp):
            if i == 3:
                self.name = line[35:]
                self.name = self.name.rstrip()

            if i == 121:
                self.trop = line[19:24]
            elif i > 125:
                break
        fp.close()



        #print(df.columns())
        self.df = df
        print('Finished CFH import, trop reported at: ' + self.trop + 'm')

    def importOther(self):
        df = pd.read_csv(self.filename, header=242, skiprows=[243], skip_blank_lines=False)
        df.columns = df.columns.str.strip()
        df['Time'] = round(df['Time'] * 60)
        if self.datarate is None: self.datarate = [df.loc[1, 'Time'] - df.loc[0, 'Time']]
        df.index = df['Time']

        fp = open(self.filename)
        for i, line in enumerate(fp):
            if i == 3:
                self.name = line[35:]
                self.name = self.name.rstrip()

            if i == 121:
                self.trop = line[19:24]
            elif i > 125:
                break
        fp.close()

    def dataclean(self):
        count = 0
        l = list(self.df.index)
        l.append(0)
        for i in l:
            if self.df.loc[i,'Press'] < self.df.loc[i+self.datarate, 'Press']:
                count += 1
                print(count)
                if count >= 5:
                    rem = i
                    print(rem)
                    self.df = self.df.loc[:rem]
                    break
            else:
                count=0
        self.df.to_csv(self.name)

    def getCFHDF(self):
        CFH.dataclean(self)
        return self.df
    def getTROP(self):
        return self.trop
    def getNAME(self):
        return self.name

    def plotRH(self,):
        df = self.df
        plt.plot(df['RH FP'],df['Alt'],df['RH'],df['Alt'])
        plt.axhline(y=int(self.trop)/1000)
        plt.xlabel('Relative Humidity (%)')
        plt.ylabel('Altitude (m)')
        plt.title('RH vs Altitude\n'+ self.name)
        plt.show()
        #print(df['RH FP'])

    def plotRHDiff(self):
        df = self.df
        plt.plot((df['RH FP']-df['RH']),df['Alt'])
        plt.axhline(y=int(self.trop) / 1000)
        plt.xlabel('CFH RH (%) - RS41 RH (%)')
        plt.ylabel('Altitude (m)')
        plt.title('RH Bias vs Altitude\n' + self.name)
        plt.show()
        # print(df['RH FP'])





#a = CFH(datarate=2)
#a.dataclean()
#a.plotRH()
#a.plotRHDiff()
#print(a.df)