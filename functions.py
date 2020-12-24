
#for months in Russ
def month_rus(month):
    if month == 'October':
        return 'Октябрь'
    elif month == 'November':
        return 'Ноябрь'
    elif month == 'December':
        return 'Декабрь'
    elif month == 'January':
        return 'Январь'
    elif month == 'February':
        return 'Февраль'
    elif month == 'March':
        return 'Март'
    elif month == 'April':
        return 'Апрель'
    elif month == 'May':
        return 'Май'
    elif month == 'June':
        return 'Июнь'
    elif month == 'July':
        return 'Июль'
    elif month == 'August':
        return 'Август'
    elif month == 'September':
        return 'Сентябрь'


#for making previous month first day
def prev_month_init(chislo):
    x = chislo.month
    date_init = f"2020-{x}-01"
    return date_init


#for making previous month end day
def prev_month_end(chislo):
    x = chislo.month
    date_end = f"2020-{x + 1}-01"
    return date_end


#for id to names
def id_to_name(id):
    if id == 1179243319:
        name = 'Армат'
    elif id == 616105665:
        name = 'Асл'
    elif id == 444933814:
        name = 'Темик'
    elif id == 1095875260:
        name = 'Арман 2'
    elif id == 629229115:
        name = 'Арман 1'
    elif id == 1136054481:
        name = 'Айбек'
    elif id == 1472282689:
        name = 'Адиль'
    elif id == 1309473859:
        name = 'Темирбек'

    return name
