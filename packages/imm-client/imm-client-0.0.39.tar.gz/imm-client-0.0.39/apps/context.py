import os, sys
from pathlib import Path


BASEDIR = Path(__file__).parents[1]
# All data directory
DATADIR = BASEDIR / "data"
# Insert the BASEDIR to system path
sys.path.insert(0, os.fspath(BASEDIR))
