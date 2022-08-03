import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

objtitle="(90377) Sedna; q = 76.19 au, i = 11.93$^\circ$"
obj = "90377-Sedna"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2449226.084084821257
da = 0.17169
abf = 506.4004055588751
obspsi = 345.23962209513206

#used to set y-axis limits
ymin =abf-6.5*da
ymax =abf+13.5*da


fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=2


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


