import db
from datetime import datetime
from xlrd2 import xldate_as_tuple

def sub_review_data(feature):
    flag = 0
    for i in range(len(feature['编号'])):
        sql = 'INSERT INTO review_data (编号,性别,疾病,理赔金额,理赔时间,截止日期) VALUES (' + str(int(feature['编号'][i])) \
              + ', "' + feature['性别'][i] + '","' + feature['疾病'][i] + '",' + str(feature['理赔金额'][i]) + ',"' \
              + datetime(*xldate_as_tuple(feature['理赔时间'][i], 0)).strftime('%Y/%m/%d') + '","' \
              + datetime(*xldate_as_tuple(feature['截止日期'][i], 0)).strftime('%Y/%m/%d') + '")'
        db.insert_or_update_data(sql)
        flag = 1
    return flag