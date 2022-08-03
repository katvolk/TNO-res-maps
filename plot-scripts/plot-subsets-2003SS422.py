import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2003 SS422; q = 39.59 au, i = 16.80$^\circ$"
obj="2003SS422"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2454390.58
da = 0.73
abf = 190.77662139564183
obspsi = 35.93687565235769

#used to set y-axis limits
ymin =abf-6.5*da
ymax =abf+4.8*da


fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.5


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


