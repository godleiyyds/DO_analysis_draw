import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cmaps
import os

import draw as draw

import config as gcc
gc = gcc.get_config()


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


stations=gc.experiment_stations

for station0 in stations:

    station = station0['station']
    # fig = plt.figure(figsize=(15, 10), dpi=20)
    fig =plt.figure()

    df = pd.read_excel('不同历史窗口对比.xlsx',sheet_name=station)
    models = df['model']
    df.set_index('model',inplace=True)
    df = df.transpose()
    x = df.index

    for model in models:

        y = df[model]
        plt.plot(x, y, 'o-')  # 绘制带点的折线图

    plt.legend(models,loc='lower right')

    plt.ylim(0,1.8)
    xticks = [ 24, 48, 72, 96, 120]  # 刻度值列表
    xticklabels = [24, 48, 72, 96, 120]  # 标签列表
    plt.xticks(xticks,xticklabels)
    plt.title(station)
    plt.xlabel('历史时长')  # 添加x轴标签
    plt.ylabel('RMSE')  # 添加y轴标签
    # plt.show()

    pic_dir = 'picture/不同历史窗口/'
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)

    fig.savefig(pic_dir + f'{station}.png', format='png')
