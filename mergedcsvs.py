import sys
import csv
import os
import pandas as pd

arguments = str(sys.argv)
mergedcsvs = pd.DataFrame()
arguments = ["Desktop/dataset/accessories.csv", "Desktop/dataset/household_cleaners.csv"]
#add the filename to csv
for i in arguments[1:][:-1]:
    df = pd.read_csv(i)
    df["filename"] = os.path.basename(i)
    mergedcsvs = mergedcsvs.append(df)

final_path = "~./datasets/" + "combined.csv" 
mergedcsvs.to_csv(final_path) 