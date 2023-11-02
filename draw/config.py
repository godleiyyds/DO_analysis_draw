
import argparse
import os

def get_config():

    ##水温、盐度：东山湾, 同心湾2号, 姥屿, 嵛山, 湄洲, 闽江口1号
    # default_stations = [
    #     {'station': '姥屿', 'split_dt': '2021-11-18 00:00:00'},
    #     {'station': '闽江口1号', 'split_dt': '2021-04-07 00:00:00'},
    #     # {'station': '湄洲', 'split_dt': '2021-04-07 00:00:00'},
    #     {'station': '同心湾2号', 'split_dt': '2021-10-04 00:00:00'},
    #
    # ]

    ##气温、气压
    default_stations = [
        {'station': '北礵', 'split_dt': '2020-04-01 00:00:00'},
        # {'station': '姥屿', 'split_dt': '2021-12-01 00:00:00'},
        # {'station': '筶杯岛', 'split_dt': '2021-10-01 00:00:00'},
        # {'station': '港南', 'split_dt': '2021-10-01 00:00:00'},
        # {'station': '闽江口1号', 'split_dt': '2021-07-01 00:00:00'},
        # {'station': '榕海Ⅳ号', 'split_dt': '2021-03-01 00:00:00'},
        # {'station': '鸟屿', 'split_dt': '2021-04-01 00:00:00'},

        # {'station': '湄洲岛', 'split_dt': '2021-04-01 00:00:00'},
        # {'station': '同心湾2号', 'split_dt': '2021-10-01 00:00:00'},

        ]
    parser = argparse.ArgumentParser(description='[Model] DO Forecasting')
    #######################

    parser.add_argument('--module_group', nargs='+',  default=['m_attention_p_group'], help='module_group')
    parser.add_argument('--training_model', nargs='+', default=['Attention_do_chl_qw_qy'], help='model of the experiment')

    parser.add_argument('--experiment_stations', nargs='+', default=default_stations, help='experiment_stations')

    ######################################
    parser.add_argument('--datasets_name', type=str, default='data_obs_p', help='datasets_name')
    parser.add_argument('--datasets_path', type=str, default='datasets', help='location of the data file')
    parser.add_argument('--processed_file', type=str, default='preprocess/processed_threshold_obs_mod_time_datas.xlsx', help='processed_file')

    parser.add_argument('--input_timesteps',  type=int, default=72, help='input_timesteps')
    parser.add_argument('--output_timesteps',  type=int, default=24, help='output_timesteps')
    parser.add_argument('--custom_input_timesteps', type=int, default=72, help='output_timesteps') #
    parser.add_argument('--X_OBS', nargs='+',  default=['气温', '气压','叶绿素',  '溶解氧',], help='X_OBS')#'气温', '气压', '叶绿素', '溶解氧','hour_sin', 'day_sin'
    # parser.add_argument('--X_OBS', nargs='+', default=['水温', '盐度', '溶解氧', 'hour_sin', 'day_sin'],help='X_OBS')
    parser.add_argument('--X_MOD',  nargs='+', default=[], help='X_MOD')
    # parser.add_argument('--X_MOD', nargs='+', default=['air_temp','qy','chl','ox'], help='X_MOD')
    ################

    parser.add_argument('--module_structure_path', type=str, default='models.structures', help='module_structure_path')
    parser.add_argument('--module_result_path', type=str, default='models/results', help='module_result_path')

    module_group_name_key = {
        'demo_model': 'DEMO_CLS',
        'lstm_dense_sum': 'DEMO_CLS',
        'lstm_densex2_sum': 'DEMO_CLS',
        'lstm_densex3_sum': 'DEMO_CLS',
        'lstm_densex4_sum': 'DEMO_CLS',
        'gru_dense_sum': 'DEMO_CLS',
        'gru_densex2_sum': 'DEMO_CLS',
        'gru_densex3_sum': 'DEMO_CLS',
        'gru_densex4_sum': 'DEMO_CLS',

        'attention_val_E32_lyr16': 'Attention_CLS',
        'attention_val_E32_lyr16_8': 'Attention_CLS',
        'attention_val_E64_lyr32': 'Attention_CLS',
        'attention_val_E64_lyr32_16': 'Attention_CLS',
        'attention_val_E64_lyr32_16_8': 'Attention_CLS',
        'attention_lyr1_8': 'Attention_CLS',
        'attention_val_lyr1_8': 'Attention_CLS',

        'attention_x1_E16': 'Attention_CLS',
        'attention_x1_E32': 'Attention_CLS',
        'attention_x1_E64': 'Attention_CLS',
        'attention_x2_E16': 'Attention_CLS',
        'attention_x5': 'Attention_CLS',

        'attention_lstm_x1_E16': 'Attention_CLS',
        'attention_lstm_x1_E32': 'Attention_CLS',
        'attention_lstm_x1_E64': 'Attention_CLS',
        'attention_lstm48_x1_E16': 'Attention_CLS',
        'attention_lstm12_x1_E16': 'Attention_CLS',

        'cla1': 'Attention_CLS',
        'cla2': 'Attention_CLS',
        'cla3': 'Attention_CLS',
        'cla4': 'Attention_CLS',
        'cla5': 'Attention_CLS',
        'cla6': 'Attention_CLS',
        'cla7': 'Attention_CLS',
        'cla8': 'Attention_CLS',
        'cla9': 'Attention_CLS',
        'cla10': 'Attention_CLS',
        'cla11': 'Attention_CLS',
        'cla12': 'Attention_CLS',

        'a1': 'Attention_CLS',
        'a2': 'Attention_CLS',
        'a3': 'Attention_CLS',
        'a4': 'Attention_CLS',
        'a5': 'Attention_CLS',
        'a6': 'Attention_CLS',
        'a7': 'Attention_CLS',
        'a8': 'Attention_CLS',
        'a9': 'Attention_CLS',
        'a10': 'Attention_CLS',
        'a11': 'Attention_CLS',
        'a12': 'Attention_CLS',

        'BP': 'DEMO_CLS',
        'BP2': 'DEMO_CLS',
        'BP3': 'DEMO_CLS',
        'BP4': 'DEMO_CLS',
        'BP5': 'DEMO_CLS',
        'BP0': 'DEMO_CLS',
        'BP_chl': 'DEMO_CLS',
        'BP_qy': 'DEMO_CLS',
        'BP_qw': 'DEMO_CLS',
        'BP_chl_qw': 'DEMO_CLS',
        'BP_chl_qy': 'DEMO_CLS',
        'BP_qw_qy': 'DEMO_CLS',
        'BP_do': 'DEMO_CLS',
        'BP_do_chl': 'DEMO_CLS',
        'BP_do_qy': 'DEMO_CLS',
        'BP_do_qw': 'DEMO_CLS',
        'BP_do_chl_qw': 'DEMO_CLS',
        'BP_do_chl_qy': 'DEMO_CLS',
        'BP_do_qw_qy': 'DEMO_CLS',
        'BP_chl_qw_qy': 'DEMO_CLS',
        'BP_do_chl_qw_qy': 'DEMO_CLS',

        'LSTM_chl': 'DEMO_CLS',
        'LSTM_qy': 'DEMO_CLS',
        'LSTM_qw': 'DEMO_CLS',
        'LSTM_chl_qw': 'DEMO_CLS',
        'LSTM_chl_qy': 'DEMO_CLS',
        'LSTM_qw_qy': 'DEMO_CLS',
        'LSTM_do': 'DEMO_CLS',
        'LSTM_do_chl': 'DEMO_CLS',
        'LSTM_do_qy': 'DEMO_CLS',
        'LSTM_do_qw': 'DEMO_CLS',
        'LSTM_do_chl_qw': 'DEMO_CLS',
        'LSTM_do_chl_qy': 'DEMO_CLS',
        'LSTM_do_qw_qy': 'DEMO_CLS',
        'LSTM_chl_qw_qy': 'DEMO_CLS',
        'LSTM_do_chl_qw_qy': 'DEMO_CLS',

        'GRU_chl': 'DEMO_CLS',
        'GRU_qy': 'DEMO_CLS',
        'GRU_qw': 'DEMO_CLS',
        'GRU_chl_qw': 'DEMO_CLS',
        'GRU_chl_qy': 'DEMO_CLS',
        'GRU_qw_qy': 'DEMO_CLS',
        'GRU_do': 'DEMO_CLS',
        'GRU_do_chl': 'DEMO_CLS',
        'GRU_do_qy': 'DEMO_CLS',
        'GRU_do_qw': 'DEMO_CLS',
        'GRU_do_chl_qw': 'DEMO_CLS',
        'GRU_do_chl_qy': 'DEMO_CLS',
        'GRU_do_qw_qy': 'DEMO_CLS',
        'GRU_chl_qw_qy': 'DEMO_CLS',
        'GRU_do_chl_qw_qy': 'DEMO_CLS',

        'GRU_Attention_chl': 'DEMO_CLS',
        'GRU_Attention_qy': 'DEMO_CLS',
        'GRU_Attention_qw': 'DEMO_CLS',
        'GRU_Attention_chl_qw': 'DEMO_CLS',
        'GRU_Attention_chl_qy': 'DEMO_CLS',
        'GRU_Attention_qw_qy': 'DEMO_CLS',
        'GRU_Attention_do': 'DEMO_CLS',
        'GRU_Attention_do_chl': 'DEMO_CLS',
        'GRU_Attention_do_qy': 'DEMO_CLS',
        'GRU_Attention_do_qw': 'DEMO_CLS',
        'GRU_Attention_do_chl_qw': 'DEMO_CLS',
        'GRU_Attention_do_chl_qy': 'DEMO_CLS',
        'GRU_Attention_do_qw_qy': 'DEMO_CLS',
        'GRU_Attention_chl_qw_qy': 'DEMO_CLS',
        'GRU_Attention_do_chl_qw_qy': 'DEMO_CLS',

        'Attention_chl': 'Attention_CLS',
        'Attention_qy': 'Attention_CLS',
        'Attention_qw': 'Attention_CLS',
        'Attention_chl_qw': 'Attention_CLS',
        'Attention_chl_qy': 'Attention_CLS',
        'Attention_qw_qy': 'Attention_CLS',
        'Attention_do': 'Attention_CLS',
        'Attention_do_chl': 'Attention_CLS',
        'Attention_do_qy': 'Attention_CLS',
        'Attention_do_qw': 'Attention_CLS',
        'Attention_do_chl_qw': 'Attention_CLS',
        'Attention_do_chl_qy': 'Attention_CLS',
        'Attention_do_qw_qy': 'Attention_CLS',
        'Attention_chl_qw_qy': 'Attention_CLS',
        'Attention_do_chl_qw_qy': 'Attention_CLS',

        'Attention_Attention': 'Attention_CLS',
        'BP_Attention': 'Attention_CLS',
        'GRU_Attention': 'Attention_CLS',
        'LSTM_Attention': 'Attention_CLS',

        'Attention_GRU': 'Attention_CLS',
        'BP_GRU': 'Attention_CLS',
        'GRU_GRU': 'Attention_CLS',
        'LSTM_GRU': 'Attention_CLS',

        'WaveNet': 'DEMO_CLS',

        'nbeats': 'DEMO_CLS',

        'trans':'Attention_CLS',

        'test': 'DEMO_CLS',
        'test2': 'DEMO_CLS',
        'test3': 'DEMO_CLS',
        'test4': 'Attention_CLS',
    }
    parser.add_argument('--module_group_name_key', type=str, default=module_group_name_key, help='analysis_directory')


    parser.add_argument('--analysis_directory', type=str, default='analysis', help='analysis_directory')
    parser.add_argument('--error_results_directory', type=str, default='err', help='error_results_directory')

    parser.add_argument('--used_model_group', type=str, default='m_Attention_group', help='analysis_directory')
    parser.add_argument('--used_model', type=str, default='Attention_do', help='error_results_directory')

    args = parser.parse_args()

    return args












