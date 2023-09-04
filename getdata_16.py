import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from threading import Thread
import os
from datetime import date
import schedule

center_num = 16
df = pd.read_csv('/data/center_'+str(center_num)+'_pair.csv')
df = df.iloc[:,1:]

"""重新定义带返回值的线程类"""
class MyThread(Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
#https://blog.csdn.net/qq_37174526/article/details/92414970

def csv_path():
    today = date.today()
    today = str(today)
    path = '/root/bingliu/baidumap/data/v/center_'+str(center_num)+'/'+str(today)+'/'
    if not os.path.exists(path):
        os.makedirs(path)
    return today


def get_dis_tm(q):
    time.sleep(0.5)
    url = 'http://map.baidu.com/?newmap=1&da_par=direct&pcevaname=pc4.1&qt=nav&sn=1$$$$'+str(q)+'$$$$$$&version=4&route_traffic=1&da_src=shareurl&extinfo=63&tn=B_NORMAL_MAP&nn=0&auth=&seckey=&ie=utf-8&newfrom=zhuzhan_webmap'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    s = str(soup)
    if 'distance' in s:
        dis_list = []
        tm_list = []
        for i in range(1,len(s.split('routes')[1].split('desc'))):
            si = s.split('routes')[1].split('desc')[i]
            dis = si.split('distance":')[1].split(',')[0]
            tm = si.split('distance":')[1].split(',')[1].split('":')[1]
            dis_list.append(dis)
            tm_list.append(tm)
        min_index = tm_list.index(min(tm_list))
        dis = dis_list[min_index]
        tm = tm_list[min_index]
        dis = int(dis)/1000
        tm = int(tm)/60
    else:
        dis = 0
        tm = 0
    return dis,tm



def get_hotresearch():
    date = csv_path()
    t_list = []
    res1_list = []
    for i in range(df.shape[0]):
        start_x = df.loc[i,'from_px']
        start_y = df.loc[i,'from_py']
        destination_x = df.loc[i,'to_px']
        destination_y = df.loc[i,'to_py']
        q = str(start_x)+','+str(start_y)+'$$0$$$$&en=1$$$$'+str(destination_x)+','+str(destination_y)
        t = MyThread(get_dis_tm, args=(q,))
        t_list.append(t)
        t.start()
        
    for t in t_list:
        t.join()
        res1 = t.get_result()
        res1_list.append(res1)

    for i in range(df.shape[0]):
        res1 = res1_list[i]
        print(res1)
        df.loc[i,'distance/km'] = res1[0]
        df.loc[i,'time/min'] = res1[1]
        time_catch = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        df.loc[i,'catchtime'] = time_catch
    time_catch = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    df.to_csv('data/v/center_'+str(center_num)+'/'+str(date)+'/'+str(time_catch)+'.csv')

# 定时运行
# 每隔半个小时运行一次

schedule.every().day.at("00:00").do(get_hotresearch)
schedule.every().day.at("00:30").do(get_hotresearch)
schedule.every().day.at("01:00").do(get_hotresearch)
schedule.every().day.at("01:30").do(get_hotresearch)
schedule.every().day.at("02:00").do(get_hotresearch)
schedule.every().day.at("02:30").do(get_hotresearch)
schedule.every().day.at("03:00").do(get_hotresearch)
schedule.every().day.at("03:30").do(get_hotresearch)
schedule.every().day.at("04:00").do(get_hotresearch)
schedule.every().day.at("04:30").do(get_hotresearch)
schedule.every().day.at("05:00").do(get_hotresearch)
schedule.every().day.at("05:30").do(get_hotresearch)
schedule.every().day.at("06:00").do(get_hotresearch)
schedule.every().day.at("06:30").do(get_hotresearch)
schedule.every().day.at("07:00").do(get_hotresearch)
schedule.every().day.at("07:30").do(get_hotresearch)
schedule.every().day.at("08:00").do(get_hotresearch)
schedule.every().day.at("08:30").do(get_hotresearch)
schedule.every().day.at("09:00").do(get_hotresearch)
schedule.every().day.at("09:30").do(get_hotresearch)
schedule.every().day.at("10:00").do(get_hotresearch)
schedule.every().day.at("10:30").do(get_hotresearch)
schedule.every().day.at("11:00").do(get_hotresearch)
schedule.every().day.at("11:30").do(get_hotresearch)
schedule.every().day.at("12:00").do(get_hotresearch)
schedule.every().day.at("12:30").do(get_hotresearch)
schedule.every().day.at("13:00").do(get_hotresearch)
schedule.every().day.at("13:30").do(get_hotresearch)
schedule.every().day.at("14:00").do(get_hotresearch)
schedule.every().day.at("14:30").do(get_hotresearch)
schedule.every().day.at("15:00").do(get_hotresearch)
schedule.every().day.at("15:30").do(get_hotresearch)
schedule.every().day.at("16:00").do(get_hotresearch)
schedule.every().day.at("16:30").do(get_hotresearch)
schedule.every().day.at("17:00").do(get_hotresearch)
schedule.every().day.at("17:30").do(get_hotresearch)
schedule.every().day.at("18:00").do(get_hotresearch)
schedule.every().day.at("18:30").do(get_hotresearch)
schedule.every().day.at("19:00").do(get_hotresearch)
schedule.every().day.at("19:30").do(get_hotresearch)
schedule.every().day.at("20:00").do(get_hotresearch)
schedule.every().day.at("20:30").do(get_hotresearch)
schedule.every().day.at("21:00").do(get_hotresearch)
schedule.every().day.at("21:30").do(get_hotresearch)
schedule.every().day.at("22:00").do(get_hotresearch)
schedule.every().day.at("22:30").do(get_hotresearch)
schedule.every().day.at("23:00").do(get_hotresearch)
schedule.every().day.at("23:30").do(get_hotresearch)

while True:
    schedule.run_pending()  # run_pending：运行所有可以运行的任务