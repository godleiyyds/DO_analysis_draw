# 定义函数
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cmaps
import os

import draw as draw

import config as gcc
gc = gcc.get_config()
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


stations=gc.experiment_stations


plt.rcParams['font.size'] = 26

for station in stations:

    station = station['station']

    pic_dir = 'picture/taylor4/'+station
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)

    df=pd.read_excel('for泰勒图.xlsx',sheet_name=station)

    fig = plt.figure(figsize=(24, 16), dpi=300)

    r=df['R']
    # mse = df['MSE']
    sstd = df['SSTD']
    # sstd = np.sqrt((1 - r ** 2) * mse )

    model = ['mod',
        # 'attention_lyr1_8',
    ]


    ax = fig.add_subplot(projection='polar')  # 添加子图
    # ax.text(0.6, 0.1, '({})'.format(chr( + 97)), fontsize=30)  # 添加子图标题
    draw.tar(ax, r, sstd, model,station)  # 调用函数绘制雷达图

    plt.savefig(pic_dir + 'station.png', format='png',  dpi=300)




