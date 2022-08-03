import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="148209 (2000 CR105); q = 44.12 au, i = 22.8$^\circ$"

obj="148209-2000CR105"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2438743.209673780631
da = 0.60836
abf = 222.04562323284304
obspsi = 216.63919506270696

#used to set y-axis limits
ymin =abf-4.1*da
ymax =abf+4*da


fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


