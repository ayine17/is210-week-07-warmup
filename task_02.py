#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""list and performing some standard access functions"""

# import local variable reference
import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])
