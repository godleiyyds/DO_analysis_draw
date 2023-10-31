import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.dates as mdates
import draw.draw as draw
import global_config.config as gc
import pandas as pd




stations=gc.experiment_stations

# models=gc.training_model
models = ['mod',
        'attention_lyr1_8','attention_val_E32_lyr16_8'
    ]

# models.append('/mod')
model_group = 'attention_group_swish'
model_groups=gc.module_group

errors = ['rmse','mae']
dir = 'analysis/only_obs_tm/'

mo_dict = {'attention_group_swish/attention_lyr1_8':'智能模型6',
               'attention_group_swish/attention_val_E32_lyr16':'智能模型1',
    'attention_group_swish/attention_val_E32_lyr16_8':'智能模型2',
    'attention_group_swish/attention_val_E64_lyr32':'智能模型3',
    'attention_group_swish/attention_val_E64_lyr32_16':'智能模型4',
    'attention_group_swish/attention_val_E64_lyr32_16_8':'智能模型5',
    'attention_group_swish/attention_val_lyr1_8':'智能模型7',

               'mod':'数值模型'
    }
mod_label=['观察值']
for model in models:
    if model != 'mod':
        model = model_group + '/' + model

    mod_label.append(mo_dict[model])

    # 创建图形
# fig = plt.figure(figsize=(60, 30), dpi=300)
plt.rcParams['font.size'] = 80
i=0
for station in stations:
    station = station['station']

    fig = plt.figure(figsize=(60, 30), dpi=300)

    df= pd.read_excel(dir+'preds_label.xlsx',sheet_name=station)

    # 将时间列转换为索引
    df = df.set_index('时间')

    # 重新采样为每个小时一个时间点，空缺的值为 NaN
    df = df.resample('1H').asfreq()

    # 将索引还原为列
    df = df.reset_index()

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    ax = fig.add_subplot(3, 2, 1 )

    x = pd.to_datetime(df['时间'])
    y = df['观察值']
    ax.plot(x, y)

    for model in models:

        if model !='mod':
            model = model_group + '/' + model

        z = df[model]
        ax.plot(x, z)

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
    # plt.show()
    plt.close()
    print(save_dir + f'/{station}___saved!')