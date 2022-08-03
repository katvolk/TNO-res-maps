import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2015 UN105; q = 41.41 au, i = 37.02$^\circ$"
obj="2015UN105"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2464562.83
da = 2.25
obspsi=46.4
abf = 184.95

#used to set y-axis limits
ymin =abf-3.2*da
ymax =abf+3.2*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


