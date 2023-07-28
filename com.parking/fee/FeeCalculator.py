#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 08:00:58 2023

@author: anurag
"""

class FeeCalculator:
    
    def __init__(self):
        self.parkingRuleList = [];
      

    def setRules(self, parkingRuleList):
        self.parkingRuleList = parkingRuleList;
       

    def calculateFee(self, entryTime, exitTime, vehicleType):
        totalFee = 0.0
        for parkingRule in self.parkingRuleList:
            if parkingRule.isRuleApplicable(vehicleType):
                totalFee = totalFee + parkingRule.getParkingFee(entryTime, exitTime)
        return totalFee;

    def set_previous_interval_counted(self, previousIntervalCounted):
        self.previousIntervalCounted = previousIntervalCounted

    def is_previous_interval_counted(self):
        return self.previous_interval_counted
