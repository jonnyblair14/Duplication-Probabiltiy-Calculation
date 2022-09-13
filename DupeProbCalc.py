# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:12:17 2022

@author: jonnyblair14
"""
f = open("output.txt", 'a')
pack = 1
negative_odds = 1
positive_odds = 0
total = 365


while pack < total + 1:
     negative_odds = ((total - pack + 1)/total) * negative_odds
     positive_odds = 1 - negative_odds
     print(str(pack) + ", \t" + str(negative_odds) + ", \t" + str(positive_odds) + "; \n")
     f.write(str(pack) + ", \t" + str(negative_odds) + ", \t" + str(positive_odds) + "; \n")
     pack += 1

f.close()