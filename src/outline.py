# -*- coding: utf-8 -*-

from common import Act, Chapter, DayTime, Description, Item, Person, Stage, Title
from acttypes import ActType

class Dooler(Person):
    """ 人形師の女
    """
    def __init__(self):
        super().__init__("女", 28, "女性", "人形師")
    def serious_face(self):
        return Act(self, ActType.FACE, "真剣な顔をする", with_subject=True)

class Man(Person):
    """ 女の許を訪れる男
    """
    def __init__(self):
        super().__init__("男", 25, "男性", "遊び人")


class WesternHouse(Stage):
    def __init__(self):
        super().__init__("洋館", "西洋風の二階建ての洋館")

class DoolRoom(Stage):
    def __init__(self):
        super().__init__("人形部屋", "等身大の人形が飾られた部屋")

    def redcarpet(self):
        return Act(self, ActType.DESC, "真っ赤な絨毯", "真っ赤な絨毯が敷かれ、人形を入れた箱が置かれていた")


class CurrentDay(DayTime):
    def __init__(self):
        super().__init__("当日", mon=6, hour=10)

def outline():
    woman = Dooler()
    man = Man()
    house = WesternHouse()
    cur_day = CurrentDay()
    return (
            Title("人形師の女"),
            cur_day.description(),
            house.description(),
            woman.tell("約束してね"),
            man.tell("たった一度のことだろう？"),
            woman.tell("その一度で充分だと、私は思うのです"),
            Description("（了）"),
            )
