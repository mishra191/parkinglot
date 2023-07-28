#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:01:15 2023

@author: anurag
"""

from datetime import datetime

class ParkingTicket:
    
    def __init__(self, parkingId, time):
        if time != None:
            self.ticketNumber = str(parkingId) + " "+ str(time);
            self.entryTime = time;
        else:
            self.entryTime = datetime.now();
            self.ticketNumber = str(parkingId) + " "+ str(self.entryTime);
        self.parkingId = parkingId;
          
    def __str__(self):
        return f"Ticket Number: {self.ticketNumber}, Parking Ticket: {self.parkingId}"
 

