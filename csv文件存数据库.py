# -*- coding:UTF-8 -*-
import pymysql
import pandas as pd
from sqlalchemy import create_engine

# 数据库信息
mysql_setting = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': '200823',
    # 数据库名称
    'db': 'test',
    'charset': 'utf8'
}
# 表名
# 如果不存在表，则自动创建
table_name = 'jordan'
# 文件路径
path = r'C:\Users\86156\Desktop\JordanData.csv'

data = pd.read_csv(path, encoding='utf8')
print(data)
engine = create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting), max_overflow=5)
data.to_sql(table_name, engine, index=False, if_exists='replace')
print('导入成功...')
