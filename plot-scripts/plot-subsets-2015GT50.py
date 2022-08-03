import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2015 GT50; q = 38.41 au, i = 8.79$^\circ$"
obj="2015GT50"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2451606.941692762231
da = 2.4843
abf = 311.43396968397633
obspsi = 229.7954852929433



#used to set y-axis limits
ymin =abf-4*da
ymax =abf+3.2*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=2


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


