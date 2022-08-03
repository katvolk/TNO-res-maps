import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2016 QV89; q = 39.95 au, i = 21.39$^\circ$"
obj="2016QV89"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2449875.464077838767
da = 0.08043
abf = 171.61710605366616
obspsi = 39.77949722070504

#used to set y-axis limits
ymin =abf-22*da
ymax =abf+10*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.5


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


