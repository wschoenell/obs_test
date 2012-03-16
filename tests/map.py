#!/usr/bin/env python

# 
# LSST Data Management System
# Copyright 2008, 2009, 2010 LSST Corporation.
# 
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the LSST License Statement and 
# the GNU General Public License along with this program.  If not, 
# see <http://www.lsstcorp.org/LegalNotices/>.
#

import unittest
import lsst.utils.tests as utilsTests

import os
from lsst.obs.test import TestMapper

# map_raw(self, dataId)
# query_raw(self, key, format, dataId)
# std_raw(self, item)
# keys(self)
# 
# __init__(self)
# getDatasetTypes(self)
# map(self, datasetType, dataId)
# queryMetadata(self, datasetType, key, format, dataId)
# canStandardize(self, datasetType)
# standardize(self, datasetType, item, dataId)
# validate(self, dataId)

class TestMapperTestCase(unittest.TestCase):
    """A test case for the test mapper."""

    def setUp(self):
        self.input = os.path.join(os.environ['OBS_TEST'],
                "tests", "data", "input")
        self.calib = os.path.join(os.environ['OBS_TEST'],
                "tests", "data", "calib")
        self.output = os.path.join(os.environ['OBS_TEST'],
                "tests", "data", "output")
        self.mapper = TestMapper(root=self.input,
                calibRoot=self.calib,
                outputRoot=self.output)

    def tearDown(self):
        del self.mapper

    def testMapRaw(self):
        pass

    def testQueryRawData(self):
        pass

    def testStdRawData(self):
        pass

    def testMapConfigData(self):
        pass

    def testQueryConfigData(self):
        pass

    def testMapMetadataData(self):
        pass

    def testQueryMetadataData(self):
        pass

    def testKeys(self):
        self.assertEqual(self.mapper.keys(),
                set(['visit', 'raft', 'sensor', 'snap', 'channel']))

    def testGetDatasetTypes(self):
        self.assertEqual(self.mapper.getDatasetTypes(),
                set(['raw', 'processCcd_config', 'processCcd_metadata']))

    def testMap(self):
        pass

    def testQueryMetadata(self):
        pass

    def testCanStandardize(self):
        pass

    def testStandardize(self):
        pass

    def testValidate(self):
        pass

def suite():
    utilsTests.init()

    suites = []
    suites += unittest.makeSuite(TestMapperTestCase)
    suites += unittest.makeSuite(utilsTests.MemoryTestCase)
    return unittest.TestSuite(suites)

def run(shouldExit=False):
    utilsTests.run(suite(), shouldExit)

if __name__ == '__main__':
    run(True)
