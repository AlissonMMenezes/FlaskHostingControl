#!/usr/bin/python

import sys
import os

sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
activate_this = os.path.dirname(os.path.abspath(__file__))+"/bin/activate_this.py" 
execfile(activate_this,dict(__file__=activate_this))


from YOURAPPLICATION.app import app as application
