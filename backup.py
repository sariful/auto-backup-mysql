import os
import string
# from os import path
from datetime import datetime
from string import ascii_uppercase


for l in string.ascii_uppercase:
    if os.path.exists('%s:\\File.ID' % l):
        USBPATH = '%s:\\' % l
        print('USB mounted to', USBPATH)
        break
# print(drive)


datetime = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')

# home_dir = os.system(
#     "mysqldump -u root -pZubizi03365656533 retech_main > retech_" + datetime + ".sql")
