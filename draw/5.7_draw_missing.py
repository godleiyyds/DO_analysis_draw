import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
# import datetime as dt
from matplotlib.ticker import IndexLocator, FuncFormatter

import config as gcc
gc = gcc.get_config()

stations = gc.experiment_stations

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

for station in stations:
    station = station['station']

    df = pd.read_excel('do_ch_etc.xlsx',sheet_name=station)[['时间','气温', '气压', '叶绿素', '溶解氧']]

    # 将时间列设置为索引
    df.set_index('时间', inplace=True)
    # 重采样到每月
    df = df.resample('H').mean()
    # 将时间索引恢复成时间列
    df = df.reset_index()

    df['时间'] = pd.to_datetime(df['时间']).dt.strftime('%Y-%m-%d')
    # 设置缺失值为NaN
    df['溶解氧'] = pd.to_numeric(df['溶解氧'], errors='coerce')
    df['气温'] = pd.to_numeric(df['气温'], errors='coerce')
    df['气压'] = pd.to_numeric(df['气压'], errors='coerce')
    df['叶绿素'] = pd.to_numeric(df['叶绿素'], errors='coerce')

    # 将时间列设置为索引并排序
    df.set_index('时间', inplace=True)
    df.sort_index(ascending=False, inplace=True)

    # 绘制缺失数据热图
    plt.figure(figsize=(30, 15))
    sns.heatmap(df.isnull(), cmap='YlGnBu', cbar=False,annot_kws={'size': 38, 'weight': 'bold'})
    # sns.heatmap(df, cmap='YlGnBu', cbar=False)
    plt.yticks( size=10)  # 设置大小及加粗
    plt.xticks(size=35)
    plt.ylabel('时间', fontsize=35)


    # # 自定义y轴刻度间隔
    # def y_tick_formatter(x, pos):
    #     # 只显示每5个月的y轴标签
    #     if pos % 5 == 0:
    #         return f'{x}'
    #     else:
    #         return ''
    #
    #
    # yticks_interval = IndexLocator(base=1, offset=-0.5)
    # yticks_formatter = FuncFormatter(y_tick_formatter)
    # plt.gca().yaxis.set_major_locator(yticks_interval)
    # plt.gca().yaxis.set_major_formatter(yticks_formatter)


    # plt.ylabel
    plt.title(f'{station}缺失数据',fontsize = 40)
    # plt.show()
    save_dir = "missing_heatmap/"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    plt.savefig(save_dir + f'{station}.png',format='png')
    print(station+"站点__缺失值热力图已生成")