import CFH_Tools
import pandas as pd
import os
import matplotlib.pyplot as plt




class RAOB(object):


    def __init__(self, *args):
        self.CFH = False
        self.RS92 = False
        self.RS41 = False
        if 'CFH' in args:
            CFHDF = CFH_Tools.CFH(datarate=2)
            self.CFHDF = CFHDF.getCFHDF()
            self.trop = CFHDF.getTROP()
            self.name = CFHDF.getNAME()
            self.CFH = True
        if 'RS92' in args:
            for i in os.listdir(os.getcwd()):
                if "72999" in i:
                    filename=str(i)
                    break
                else:
                    print("Cannot find filename")
            self.RS92DF = pd.read_csv(filename,sep='\s+',header=None,skiprows=11,names =('Press','Temp','Dewp','RH',
                                                                                         'Dir','Sped','Alt','Lat',
                                                                                         'Lon','Time'))
            self.RS92DF['Alt'] /= 1000
            self.RS92 = True

        if 'RS41' in args:
            for i in os.listdir(os.getcwd()):
                if "70999" in i:
                    filename=str(i)
                    break
                else:
                    print("Cannot find filename")
            self.RS41DF = pd.read_csv(filename,sep='\s+',header=None,skiprows=11,names =('Press','Temp','Dewp','RH',
                                                                                         'Dir','Sped','Alt','Lat',
                                                                                         'Lon','Time'))
            self.RS41DF['Alt'] /= 1000
            self.RS41 = True

    def plotRH(self):
        if self.CFH is True:
            CFHDF = self.CFHDF
            plt.plot(CFHDF['RH FP'],CFHDF['Alt'])
        if self.RS92 is True:
            plt.plot(self.RS92DF['RH'],self.RS92DF['Alt'])
        if self.RS41 is True:
            plt.plot(self.RS41DF['RH'],self.RS41DF['Alt'])
        plt.axhline(y=int(self.trop)/1000)
        plt.xlabel('Relative Humidity (%)')
        plt.ylabel('Altitude (m)')
        plt.title('RH vs Altitude\n'+ self.name)
        plt.show()

    def plotRHDiff(self,RAOB1,RAOB2):

        if RAOB1 or RAOB2 == 'CFH':
            plt.plot(self.CFHDF['RH FP']-RAOB2['RH']),self.CFHDF['Alt']
        else:
            plt.plot((RAOB1['RH']-RAOB2['RH']),RAOB1['RH'])

        plt.axhline(y=int(self.trop) / 1000)
        plt.xlabel('CFH RH (%) - RS41 RH (%)')
        plt.ylabel('Altitude (m)')
        plt.title('RH Bias vs Altitude\n' + self.name)
        plt.show()

a = RAOB('CFH','RS92')
a.plotRH()