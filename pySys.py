#!/usr/bin/env python

import os


def clear():
    name = os.name
    if(name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
    
