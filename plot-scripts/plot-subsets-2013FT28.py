import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2013 FT28; q = 43.50 au, i = 17.38$^\circ$"
obj="2013FT28"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2458905.648215038958 
da = 1.591
abf = 291.7332777954395
obspsi = 182.097362160024




#used to set y-axis limits
ymin =abf-3.5*da
ymax =abf+4.2*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.7


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


