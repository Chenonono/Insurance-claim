import pandas as pd
import numpy as np
from datetime import datetime
from xlrd2 import xldate_as_tuple
from sklearn.preprocessing import LabelEncoder
import joblib

def Characteristics(feature):
    for i in range(len(feature['CL_NO'])):
        feature['INCUR_DATE_FROM'][i] = datetime(*xldate_as_tuple(feature['INCUR_DATE_FROM'][i], 0)).strftime('%Y/%m/%d')
        feature['INCUR_DATE_TO'][i] = datetime(*xldate_as_tuple(feature['INCUR_DATE_TO'][i], 0)).strftime('%Y/%m/%d')
        feature['RCV_DATE'][i] = datetime(*xldate_as_tuple(feature['RCV_DATE'][i], 0)).strftime('%Y/%m/%d')
        feature['PROV_CODE'][i] = int(feature['PROV_CODE'][i])
        feature['MBR_NO'][i] = int(feature['MBR_NO'][i])
    data = pd.DataFrame(feature)
    newdata=data
    code_list = ['M028', 'M110', 'M116', 'M130', 'M133', 'P1', 'P10', 'P11', 'P12', 'P15', 'P16', 'P17', 'P18', 'P19', 'P2', 'P20',
                'P3', 'P4', 'P5','P8', 'P9', 'R060', 'R100', 'R140', 'R170', 'R520', 'R530', 'R540','R560', 'R600', 'R605', 'R610',
                'R658', 'R898', 'R899', 'T180', 'W040', 'W050', 'W055', 'W070','W080', 'W100', 'W105', 'W180', 'W210', 'W220', 'W230',
                'W250', 'W260', 'W270',  'W420', 'W450', 'W560', 'W600', 'W620']
    l = 0
    labs = []
    for j in range(len(code_list)):
        lab = []
        for i in newdata['CODES']:
            l = 0
            item = str(i).replace(", "," ").split(" ")
            for k in item:
                if code_list[j] == k:
                    l = 1
            lab.append(l)
        labs.append(lab)
    for j in range(len(code_list)):
        data[code_list[j]]=labs[j]
    data2=data.drop(labels=['CL_NO','NAME','CODES'], axis=1)
    #日期处理
    timedata=data2
    timedata1 = pd.to_datetime(timedata['INCUR_DATE_FROM'])
    timedata2 = pd.to_datetime(timedata['INCUR_DATE_TO'])
    timedata['时间差'] = timedata2 - timedata1
    timedata['时间差'] = pd.to_timedelta(timedata['时间差'])
    timedata['time interval'] = timedata['时间差'].dt.total_seconds()
    timedata['time interval']
    data2['INCUR_DATE_FROM']=timedata1
    data2['INCUR_DATE_TO']=timedata2
    data2['time interval']=timedata['time interval']
    data2=data2.drop('时间差',axis=1)
    y = data2['INCUR_DATE_FROM']
    le = LabelEncoder()
    le = le.fit(y)
    label = le.transform(y)
    data2['INCUR_DATE_FROM'] = label
    y1 = data2['INCUR_DATE_TO']
    le = LabelEncoder()
    le = le.fit(y1)
    label1 = le.transform(y1)
    data2['INCUR_DATE_TO'] = label1
    data2['INCUR_DATE_FROM']
    RCV_DATE=pd.to_datetime(data2['RCV_DATE'],format='%Y-%m-%d %H:%M:%S' )
    t=RCV_DATE-timedata1
    data2['RCV_DATE']=t
    #福利类型处理
    be = data2.loc[:,"BEN_TYPE"]
    be_u = be.unique()
    bs = []
    for j in be:
        for i in range(len(be_u)):
            if be_u[i] == j:
                bs.append(i)
    copy = data2
    data2["BEN_TYPE"] = bs
    #被保险人类型
    mem = data2.loc[:,"MBR_TYPE"]
    mem_u = mem.unique()
    ms = []
    for j in mem:
        for i in range(len(mem_u)):
            if mem_u[i] == j:
                ms.append(i)
    data2["MBR_TYPE"] = ms
    #福利项目
    bed = data2.loc[:,"BEN_HEAD"]
    bed_u = bed.unique()
    beds = []
    for j in bed:
        for i in range(len(bed_u)):
            if bed_u[i] == j:
                beds.append(i)
    data2["BEN_HEAD"] = beds
    #医院水平
    lel = data2.loc[:,"PROV_LEVEL"]
    lel = lel.fillna(str(-1))
    lel_u = lel.unique()
    lels = []
    for j in lel:
        for i in range(len(lel_u)):
            if lel_u[i] == j:
                lels.append(i)
    data2["PROV_LEVEL"] = lels
    #疾病代码
    dia = data2.loc[:,"DIAG_CODE"]
    dia = dia.astype(str)
    dia_u = dia.unique()
    ds = []
    for i in dia:
        s = [k for k in i]
        for j in range(len(s)):
            if s[j] >= 'A':
                num = ord(i[j])-ord('A')
                s[j] = str(num)
            if s[j]== '+':
                s[j] = " "
            Str = "".join(s)
        ds.append(Str)
    data2["DIAG_CODE"] = ds
    #险种代码
    kind = data2.loc[:,"KIND_CODE"]
    kind = kind.fillna(-1).astype(str)
    kind_u = kind.unique()
    AC_high = ['0','7100012','7100014','7102001','高层配偶','高层员工','配偶','员工配偶','员工子女','子女','普通员工'] #90
    AC_low60 = ['761','765','大病'] #60
    AC_all = ['-1','762','6100016','70P','员工','高级员工','高管'] #80
    RJ_high80 = ['763'] #10
    RJ_high60 = ['764'] #40
    ks = []
    n = 0
    for j in kind:
        f = 0
        for i in range(len(AC_high)):
            if AC_high[i] == j:
                ks.append(90)
                f = 1
                break
        for i in range(len(AC_low60)):
            if AC_low60[i] == j:
                ks.append(60)
                f = 1
                break
        for i in range(len(AC_all)):
            if AC_all[i] == j:
                ks.append(80)
                f = 1
                break
        for i in range(len(RJ_high80)):
            if RJ_high80[i] == j:
                ks.append(10)
                f = 1
                break
        for i in range(len(RJ_high60)):
            if RJ_high60[i] == j:
                ks.append(40)
                f = 1
                break
        n = n+1
    data2["KIND_CODE"] = ks
    data2["RCV_DATE"]=data2["RCV_DATE"].astype(str)
    ttt=np.array(data2["RCV_DATE"])
    ddd=[]
    for i in range(ttt.shape[0]):
        a=[]
        a=ttt[i].split(" ")
        ddd.append(float(a[0]))
    data2["RCV_DATE"]=ddd
    ds = []
    for i in ddd:
        if i == -1:
            i = 0
        if i >= -365 and i < -1:
            i = i +365
        if i < -365 :
            i = i +730
        ds.append(i)
    data2["RCV_DATE"] = ds
    return data2

def predict(feature):
    prob = []
    clf = joblib.load('D:\Learn\python\workspace-Pycharm\web\static\model\pre_model.pkl')
    label = clf.predict(feature)
    all_prob = clf.predict_proba(feature)
    for i in range(len(label)):
        if not label[i]:
            prob.append(all_prob[i][0])
        elif label[i]:
            prob.append(all_prob[i][1])
    return prob, label