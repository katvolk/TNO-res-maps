import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2015 KH163; q = 39.94 au, i = 27.14$^\circ$"
obj="2015KH163"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2451690.809469654603
da = 0.58375
abf = 152.98469212347587
obspsi = 233.01881892222903

#used to set y-axis limits
ymin =abf-3.2*da
ymax =abf+3.6*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.3


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


