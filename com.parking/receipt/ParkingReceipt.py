#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:04:59 2023

@author: anurag
"""
import time

class ParkingReceipt:
    def __init__(self, entryTime, exitTime, feeAmount):
        self.entryTime = entryTime
        self.exitTime = exitTime
        self.feeAmount = feeAmount
        self.receiptNumber = int(time.time() * 1000)

    def __str__(self):
        return f"ParkingReceipt:\nReceiptNumber: {self.receiptNumber}\nEntry Date-time: {self.entryTime}\nExit Date-time: {self.exitTime}\nFees: {self.feeAmount}"



