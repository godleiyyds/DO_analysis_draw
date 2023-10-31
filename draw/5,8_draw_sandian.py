import matplotlib.pyplot as plt
import numpy as np
import os
import draw.draw as draw
import global_config.config as gc
import pandas as pd

stations=gc.experiment_stations

models = ['mod',
        'attention_lyr1_8','attention_val_E32_lyr16_8'
    ]

# models.append('/mod')
model_group = 'attention_group_swish'
model_groups=gc.module_group




mo_dict = {'attention_group_swish/attention_lyr1_8':'智能模型6',
               'attention_group_swish/attention_val_E32_lyr16':'智能模型1',
    'attention_group_swish/attention_val_E32_lyr16_8':'智能模型2',
    'attention_group_swish/attention_val_E64_lyr32':'智能模型3',
    'attention_group_swish/attention_val_E64_lyr32_16':'智能模型4',
    'attention_group_swish/attention_val_E64_lyr32_16_8':'智能模型5',
    'attention_group_swish/attention_val_lyr1_8':'智能模型7',

               'mod':'数值模型'
    }

file_dir= gc.analysis_directory + '/'  + gc.datasets_name

file=file_dir + '/' + model_group + '/preds_label.xlsx'

stations=[ '北礵',  '同心湾2号','姥屿','榕海Ⅳ号','港南','湄洲岛', '筶杯岛', '闽江口1号', '鸟屿']

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


i=0

for station in stations:
    df = pd.read_excel(file, sheet_name=station, engine='openpyxl')
    obs = df["观察值"]

    fig = plt.figure(figsize=(48, 48), dpi=300)

    ty=0.1

    model_name = 'mod'

    i=0

    for model in models:

        fig, ax = plt.subplots()

        if model != 'mod':
            model_name = model_group + '/' + model


        pred = df[model_name]

        ax.scatter(obs, pred,label=mo_dict[model_name])

        ax.plot(obs, obs, "k--")
        z = np.polyfit(obs, pred, 1)
        p = np.poly1d(z)
        ax.plot(obs, p(obs), "r-")

        slope = z[0]

        ax.text(0.7, ty, f"{mo_dict[model_name]}_Slope: %.2f" % slope, transform=ax.transAxes)
        # ty=ty+0.1

        ax.legend(fontsize=12)
        ax.set_ylabel("预测值(mg/L)", fontsize=15)
        ax.set_xlabel("观测值(mg/L)", fontsize=15)
        xmin=ymin=0
        xmax=ymax=15
        ax.axis([xmin, xmax, ymin, ymax])

        i=i+1

        fig.suptitle(f"{station}:{mo_dict[model_name]}", fontsize=15)

        save_dir = "picture/sandian5/" + station + '/'

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # # 保存为矢量图 (SVG格式)
        plt.savefig(save_dir + f'{model}.png',format='png', bbox_inches="tight", dpi=300)


        # 显示图形
        # plt.show()
        plt.close()
        print(save_dir + ".svg___saved!")