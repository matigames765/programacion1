def home(buy_list):
    home_list = []
    for i in buy_list:
        if (i[3] not in home_list):
            home_list.append(i[3])
        else:
            pass
    return home_list