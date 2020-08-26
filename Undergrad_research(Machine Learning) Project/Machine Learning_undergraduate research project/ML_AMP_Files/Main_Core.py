import os.path
from os import path
import Create_MD_v
import train
import AMPGraphFrame
import LJGraphFrame
import test

def Control_main(temp,Method1,Method2):
    #remove previously trained model if retraining or remove test set if generating new test set
    #trainingsetname and testingsetname are global variables
    if path.exists('./structures/lj5/'+str(temp)+'.traj'):
        os.system('rm -r amp* ')#+filename)
        os.system('rm ./structures/lj7_MD/'+str(temp)+'.traj, amp*')
        print('Previous traj file and amp records exist. Delete Complete!')
    elif path.exists('./Final_Collection/'+str(temp)+'K_AMP_'+Method1+'.png'):
        os.system('rm ./Final_Collection/'+str(temp)+'K_AMP_'+Method1+'.png')
        print('Previous graph exists. Delete Complete!')
    ### Method 1 : FIRE or SDLBFGS, Method 2 : AMP or LJ
    ### set the creating MD and optimization
    Create_MD_v.MD_Opt_Section(temp,Method1)
    ### Training starts in this time.
    SetName = str(temp)+'.traj'
    ### Show the training data in the graph
    if Method1=='FIRE' and Method2=='AMP':
        print('MD Optimization is done, and Training starts as FIRE.')
        ConvergenceCriteria = {'energy_maxresid' : 0.05, 'force_maxresid' : None}
        result, calc = train.train_amp(ConvergenceCriteria,SetName,5)
        if result != 'success' :
            print('Your training has a problem. Restart training!')
            result, calc = train.train_amp(ConvergenceCriteria,SetName,5)
        print('Training is done, and next process graph results.')
        test.test_amp(calc,SetName,500,'Training and testing at '+str(temp)+'K',str(temp)+'K_AMP_FIRE.png')
    elif Method1=='FIRE' and Method2=='LJ':
        print('MD Optimization is done, and LJ computation and graphing starts!')
        LJGraphFrame.show_LJ(SetName,5000,'Training and testing at '+str(temp)+'K',str(temp)+'K_LJ_FIRE.png')
    elif Method1=='SDLBFGS' and Method2=='AMP':
        print('MD Optimization is done, and Training starts as SDLBFGS.')
        ConvergenceCriteria = {'energy_maxresid' : 0.05, 'force_maxresid' : None}
        result, calc = train.train_amp(ConvergenceCriteria,SetName,5)
        if result != 'success' :
            print('Your training has a problem. Restart training!')
            result, calc = train.train_amp(ConvergenceCriteria,SetName,5)
        print('Training is done, and next process graph results.')
        test.test_amp(calc,SetName,500,'Training and testing at '+str(temp)+'K',str(temp)+'K_AMP_SDLBFGS.png')
    elif Method1=='SDLBFGS' and Method2=='LJ':
        print('MD Optimization is done, and LJ computation and graphing starts!')
        LJGraphFrame.show_LJ(SetName,5000,'Training and testing at '+str(temp)+'K',str(temp)+'K_L_LJ_SDLBFGS.png')
    print(str(temp)+'K ended, and go to the next temperature')
