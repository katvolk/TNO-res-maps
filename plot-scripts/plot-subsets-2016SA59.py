import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2016 SA59; q = 39.09 au, i = 21.50$^\circ$"
obj="2016SA59"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2453106.10
da = 0.604
abf = 244.8719795085415
obspsi = 60.78847557555366

#used to set y-axis limits
ymin =abf-5.2*da
ymax =abf+5.8*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.8


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


