# coding = utf-8
# 张依
from app.get_stations import *


def query(date, from_station, to_station, type_stu):
    data = []
    type_data = []
    data.clear()
    type_data.clear()
    cookie = '''JSESSIONID=19244E64B10E57EFB354E317CC0DD2C5; BIGipServerotn=535822858.50210.0000; RAIL_EXPIRATION=1582333451491; RAIL_DEVICEID=McIuEPF2UftrVKz1eNePew8hyOmYixP1IVU1JOTtULuRy2igIY3K71OCqb2YQni1FEkLyWbxf508zd6v91pHbnHRZ2UU0SLJBBsbittDazpLO-ZB7zoirqGyH9ao0cAv_d76BNGKrAVsosQuv0EkQuOczvUHWMcx; BIGipServerpool_passport=317522442.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_fromDate=2020-02-19; _jc_save_toDate=2020-02-19'''
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Connection': 'keep-alive',
        'accept': '*/*',
        'Cookie': cookie}
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes={}' \
        .format(date, from_station, to_station, type_stu)
    # url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-10-13&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT"
    response = requests.get(url, headers=header)
    result = response.json()
    print(result)
    result = result['data']['result']
    if isStations() == True:
        station = eval(read())
        print(station)
        if len(result) != 0:
            for i in result:
                tmp_list = i.split('|')
                from_station = station[tmp_list[6]]
                to_station = station[tmp_list[7]]
                seat = [tmp_list[3], from_station, to_station, tmp_list[8],
                        tmp_list[9], tmp_list[10], tmp_list[32], tmp_list[31],
                        tmp_list[30], tmp_list[21], tmp_list[23], tmp_list[33],
                        tmp_list[28], tmp_list[24], tmp_list[29], tmp_list[26]]
                newSeat = []
                for s in seat:
                    if s == "":
                        s = "--"
                    else:
                        s = s
                    newSeat.append(s)
                data.append(newSeat)
        print(data)
        return data

# if __name__ == '__main__':
#     query("2020-10-13", "BJP", "SHH", "0X00")
