#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from ase import Atoms, Atom, units
import ase.io
import tsase
import numpy as np
import sys
from amp import Amp
import matplotlib
matplotlib.use("agg")
import matplotlib.mlab as mlab
#import plotly.tools as tls
#import plotly.plotly as py
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def show_LJ(testingsetname,testingnumber,plottitle,plotfigure):
    #creating array for energies calculated with LJ calculator
    lennardjones=[]
    #reads in testing set
    traj=ase.io.Trajectory('./structures/lj5/'+testingsetname, 'r')
    numb2=0
    for p in traj:
        #Set the LJ calculator
        lj = tsase.calculators.lj(cutoff=15)
        p.center(50.0)
        p.set_calculator(lj)
        lennardjones.append(p.get_potential_energy())
        numb2=numb2+1
        #catch if more items in test set than intended
        if numb2 >= testingnumber:
            break
    traj.close()
    # set the maximum and minimum value, bins of lennardjones for histogram
    Max_len = np.amax(lennardjones)
    Min_len = np.amin(lennardjones)
    gap = (Max_len-Min_len)/20.0
    bins_conf = np.arange(Min_len,Max_len,gap)
    # erase the previous histogram.
#    plt.clf()
    # set a new plot to make new histogram
    fig, ax = plt.subplots()
    # make a Lennardjones histogram
    n, bins, patches = plt.hist(lennardjones, bins_conf, range=(Min_len,Max_len), color = 'skyblue', alpha = 0.5, rwidth = 0.85, histtype='bar',stacked=True)
    # Set the xaxis' stick labels to be formatted with 3 decimal place as vertical
    ax.set_xticks(bins)
    ax.set_xticklabels(bins, rotation = 90)
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.3f'))
    # refine histogram distribution from float to int
    n = n.astype(int)
    # set y(count, percentage) value display to view the histogram as statistics.
    bin_x_centers = 0.5 * np.diff(bins) + bins[:-1]
    bin_y_centers = ax.get_yticks()[1] * 0.25
    # Display the count of data points and % for each bar in histogram
    for i in range(len(bins)-1):
        bin_label = "{0:,}".format(n[i]) + "  ({0:,.2f}%)".format((float(n[i])/n.sum())*100)
        plt.text(bin_x_centers[i], bin_y_centers, bin_label, rotation=90, rotation_mode='anchor')
    # set the x label, ylabel, and title and adjust size
    plt.xlabel('Energy Calculated using LJ Potential (eV)')
    plt.ylabel('Frequency')
    plt.title(plottitle)
    plt.subplots_adjust(bottom=0.15)
    #save as .png file about the histogram
    plt.savefig("./Final_Collection/"+plotfigure)
