import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2015 RX245; q = 45.55 au, i = 12.14$^\circ$"
obj="2015RX245"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2455525.846925336740
da = 5.2
abf = 423.7
obspsi = 345.4169467106339




#used to set y-axis limits
ymin =abf-3.8*da
ymax =abf+3.7*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.8


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


