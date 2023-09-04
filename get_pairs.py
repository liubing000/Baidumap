# 引入库
# -*- coding: utf-8 -*-
import json
import urllib
import math
import pandas as pd


# 中心点
# 中间节点数量
center_num = 16
lng = 116.403963
lat = 39.915119


# 选择大致包含五环的四个顶点

df_4 = pd.DataFrame([])
df_4.loc[0,'lng'] = 116.403963-0.18
df_4.loc[0,'lat'] = 39.915119+0.14

df_4.loc[1,'lng'] = 116.403963+0.18
df_4.loc[1,'lat'] = 39.915119+0.14

df_4.loc[2,'lng'] = 116.403963-0.18
df_4.loc[2,'lat'] = 39.915119-0.14

df_4.loc[3,'lng'] = 116.403963+0.18
df_4.loc[3,'lat'] = 39.915119-0.14


# 得到四个顶点


# 平均分布点，找到对应的36个顶点
# 粒度
# 平面上均匀分布36个点，中心是16个点，外围25个点，这样每行需要6个点，需要5个间隔
h_lng = (df_4['lng'][3]-df_4['lng'][0])/5
h_lat = (df_4['lat'][0]-df_4['lat'][3])/5

df = pd.DataFrame([])
# 第一行
df.loc[0,'lat'] = d_4.loc[0,'lat']
df.loc[0,'lng'] = d_4.loc[0,'lng']

df.loc[1,'lat'] = d_4.loc[0,'lat']
df.loc[1,'lng'] = d_4.loc[0,'lng']+h_lng

df.loc[2,'lat'] = d_4.loc[0,'lat']
df.loc[2,'lng'] = d_4.loc[0,'lng']+2*h_lng

df.loc[3,'lat'] = d_4.loc[0,'lat']
df.loc[3,'lng'] = d_4.loc[0,'lng']+3*h_lng

df.loc[4,'lat'] = d_4.loc[0,'lat']
df.loc[4,'lng'] = d_4.loc[0,'lng']+4*h_lng

df.loc[5,'lat'] = d_4.loc[0,'lat']
df.loc[5,'lng'] = d_4.loc[0,'lng']+5*h_lng

# 第二行
df.loc[6,'lat'] = d_4.loc[0,'lat']-h_lat
df.loc[6,'lng'] = d_4.loc[0,'lng']

df.loc[7,'lat'] = df.loc[6,'lat']
df.loc[7,'lng'] = df.loc[6,'lng']+h_lng
df.loc[7,'type'] = 1


df.loc[8,'lat'] = df.loc[6,'lat']
df.loc[8,'lng'] = df.loc[6,'lng']+2*h_lng
df.loc[8,'type'] = 1

df.loc[9,'lat'] = df.loc[6,'lat']
df.loc[9,'lng'] = df.loc[6,'lng']+3*h_lng
df.loc[9,'type'] = 1

df.loc[10,'lat'] = df.loc[6,'lat']
df.loc[10,'lng'] = df.loc[6,'lng']+4*h_lng
df.loc[10,'type'] = 1

df.loc[11,'lat'] = df.loc[6,'lat']
df.loc[11,'lng'] = df.loc[6,'lng']+5*h_lng

# 第三行
df.loc[12,'lat'] = d_4.loc[0,'lat']-2*h_lat
df.loc[12,'lng'] = d_4.loc[0,'lng']

df.loc[13,'lat'] = df.loc[12,'lat']
df.loc[13,'lng'] = df.loc[12,'lng']+h_lng
df.loc[13,'type'] = 1

df.loc[14,'lat'] = df.loc[12,'lat']
df.loc[14,'lng'] = df.loc[12,'lng']+2*h_lng
df.loc[14,'type'] = 1

df.loc[15,'lat'] = df.loc[12,'lat']
df.loc[15,'lng'] = df.loc[12,'lng']+3*h_lng
df.loc[15,'type'] = 1

df.loc[16,'lat'] = df.loc[12,'lat']
df.loc[16,'lng'] = df.loc[12,'lng']+4*h_lng
df.loc[16,'type'] = 1

df.loc[17,'lat'] = df.loc[12,'lat']
df.loc[17,'lng'] = df.loc[12,'lng']+5*h_lng

# 第四行

df.loc[18,'lat'] = d_4.loc[0,'lat']-3*h_lat
df.loc[18,'lng'] = d_4.loc[0,'lng']

df.loc[19,'lat'] = df.loc[18,'lat']
df.loc[19,'lng'] = df.loc[18,'lng']+h_lng
df.loc[19,'type'] = 1

df.loc[20,'lat'] = df.loc[18,'lat']
df.loc[20,'lng'] = df.loc[18,'lng']+2*h_lng
df.loc[20,'type'] = 1

df.loc[21,'lat'] = df.loc[18,'lat']
df.loc[21,'lng'] = df.loc[18,'lng']+3*h_lng
df.loc[21,'type'] = 1

df.loc[22,'lat'] = df.loc[18,'lat']
df.loc[22,'lng'] = df.loc[18,'lng']+4*h_lng
df.loc[22,'type'] = 1

df.loc[23,'lat'] = df.loc[18,'lat']
df.loc[23,'lng'] = df.loc[18,'lng']+5*h_lng

# 第五行

df.loc[24,'lat'] = d_4.loc[0,'lat']-4*h_lat
df.loc[24,'lng'] = d_4.loc[0,'lng']


df.loc[25,'lat'] = df.loc[24,'lat']
df.loc[25,'lng'] = df.loc[24,'lng']+h_lng
df.loc[25,'type'] = 1

df.loc[26,'lat'] = df.loc[24,'lat']
df.loc[26,'lng'] = df.loc[24,'lng']+2*h_lng
df.loc[26,'type'] = 1

