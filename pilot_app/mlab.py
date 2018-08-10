import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds215502.mlab.com:15502/muadongkhonglanh
# mongodb://admin:adminc4e19@ds215502.mlab.com:15502/muadongkhonglanh
# mongodb://order:adminc4e19@ds215502.mlab.com:15502/muadongkhonglanh

host = "ds215502.mlab.com"
port = 15502
db_name = "muadongkhonglanh"
user_name = "admin0"
password = "adminc4e19"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())