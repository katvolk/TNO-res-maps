import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2016 SD106; q = 42.70 au, i = 4.81$^\circ$"
obj="2016SD106"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2464562.83
da = 3.84
obspsi = 359.626
abf = 350.2

#used to set y-axis limits
ymin =abf-3.2*da
ymax =abf+4.2*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.5


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


