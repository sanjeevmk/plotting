import argparse
import sys
import matplotlib.pyplot as plt
from omegaconf import OmegaConf
import pandas as pd 
import numpy as np

if __name__ == '__main__':
    config_file = sys.argv[1]
    config = OmegaConf.load(config_file)

    min_val = np.inf    
    for plot,plot_config in config.items():
        csv_path = plot_config['path']
        dataframe = pd.read_csv(csv_path)
        X = plot_config['X']
        Y = plot_config['Y']
        Xvals = dataframe[X].values
        Yvals = dataframe[Y].values

        if np.max(Yvals) < min_val:
            min_val = np.max(Yvals)
        plt.plot(Xvals,Yvals,plot_config['color']+"-",label=plot_config['label'])
    plt.ylim([0,min_val])
    #plt.xlim([0,1000])
    plt.yticks(np.arange(0,min_val,3e-4))
    plt.legend(loc='best')
    plt.show()