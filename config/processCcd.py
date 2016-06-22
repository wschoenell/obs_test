"""obs_test-specific overrides for the processCcd task
"""
import os.path
from lsst.utils import getPackageDir

configDir = os.path.join(getPackageDir("obs_test"), "config")
config.isr.load(os.path.join(configDir, 'isr.py'))
# we don't have astrometry_net data (yet) so astrom and photo cal are impossible
config.calibrate.doAstrometry=False
config.calibrate.doPhotoCal=False
