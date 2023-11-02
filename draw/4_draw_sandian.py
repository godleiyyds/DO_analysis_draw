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


stations=gc.experiment_stations
# model_dict = {'attention_group_swish':'attention_val_lyr1_8',
#               'BW_group':'BP',
#               'gru_group':'gru_dense_sum',
#               'lstm_group':'lstm_dense_sum',
#               'm_attention_p_group':'Attention_do_chl_qw_qy',}
# model_groups=['attention_group_swish','BW_group','gru_group','lstm_group','m_attention_p_group',]

models = ['mod',
         # 'attention_group_swish/attention_val_lyr1_8',
         # 'BW_group/BP',
         # 'gru_group/gru_dense_sum',
         # 'lstm_group/lstm_dense_sum',
         # 'Nbeats/nbeats',
         'm_attention_p_group/Attention_do_chl_qw_qy',
          ]

i=0

for station0 in stations:
    station = station0['station']
    split_dt = station0['split_dt']

    dir = 'station_error.xlsx'
    df = pd.read_excel(dir,sheet_name=station)

    obs = df["观察值"]

    fig = plt.figure(figsize=(48, 48), dpi=300)

    ty=0.1

    i=0

    for model in models:

        fig, ax = plt.subplots()

        pred = df[model]

        ax.scatter(obs, pred,s=0.5, label=model)

        ax.plot(obs, obs, "k--")
        z = np.polyfit(obs, pred, 1)
        p = np.poly1d(z)
        ax.plot(obs, p(obs), "r-")

        slope = z[0]

        ax.text(0.7, ty, f"Slope: %.2f" % slope, transform=ax.transAxes)
        # ty=ty+0.1

        ax.legend(fontsize=12)
        ax.set_ylabel("预测值(mg/L)", fontsize=15)
        ax.set_xlabel("观测值(mg/L)", fontsize=15)
        xmin=ymin=0
        xmax=ymax=15
        ax.axis([xmin, xmax, ymin, ymax])

        i=i+1

        fig.suptitle(f"{station}:{model}", fontsize=15)

        save_dir = "picture/sandian5/" + station + '/'

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # # 保存为矢量图 (SVG格式)
        plt.savefig(save_dir + f'model_{i}.png',format='png', bbox_inches="tight", dpi=300)


        # 显示图形
        # plt.show()
        plt.close()
        print(save_dir + ".png___saved!")