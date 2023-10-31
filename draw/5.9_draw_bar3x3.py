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
# 创建随机数据集，含有4个站点，4个季节，误差指标为均方根误差（RMSE）
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# stations = ['Station A', 'Station B', 'Station C', 'Station D']

# rmse_data = pd.DataFrame({
#     'Season': np.random.choice(seasons, size=100),
#     'Station': np.random.choice(stations, size=100),
#     'RMSE': np.random.uniform(low=0.0, high=5.0, size=100)
# })
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 13




# 设置模型的名称和颜色
# models = ['模型1', '模型2', '模型3']
models = ['attention_group_swish/attention_val_E32_lyr16_8',
         'attention_group_swish/attention_lyr1_8', '/mod']
colors = ['blue', 'orange', 'green']
mo_dict = {'attention_group_swish/attention_lyr1_8':'智能模型6',
               'attention_group_swish/attention_val_E32_lyr16':'智能模型1',
    'attention_group_swish/attention_val_E32_lyr16_8':'智能模型2',
    'attention_group_swish/attention_val_E64_lyr32':'智能模型3',
    'attention_group_swish/attention_val_E64_lyr32_16':'智能模型4',
    'attention_group_swish/attention_val_E64_lyr32_16_8':'智能模型5',
    'attention_group_swish/attention_val_lyr1_8':'智能模型7',

               '/mod':'数值模型'
    }
# 绘制柱状图
ind = np.arange(4)
width = 0.2
plt.rcParams['font.size'] = 30
k=0
fig = plt.figure(figsize=(48, 32), dpi=300)
for station in stations:
    station=station['station']
    # fig, ax = plt.subplots()

    ax = fig.add_subplot(3, 3, k + 1)  # 添加子图
    ax.text(0.6, 0.1, '({})'.format(chr(k + 97)), fontsize=30)  # 添加子图标题
################################################################################3
    data = pd.read_excel('analysis/only_obs_tm/quarter-rmse.xlsx',
                         index_col=0,sheet_name=station)[
        ['attention_group_swish/attention_val_E32_lyr16_8',
         'attention_group_swish/attention_lyr1_8', '/mod']]

    arr = data.values
    num_model = 3

    for i in range(3):
        # if model != '/mod':
        #     model = model_group + '/' + model

        ax.bar(ind + i*width, arr[:,i], width,
               color=colors[i], alpha=0.7,
               label=mo_dict[models[i]])

        # 将季节名称设置为x轴标签
    ax.set_xticks(ind + width*num_model / 2)
    ax.set_xticklabels(['春','夏','秋','冬'])
    ax.set_xlabel('季节')
    ####################################3
    ax.set_ylabel('RMSE(mg/L)')
    ax.set_title(station)


    ax.legend()

    k = k + 1

    # plt.show()
dir=f'picture/季节2/'
if not os.path.exists(dir):
    os.makedirs(dir)
###########################################
plt.savefig(dir + 'season_rmse.png', format='png', bbox_inches="tight", dpi=300)

