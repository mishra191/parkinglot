#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:23:56 2023

@author: anurag
"""
from model.ParkingRule import ParkingRule;

class RulesModel:
    def __init__(self, rules=None):
        self.rules = rules or []

    @classmethod
    def from_json(cls, json_data):
        rules_data = json_data.get("rules", [])
        rules = [ParkingRule(rule.get("id"), rule.get("type"), rule.get("interval"), rule.get("min"), rule.get("max"), rule.get("fee")) for rule in rules_data];
        return cls(rules)

   