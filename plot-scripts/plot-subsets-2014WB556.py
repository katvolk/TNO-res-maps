import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2014 WB556; q = 42.70 au, i = 24.16$^\circ$"

obj="2014WB556"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"


tp = 2451300.249166475975
da = 1.1
abf = 280.4023853208455
obspsi = 46.80650498964833


#used to set y-axis limits
ymin =abf-4.2*da
ymax =abf+4.2*da



fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.8


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


