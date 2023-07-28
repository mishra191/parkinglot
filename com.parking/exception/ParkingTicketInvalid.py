#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 23:12:36 2023

@author: anurag
"""

class ParkingTicketInvalid(Exception):
    
    def __init__(self,message):
        super().__init__(self.message);