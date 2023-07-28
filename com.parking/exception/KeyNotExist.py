#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 07:28:40 2023

@author: anurag
"""

class KeyNotExist(Exception):
    
    def __init__(self, message):
        super().__init__(message);
        
        
     