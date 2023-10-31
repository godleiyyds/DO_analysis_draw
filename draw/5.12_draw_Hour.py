import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
import global_config.config as gc


stations=gc.experiment_stations

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 15

models = ['attention_group_swish/attention_val_E32_lyr16_8',
         'attention_group_swish/attention_lyr1_8', '/mod']

mo_dict = {'attention_group_swish/attention_lyr1_8':'智能模型6',
               'attention_group_swish/attention_val_E32_lyr16':'智能模型1',
    'attention_group_swish/attention_val_E32_lyr16_8':'智能模型2',
    'attention_group_swish/attention_val_E64_lyr32':'智能模型3',
    'attention_group_swish/attention_val_E64_lyr32_16':'智能模型4',
    'attention_group_swish/attention_val_E64_lyr32_16_8':'智能模型5',
    'attention_group_swish/attention_val_lyr1_8':'智能模型7',

               '/mod':'数值模型'
    }
mod_label=[]
for model in models:
    mod_label.append(mo_dict[model])


fig = plt.figure(figsize=(48, 20), dpi=300)

errors = ['rmse','mae']
dir = 'analysis/only_obs_tm/'
for error in errors:

    for station in stations:
        station=station['station']

        fig, ax = plt.subplots()

    ################################################################################3
        df = pd.read_excel(dir+'timeslice-' + error + '.xlsx',
                             index_col=0,sheet_name=station)[
            ['attention_group_swish/attention_val_E32_lyr16_8',
             'attention_group_swish/attention_lyr1_8', '/mod']]

        for model in models:

            y = df[model]
            x = [i for i in range(24)]

            ax.plot(x, y)
            plt.xticks(range(24), x)
            plt.yticks(fontsize=24)
            plt.ylim(0, 2)

            ax.set_xlabel("Hour")
            ax.set_ylabel(f'{error.upper()}(mg/L)')

        ####################################3
        ax.set_title(station)

        ax.legend(loc='upper right', labels=mod_label)

        # plt.show()
        err_dir= f'picture/Hour_err/{error}/'
        if not os.path.exists(err_dir):
            os.makedirs(err_dir)
        ###########################################
        plt.savefig(err_dir + station+'.png', format='png', bbox_inches="tight", dpi=300)

        plt.close()

        print(err_dir + station+'.png___saved!')

