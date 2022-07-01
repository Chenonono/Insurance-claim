import db


# 实现登录验证
def login_verify(user, pwd):
    sql = 'SELECT * FROM `user_login` WHERE `user`=' + str(user) + ' AND `pwd`=' + str(pwd) + ';'
    flag = db.query_data(sql)
    return flag


# 实现管理员验证
def admin_verify(user):
    sql = 'SELECT `admin` FROM `user_login` WHERE `user`=' + str(user) + ';'
    flag = db.query_data(sql)[0]['admin']
    return flag


# 获取所有未审核数据
def show_review():
    sql = 'SELECT * FROM `review_data`;'
    data = db.query_data(sql)
    return data


# 获取未审核的单项数据
def get_onereview(id):
    sql = 'SELECT * FROM `review_data` WHERE `ID`=' + str(id) + ';'
    data = db.query_data(sql)
    return data


# 获取所有已审核数据
def show_reviewed():
    sql = 'SELECT * FROM `reviewed_data`;'
    data = db.query_data(sql)
    return data


# 获取所有预测的数据
def show_result():
    sql = 'SELECT * FROM `review_data`;'
    sql = 'SELECT `ID`,`CL_NO`,`Forecast_Status`,`Probability` FROM `review_data`;'
    data = db.query_data(sql)
    return data
