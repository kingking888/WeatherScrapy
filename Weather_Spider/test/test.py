'''
    -*- coding: utf-8 -*- 
    @Time : 2020/2/13 16:32 
    @Author : Bulin Liang 
    @File : test.py 
    @Software: PyCharm
'''

'''
该文件完成功能：
    
'''
n = int(input("input a number："))
N = [0] * n

for i in range(len(N)):
    N[i] = int(input(f"输入第{i}个数："))
for i in range(len(N)):
    for j in range(len(N) - i - 1):
        if N[j] > N[j + 1]:
            print("change")
            N[j], N[j + 1] = N[j + 1], N[j]

