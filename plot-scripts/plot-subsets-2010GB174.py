import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2010 GB174; q = 48.59 au, i = 21.56$^\circ$"
obj="2010GB174"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"


tp = 2433810.730676114021
da = 7.3
abf = 348.5956629320529
obspsi = 279.1616254760241


#used to set y-axis limits
ymin =abf-1.5*da
ymax =abf+1.5*da



fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


