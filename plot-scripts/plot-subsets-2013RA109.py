import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2013 RA109; q = 46.01 au, i = 12.40$^\circ$"
obj="2013RA109"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2454244.919821578513
da = 2.1454
abf = 462.6361322185546
obspsi = 46.677468882203755



#used to set y-axis limits
ymin =abf-3.8*da
ymax =abf+3.2*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.8


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


