# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:42:36 2024

@author: student
"""

import random

# 使用者輸入 n, a, b 三個整數值
n = int(input("請輸入 n："))
a = int(input("請輸入 a："))
b = int(input("請輸入 b："))

# 隨機抽取 n 個 a 到 b 之間的數
random_numbers = random.sample(range(a, b+1), n)

# 刪除重複的數字並由大到小排序
random_numbers = sorted(list(set(random_numbers)), reverse=True)

# 顯示結果
print("隨機抽取且刪除重複後的數字（由大到小排序）：", random_numbers)
