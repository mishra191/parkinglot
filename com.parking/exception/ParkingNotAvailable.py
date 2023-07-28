#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 08:52:32 2023

@author: anurag
"""

    
class ParkingNotAvailable(Exception):
    
    def __init__(self,message):
        super().__init__(self.message);


