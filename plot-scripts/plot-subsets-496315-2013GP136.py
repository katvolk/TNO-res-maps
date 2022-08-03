import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="496315 (2013 GP136); q = 41.04 au, i = 33.54$^\circ$"
obj="496315-2013GP136"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2457755.912684100336
da = 0.18543
abf = 150.18798654781025
obspsi = 227.61277069037206


#used to set y-axis limits
ymin =abf-12*da
ymax =abf+3.4*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.8


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


