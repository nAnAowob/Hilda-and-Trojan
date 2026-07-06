import pandas as pd
import matplotlib.pyplot as plt

"""
    import ข้อมูล
    df = pd.read_csv(r'/Users/chompunick/Dropbox/Mac/Desktop/CoMat/CoMat_finalCode/CoMatDataDummy.csv')
    rf = pd.read_csv(r'/Users/chompunick/Dropbox/Mac/Desktop/CoMat/CoMat_finalCode/coordinate.csv')
    คิดเลขให้ import numpy as np
    pandas ใช้ import file
    matplotlib ใช้ plot data
"""

fig = plt.figure()
ax = plt.axes(projection="3d")

x = [0 for I in range(0,3,1)]
y = [0 for I in range(0,3,1)]
z = [0 for I in range(0,3,1)]
#ในกรณีที่ importf file, ใช้ len(column)

for i in range (0,3):
    x[i] = i+2
    y[i] = i*2
    z[i] = i-2
    #input ค่าลงไป ถ้าตอนอ่านไฟล์ไม่ต้องทำอันนี้

ax.scatter(x,y,z)
plt.show()