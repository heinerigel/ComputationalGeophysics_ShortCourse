from progress_bar import ProgressBarHandler

import numpy as np
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_animation_cheby_elastic(local_dict):
    fig = local_dict['fig']
    ax = local_dict['ax']
    line = local_dict['line']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    u_results = local_dict['u_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    def update(n, l):
        it = n * idisp

        l.set_ydata(u_results[n])
        
        animation_progress_handler(n)
        
        return l, 

    return animation.FuncAnimation(fig, update, math.ceil(nt/idisp), fargs=(line, ), interval=50)


def create_animation_fourier_acoustic_1d(local_dict):
    fig = local_dict['fig']
    l1 = local_dict['line1']
    l2 = local_dict['line2']
    l3 = local_dict['line3']

    ax1 = local_dict['ax1']
    ax2 = local_dict['ax2']
    ax3 = local_dict['ax3']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    isx = local_dict['isx']

    p_results = local_dict['p_results']
    ap_results = local_dict['ap_results']
    sp_results = local_dict['sp_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    y_min = min(np.min(p_results), np.min(ap_results), np.min(sp_results))
    y_max = max(np.max(p_results), np.max(ap_results), np.max(sp_results))
    y_diff = y_max - y_min

    y_min = y_min - y_diff * 0.1
    y_max = y_max + y_diff * 0.1
    
    ax1.set_ylim(y_min, y_max)
    ax2.set_ylim(y_min, y_max)
    ax3.set_ylim(y_min, y_max)
    
    def update(n, l1, l2, l3):
        it = n * idisp

        l1.set_ydata(p_results[n][isx:])
        l2.set_ydata(ap_results[n][isx:])
        l3.set_ydata(sp_results[n][isx:])

        animation_progress_handler(n)
        
        return l1, l2, l3
        
    return animation.FuncAnimation(fig, update, math.ceil(nt/idisp), fargs=(l1, l2, l3), interval=50)


def create_animation_fourier_acoustic_2d(local_dict):
    fig = local_dict['fig']
    
    ax1 = local_dict['ax1']
    ax2 = local_dict['ax2']

    l1 = local_dict['line1']
    l2 = local_dict['line2']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    sp_results = local_dict['sp_results']
    ap_results = local_dict['ap_results']

    def update(n, l1, l2):
        it = n * idisp

        ax1.imshow(sp_results[n], interpolation="bicubic", cmap=plt.cm.RdBu)
        ax2.imshow(ap_results[n], interpolation="bicubic", cmap=plt.cm.RdBu)

        # l1.set_data(sp_results[n])
        # l2.set_data(ap_results[n])

        animation_progress_handler(n)
        
        return (l1, l2)

    return animation.FuncAnimation(fig, update, math.ceil(nt/idisp), fargs=(l1, l2), interval=50)
    