"""obs_test-specific overrides for the processCcd task
"""
import os.path
from lsst.utils import getPackageDir

configDir = os.path.join(getPackageDir("obs_test"), "config")
config.isr.load(os.path.join(configDir, 'isr.py'))

configDir = os.path.join(getPackageDir("obs_test"), "config")
config.calibrate.load(os.path.join(configDir, 'calibrate.py'))
