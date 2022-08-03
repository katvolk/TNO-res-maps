import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

objtitle="505478 (2013 UT15); q = 43.92 au, i = 10.65$^\circ$"
obj = "505478-2013UT15"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2459124.466113724302
da = 0.83122
abf = 200.30611824555663
obspsi = 353.3747921110522


#used to set y-axis limits
ymin =abf-3.2*da
ymax =abf+4.1*da


fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1.3


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


