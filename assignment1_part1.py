#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Working with Functions"""

def  listDivide(numbers, divide =2):

   dividable = []
   for digits in numbers:
       if digits % divide == True
   return dividable.append(digits)


class ListDivideException(Exception):
    pass


def testListDivide(listDivide):
    try:
        list_divide([1, 2, 3, 4, 5])
        list_divide([2, 4, 6, 8, 10])
        list_divide([30, 54, 63, 98, 100], divide=10)
        list_divide([0])
        list_divide([1, 2, 3, 4, 5], 1)
    except:
        raise ListDivideException()

