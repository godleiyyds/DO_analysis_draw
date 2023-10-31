import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
import global_config.config as gc

stations=gc.experiment_stations

hours = [i for i in range(24)]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 13

models = ['attention_group_swish/attention_val_E32_lyr16_8',
         'attention_group_swish/attention_lyr1_8', 'mod']

mo_dict = {'attention_group_swish/attention_lyr1_8':'智能模型6',
               'attention_group_swish/attention_val_E32_lyr16':'智能模型1',
    'attention_group_swish/attention_val_E32_lyr16_8':'智能模型2',
    'attention_group_swish/attention_val_E64_lyr32':'智能模型3',
    'attention_group_swish/attention_val_E64_lyr32_16':'智能模型4',
    'attention_group_swish/attention_val_E64_lyr32_16_8':'智能模型5',
    'attention_group_swish/attention_val_lyr1_8':'智能模型7',

               'mod':'数值模型'
    }
mod_label=[]

for model in models:
    mod_label.append(mo_dict[model])

# 绘制柱状图
ind = np.arange(4)
width = 0.2
plt.rcParams['font.size'] = 15
k=0
fig = plt.figure(figsize=(48, 32), dpi=300)
for station in stations:
    station=station['station']
    fig, ax = plt.subplots()

    # ax = fig.add_subplot(3, 3, k + 1)  # 添加子图
    # ax.text(0.6, 0.1, '({})'.format(chr(k + 97)), fontsize=30)  # 添加子图标题
################################################################################3
    data = pd.read_excel(f'err/only_obs_tm/{station}_errors.xlsx',
                         sheet_name='Hourly')[
        ['hour',
         'CORR']]


    num_model = 3

    i=0
    for model in models:
    # data2 = data['CORR']['mod' in data['quarter']]
    # 获取符合条件的行的索引
        indices = (data['hour'].str.contains(model)) & (~data['CORR'].isna())

        # 根据索引获取符合条件的行，并挑选相应的列
        data2 = data.loc[indices, ['CORR']]

        arr = data2.values.ravel().astype(float)

        ax.plot(hours,arr)
        plt.xticks(range(24), hours)

        i=i+1

    ax.legend(mod_label)

    ax.set_xlabel('Hour')
    ####################################3
    ax.set_ylabel('CORR')
    ax.set_title(station)




    k = k + 1

    # plt.show()
    dir=f'picture/H_Corr/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    ###########################################
    plt.savefig(dir + f'{station}_hour_corr.png', format='png', dpi=300)