df.loc[27,'lat'] = df.loc[24,'lat']
df.loc[27,'lng'] = df.loc[24,'lng']+3*h_lng
df.loc[27,'type'] = 1

df.loc[28,'lat'] = df.loc[24,'lat']
df.loc[28,'lng'] = df.loc[24,'lng']+4*h_lng
df.loc[28,'type'] = 1

df.loc[29,'lat'] = df.loc[24,'lat']
df.loc[29,'lng'] = df.loc[24,'lng']+5*h_lng


# 第六行

df.loc[30,'lat'] = d_4.loc[0,'lat']-5*h_lat
df.loc[30,'lng'] = d_4.loc[0,'lng']


df.loc[31,'lat'] = df.loc[30,'lat']
df.loc[31,'lng'] = df.loc[30,'lng']+h_lng

df.loc[32,'lat'] = df.loc[30,'lat']
df.loc[32,'lng'] = df.loc[30,'lng']+2*h_lng

df.loc[33,'lat'] = df.loc[30,'lat']
df.loc[33,'lng'] = df.loc[30,'lng']+3*h_lng

df.loc[34,'lat'] = df.loc[30,'lat']
df.loc[34,'lng'] = df.loc[30,'lng']+4*h_lng


df.loc[35,'lat'] = df.loc[30,'lat']
df.loc[35,'lng'] = df.loc[30,'lng']+5*h_lng

df = df.fillna(0)
df = df.iloc[:,[1,0,2]]
# df是36个格点的数据




# 准备转换坐标
# 从百度地图的经纬度转换为墨卡托坐标x，y
# 用于快速抓取数据

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = math.pi  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方

def gcj02_to_bd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]


def bd09_to_gcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]


def wgs84_to_gcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)


def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)


def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


import numpy as np
MCBAND = (12890594.86, 8362377.87, 5591021, 3481989.83, 1678043.12, 0)
MC2LL = ([1.410526172116255e-8, 0.00000898305509648872, -1.9939833816331,
          200.9824383106796, -187.2403703815547, 91.6087516669843, - 23.38765649603339,
          2.57121317296198, -0.03801003308653, 17337981.2],
         [-7.435856389565537e-9, 0.000008983055097726239, -0.78625201886289,
          96.32687599759846, -1.85204757529826, -59.36935905485877, 47.40033549296737,
          -16.50741931063887, 2.28786674699375, 10260144.86],
         [-3.030883460898826e-8, 0.00000898305509983578, 0.30071316287616,
          59.74293618442277, 7.357984074871, -25.38371002664745, 13.45380521110908,
          -3.29883767235584, 0.32710905363475, 6856817.37],
         [-1.981981304930552e-8, 0.000008983055099779535, 0.03278182852591, 40.31678527705744,
          0.65659298677277, -4.44255534477492, 0.85341911805263, 0.12923347998204,
          -0.04625736007561, 4482777.06],
         [3.09191371068437e-9, 0.000008983055096812155, 0.00006995724062, 23.10934304144901,
          -0.00023663490511, -0.6321817810242, -0.00663494467273, 0.03430082397953,
          -0.00466043876332, 2555164.4],
         [2.890871144776878e-9, 0.000008983055095805407, -3.068298e-8, 7.47137025468032,
          -0.00000353937994, -0.02145144861037, -0.00001234426596, 0.00010322952773,
          -0.00000323890364, 826088.5])
'''
# 获取常量ax
        for j in range(len(MCBAND)):
            if lat >= MCBAND[j]:
                ax = MC2LL[j]
                break

        if ax is None:
            raise GISError("error lat:%s" % lat)
'''

def bd09_to_MCT(lng,lat):
    # 获取常量ax
    # 这里是验证给定的px值范围
    j = 3
    ax = MC2LL[j]
    
    px = (lng - ax[0])/ax[1]
    
    # 计算py
    p = np.array([ax[8],ax[7],ax[6],ax[5],ax[4],ax[3],ax[2]-lat])
    i = np.roots(p)
    q = []
    # 找到虚部为0的解
    for t in range(len(i)):
        if i[t].imag == 0:
            q.append(np.real(i[t]))

    i = min(q)
    py = i*ax[9]
    
    return px,py

for i in range(df.shape[0]):
    df.loc[i,'p_x'] =  bd09_to_MCT(df['lng'][i],df['lat'][i])[0]
    df.loc[i,'p_y'] = bd09_to_MCT(df['lng'][i],df['lat'][i])[1]
#df.to_csv('/Users/bingliu/Desktop/🌟/21 地图数据/交通可视化/data/选点/center_'+str(center_num)+'_p.csv',index = None)
#df


# 保存点对数据。对这些对抓取travel time和distance
df_1 = pd.DataFrame([])
k = 0
for i in range(df.shape[0]):
    for j in range(df.shape[0]):
        if i != j:
            df_1.loc[k,'from_lng'] = df.iloc[i][0]
            df_1.loc[k,'from_lat'] = df.iloc[i][1]
            df_1.loc[k,'from_px'] = df.iloc[i][3]
            df_1.loc[k,'from_py'] = df.iloc[i][4]
            df_1.loc[k,'from_type'] = df.iloc[i][2]
            
            df_1.loc[k,'to_lng'] = df.iloc[j][0]
            df_1.loc[k,'to_lat'] = df.iloc[j][1]
            df_1.loc[k,'to_px'] = df.iloc[j][3]
            df_1.loc[k,'to_py'] = df.iloc[j][4]
            df_1.loc[k,'to_type'] = df.iloc[j][2]
            k = k+1
df_1.to_csv('/data/center_'+str(center_num)+'_pair.csv')
df_1