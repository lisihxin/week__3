# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 建立字典，key為小寫字母，value為大寫字母
letter_dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

# 使用者輸入
user_input = input("請輸入小寫英文字母：")

# 將輸入的字母轉換為大寫
result = ""
for letter in user_input:
    if letter in letter_dict:
        result += letter_dict[letter]
    else:
        result += letter

# 顯示結果
print("轉換後的結果為：", result)
