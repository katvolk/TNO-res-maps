import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2012 VP113; q = 80.52 au, i = 24.05$^\circ$"
obj="2012VP113"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"


tp = 2443763.055879228688
da = 1.5
abf = 262.0052462981434
obspsi = 126.36968000814826

#used to set y-axis limits
ymin =abf-1.1*da
ymax =abf+1.1*da



fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.5


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


