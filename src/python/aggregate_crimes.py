import argparse
import pandas as pd

def parse_args():
    argumentParser = argparse.ArgumentParser()
    #input parameters
    argumentParser.add_argument("-i", "--inputFile", help="Location of input file", default="./data/Crimes.csv", type=str)
    #output parameters
    argumentParser.add_argument("-o", "--outputFile", help="Location of input file", default="./data/CrimesAggregated.csv", type=str)
    #run settings parameters
    argumentParser.add_argument("-relativeCrimesCalc", "--relativeCrimesCalc", help="Should calculate crime percentage of total districts", default=False, action="store_true")
    argumentParser.add_argument("-debug", "--debug", help="Should print debug info", default=False, action="store_true")

    return argumentParser.parse_args()

def readInput(inputFile):
    return pd.read_csv(inputFile, delimiter=",")



def writeDF(outputFile, df):
    return df.to_csv(outputFile, header=True)

def main():
    #process input
    arguments = parse_args()
        
    #process input
    data = readInput(arguments.inputFile)
    if arguments.debug:
        print lineno()
        data[:30].show()

    dataAgg = data.groupby(["District","Primary Type"]).size()
    if arguments.relativeCrimesCalc:
        dataAgg = dataAgg.groupby(level=0).apply(lambda x:  100 * x / float(x.sum()))
    writeDF(arguments.outputFile, dataAgg)
    
    #print summary


if __name__ == "__main__":
    main()