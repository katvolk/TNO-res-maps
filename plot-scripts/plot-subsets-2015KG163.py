import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2015 KG163; q = 40.49 au, i = 13.99$^\circ$"
obj="2015KG163"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2459399.633954899977
da = 5.1
abf = 680.5153184173219
obspsi = 256.94736881290476


#used to set y-axis limits
ymin =abf-1.5*da
ymax =abf+1.5*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=3


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


