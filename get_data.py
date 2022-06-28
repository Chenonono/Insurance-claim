import numpy as np
import db

def get_rolled(sql):
    sql = sql
    datas = db.query_data(sql)

    datas_list = []
    for i in range(len(datas)):
        data_list = []
        for it in datas[i].items():
            data_list.append(it[1])
        datas_list.append(data_list)

    datas_array = np.array(datas_list)

    temp = datas_array[:, 1].copy()
    datas_array[:, 1] = datas_array[:, 7]
    datas_array[:, 7] = temp

    rolled_datas = datas_array.tolist()
    for i in range(len(rolled_datas)):
        rolled_datas[i][0] = int(rolled_datas[i][0])

    return rolled_datas

def get_steel(sql):
    sql = sql
    datas = db.query_data(sql)

    datas_list = []
    for i in range(len(datas)):
        data_list = []
        for it in datas[i].items():
            data_list.append(it[1])
        datas_list.append(data_list)

    datas_array = np.array(datas_list)

    temp = datas_array[:, 1].copy()
    datas_array[:, 1] = datas_array[:, 15]
    datas_array[:, 15] = temp

    steel_datas = datas_array.tolist()
    for i in range(len(steel_datas)):
        steel_datas[i][0] = int(steel_datas[i][0])

    return steel_datas