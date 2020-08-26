""" This script processes all the log files created by local_min_finder and creates histograms for each logfile. Prior to using this script, move
all log fils to a separate directory. """

import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

def read_logs():
    """ This function processes the logs and collects all the energies from each step of the optimization """
    # iterate 'nuber of log files times'
    for i in range(50):
        # open the log file
        with open('carbon_logs/log_'+str(i), 'r') as log:
            FIRE_energies_array = []
            lines = log.readlines()
            line_index = 0
            # read the file line by line
            for line in lines:
                # ignore the first 2 lines.
                if line_index > 1:
                    data = line.split()
                    # get the energy for the step and append it to the energy array.
                    FIRE_energies_array.append(float(data[3].replace('*', '')))
                line_index = line_index + 1
            print('steps in optimization: {}, final energy: {}'.format(line_index-2, FIRE_energies_array[len(FIRE_energies_array)-1]))
            plot(FIRE_energies_array, i)

  
def plot(FIRE_energies, pic_num):
    """This function plots a histogram of the energies collected from the log file."""
    plt.figure()
    plt.hist(FIRE_energies)
    fig_name = 'carbon_plots/plot_'+str(pic_num)+'.png'
    plt.savefig(fig_name)    

#plot(FIRE_energies_array)
read_logs()
