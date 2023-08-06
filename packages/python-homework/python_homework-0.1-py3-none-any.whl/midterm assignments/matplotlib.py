# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:07:13 2022

@author: 21010104   建筑2104郑思瑶
"""
def evenplot_custtom(data1,**args):
    '''
    Parameters
    ----------
    data_dict : TYPE    二维数组
        DESCRIPTION.    由类数组结构构成的列表可以表示多组事件，每组事件都可以单独设置
    **args : TYPE      用以设置更新样式的参数
        DESCRIPTION.   (可调整的图形样式参数)    

    Returns
    -------
    paras : dict   样式更新后的参数值.
    '''

    import matplotlib.pyplot as plt
    
    
    #配置参数:
    paras={'figuresize':(5,5), #画布大小
           'back_style':'ggplot',#背景风格样式
           'fontsize':10,  #设置字大小
           'font_style':'normal',#设置字风格
           'font_family':'serif',#设置字体形式
           'lines_style':None , #设置线条样式 默认为‘soild’
           'line_width':3, #线条宽度
           'lines_color':('b','c','g','k','r','y'),#线条颜色
           'frame_color':'black',
           'orientation':'horizontal',#时间序列的方向 即方向是垂直的还是水平的
           'lineoffsets':(1,1,1,1,1,1),#直线中心相对原点的偏移量 输入的参数个数应和data1长度相等
           'linelength':(1,1,1,1,1,1),#直线的长度 输入的参数个数应和data1长度相等
           'xlabel':None,  #x轴标签
           'ylabel':None,  #y轴标签
           'title':None,    #设置标题
           'lable_size':10, #标签的大小
           'titlesize':20, #标题大小
           'tick_length':7,  #轴刻度长
           'tick_width':3,   #轴刻度宽
           'tick_color':'b',  #轴刻度的颜色
           }
           
    print(paras)
    paras.update(args)
    print(paras)       
    color_palette=list(paras['lines_color'])#设置线颜色的显示
    lineoff_sets=list(paras['lineoffsets'])
    linelength=list(paras['linelength'])
    
    #根据参数调整打印图表样式
    plt.style.use(paras['back_style'])
    plt.rcParams.update({'font.size':paras['fontsize'],
                         'font.style':paras['font_style'],
                         'font.family':paras['font_family'],
                         'lines.linestyle': paras['lines_style'],
                         'lines.linewidth':paras['line_width'],
                         
                         })
    
    #图表打印
    fig, ax=plt.subplots(1,1,figsize=paras['figuresize']) 
    plt.eventplot(data1,orientation=paras['orientation'],
                  lineoffsets=lineoff_sets,
                  color=color_palette,
                  linelengths=linelength
                  )
   
        
        #配置X和Y轴标签
    ax.set_title(paras['title'],fontsize=paras['titlesize'])
    ax.set_xlabel(paras['xlabel'])
    ax.set_ylabel(paras['ylabel'])
         #配置X和Y轴标签字体大小
    ax.xaxis.label.set_size(paras['labelsize'])
    ax.yaxis.label.set_size(paras['labelsize'])
         #配置轴刻度样式
    ax.tick_params(length=paras['tick_length'],
                   width=paras['tick_width'],
                   color=paras['tick_color'])
    plt.show()    
    
    return paras
#Test:
import numpy as np
data2=np.random.random([6,50])
test_1=evenplot_custtom(data2,
                        figsize=(20,20),
                        back_style='classic',
                        fontsize=20,
                        font_style='italic',
                        font_family='fantasy',#‘serif’, ‘sans-serif’, ‘cursive’, ‘fantasy’, or ‘monospace’
                        lines_style='-',
                        lines_width=5,
                        lines_color=('b','c','g','k','r','y'),
                        linelength=(2,2,3,1,6,1),
                        lineoffsets=(-9, -13, 1, 15, 6, 10),
                        xlabel='Zheng Siyao',
                        ylabel='Architecture2104',
                        title='homework',
                        labelsize=30,
                        titlesize=60,
                        tick_length=5,
                        tick_width=2,
                        tick_color='red'
                        
                        )
print(test_1)
    
                        
                        
                        
                        
                        
    
    
    
    
    
    
    
    