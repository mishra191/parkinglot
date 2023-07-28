#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:22:33 2023

@author: anurag
"""
    
class ParkingSpot:
    
    def __init__(self, parkingId, parkingFloorId, parkingRowId, parkingSpotId, parkingType):     
        self.parkingId = parkingId;
        self.parkingFloorId = int(parkingFloorId);
        self.parkingRowId = int(parkingRowId);
        self.spotId = int(parkingSpotId);
        self.parkingType = parkingType;
 
    