#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_03.py create tuple"""


# import user lib 'data'
from data import DIRECTIONS

DIRECTIONS = DIRECTIONS
LENG = len(DIRECTIONS)-1
DIRECTIONS = DIRECTIONS[0:LENG] + ('West', )
