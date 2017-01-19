import pandas as pd


class CFH(object):


    def CFHtoSFSC(self, filename=None,)
        if self.filename is None:
            os.chdir("C:\PythonProjects\CFH_Analysis\Upload")
            for i in os.listdir(os.getcwd()):
                if ".dat" in i:
                    print("Identified an unprocessed CFH file")
                    self.filename=i
                else:
                    print("No raw CFH files found")

        pd.read_csv(filename,header=[243,244],index_col=1)

