import Main_Core
import sys
#import runamp

temperature_array = [2000,3000,4000,5000,6000,7000,8000,9000,10000]
temp={2000}
timestep_array = [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02]
#Method1='FIRE'
#Method2='AMP'
#for i,j,k in zip(temperature_array,Method1,Method2):
#for i in temp:
#    Main_Core.Control_main(i,Method1,Method2)
Method2='LJ'
#for j in temperature_array:
#    Main_Core.Control_main(j,Method1,Method2)
Method1='SDLBFGS'
#Method2='AMP'
#for k in temperature_array:
#    Main_Core.Control_main(i,Method1,Method2)
#Method2='LJ'
for l in temperature_array:
    Main_Core.Control_main(l,Method1,Method2)
print('Mission Complete. System ended!')
sys.exit()
