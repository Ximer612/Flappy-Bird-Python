#1)
#write your own reader and writer for csv files using file IO and string manipulation
def read_data_from_csv(path):
    with open(path, "r") as csv_file:
        rows = csv_file.readlines()

        data = []

        for row in rows:
            key = row.split(',')
            key[len(key)-1] = key[len(key)-1].rstrip("\n")
            data.append(key)

        return data

def write_data_from_csv(path,data):
    with open(path, "w") as csv_file:
        for rows in data:
            for value in rows:
                if(value == rows[0]):
                    csv_file.write(value)
                else:
                    csv_file.write(','+value)
            csv_file.write('\n')


data = read_data_from_csv("D:\Python AIV\L5\exercises\data.csv")
write_data_from_csv("D:\Python AIV\L5\exercises\data_2.csv",data)

#2)
# using csv writer and one of the pyxel app you created
# write data from the app down to a csv file
# as an example you could store the update (frame) time over the total execution times using the time module (import time)
# find the information you want to store to a csv file
# use then the csv file to plot them on the graph that suits them the most
# #feel free to use numpy, pandas or csv to read the csv file
# try to compare graphs from different executions (try to run the program for the same amount of time when comparing)
# 
# hint: opening a file, writing to disk and closing a file is a slow operation, try to avoid doing it every single frame
#  

import plot

plot.plot_data()