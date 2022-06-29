import db

#实现登录验证
def login_verify(user, pwd):
    sql = 'SELECT * FROM `user_login` WHERE `工号`='+str(user)+' AND `密码`='+str(pwd)+';'
    data = db.query_data(sql)
    if len(data):
        flag = 1
    else:
        flag = 0
    return flag

#实现登录验证
def show_review():
    sql = 'SELECT * FROM `review_data`;'
    data = db.query_data(sql)
    return data