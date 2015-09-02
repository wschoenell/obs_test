"""lsstSim-specific overrides for the processCcd task
"""
config.isr.doDark=False
config.isr.doFringe=False
config.calibrate.doAstrometry=False # no astrometry_net data?
config.calibrate.doPhotoCal=False # forbidden if doAstrometry false
