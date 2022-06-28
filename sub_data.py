import db

def steel_slab_data_add(request):
    values = []
    flag = 0
    for it in request.form.items():
        if it[1] == '':
            flag = 1
            break
        else:
            values.append(it[1])

    if flag == 0:
        sql = 'INSERT INTO steel_slab_train (ws_mm,cs_mm,fs_mm,mn_mm,cl_sm,out_te,s_el,sn_qm,ud_qm,ni_qm,oe_qm,po_qm,c_qm,si_qm,L) VALUES (' + \
              values[0] + ', ' + values[1] + ', ' + values[2] + ', ' + values[3] + ', ' + values[4] + ', ' + values[
                  5] + ', ' + values[6] + ', ' + values[7] + ', ' + values[8] + ', ' + values[9] + ', ' + values[
                  10] + ', ' + values[11] + ', ' + values[12] + ', ' + values[13] + ', ' + values[14] + ')'
        db.insert_or_update_data(sql)

    return flag

def steel_slab_data_pre(request):
    values = []
    flag = 0
    for it in request.form.items():
        if it[1] == '':
            flag = 1
            break
        else:
            values.append(it[1])

    if flag == 0:
        L = str(1)
        values.append(L)

        sql = 'INSERT INTO steel_slab_test (ws_mm,cs_mm,fs_mm,mn_mm,cl_sm,out_te,s_el,sn_qm,ud_qm,ni_qm,oe_qm,po_qm,c_qm,si_qm,L) VALUES (' + \
              values[0] + ', ' + values[1] + ', ' + values[2] + ', ' + values[3] + ', ' + values[4] + ', ' + values[
                  5] + ', ' + values[6] + ', ' + values[7] + ', ' + values[8] + ', ' + values[9] + ', ' + values[
                  10] + ', ' + values[11] + ', ' + values[12] + ', ' + values[13] + ', ' + values[14] + ')'
        db.insert_or_update_data(sql)

    return flag

def rolled_steel_data_add(request):
    values = []
    flag = 0
    for it in request.form.items():
        if it[1] == '':
            flag = 1
            break
        else:
            values.append(it[1])

    if flag == 0:
        sql = 'INSERT INTO rolled_steel_train (x31, x32, x33, x34, x35, x36, Rc) VALUES (' + values[0] + ', ' + values[
            1] + ', ' + values[2] + ', ' + values[3] + ', ' + values[4] + ', ' + values[5] + ', ' + values[6] + ')'
        db.insert_or_update_data(sql)

    return flag

def rolled_steel_data_pre(request):
    values = []
    flag = 0
    for it in request.form.items():
        if it[1] == '':
            flag = 1
            break
        else:
            values.append(it[1])

    if flag == 0:
        Rc = str(1)
        values.append(Rc)

        sql = 'INSERT INTO rolled_steel_test (x31, x32, x33, x34, x35, x36, Rc) VALUES (' + values[0] + ', ' + values[
            1] + ', ' + values[2] + ', ' + values[3] + ', ' + values[4] + ', ' + values[5] + ', ' + values[6] + ')'
        db.insert_or_update_data(sql)

    return flag