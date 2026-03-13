import os
import sys

# 请在此输入您的代码
from datetime import datetime, timedelta
t = int(input())

for i in range(t):
  data = input().split()
  date = list(map(int, data[0].split('-')))
  time = list(map(int, data[1].split(':')))
  x = int(data[2])

  start = datetime(1970, 1, 1)
  delta = datetime(date[0], date[1], date[2], time[0], time[1]) - start
  ans_m = 0
  
  n = delta.total_seconds() // 60 // x
  ans_m = n * x

  print(start + timedelta(minutes=ans_m))
