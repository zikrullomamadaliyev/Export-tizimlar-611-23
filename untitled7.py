# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fxDg1QcPtsRRqRfGHYJoHbDGrlfvmRmo
"""

def iphone(belgi):
  if belgi == "iphone 1":
    return "900 "
  elif belgi=="iphone 2":
    return "1000"
  elif belgi=="iphone 3":
    return "2000"
  if belgi=="iphone 4":
    return "3000$"
  elif belgi=="iphone 5":
    return "4000$"
  elif belgi=="iphone 6":
    return "5000$"
  elif belgi=="iphone 7":
    return "6000$"
  elif belgi=="iphone 8":
    return "7000$"
  elif belgi=="iphone 9":
    return "8000$"
  elif belgi=="iphone 10":
    return "9000$"
  elif belgi=="iphone 11":
    return "1000$"
  elif belgi=="iphone 12":
    return "11000$"
  elif belgi=="iphone 13":
    return "12000$"
  else:
    return "iphone magazinga hush kelibsiz"
  belgi =input ("telefondi tanlang")
  natija=iphone(belgi)
  print(natija)