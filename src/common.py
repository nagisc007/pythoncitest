# -*- coding: utf-8 -*-


from acttypes import ActType


class Act(object):
    """ basic action class.
    """
    def __init__(self, subject, act_type, action, description, with_subject=False):
        self.action = action
        self.act_type = act_type
        self.description = description
        self.subject = subject
        self.with_subject = with_subject


class Title(Act):
    """ For title act
    """
    def __init__(self, title, desc=""):
        super().__init__(self, ActType.SYMBOL, title, desc)


class Chapter(Act):
    """ For chapter start act
    """
    def __init__(self, chapter_title, desc=""):
        super().__init__(self, ActType.SYMBOL, chapter_title, desc)


class Description(Act):
    """ Nothing subject description act.
    """
    def __init__(self, act, desc=""):
        super().__init__(self, ActType.DESC, act, desc)


class Person(object):
    """ basic character class.
    """
    def __init__(self, name, age, sex, job):
        self.name = name
        self.age = age
        self.sex = sex
        self.job = job

    def tell(self, what, desc="", with_subject=False):
        ''' For dialogue
        '''
        return Act(self, ActType.TELL, "「{}」".format(what), desc, with_subject)


class Stage(object):
    """ basic stage class.
    """
    def __init__(self, name, act):
        self.name = name
        self.act = act

    def description(self, desc=""):
        return Act(self, ActType.DESC, self.act, desc)

class Item(object):
    """ basic item class.
    """
    def __init__(self, name, act):
        self.name = name
        self.act = act

    def description(self, desc=""):
        return Act(self, ActType.DESC, self.act, desc)

class DayTime(object):
    """ basic day and time class.
    """
    def __init__(self, act, mon=0, day=0, year=0, hour=0):
        self.year = year
        self.mon = mon
        self.day = day
        self.hour = hour
        self.act = act

    def description(self, desc=""):
        return Act(self, ActType.DESC, self.act, desc)

