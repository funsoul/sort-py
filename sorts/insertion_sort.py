#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insertion sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from .base import *
from typing import List
import copy

class InsertionSort(Base):
    length = 10
    process = []

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        self.process.append(copy.deepcopy(L))
        for p in range(1, self.length):
            tmp = L[p]
            i = p
            while i > 0 and L[i-1] > tmp:
                L[i] = L[i-1]
                i = i-1
                print(L)
                self.process.append(copy.deepcopy(L))
            L[i] = tmp
            self.process.append(copy.deepcopy(L))
        return L