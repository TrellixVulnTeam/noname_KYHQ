from connection import *
import datetime
from dateutil.relativedelta import relativedelta
from functions import *
from datetime import date
from dateutil.relativedelta import relativedelta

a = date.today()

curr_date_init = f"2020-{a.month}-01"


###########################
def curr_trans_all_by_name_date(name):
    n_tag = ZenObject.to_dict(diff.tag)
    id_tag = 0

    for item in n_tag:
        if item['title'] == 'Аванс ' + name:
            id_tag = item['id']

    n_tran = ZenObject.to_dict(diff.transaction)
    n_tran = sorted(n_tran, key=lambda k: k['date'])

    dates = []
    money = []
    comments = []

    for item in n_tran:
        if item['tag'] == [id_tag] and item['deleted'] == False and curr_date_init <= item['date']:
            info = datetime.datetime.strptime(item['date'], "%Y-%m-%d")
            x = datetime.datetime.strftime(info + relativedelta(days=-1), "%Y-%m-%d")
            dates.append(x)
            money.append("{:,} тенге".format(item['outcome']))
            if item['comment'] == None:
                comments.append("")
            else:
                comments.append(item['comment'])

    all = []
    for i in range(0, len(dates)):
        all.append(f"{dates[i]} - {money[i]} - {comments[i]}")

    return '\n'.join(all)


def curr_avans_by_name(name):
    n_tag = ZenObject.to_dict(diff.tag)
    id_tag = 0

    for item in n_tag:
        if item['title'] == 'Аванс ' + name:
            id_tag = item['id']

    n_tran = ZenObject.to_dict(diff.transaction)
    n_tran = sorted(n_tran, key=lambda k: k['date'])

    avans = 0

    for item in n_tran:
        if item['tag'] == [id_tag] and item['deleted'] == False and curr_date_init <= item['date']:
            avans += item['outcome']

    return "{:,} тенге".format(avans)
