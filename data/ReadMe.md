# obs_test data repository

This ReadMe describes the obs_test data in the "input" repository.

The data is derived from the following lsstSim data, on NCSA's lsst-dev machine:
/lsst4/krughoff/Tuesday_data/imSim/S12_lsstsim

For reference, the associated astrometry_net_data is:
/lsst2/krughoff/astrometry_net_data/imsim-2012-06-20-0

The obs_test sensor is a 1018x2000 subregion of a single LSST sensor:
    R2,2 (the center raft)
    S0,0 (lower left sensor/detector)
    C0,0, C0,1, C1,0 C1,1 but just the 1000 pixels in Y from each nearest the Y center line
A subregion is used to keep the test images smaller. The region is chosen to be near, but not at,
the center of the LSST focal plane, in order to make the obs_test camera geometry nontrivial
and to provide a bit of distortion.

The obs_test raw data uses E000 R22 S00 of the following lsstSim visits:
    obs_test            lsstSim
    visit=1 filter=g    v890104911-fg
    visit=2 filter=g    v890106021-fg
    visit=3 filter=r    v890880321-fr

## How to make the data

To create the repository database, from the obs_test directory
(use bin/ to disambiguate from other obs_ packages that may be setup):

    setup -r .
    bin/genInputRegistry.py data/input


To make the obs_test bias image, from the obs_test directory:

    setup -r .
    data/utils/assembleLsstChannels.py /lsst4/krughoff/Tuesday_data/imSim/S12_lsstsim/bias/v0/R22/S00
    mv image.fits bias.fits

To make obs_test flat images, from the obs_test directory:

    setup -r .
    data/utils/assembleLsstChannels.py /lsst4/krughoff/Tuesday_data/imSim/S12_lsstsim/flat/v2-fg/R22/S00
    mv image.fits flat_fg.fits
    data/utils/assembleLsstChannels.py /lsst4/krughoff/Tuesday_data/imSim/S12_lsstsim/flat/v2-fr/R22/S00
    mv image.fits flat_fr.fits

To make obs_test raw images, from the obs_test directory:

    setup -r .
    data/utils/assembleLsstChannels.py /lsst4/krughoff/Tuesday_data/imSim/S12_lsstsim/raw/v890104911-fg/E000/R22/S00
    mv image.fits raw_v1_fg.fits
    data/utils/assembleLsstChannels.py /lsst4/krughoff/Tuesday_data/imSim/S12_lsstsim/raw/v890106021-fg/E000/R22/S00
    mv image.fits raw_v2_fg.fits
    data/utils/assembleLsstChannels.py /lsst4/krughoff/Tuesday_data/imSim/S12_lsstsim/raw/v890880321-fr/E000/R22/S00
    mv image.fits raw_v3_fr.fits

To make an obs_test defects file from the bias frame generated above, from the obs_test directory:

    setup -r .
    data/utils/defectsFromBias.py data/input/bias/bias.fits.gz
    mv defects_c0.fits data/input/defects/

## Hints for using the data

To run processCcd.py (the r band image requires increasing nCrPixelMax to be successfully processed):

    setup pipe_tasks
    processCcd.py data/input --id filter=r^g --config calibrate.repair.cosmicray.nCrPixelMax=20000 --output=output
