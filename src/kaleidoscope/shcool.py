import re
from random import random, choice
from time import sleep
import numpy as np
import pymssql
from mingzi.mingzi import *


def rand_data():
    data = []
    for exam_number in range(75001, 75400):
        examinee = [str(exam_number), mingzi(volume=1, show_gender=False)[0]]
        examinee.append(min(abs(int(np.random.normal(100, 12, 1))), 132))
        examinee.append(min(abs(int(np.random.normal(70, 20, 1))), 135))
        examinee.append(min(abs(int(np.random.normal(110, 20, 1))), 138))
        examinee.append(min(abs(int(np.random.normal(60, 20, 1))), 92))
        examinee.append(min(abs(int(np.random.normal(70, 20, 1))), 95))
        examinee.append(sum(examinee[2:]))
        data.append(examinee)
    return data


with pymssql.connect(server="localhost", user="sa", password="256077", database="cube", tds_version="7.0") as db:
    with db.cursor() as cursor:
        db.autocommit(True)
        sql = "TRUNCATE TABLE [dbo].[grade_table]"
        cursor.execute(sql)
        for i in rand_data():
            sql = "INSERT INTO [dbo].[grade_table] VALUES{}".format(tuple(i))
            cursor.execute(sql)
print("done")
