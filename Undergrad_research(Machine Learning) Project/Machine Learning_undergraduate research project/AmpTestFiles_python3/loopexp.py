import LBFGS_run
#import runamp

temperature_array = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
timestep_array = [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02]
#def Iterate_array(num):
#    runamp.main_ML(i)

for i,j in zip(temperature_array, timestep_array):
    LBFGS_run.main_ML(i, j)
