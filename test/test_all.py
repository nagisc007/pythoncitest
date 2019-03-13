# -*- coding: utf-8 -*-

import unittest
from test_hoge import HogeTest
from test_outline import OutlineTest

def suite():
    ''' Packing all tests.
    '''
    suite = unittest.TestSuite()
    suite.addTests((
        unittest.makeSuite(HogeTest),
        unittest.makeSuite(OutlineTest),
        ))
    return suite
