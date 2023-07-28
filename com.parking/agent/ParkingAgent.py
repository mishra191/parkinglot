#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 07:47:17 2023

@author: anurag
"""
from util.Util import Util;
from constants.ParkingConstants import ParkingConstants;
from sorting.SortingAgent import SortingAgent;
from store.ParkingStore import ParkingStore;
from exception.ParkingNotAvailable import ParkingNotAvailable;
from ticket.ParkingTicket import ParkingTicket;
from fee.FeeCalculator import FeeCalculator;
from receipt.ParkingReceipt import ParkingReceipt;

class ParkingAgent:
    
  def __init__(self):
      self.parkingStore = ParkingStore();
      self.feeCalculatorAgent = FeeCalculator();
      self.sortingAgent = SortingAgent();
  
  def allocateParking(self):
      parkingStoreDict = Util().loadParkingSpots();
      self.parkingStore.storeParking(parkingStoreDict); 
      
  def loadRules(self, ruleFile):
      self.feeCalculatorAgent.setRules(Util().loadRules(ruleFile));
      
      
  def __parkingAvailable(self, parkingType):
      return  self.parkingStore.parkingAvailable(parkingType);
      
  def reserveParking(self, parkingType, sortingAlgorithm, time):
      
      if self.__parkingAvailable(parkingType) != True:
          raise ParkingNotAvailable(ParkingConstants.PARKINGNOTAVAILABLE);
      
      #parking sorted here
      sortedParkingList= self.sortingAgent.sortParkingSpots(list(self.parkingStore.parkingStoreDict[parkingType].values()), sortingAlgorithm);
      parkingId = sortedParkingList[0].parkingId;
      self.parkingStore.reserveParking(parkingId, parkingType);
      return ParkingTicket(parkingId, time);
  
      
  def unReserveParking(self, parkingTicket, outTime):
      parkingSpot = self.parkingStore.unReserveParking(parkingTicket);      
      total = self.feeCalculatorAgent.calculateFee(parkingTicket.entryTime, outTime, parkingSpot.parkingType);
      return ParkingReceipt(parkingTicket.entryTime, outTime, total);
      

 

    
    

    