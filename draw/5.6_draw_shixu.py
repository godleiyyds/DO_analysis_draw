import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.dates as mdates
import openpyxl
import config as gcc
gc = gcc.get_config()
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


stations=gc.experiment_stations
model_dict = {'attention_group_swish':'attention_val_lyr1_8',
              'BW_group':'BP',
              'gru_group':'gru_dense_sum',
              'lstm_group':'lstm_dense_sum',
              'm_attention_p_group':'Attention_do_chl_qw_qy',}
# model_groups=['attention_group_swish','BW_group','gru_group','lstm_group','m_attention_p_group',]
model_groups = [ 'm_attention_p_group', ]
mod_label=['obs','mod','mk2']

plt.rcParams['font.size'] = 80
i=0
for station0 in stations:
    station = station0['station']
    split_dt = station0['split_dt']
    fig = plt.figure(figsize=(60, 30), dpi=300)
    ax = fig.add_subplot(3, 2, 1)

    # dir = f'errors/data_obs_72_48/{station}/{model_group}/{model_dict[model_group]}.xlsx'
    dir = f'errors/data_obs/{station}/mod.xlsx'
    df= pd.read_excel(dir)

    # 将时间列转换为索引
    df = df.set_index('时间')
    # 重新采样为每个小时一个时间点，空缺的值为 NaN
    df = df.resample('1H').asfreq()
    # 将索引还原为列
    df = df.reset_index()

    x = pd.to_datetime(df['时间'])
    y = df['观察值']
    ax.plot(x, y)
    z = df['mod']
    ax.plot(x, z)

    for model_group in model_groups:
        dir = f'errors/data_obs/{station}/{model_group}/{model_dict[model_group]}.xlsx'
        df = pd.read_excel(dir)
        # 将时间列转换为索引
        df = df.set_index('时间')
        # 重新采样为每个小时一个时间点，空缺的值为 NaN
        df = df.resample('1H').asfreq()
        # 将索引还原为列
        df = df.reset_index()
        x = pd.to_datetime(df['时间'])
        y = df[f'{model_group}/{model_dict[model_group]}']
        ax.plot(x, y)

    ax.axvline(x=pd.to_datetime(split_dt), linestyle='--')

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    date_fmt = mdates.DateFormatter('%Y-\n%m-%d')
    ax.xaxis.set_major_formatter(date_fmt)

    plt.xticks(fontsize=12)
    plt.yticks(fontsize = 12)

    ax.legend(mod_label, fontsize=18, loc='best')
    fig.subplots_adjust(bottom=0.2)  # 调整底部边距
    ax.set_xlabel('时间', fontsize=20)
    ax.set_ylabel('溶解氧(mg/L)', fontsize=20)

    ax.set_title(station, fontsize=38)
    save_dir = "picture/时序图/"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    plt.savefig(save_dir + f'/{station}.png',format='png', bbox_inches="tight", dpi=300)

    # 显示图形
    plt.show()
    plt.close()
    print(save_dir + f'/{station}___saved!')