#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 08:01:30 2023

@author: shaurya
"""

from constants.ParkingConstants import ParkingConstants;
from exception.ParkingTicketInvalid import ParkingTicketInvalid

class ParkingStore:
    
    def __init__(self):
        self.reservedParkingDict = {};
    
    def storeParking(self, parkingStoreDict):
        self.parkingStoreDict = parkingStoreDict;
        
    def parkingAvailable(self, parkingType):
       parkingStoreDict = self.parkingStoreDict[parkingType];
       for parkingSpot in list(parkingStoreDict.values()):
         if parkingSpot.parkingType == parkingType:
           return True;
       return False;    
        
    def reserveParking(self, parkingId, parkingType):
        parkingStore = self.parkingStoreDict[parkingType][parkingId];
        self.parkingStoreDict[parkingType].pop(parkingId)
        self.reservedParkingDict[parkingId] = parkingStore;
        
        
    def unReserveParking(self, parkingTicket):
        print(' reserve parking', self.reservedParkingDict);
        parkingSpot = self.reservedParkingDict.pop(parkingTicket.parkingId);
        if parkingSpot is None:
            raise ParkingTicketInvalid(ParkingConstants.PARKINGTICKETINVALID)
        parkingSpotList = self.parkingStoreDict[parkingSpot.parkingType];    
        parkingSpotList[parkingTicket.parkingId] = parkingSpot
        self.parkingStoreDict[parkingSpot.parkingType] = parkingSpotList;
        return parkingSpot;
       