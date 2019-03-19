import psycopg2
import datetime
import time
from array import *
conn = psycopg2.connect(user = "postgres",
                        password ="7623148",
                        host = "localhost",
                        port = "5432",
                        database = "nyc_feb")

cursor = conn.cursor()


def gen_intervals():

    doi = input("Enter the date in YYYY-MM-DD: \n")
    year,month, day = map(int, doi.split("-"))
    doi = datetime.date(year,month,day)

    interval = int(input("Enter the interval: \n"))
    time_difference = datetime.timedelta(minutes = interval)
    current_time = datetime.datetime(doi.year,
                                    doi.month,
                                    doi.day,
                                    0,
                                    0,
                                    0)
    num_intervals = int((24 * 60) / interval)
    x = int(num_intervals/2)
    #print(num_intervals)
    intervals = []
    for i in range(num_intervals):
        t1 = current_time
        t2 = current_time + time_difference
        print("t1",t1)
        print("t2",t2,"\n")
        intervals.append([])
        for j in range(x):
            intervals[i].append([t1,t2])# https://stackoverflow.com/questions/8183146/two-dimensional-array-in-python
        current_time += time_difference # https://stackoverflow.com/questions/43291165/how-to-append-multi-dimensional-array-using-for-loop-in-python/43291192

    return intervals
    print(intervals)
gen_intervals()
