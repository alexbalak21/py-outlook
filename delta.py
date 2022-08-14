from datetime import datetime

time1 = datetime.strptime('2022-08-10 15:37:20.154300', '%Y-%m-%d %H:%M:%S.%f')


time2 = datetime.strptime('2022-08-10 16:37:00.000000', '%Y-%m-%d %H:%M:%S.%f')


delta = time2 - time1

print(delta.seconds / 60)