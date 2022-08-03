import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2013 SL102; q = 38.13 au, i = 6.50$^\circ$"
obj="2013SL102"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2455316.175634692635
da = 0.75187
abf = 314.3782503138746
obspsi = 32.7778869767315


#used to set y-axis limits
ymin =abf-3.5*da
ymax =abf+3.5*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=2


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


