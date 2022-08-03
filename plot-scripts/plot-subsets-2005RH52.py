import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2005 RH52; q = 39.00 au, i = 20.45$^\circ$"
obj="2005RH52"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2452830.712495823092
da = 0.18
abf = 153.68355198125914
obspsi = 26.055412135766158

#used to set y-axis limits
ymin =abf-5.2*da
ymax =abf+4.2*da


fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=2


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


