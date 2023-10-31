import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
import global_config.config as gc


stations=gc.experiment_stations
# models.append('/mod')
model_group = 'attention_group_swish'
model_groups=gc.module_group

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 13

models = ['/mod','attention_lyr1_8','attention_val_E32_lyr16_8']
colors = ['blue', 'orange', 'green']
mo_dict = {'attention_lyr1_8':'智能模型6',
    'attention_val_E32_lyr16_8':'智能模型2',

               '/mod':'数值模型'
    }
mod_label=[]
for model in models:
    mod_label.append(mo_dict[model])
# 绘制柱状图
ind = np.arange(4)
width = 0.2

errors = ['rmse','mae']
dir = 'analysis/only_obs_tm/'
for error in errors:

    for station in stations:
        station=station['station']
        fig, ax = plt.subplots()

        data = pd.read_excel(dir+'quarter-' + error + '.xlsx',
                             index_col=0,sheet_name=station)[
            ['attention_group_swish/attention_val_E32_lyr16_8',
             'attention_group_swish/attention_lyr1_8', '/mod']]

        arr = data.values
        num_model = 3

        for i in range(3):
            ax.bar(ind + i*width, arr[:,i], width,
                   color=colors[i], alpha=0.7,
                   label=models[i])

        ax.set_xticks(ind + width*num_model / 2)
        ax.set_xticklabels(['春','夏','秋','冬'])
        ax.set_xlabel('季节')

        ax.set_ylabel(f'{error.upper()}(mg/L)')

        ax.set_title(station)
        ax.legend(loc='upper right', labels=mod_label)

        # plt.show()
        err_dir=f'picture/季节/{error}/'
        if not os.path.exists(err_dir):
            os.makedirs(err_dir)
        plt.savefig(err_dir + f'{station}.png', format='png', dpi=300)

        plt.close()

        print(err_dir + station + '.png___saved!')