#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:44:32 2022

@author: rene
"""

import numpy as np;

NUM = 8;

total = np.zeros(NUM + 5);
total[5] = 1;

for i in range(NUM - 1):
    total[i + 6] = sum(total[i : i + 6]) / 6;
    print("Kans op een tussentotaal van " + str(i + 1) + ": " + str(total[i + 6]));

print("\nKans op een solo: " + str(sum(total[5 : NUM + 5]) / NUM / 6));
