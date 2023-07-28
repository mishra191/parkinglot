#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:17:18 2023

@author: anurag
"""

import math

class ParkingRule:
    
    def __init__(self, id, type, interval=None, min=None, max=None, fee=None):
        self.id = id
        self.type = type
        self.interval = interval
        self.min = min
        self.max = max
        self.fee = fee
        self.totalInterval = None
        
    def getParkingFeeIntervalBased(self, minutes):
        print("self.id", self.id)
        print("self.interval", self.interval)
        print("minutes", minutes)
        
        if self.min !=None:
            if minutes >= self.min:
              totalInterval = math.ceil(minutes- self.min/60);
              return self.fee*totalInterval
            else:
                return 0;
        totalInterval = 1 if self.interval >= minutes else math.ceil((minutes- self.interval) / 60)
        return self.fee*totalInterval
      
    def getParkingFeeTimeBased(self, minutes): 
        if self.min <= minutes < self.max:
            return self.fee;
        
    def getParkingFee(self, entry_time, exit_time):
       minutes = (exit_time - entry_time).total_seconds() / 60 
       if self.interval != None:
         return self.getParkingFeeIntervalBased(minutes)
       return  self.getParkingFeeTimeBased(minutes)
        
         
 
    def isRuleApplicable(self, vehicle_type):
        if self.type != vehicle_type:
            return False
        return True
        
   
   
      
       
     

    
           
