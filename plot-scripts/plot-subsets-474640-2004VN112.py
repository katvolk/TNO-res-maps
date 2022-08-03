import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

objtitle="474640 (2004 VN112); q = 47.32 au, i = 25.55$^\circ$"
obj = "474640-2004VN112"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"

tp = 2455006.151063675509
da = 1.7
abf = 327.77541250129303
obspsi = 67.40572984153434

#used to set y-axis limits
ymin =abf-4*da
ymax =abf+4*da

fig = plt.figure(figsize=(4.1,3.5))
#(ideal point size depends on the zoom)
pointsize=1


#####really lazy way of running the plotting script without having
#####to clean it up and make it a nice function.....
def run_file(path):
    return exec(open(path).read());
run_file('code-to-plot-tp-file.py')


