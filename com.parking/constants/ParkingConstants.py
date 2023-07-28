#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:23:47 2023

@author: anurag
"""

class ParkingConstants:
    
    def __init__(self):
        print('FILENAME', ParkingConstants.FILENAME);
        
    RESERVEFILENAME = 'reserve.txt';
    UNRESERVEFILENAME = 'unreserve.txt'
    PARKINGSPOTFILE = "parkingspot.json";
    PARKINGRULEFILE = "rules.json";
    PARKINGNOTAVAILABLE = "Parking is not available";
    KEYNOTEXISTS = "sorting not supported";
    PARKINGTICKETINVALID = "parking ticket is invalid";
    NEARESTPARKING = 'NP'
    ROOTPATH = "/Users/shaurya/python-workspace/parkinglot/";
    RESERVE='RESERVE'
    UNRESERVE='UNRESERVE'
    SMALL='0'
    MEDIUM='1'
    LARGE='2'
    KEYNOTEXISTS='Key Not Exist'