# coding = utf-8
import re
import requests
import os


def getStion():
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9161"
    response = requests.get(url, verify=True)
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    stations = dict((stations))
    # stations = str(stations)
    new_stations = {}
    new_stations2 = {}
    for i, j in stations.items():
        new_stations[j] = i
        new_stations2[i] = j
    write(str(new_stations))
    write2(str(new_stations2))


def write(stations):
    with open('../stations.txt', 'w', encoding='utf-8') as fp:
        fp.write(stations)
        fp.close()


def write2(stations):
    with open('../stations2.txt', 'w', encoding='utf-8') as fp:
        fp.write(stations)
        fp.close()


def read():
    with open('../stations.txt', 'r', encoding='utf-8') as fp:
        data = fp.readline()
        fp.close()
        return data


def read2():
    with open('../stations2.txt', 'r', encoding='utf-8') as fp:
        data = fp.readline()
        fp.close()
        return data


def isStations():
    isStation = os.path.exists('../stations.txt')
    return isStation


def isStations2():
    isStation = os.path.exists('../stations2.txt')
    return isStation


if __name__ == '__main__':
    getStion()
