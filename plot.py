import matplotlib.pyplot as plt
import numpy as np
from file_IO import read_csv_pandas,take_data_from_csv

def plot_data():
    data1 = read_csv_pandas('data.csv')
    data2 = read_csv_pandas('data2.csv')

    fig = plt.figure(figsize=(10,5))

    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    columns_name = data1.columns
    x = take_data_from_csv(data1,0)

    fps1 = take_data_from_csv(data1,1)
    ax1.plot(x,fps1,'g',linewidth=3,marker='o')
    fps2 = take_data_from_csv(data2,1)
    ax1.plot(x,fps2,'b',linewidth=3,marker='o')
    ax1.grid(True)
    ax1.set_xlabel("Game number")
    ax1.set_ylabel("Average FPS")
    ax1.set_xticks(x)
    ax1.set_yticks(np.arange(23,33,1))
    ax1.set_xlim(1,len(x))

    coin1 = take_data_from_csv(data1,2)
    ax2.plot(x,coin1,'y',linewidth=3,marker='o')
    coin2 = take_data_from_csv(data2,2)
    ax2.plot(x,coin2,'r',linewidth=3,marker='o')
    ax2.grid(True)
    ax2.set_xlabel("Game number")
    ax2.set_ylabel("Coins")
    ax2.set_xticks(x)

    plt.show()