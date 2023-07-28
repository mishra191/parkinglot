#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 09:17:18 2023

@author: anurag
"""

import json
from model.ParkingSpot import ParkingSpot
from constants.ParkingConstants import ParkingConstants
from model.ParkingRule import ParkingRule


class Util:

  def loadParkingSpots(self):
    file = open(ParkingConstants.ROOTPATH + ParkingConstants.PARKINGSPOTFILE)
    data = json.load(file)
    parkingSpotSmallList = {}
    parkingSpotMediumList = {}
    parkingSpotLargeList = {}
    parkingSpotDict = {}

    for floor in data['spots']['floor']:
        floor_key = floor['id']
        rows = floor['row']
        for row in rows:
            row_id = row['id']
            spots = row['spot']
            for spot in spots:
                spot_id = spot['id']
                spot_type = spot['type']
                parkingId = str(floor_key)+str(row_id)+str(spot_id)
                parkingSpot = ParkingSpot(
                    parkingId, floor_key, row_id, spot_id, spot_type)
                if spot_type == ParkingConstants.SMALL:
                  parkingSpotSmallList[parkingId] = parkingSpot
                if spot_type == ParkingConstants.MEDIUM:
                  parkingSpotMediumList[parkingId] = parkingSpot
                if spot_type == ParkingConstants.LARGE:
                   parkingSpotLargeList[parkingId] = parkingSpot

    parkingSpotDict[ParkingConstants.SMALL] = parkingSpotSmallList
    parkingSpotDict[ParkingConstants.MEDIUM] = parkingSpotMediumList
    parkingSpotDict[ParkingConstants.LARGE] = parkingSpotLargeList
    return parkingSpotDict

  def loadRules(self, ruleFile):
    file = open(ParkingConstants.ROOTPATH + ruleFile)
    data = json.load(file)


     # Retrieve the rules from the JSON data
    rules_data = data.get('rules', [])

    # Create a list of Rule objects
    rule_list = []
    for rule in rules_data:
        rule_obj = ParkingRule(
          rule.get('id'),
          rule.get('type'),
          rule.get('interval'),
          rule.get('min'),
          rule.get('max'),
          rule.get('fee')
         )
        rule_list.append(rule_obj)
    return rule_list;   
    
