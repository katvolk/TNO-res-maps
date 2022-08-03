import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


objtitle="2018 AD39; q = 38.67 au, i = 19.77$^\circ$"

obj="2018AD39"

figfile= "../plots/" + obj + ".pdf"
filename = "../data/selected-tp-" + obj + ".txt"


tp = 2428354.929905455658
da = 7.5512
abf = 165.80691350946438
obspsi = 213.1215735331265

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


