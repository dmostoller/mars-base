import sys

import ipdb

from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
    pass
    # remove pass and write your debug implementation
  ipdb.set_trace(sys._getframe())
