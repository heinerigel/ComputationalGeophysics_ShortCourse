from progress_bar import ProgressBarHandler

import numpy as np
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_animation_staggered(local_dict):
    fig = local_dict['fig']
    ax1 = local_dict['ax1']
    ax2 = local_dict['ax2']
    line1 = local_dict['line1']
    line2 = local_dict['line2']

    title = local_dict['title']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    x = local_dict['x']
    v_results = local_dict['v_results']
    s_results = local_dict['s_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    ax1_min_y_lim = None
    ax1_max_y_lim = None
    ax2_min_y_lim = None
    ax2_max_y_lim = None

    def update(n, l1, l2):
        nonlocal ax1_min_y_lim, ax1_max_y_lim, ax2_min_y_lim, ax2_max_y_lim
        
        it = n * idisp
        
        l1.set_data(x, v_results[n])
        l2.set_data(x, s_results[n])
        ax1.set_title(title + ", time step: %i" % (it))

        min_v = min(v_results[n])
        max_v = max(v_results[n])
        min_s = min(s_results[n])
        max_s = max(s_results[n])

        ax1_min = min_v - (max_v - min_v) * 0.05
        ax1_max = max_v + (max_v - min_v) * 0.05
        ax2_min = min_s - (max_s - min_s) * 0.05
        ax2_max = max_s + (max_s - min_s) * 0.05

        if ax1_min_y_lim is None or ax1_min < ax1_min_y_lim:
            ax1_min_y_lim = ax1_min
        else:
            ax1_min = ax1_min_y_lim
            
        if ax1_max_y_lim is None or ax1_max > ax1_max_y_lim:
            ax1_max_y_lim = ax1_max
        else:
            ax1_max = ax1_max_y_lim
            
        if ax2_min_y_lim is None or ax2_min < ax2_min_y_lim:
            ax2_min_y_lim = ax2_min
        else:
            ax2_min = ax2_min_y_lim
            
        if ax2_max_y_lim is None or ax2_max > ax2_max_y_lim:
            ax2_max_y_lim = ax2_max
        else:
            ax2_max = ax2_max_y_lim

        ax1.set_ylim([ax1_min, ax1_max])
        ax2.set_ylim([ax2_min, ax2_max])

        animation_progress_handler(n)
        
        return l1, l2

    return animation.FuncAnimation(fig, update, math.ceil(nt/idisp), fargs=(line1, line2), interval=50)
    
def create_animation_optimal_operator(local_dict):
    fig = local_dict['fig']
    ax = local_dict['ax']
    up31 = local_dict['up31']
    up32 = local_dict['up32']
    up33 = local_dict['up33']
    up34 = local_dict['up34']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    p_results = local_dict['p_results']
    mp_results = local_dict['mp_results']
    op_results = local_dict['op_results']
    ap_results = local_dict['ap_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    def update(n, up31, up32, up33, up34):
        it = n * idisp
        p = p_results[n]
        mp = mp_results[n]
        op = op_results[n]
        ap = ap_results[n]
        
        ax.set_title('Time Step (nt) = %d' % it)
        
        up31.set_ydata(p)
        up32.set_ydata(mp)
        up33.set_ydata(op)
        up34.set_ydata(ap)

        error1 = np.sum((np.abs(p - ap))) / np.sum(np.abs(ap)) * 100
        error2 = np.sum((np.abs(mp - ap))) / np.sum(np.abs(ap)) * 100
        error3 = np.sum((np.abs(op - ap))) / np.sum(np.abs(ap)) * 100

        ax.legend((up31, up32, up33, up34),
            ('3 point FD: %g %%' % error1,
            '5 point FD: %g %%' % error2,
            'optimal FD: %g %%' % error3,
            'analytical'), loc='lower right', fontsize=10, numpoints=1)
        
        animation_progress_handler(n)
        
        return up31, up32, up33, up34

    return animation.FuncAnimation(fig, update, math.ceil(nt/idisp), fargs=(up31, up32, up33, up34), interval=50)


def create_animation_heterogeneous(local_dict):
    fig = local_dict['fig']
    ax = local_dict['ax']
    im_wave = local_dict['im_wave']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    p_results = local_dict['p_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    def update(n, w):
        it = n * idisp
        
        w.set_data(p_results[n])
        ax.set_title(f'Time Step (nt) = {it}, Max P = {p_results[n].max():.2f}')

        animation_progress_handler(n)
        
        return im_wave

    return animation.FuncAnimation(fig, update, math.ceil(nt/idisp), fargs=(im_wave, ), interval=50)


def create_animation_homogeneous(local_dict):
    fig2 = local_dict['fig2']
    ax3 = local_dict['ax3']
    up41 = local_dict['up41']
    up42 = local_dict['up42']
    
    lim = local_dict['lim']
    time = local_dict['time']
    
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    
    p_results = local_dict['p_results']
    seis_results = local_dict['seis_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    def update(n, up41, up42):
        it = n * idisp
        
        up41.set_ydata(seis_results[n])
        up42.set_data(time[it], seis_results[n][it])
        
        ax3.set_title('Time Step (nt) = %d' % it)
        ax3.imshow(p_results[n], vmin=-lim, vmax=+lim, interpolation="nearest", cmap=plt.cm.RdBu)

        animation_progress_handler(n)
        
        return up41, up42

    return animation.FuncAnimation(fig2, update, math.ceil(nt/idisp), fargs=(up41, up42), interval=50)


def create_animation_advection_1d_euler_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig1 = local_dict['fig1']
    ax1 = local_dict['ax1']
    line1 = local_dict['line1']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title1 = local_dict['title1']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)
    
    def update(n, line):
        line.set_ydata(unew_results[n])
        ax1.set_title(title1 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))

        animation_progress_handler(n)
                
        return line,
    
    return animation.FuncAnimation(fig1, update, math.ceil(nt/idisp), fargs=(line1, ), interval=50)


def create_animation_advection_1d_predictor_corrector_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig2 = local_dict['fig2']
    ax2 = local_dict['ax2']
    line2 = local_dict['line2']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title2 = local_dict['title2']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    def update(n, line):
        line.set_ydata(unew_results[n])
        ax2.set_title(title2 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))

        animation_progress_handler(n)

        return line,
    
    return animation.FuncAnimation(fig2, update, math.ceil(nt/idisp), fargs=(line2, ), interval=50)

def create_animation_advection_1d_mccormack_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig3 = local_dict['fig3']
    ax3 = local_dict['ax3']
    line3 = local_dict['line3']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title3 = local_dict['title3']
    
    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    def update(n, line):
        line.set_ydata(unew_results[n])
        ax3.set_title(title3 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))

        animation_progress_handler(n)
        
        return line,
    
    return animation.FuncAnimation(fig3, update, math.ceil(nt/idisp), fargs=(line3, ), interval=50)

def create_animation_advection_1d_lax_wendroff_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig4 = local_dict['fig4']
    ax4 = local_dict['ax4']
    line4 = local_dict['line4']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title4 = local_dict['title4']
    
    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    def update(n, line):
        line.set_ydata(unew_results[n])
        ax4.set_title(title4 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))

        animation_progress_handler(n)
        
        return line,
    
    return animation.FuncAnimation(fig4, update, math.ceil(nt/idisp), fargs=(line4, ), interval=50)