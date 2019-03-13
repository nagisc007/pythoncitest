# -*- coding: utf-8 -*-

import unittest
import common
from outline import outline

class OutlineTest(unittest.TestCase):
    def test_outline_all_actions(self):
        actions = outline()
        for a in actions:
            self.assertIsInstance(a, common.Act)

    def test_outline_contains_elements(self):
        story = outline()

        for s in story:
            if isinstance(s.subject, common.Person):
                break
        else:
            raise AssertionError('Person not exists in outline')
        
        for s in story:
            if isinstance(s.subject, common.Stage):
                break
        else:
            raise AssertionError('Stage not exits is outline')

        for s in story:
            if isinstance(s.subject, common.DayTime):
                break
        else:
            raise AssertionError("DayTime not exits is outline")
