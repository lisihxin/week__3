# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:44:01 2024

@author: student
"""

import random

# 建立撲克牌
suits = ['♥', '♦', '♣', '♠']
numbers = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
deck = [(suit, number) for suit in suits for number in numbers]

# 洗牌
random.shuffle(deck)

# 發牌給四個人
player_hands = [[] for _ in range(4)]
for i, card in enumerate(deck):
    player_hands[i % 4].append(card)

# 對每個玩家的手牌進行排序
for hand in player_hands:
    hand.sort(key=lambda x: (numbers.index(x[1]), suits.index(x[0])))

# 顯示結果
for i, hand in enumerate(player_hands):
    print(f"玩家 {i+1} 的手牌：", hand)
