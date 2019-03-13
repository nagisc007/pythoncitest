# -*- coding: utf-8 -*-

from enum import Enum


class ActType(Enum):
    ANGRY = 'angry' # 怒る
    APPEAR = 'appear' # 現れる
    BITTER = 'bitter' # 苦笑する
    CLICK = 'click' # クリックする
    CLOSEDOOR = 'closedoor' # ドアを閉める
    COME = 'come' # 来る
    CRY = 'cry' # 叫ぶ
    DESC = 'description' # その他の描写
    DICK = 'dick' # 掘る
    DRINK = 'drink' # 飲む
    EAT = 'eat' # 食べる
    ENTER = 'enter' # 入る
    FACE = 'face' # 表情をする
    FACEUP = 'faceup' # 顔を上げる
    GET = 'get' # 手に入れる
    GIVE = 'give' # 与える
    GO = 'go' # 行く
    LOOK = 'look' # 見る
    MAKE = 'make' # 作る
    MOUTH = 'mouth' # 口をする
    MUST = 'must' # しなければならない
    OFFFIRE = 'offfire' # 日を消す
    ONFIRE = 'onfire' # 火を点ける
    OPENDOOR = 'opendoor' # ドアを開ける
    POUR = 'pour' # 注ぐ
    READ = 'read' # 読む
    REMEMBER = 'remember' # 思い出す
    RIDE = 'ride' # 乗る
    ROUGH = 'rough' # 笑う
    SAD = 'sad' # 悲しむ
    SHAKEHAND = 'shakehand' # 握手する
    SHAKEHEAD = 'shakehead' # 首／頭を振る
    SMILE = 'smile' # 微笑する
    SURPRISED = 'surprised' # 驚く
    SYMBOL = 'symbol' # 記号用。タイトル等
    TEAR = 'tear' # 涙を流す
    TELL = 'tell' # 言う。台詞用
    THINK = 'think' # 考える
    TREMBLE = 'tremble' # 震える
    TURNOFF = 'turnoff' # 消す
    TURNON = 'turnon' # 点ける
    WALK = 'walk' # 歩く
    WINCE = 'wince' # たじろぐ
    WIPE = 'wipe' # 拭う
    WRITE = 'write' # 書く
    WRY = 'wry' # 顔を顰める
