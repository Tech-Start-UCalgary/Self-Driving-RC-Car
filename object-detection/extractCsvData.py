import sys
import pandas as pd

class imageData():

    def __init__(self, csvFilepath):
        print("Extracting CSV Data")
        self.dataframe = pd.read_csv(csvFilepath)
        self.iter      =  self.dataframe.iterrows()
        self.retrieveNextDataset()

    def retrieveNextDataset(self):
        try:
            index, info = next(self.iter)
        except:
            index = None
            info  = None

        self.index          = index
        self.filename       = info['filename']
        self.width          = info['width']
        self.height         = info['height']
        self.classification = info['class']
        self.xmin           = info['xmin']
        self.ymin           = info['ymin']
        self.xmax           = info['xmax']
        self.ymax           = info['ymax']

        self.imageDimension = (self.width, self.height)
        self.objectBounds   = (self.xmin, self.ymin, self.xmax, self.ymax)


def main():

    filepath = "./test.csv"
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print("Using file: {}".format(filepath))
    else:
        print("Using default file: ./test.csv")

    data = imageData(filepath)
    
    #first row
    print(data.xmin)
    
    data.retrieveNextDataset()
    print(data.filename)
    
    data.retrieveNextDataset()
    print(data.filename)

if __name__ == "__main__":
    main()