import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.dates as mdates

import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
import config as gcc
gc = gcc.get_config()
datasets_file = 'obs'
stations = gc.experiment_stations
for station0 in stations:
    station = station0['station']
    split_dt = station0['split_dt']
    fig = plt.figure(figsize=(60, 30), dpi=300)

    df= pd.read_excel(f'datasets/{datasets_file}/xlsx-datasets-X/{station}.xlsx')
    # df2 = pd.read_excel(f'datasets/{datasets_file}/xlsx-datasets-Y/{station}.xlsx')
    # df = pd.concat([df, df2], on='时间')
    df = df.drop(columns=df.columns[0], axis=1)
    # 将时间列转换为索引
    df = df.set_index('时间')
    # 将索引转换为DatetimeIndex对象
    df.index = pd.to_datetime(df.index)

    df.drop_duplicates(inplace=True)
    # 重新采样为每个小时一个时间点，空缺的值为 NaN
    df = df.resample('1H').asfreq()

    # 将索引还原为列
    df = df.reset_index()

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    ax = fig.add_subplot(3, 2, 1 )

    x = pd.to_datetime(df['时间'])
    y = df['溶解氧']
    ax.plot(x, y)
    ax.axvline(x=pd.to_datetime(split_dt), linestyle='--')

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    date_fmt = mdates.DateFormatter('%Y-\n%m-%d')
    ax.xaxis.set_major_formatter(date_fmt)

    plt.xticks(fontsize=12)
    plt.yticks(fontsize = 12)

    # ax.legend(mod_label, fontsize=18, loc='best')
    fig.subplots_adjust(bottom=0.2)  # 调整底部边距
    ax.set_xlabel('时间', fontsize=20)
    ax.set_ylabel('溶解氧(mg/L)', fontsize=20)

    ax.set_title(station, fontsize=38)
    save_dir = f"picture/时序图/{datasets_file}/"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    plt.savefig(save_dir + f'/{station}.png',format='png', bbox_inches="tight", dpi=300)

    # 显示图形
    # plt.show()
    plt.close()
    print(save_dir + f'{station}___saved!')