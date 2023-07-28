#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 08:09:44 2023

@author: anurag
"""

from exception.KeyNotExist import KeyNotExist;
from constants.ParkingConstants import ParkingConstants;

class SortingAgent:
    
    def __init__(self):
      self.supportedSorting = {ParkingConstants.NEARESTPARKING : lambda parkingSpot: parkingSpot.parkingRowId + parkingSpot.parkingFloorId};
    
    # sort on basis of specific key
    def sortParkingSpots(self, parkingStoreList, sortingKey):
       sortedParkingDict = [];
       keys = self.supportedSorting.keys()
       print(keys)
       if sortingKey in self.supportedSorting :
          sortedParkingDict = sorted(parkingStoreList, key=self.supportedSorting[sortingKey]);          
       else:
          raise KeyNotExist(ParkingConstants.KEYNOTEXISTS);
       return sortedParkingDict;    