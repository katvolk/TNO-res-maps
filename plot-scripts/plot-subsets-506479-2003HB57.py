import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


obj="506479-2003HB57"
objtitle="506479 (2003 HB57); q = 38.10 au, i = 15.50$^\circ$"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"


tp = 2454925.405929488149
da = 0.35359
abf = 159.67434702143288
obspsi = 243.62369676457348

#used to set y-axis limits
ymin =abf-9*da
ymax =abf+4.5*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.5


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')

