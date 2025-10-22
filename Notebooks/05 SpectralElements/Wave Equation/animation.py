from progress_bar import ProgressBarHandler

import numpy as np
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_animation_se_hetero_1d_solution(local_dict):
    fig1 = local_dict['fig1']
    ax1 = local_dict['ax1']
    line1 = local_dict['line1']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    u_results = local_dict['u_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    
    def update(n, l1):        
        it = n * idisp

        l1.set_ydata(u_results[n])

        y_min = np.min(u_results[n])
        y_max = np.max(u_results[n])
        y_diff = y_max - y_min

        y_min = y_min - y_diff * 0.1
        y_max = y_max + y_diff * 0.1

        ax1.set_ylim(y_min, y_max)

        animation_progress_handler(n)
        
        return l1 

    return animation.FuncAnimation(fig1, update, math.ceil(nt/idisp), fargs=(line1, ), interval=50)

def create_animation_se_homo_1d_solution(local_dict):
    fig1 = local_dict['fig1']
    ax1 = local_dict['ax1']
    line1 = local_dict['line1']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    u_results = local_dict['u_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    
    def update(n, l1):        
        it = n * idisp

        l1.set_ydata(u_results[n])

        y_min = np.min(u_results[n])
        y_max = np.max(u_results[n])
        y_diff = y_max - y_min

        y_min = y_min - y_diff * 0.1
        y_max = y_max + y_diff * 0.1

        ax1.set_ylim(y_min, y_max)

        animation_progress_handler(n)
        
        return l1 

    return animation.FuncAnimation(fig1, update, math.ceil(nt/idisp), fargs=(line1, ), interval=50)

