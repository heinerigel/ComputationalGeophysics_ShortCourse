from progress_bar import ProgressBarHandler

import numpy as np
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_animation_fe_elastic_1d_solution(local_dict):
    fig1 = local_dict['fig1']
    ax1 = local_dict['ax1']
    line1 = local_dict['line1']
    line2 = local_dict['line2']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    u_results = local_dict['u_results']
    p_results = local_dict['p_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    y_min = min(np.min(u_results), np.min(p_results))
    y_max = max(np.max(u_results), np.max(p_results))
    y_diff = y_max - y_min

    y_min = y_min - y_diff * 0.1
    y_max = y_max + y_diff * 0.1

    ax1.set_ylim(y_min, y_max)
    
    def update(n, l1, l2):
        global ylim_min, ylim_max
        
        it = n * idisp

        l1.set_ydata(u_results[n])
        l2.set_ydata(p_results[n])
        
        animation_progress_handler(n)
        
        return l1, l2 

    return animation.FuncAnimation(fig1, update, math.ceil(nt/idisp), fargs=(line1, line2, ), interval=50)