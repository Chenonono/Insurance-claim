import db
from datetime import datetime
from xlrd2 import xldate_as_tuple


# 提交需要分类的客户特征
def sub_review_data(feature, prob, label):
    flag = 0
    for i in range(len(feature['CL_NO'])):
        sql = 'INSERT INTO review_data (CL_NO,NAME,INCUR_DATE_FROM,INCUR_DATE_TO,SUB_AMT,CL_SOCIAL_PAY_AMT' \
              ',CL_THIRD_PARTY_PAY_AMT,CL_OWNER_PAY_AMT,CL_SELF_CAT_PAY_AMT,COPAY_PCT,TOTAL_RECEIPT_AMT,BEN_TYPE' \
              ',MBR_TYPE,BEN_HEAD,DIAG_CODE,ORG_PRES_AMT_VALUE,PROV_CODE,RCV_DATE,MBR_NO,PROV_LEVEL,KIND_CODE,NO_OF_YR' \
              ',CODES,Probability,Forecast_Status) VALUES (' \
              + str(int(feature['CL_NO'][i])) + ', "' + feature['NAME'][i] + '","' \
              + datetime(*xldate_as_tuple(feature['INCUR_DATE_FROM'][i], 0)).strftime('%Y/%m/%d') + '","' \
              + datetime(*xldate_as_tuple(feature['INCUR_DATE_TO'][i], 0)).strftime('%Y/%m/%d') + '",' \
              + str(feature['SUB_AMT'][i]) + ','+ str(feature['CL_SOCIAL_PAY_AMT'][i]) + ','\
              + str(feature['CL_THIRD_PARTY_PAY_AMT'][i]) +','+ str(feature['CL_OWNER_PAY_AMT'][i]) +','\
              + str(feature['CL_SELF_CAT_PAY_AMT'][i]) +','+ str(feature['COPAY_PCT'][i]) +','\
              + str(feature['TOTAL_RECEIPT_AMT'][i]) +',"'+ str(feature['BEN_TYPE'][i]) +'","'\
              + str(feature['MBR_TYPE'][i]) +'","'+ str(feature['BEN_HEAD'][i]) +'","'\
              + str(feature['DIAG_CODE'][i]) +'",'+ str(feature['ORG_PRES_AMT_VALUE'][i]) +','\
              + str(int(feature['PROV_CODE'][i])) +',"'+ datetime(*xldate_as_tuple(feature['RCV_DATE'][i], 0)).strftime('%Y/%m/%d') +'",'\
              + str(int(feature['MBR_NO'][i])) +',"'+ str(feature['PROV_LEVEL'][i]) +'","'\
              + str(feature['KIND_CODE'][i]) +'",'+ str(int(feature['NO_OF_YR'][i])) +',"'\
              + str(feature['CODES'][i]) +'",'+ str(prob[i]) +','\
              + str(label[i]) + ')'
        db.insert_or_update_data(sql)
        flag = 1
    return flag


# 删除指定的未审核数据
def del_onereview(id):
    sql = 'delete from review_data where `ID`=' + str(id)
    db.insert_or_update_data(sql)
    flag = 1
    return flag


# 提交已审核的数据
def sub_onereviewed(feature, label):
    flag = 0
    sql = 'INSERT INTO reviewed_data (CL_NO,NAME,INCUR_DATE_FROM,INCUR_DATE_TO,SUB_AMT,CL_SOCIAL_PAY_AMT' \
          ',CL_THIRD_PARTY_PAY_AMT,CL_OWNER_PAY_AMT,CL_SELF_CAT_PAY_AMT,COPAY_PCT,TOTAL_RECEIPT_AMT,BEN_TYPE' \
          ',MBR_TYPE,BEN_HEAD,DIAG_CODE,ORG_PRES_AMT_VALUE,PROV_CODE,RCV_DATE,MBR_NO,PROV_LEVEL,KIND_CODE,NO_OF_YR' \
          ',CODES,CL_LINE_STATUS) VALUES (' \
          + str(int(feature['CL_NO'])) + ', "' + feature['NAME'] + '","' \
          + str(feature['INCUR_DATE_FROM']) + '","' + str(feature['INCUR_DATE_TO']) + '",' \
          + str(feature['SUB_AMT']) + ',' + str(feature['CL_SOCIAL_PAY_AMT']) + ',' \
          + str(feature['CL_THIRD_PARTY_PAY_AMT']) + ',' + str(feature['CL_OWNER_PAY_AMT']) + ',' \
          + str(feature['CL_SELF_CAT_PAY_AMT']) + ',' + str(feature['COPAY_PCT']) + ',' \
          + str(feature['TOTAL_RECEIPT_AMT']) + ',"' + str(feature['BEN_TYPE']) + '","' \
          + str(feature['MBR_TYPE']) + '","' + str(feature['BEN_HEAD']) + '","' \
          + str(feature['DIAG_CODE']) + '",' + str(feature['ORG_PRES_AMT_VALUE']) + ',' \
          + str(int(feature['PROV_CODE'])) + ',"' + str(feature['RCV_DATE']) + '",' \
          + str(int(feature['MBR_NO'])) + ',"' + str(feature['PROV_LEVEL']) + '","' \
          + str(feature['KIND_CODE']) + '",' + str(int(feature['NO_OF_YR'])) + ',"' \
          + str(feature['CODES']) + '",' + str(label) + ')'
    db.insert_or_update_data(sql)
    flag = 1
    return flag

# 删除指定的已审核数据
def del_onereviewed(id):
    sql = 'delete from reviewed_data where `ID`=' + str(id)
    db.insert_or_update_data(sql)
    flag = 1
    return flag
