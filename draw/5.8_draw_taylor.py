# 定义函数
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cmaps
import os

import draw.draw as draw

import draw.draw as draw
import global_config.config as gc
models = ['mod',
        'attention_lyr1_8','attention_val_E32_lyr16_8'
    ]
stations=gc.experiment_stations
# models.append('/mod')
model_group = 'attention_group_swish'
model_groups=gc.module_group
import pandas as pd
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


file_dir= 'err/only_obs_tm/'


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 13

for station in stations:

    station = station['station']

    pic_dir = 'picture/taylor4/'+station
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)

    file = file_dir + station + '_errors.xlsx'

    df=pd.read_excel(file,sheet_name="All_Data")

    fig = plt.figure(figsize=(48, 32), dpi=300)

    r=df['CORR']
    sstd = df['SSTD']
    model = ['mod',
        'attention_lyr1_8','attention_val_E32_lyr16_8'
    ]


    ax = fig.add_subplot(3, 3, i + 1, projection='polar')  # 添加子图
    ax.text(0.6, 0.1, '({})'.format(chr(i + 97)), fontsize=30)  # 添加子图标题
    draw.tar(ax, r, sstd, model,station)  # 调用函数绘制雷达图

    plt.savefig(pic_dir + 'station.png', format='png',  dpi=300)




