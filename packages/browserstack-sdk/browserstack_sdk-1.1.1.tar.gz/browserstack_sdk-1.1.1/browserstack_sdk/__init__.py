# coding: UTF-8
import sys
bstack1l11_opy_ = sys.version_info [0] == 2
bstack1_opy_ = 2048
bstack1l1_opy_ = 7
def bstack11_opy_ (bstack111_opy_):
    global bstack1l_opy_
    bstack1lll_opy_ = ord (bstack111_opy_ [-1])
    bstack1ll_opy_ = bstack111_opy_ [:-1]
    bstack1ll1_opy_ = bstack1lll_opy_ % len (bstack1ll_opy_)
    bstack11l_opy_ = bstack1ll_opy_ [:bstack1ll1_opy_] + bstack1ll_opy_ [bstack1ll1_opy_:]
    if bstack1l11_opy_:
        bstack1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1_opy_ - (bstackl_opy_ + bstack1lll_opy_) % bstack1l1_opy_) for bstackl_opy_, char in enumerate (bstack11l_opy_)])
    else:
        bstack1l1l_opy_ = str () .join ([chr (ord (char) - bstack1_opy_ - (bstackl_opy_ + bstack1lll_opy_) % bstack1l1_opy_) for bstackl_opy_, char in enumerate (bstack11l_opy_)])
    return eval (bstack1l1l_opy_)
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
from packaging import version
from browserstack.local import Local
bstack1l1ll_opy_ = {
	bstack11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫी"): bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸࠧु"),
  bstack11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧू"): bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡰ࡫ࡹࠨृ"),
  bstack11_opy_ (u"࠭࡯ࡴࠩॄ"): bstack11_opy_ (u"ࠧࡰࡵࠪॅ"),
  bstack11_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫॆ"): bstack11_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭े"),
  bstack11_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪै"): bstack11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫॉ"),
  bstack11_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪॊ"): bstack11_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࠧो"),
  bstack11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪौ"): bstack11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ्ࠧ"),
  bstack11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧॎ"): bstack11_opy_ (u"ࠪࡲࡦࡳࡥࠨॏ"),
  bstack11_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪॐ"): bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩࠪ॑"),
  bstack11_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶ॒ࠫ"): bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡶࡳࡱ࡫ࠧ॓"),
  bstack11_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭॔"): bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ॕ"),
  bstack11_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧॖ"): bstack11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧॗ"),
  bstack11_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫक़"): bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡼࡩࡥࡧࡲࠫख़"),
  bstack11_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭ग़"): bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭ज़"),
  bstack11_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩड़"): bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩढ़"),
  bstack11_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩफ़"): bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩय़"),
  bstack11_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨॠ"): bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨॡ"),
  bstack11_opy_ (u"ࠨࡴࡨࡷࡴࡲࡵࡵ࡫ࡲࡲࠬॢ"): bstack11_opy_ (u"ࠩࡵࡩࡸࡵ࡬ࡶࡶ࡬ࡳࡳ࠭ॣ"),
  bstack11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ।"): bstack11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭॥"),
  bstack11_opy_ (u"ࠬࡳࡡࡴ࡭ࡆࡳࡲࡳࡡ࡯ࡦࡶࠫ०"): bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡳࡡࡴ࡭ࡆࡳࡲࡳࡡ࡯ࡦࡶࠫ१"),
  bstack11_opy_ (u"ࠧࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬ२"): bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬ३"),
  bstack11_opy_ (u"ࠩࡰࡥࡸࡱࡂࡢࡵ࡬ࡧࡆࡻࡴࡩࠩ४"): bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡰࡥࡸࡱࡂࡢࡵ࡬ࡧࡆࡻࡴࡩࠩ५"),
  bstack11_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭६"): bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭७"),
  bstack11_opy_ (u"࠭ࡡࡶࡶࡲ࡛ࡦ࡯ࡴࠨ८"): bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡶࡶࡲ࡛ࡦ࡯ࡴࠨ९"),
  bstack11_opy_ (u"ࠨࡪࡲࡷࡹࡹࠧ॰"): bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡪࡲࡷࡹࡹࠧॱ"),
  bstack11_opy_ (u"ࠪࡦ࡫ࡩࡡࡤࡪࡨࠫॲ"): bstack11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦ࡫ࡩࡡࡤࡪࡨࠫॳ"),
  bstack11_opy_ (u"ࠬࡽࡳࡍࡱࡦࡥࡱ࡙ࡵࡱࡲࡲࡶࡹ࠭ॴ"): bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡽࡳࡍࡱࡦࡥࡱ࡙ࡵࡱࡲࡲࡶࡹ࠭ॵ"),
  bstack11_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡄࡱࡵࡷࡗ࡫ࡳࡵࡴ࡬ࡧࡹ࡯࡯࡯ࡵࠪॶ"): bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥ࡫ࡶࡥࡧࡲࡥࡄࡱࡵࡷࡗ࡫ࡳࡵࡴ࡬ࡧࡹ࡯࡯࡯ࡵࠪॷ"),
  bstack11_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ॸ"): bstack11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪॹ"),
  bstack11_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨॺ"): bstack11_opy_ (u"ࠬࡸࡥࡢ࡮ࡢࡱࡴࡨࡩ࡭ࡧࠪॻ"),
  bstack11_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ॼ"): bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡱࡲ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧॽ"),
  bstack11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡐࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬॾ"): bstack11_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡑࡵ࡭ࡪࡴࡴࡢࡶ࡬ࡳࡳ࠭ॿ"),
  bstack11_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪঀ"): bstack11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪঁ"),
  bstack11_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ং"): bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ঃ"),
  bstack11_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭঄"): bstack11_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࡴࠩঅ"),
  bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫআ"): bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫই"),
  bstack11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫঈ"): bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸࡵࡵࡳࡥࡨࠫউ"),
  bstack11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨঊ"): bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨঋ"),
  bstack11_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪঌ"): bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡪࡲࡷࡹࡔࡡ࡮ࡧࠪ঍"),
}
bstack11ll_opy_ = [
  bstack11_opy_ (u"ࠪࡳࡸ࠭঎"),
  bstack11_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧএ"),
  bstack11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧঐ"),
  bstack11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ঑"),
  bstack11_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ঒"),
  bstack11_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬও"),
  bstack11_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩঔ"),
]
bstack1ll11_opy_ = {
  bstack11_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ক"): bstack11_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨখ"),
  bstack11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧগ"): [bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨঘ"), bstack11_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪঙ")],
  bstack11_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭চ"): bstack11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧছ"),
  bstack11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧজ"): bstack11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫঝ"),
  bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪঞ"): [bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧট"), bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ঠ")],
  bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩড"): bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫঢ"),
  bstack11_opy_ (u"ࠪࡶࡪࡧ࡬ࡎࡱࡥ࡭ࡱ࡫ࠧণ"): bstack11_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡡࡰࡳࡧ࡯࡬ࡦࠩত"),
  bstack11_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬথ"): [bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡰࡱ࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭দ"), bstack11_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨধ")],
  bstack11_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࠧন"): [bstack11_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࡵࠪ঩"), bstack11_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࠪপ")]
}
bstack11l1_opy_ = {
  bstack11_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪফ"): [bstack11_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡘࡹ࡬ࡄࡧࡵࡸࡸ࠭ব"), bstack11_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹ࠭ভ")]
}
bstack1111_opy_ = [
  bstack11_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ম"),
  bstack11_opy_ (u"ࠨࡲࡤ࡫ࡪࡒ࡯ࡢࡦࡖࡸࡷࡧࡴࡦࡩࡼࠫয"),
  bstack11_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨর"),
  bstack11_opy_ (u"ࠪࡷࡪࡺࡗࡪࡰࡧࡳࡼࡘࡥࡤࡶࠪ঱"),
  bstack11_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࠭ল"),
  bstack11_opy_ (u"ࠬࡹࡴࡳ࡫ࡦࡸࡋ࡯࡬ࡦࡋࡱࡸࡪࡸࡡࡤࡶࡤࡦ࡮ࡲࡩࡵࡻࠪ঳"),
  bstack11_opy_ (u"࠭ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡒࡵࡳࡲࡶࡴࡃࡧ࡫ࡥࡻ࡯࡯ࡳࠩ঴"),
  bstack11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ঵"),
  bstack11_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭শ"),
  bstack11_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪষ"),
  bstack11_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩস"),
  bstack11_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬহ"),
]
bstack11l1l_opy_ = [
  bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ঺"),
  bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ঻"),
  bstack11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ়࠭"),
  bstack11_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨঽ"),
  bstack11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬা"),
  bstack11_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬি"),
  bstack11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧী"),
  bstack11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩু"),
  bstack11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩূ"),
]
bstack11ll1_opy_ = [
  bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫৃ"),
  bstack11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧৄ"),
]
bstack1l111_opy_ = bstack11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡻࡩ࠵ࡨࡶࡤࠪ৅")
bstack11111_opy_ = bstack11_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧ࠭৆")
bstack11l11_opy_ = {
  bstack11_opy_ (u"ࠫࡨࡸࡩࡵ࡫ࡦࡥࡱ࠭ে"): 50,
  bstack11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫৈ"): 40,
  bstack11_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧ৉"): 30,
  bstack11_opy_ (u"ࠧࡪࡰࡩࡳࠬ৊"): 20,
  bstack11_opy_ (u"ࠨࡦࡨࡦࡺ࡭ࠧো"): 10
}
DEFAULT_LOG_LEVEL = bstack11l11_opy_[bstack11_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧৌ")]
bstack1l1l1_opy_ = bstack11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰্ࠩ")
bstack1ll1l_opy_ = bstack11_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࠩৎ")
bstack1l11l_opy_ = [bstack11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭৏"), bstack11_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭৐")]
bstack1111l_opy_ = [bstack11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ৑"), bstack11_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ৒")]
bstack111l1_opy_ = [
  bstack11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡔࡡ࡮ࡧࠪ৓"),
  bstack11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ৔"),
  bstack11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ৕"),
  bstack11_opy_ (u"ࠬࡴࡥࡸࡅࡲࡱࡲࡧ࡮ࡥࡖ࡬ࡱࡪࡵࡵࡵࠩ৖"),
  bstack11_opy_ (u"࠭ࡡࡱࡲࠪৗ"),
  bstack11_opy_ (u"ࠧࡶࡦ࡬ࡨࠬ৘"),
  bstack11_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ৙"),
  bstack11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡦࠩ৚"),
  bstack11_opy_ (u"ࠪࡳࡷ࡯ࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨ৛"),
  bstack11_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡨࡦࡻ࡯ࡥࡸࠩড়"),
  bstack11_opy_ (u"ࠬࡴ࡯ࡓࡧࡶࡩࡹ࠭ঢ়"), bstack11_opy_ (u"࠭ࡦࡶ࡮࡯ࡖࡪࡹࡥࡵࠩ৞"),
  bstack11_opy_ (u"ࠧࡤ࡮ࡨࡥࡷ࡙ࡹࡴࡶࡨࡱࡋ࡯࡬ࡦࡵࠪয়"),
  bstack11_opy_ (u"ࠨࡧࡹࡩࡳࡺࡔࡪ࡯࡬ࡲ࡬ࡹࠧৠ"),
  bstack11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡒࡨࡶ࡫ࡵࡲ࡮ࡣࡱࡧࡪࡒ࡯ࡨࡩ࡬ࡲ࡬࠭ৡ"),
  bstack11_opy_ (u"ࠪࡳࡹ࡮ࡥࡳࡃࡳࡴࡸ࠭ৢ"),
  bstack11_opy_ (u"ࠫࡵࡸࡩ࡯ࡶࡓࡥ࡬࡫ࡓࡰࡷࡵࡧࡪࡕ࡮ࡇ࡫ࡱࡨࡋࡧࡩ࡭ࡷࡵࡩࠬৣ"),
  bstack11_opy_ (u"ࠬࡧࡰࡱࡃࡦࡸ࡮ࡼࡩࡵࡻࠪ৤"), bstack11_opy_ (u"࠭ࡡࡱࡲࡓࡥࡨࡱࡡࡨࡧࠪ৥"), bstack11_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡂࡥࡷ࡭ࡻ࡯ࡴࡺࠩ০"), bstack11_opy_ (u"ࠨࡣࡳࡴ࡜ࡧࡩࡵࡒࡤࡧࡰࡧࡧࡦࠩ১"), bstack11_opy_ (u"ࠩࡤࡴࡵ࡝ࡡࡪࡶࡇࡹࡷࡧࡴࡪࡱࡱࠫ২"),
  bstack11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨ৩"),
  bstack11_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡗࡩࡸࡺࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠨ৪"),
  bstack11_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡉ࡯ࡷࡧࡵࡥ࡬࡫ࠧ৫"), bstack11_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡃࡰࡸࡨࡶࡦ࡭ࡥࡆࡰࡧࡍࡳࡺࡥ࡯ࡶࠪ৬"),
  bstack11_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡅࡧࡹ࡭ࡨ࡫ࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬ৭"),
  bstack11_opy_ (u"ࠨࡣࡧࡦࡕࡵࡲࡵࠩ৮"),
  bstack11_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡇࡩࡻ࡯ࡣࡦࡕࡲࡧࡰ࡫ࡴࠨ৯"),
  bstack11_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡍࡳࡹࡴࡢ࡮࡯ࡘ࡮ࡳࡥࡰࡷࡷࠫৰ"),
  bstack11_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡎࡴࡳࡵࡣ࡯ࡰࡕࡧࡴࡩࠩৱ"),
  bstack11_opy_ (u"ࠬࡧࡶࡥࠩ৲"), bstack11_opy_ (u"࠭ࡡࡷࡦࡏࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩ৳"), bstack11_opy_ (u"ࠧࡢࡸࡧࡖࡪࡧࡤࡺࡖ࡬ࡱࡪࡵࡵࡵࠩ৴"), bstack11_opy_ (u"ࠨࡣࡹࡨࡆࡸࡧࡴࠩ৵"),
  bstack11_opy_ (u"ࠩࡸࡷࡪࡑࡥࡺࡵࡷࡳࡷ࡫ࠧ৶"), bstack11_opy_ (u"ࠪ࡯ࡪࡿࡳࡵࡱࡵࡩࡕࡧࡴࡩࠩ৷"), bstack11_opy_ (u"ࠫࡰ࡫ࡹࡴࡶࡲࡶࡪࡖࡡࡴࡵࡺࡳࡷࡪࠧ৸"),
  bstack11_opy_ (u"ࠬࡱࡥࡺࡃ࡯࡭ࡦࡹࠧ৹"), bstack11_opy_ (u"࠭࡫ࡦࡻࡓࡥࡸࡹࡷࡰࡴࡧࠫ৺"),
  bstack11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡋࡸࡦࡥࡸࡸࡦࡨ࡬ࡦࠩ৻"), bstack11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡁࡳࡩࡶࠫৼ"), bstack11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࡈ࡮ࡸࠧ৽"), bstack11_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡅ࡫ࡶࡴࡳࡥࡎࡣࡳࡴ࡮ࡴࡧࡇ࡫࡯ࡩࠬ৾"), bstack11_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡘࡷࡪ࡙ࡹࡴࡶࡨࡱࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࠨ৿"),
  bstack11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡔࡴࡸࡴࠨ਀"), bstack11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡕࡵࡲࡵࡵࠪਁ"),
  bstack11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡊࡩࡴࡣࡥࡰࡪࡈࡵࡪ࡮ࡧࡇ࡭࡫ࡣ࡬ࠩਂ"),
  bstack11_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡥࡣࡸ࡬ࡩࡼ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ਃ"),
  bstack11_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡃࡦࡸ࡮ࡵ࡮ࠨ਄"), bstack11_opy_ (u"ࠪ࡭ࡳࡺࡥ࡯ࡶࡆࡥࡹ࡫ࡧࡰࡴࡼࠫਅ"), bstack11_opy_ (u"ࠫ࡮ࡴࡴࡦࡰࡷࡊࡱࡧࡧࡴࠩਆ"), bstack11_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡦࡲࡉ࡯ࡶࡨࡲࡹࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨਇ"),
  bstack11_opy_ (u"࠭ࡤࡰࡰࡷࡗࡹࡵࡰࡂࡲࡳࡓࡳࡘࡥࡴࡧࡷࠫਈ"),
  bstack11_opy_ (u"ࠧࡶࡰ࡬ࡧࡴࡪࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩਉ"), bstack11_opy_ (u"ࠨࡴࡨࡷࡪࡺࡋࡦࡻࡥࡳࡦࡸࡤࠨਊ"),
  bstack11_opy_ (u"ࠩࡱࡳࡘ࡯ࡧ࡯ࠩ਋"),
  bstack11_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࡘࡲ࡮ࡳࡰࡰࡴࡷࡥࡳࡺࡖࡪࡧࡺࡷࠬ਌"),
  bstack11_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡴࡤࡳࡱ࡬ࡨ࡜ࡧࡴࡤࡪࡨࡶࡸ࠭਍"),
  bstack11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ਎"),
  bstack11_opy_ (u"࠭ࡲࡦࡥࡵࡩࡦࡺࡥࡄࡪࡵࡳࡲ࡫ࡄࡳ࡫ࡹࡩࡷ࡙ࡥࡴࡵ࡬ࡳࡳࡹࠧਏ"),
  bstack11_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡗࡦࡤࡖࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭ਐ"),
  bstack11_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡕࡧࡴࡩࠩ਑"),
  bstack11_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡖࡴࡪ࡫ࡤࠨ਒"),
  bstack11_opy_ (u"ࠪ࡫ࡵࡹࡅ࡯ࡣࡥࡰࡪࡪࠧਓ"),
  bstack11_opy_ (u"ࠫ࡮ࡹࡈࡦࡣࡧࡰࡪࡹࡳࠨਔ"),
  bstack11_opy_ (u"ࠬࡧࡤࡣࡇࡻࡩࡨ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ਕ"),
  bstack11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡪ࡙ࡣࡳ࡫ࡳࡸࠬਖ"),
  bstack11_opy_ (u"ࠧࡴ࡭࡬ࡴࡉ࡫ࡶࡪࡥࡨࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠫਗ"),
  bstack11_opy_ (u"ࠨࡣࡸࡸࡴࡍࡲࡢࡰࡷࡔࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠨਘ"),
  bstack11_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡑࡥࡹࡻࡲࡢ࡮ࡒࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧਙ"),
  bstack11_opy_ (u"ࠪࡷࡾࡹࡴࡦ࡯ࡓࡳࡷࡺࠧਚ"),
  bstack11_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡅࡩࡨࡈࡰࡵࡷࠫਛ"),
  bstack11_opy_ (u"ࠬࡹ࡫ࡪࡲࡘࡲࡱࡵࡣ࡬ࠩਜ"), bstack11_opy_ (u"࠭ࡵ࡯࡮ࡲࡧࡰ࡚ࡹࡱࡧࠪਝ"), bstack11_opy_ (u"ࠧࡶࡰ࡯ࡳࡨࡱࡋࡦࡻࠪਞ"),
  bstack11_opy_ (u"ࠨࡣࡸࡸࡴࡒࡡࡶࡰࡦ࡬ࠬਟ"),
  bstack11_opy_ (u"ࠩࡶ࡯࡮ࡶࡌࡰࡩࡦࡥࡹࡉࡡࡱࡶࡸࡶࡪ࠭ਠ"),
  bstack11_opy_ (u"ࠪࡹࡳ࡯࡮ࡴࡶࡤࡰࡱࡕࡴࡩࡧࡵࡔࡦࡩ࡫ࡢࡩࡨࡷࠬਡ"),
  bstack11_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩ࡜࡯࡮ࡥࡱࡺࡅࡳ࡯࡭ࡢࡶ࡬ࡳࡳ࠭ਢ"),
  bstack11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡘࡴࡵ࡬ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩਣ"),
  bstack11_opy_ (u"࠭ࡥ࡯ࡨࡲࡶࡨ࡫ࡁࡱࡲࡌࡲࡸࡺࡡ࡭࡮ࠪਤ"),
  bstack11_opy_ (u"ࠧࡦࡰࡶࡹࡷ࡫ࡗࡦࡤࡹ࡭ࡪࡽࡳࡉࡣࡹࡩࡕࡧࡧࡦࡵࠪਥ"), bstack11_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࡆࡨࡺࡹࡵ࡯࡭ࡵࡓࡳࡷࡺࠧਦ"), bstack11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦ࡙ࡨࡦࡻ࡯ࡥࡸࡆࡨࡸࡦ࡯࡬ࡴࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠬਧ"),
  bstack11_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡄࡴࡵࡹࡃࡢࡥ࡫ࡩࡑ࡯࡭ࡪࡶࠪਨ"),
  bstack11_opy_ (u"ࠫࡨࡧ࡬ࡦࡰࡧࡥࡷࡌ࡯ࡳ࡯ࡤࡸࠬ਩"),
  bstack11_opy_ (u"ࠬࡨࡵ࡯ࡦ࡯ࡩࡎࡪࠧਪ"),
  bstack11_opy_ (u"࠭࡬ࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭ਫ"),
  bstack11_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࡕࡨࡶࡻ࡯ࡣࡦࡵࡈࡲࡦࡨ࡬ࡦࡦࠪਬ"), bstack11_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࡖࡩࡷࡼࡩࡤࡧࡶࡅࡺࡺࡨࡰࡴ࡬ࡾࡪࡪࠧਭ"),
  bstack11_opy_ (u"ࠩࡤࡹࡹࡵࡁࡤࡥࡨࡴࡹࡇ࡬ࡦࡴࡷࡷࠬਮ"), bstack11_opy_ (u"ࠪࡥࡺࡺ࡯ࡅ࡫ࡶࡱ࡮ࡹࡳࡂ࡮ࡨࡶࡹࡹࠧਯ"),
  bstack11_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨࡍࡳࡹࡴࡳࡷࡰࡩࡳࡺࡳࡍ࡫ࡥࠫਰ"),
  bstack11_opy_ (u"ࠬࡴࡡࡵ࡫ࡹࡩ࡜࡫ࡢࡕࡣࡳࠫ਱"),
  bstack11_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡏ࡮ࡪࡶ࡬ࡥࡱ࡛ࡲ࡭ࠩਲ"), bstack11_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡁ࡭࡮ࡲࡻࡕࡵࡰࡶࡲࡶࠫਲ਼"), bstack11_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡊࡩࡱࡳࡷ࡫ࡆࡳࡣࡸࡨ࡜ࡧࡲ࡯࡫ࡱ࡫ࠬ਴"), bstack11_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡑࡳࡩࡳࡒࡩ࡯࡭ࡶࡍࡳࡈࡡࡤ࡭ࡪࡶࡴࡻ࡮ࡥࠩਵ"),
  bstack11_opy_ (u"ࠪ࡯ࡪ࡫ࡰࡌࡧࡼࡇ࡭ࡧࡩ࡯ࡵࠪਸ਼"),
  bstack11_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡾࡦࡨ࡬ࡦࡕࡷࡶ࡮ࡴࡧࡴࡆ࡬ࡶࠬ਷"),
  bstack11_opy_ (u"ࠬࡶࡲࡰࡥࡨࡷࡸࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨਸ"),
  bstack11_opy_ (u"࠭ࡩ࡯ࡶࡨࡶࡐ࡫ࡹࡅࡧ࡯ࡥࡾ࠭ਹ"),
  bstack11_opy_ (u"ࠧࡴࡪࡲࡻࡎࡕࡓࡍࡱࡪࠫ਺"),
  bstack11_opy_ (u"ࠨࡵࡨࡲࡩࡑࡥࡺࡕࡷࡶࡦࡺࡥࡨࡻࠪ਻"),
  bstack11_opy_ (u"ࠩࡺࡩࡧࡱࡩࡵࡔࡨࡷࡵࡵ࡮ࡴࡧࡗ࡭ࡲ࡫࡯ࡶࡶ਼ࠪ"), bstack11_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡗࡢ࡫ࡷࡘ࡮ࡳࡥࡰࡷࡷࠫ਽"),
  bstack11_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡈࡪࡨࡵࡨࡒࡵࡳࡽࡿࠧਾ"),
  bstack11_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡹࡹ࡯ࡥࡈࡼࡪࡩࡵࡵࡧࡉࡶࡴࡳࡈࡵࡶࡳࡷࠬਿ"),
  bstack11_opy_ (u"࠭ࡳ࡬࡫ࡳࡐࡴ࡭ࡃࡢࡲࡷࡹࡷ࡫ࠧੀ"),
  bstack11_opy_ (u"ࠧࡸࡧࡥ࡯࡮ࡺࡄࡦࡤࡸ࡫ࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧੁ"),
  bstack11_opy_ (u"ࠨࡨࡸࡰࡱࡉ࡯࡯ࡶࡨࡼࡹࡒࡩࡴࡶࠪੂ"),
  bstack11_opy_ (u"ࠩࡺࡥ࡮ࡺࡆࡰࡴࡄࡴࡵ࡙ࡣࡳ࡫ࡳࡸࠬ੃"),
  bstack11_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࡇࡴࡴ࡮ࡦࡥࡷࡖࡪࡺࡲࡪࡧࡶࠫ੄"),
  bstack11_opy_ (u"ࠫࡦࡶࡰࡏࡣࡰࡩࠬ੅"),
  bstack11_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡘ࡙ࡌࡄࡧࡵࡸࠬ੆"),
  bstack11_opy_ (u"࠭ࡴࡢࡲ࡚࡭ࡹ࡮ࡓࡩࡱࡵࡸࡕࡸࡥࡴࡵࡇࡹࡷࡧࡴࡪࡱࡱࠫੇ"),
  bstack11_opy_ (u"ࠧࡴࡥࡤࡰࡪࡌࡡࡤࡶࡲࡶࠬੈ"),
  bstack11_opy_ (u"ࠨࡹࡧࡥࡑࡵࡣࡢ࡮ࡓࡳࡷࡺࠧ੉"),
  bstack11_opy_ (u"ࠩࡶ࡬ࡴࡽࡘࡤࡱࡧࡩࡑࡵࡧࠨ੊"),
  bstack11_opy_ (u"ࠪ࡭ࡴࡹࡉ࡯ࡵࡷࡥࡱࡲࡐࡢࡷࡶࡩࠬੋ"),
  bstack11_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡆࡳࡳ࡬ࡩࡨࡈ࡬ࡰࡪ࠭ੌ"),
  bstack11_opy_ (u"ࠬࡱࡥࡺࡥ࡫ࡥ࡮ࡴࡐࡢࡵࡶࡻࡴࡸࡤࠨ੍"),
  bstack11_opy_ (u"࠭ࡵࡴࡧࡓࡶࡪࡨࡵࡪ࡮ࡷ࡛ࡉࡇࠧ੎"),
  bstack11_opy_ (u"ࠧࡱࡴࡨࡺࡪࡴࡴࡘࡆࡄࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠨ੏"),
  bstack11_opy_ (u"ࠨࡹࡨࡦࡉࡸࡩࡷࡧࡵࡅ࡬࡫࡮ࡵࡗࡵࡰࠬ੐"),
  bstack11_opy_ (u"ࠩ࡮ࡩࡾࡩࡨࡢ࡫ࡱࡔࡦࡺࡨࠨੑ"),
  bstack11_opy_ (u"ࠪࡹࡸ࡫ࡎࡦࡹ࡚ࡈࡆ࠭੒"),
  bstack11_opy_ (u"ࠫࡼࡪࡡࡍࡣࡸࡲࡨ࡮ࡔࡪ࡯ࡨࡳࡺࡺࠧ੓"), bstack11_opy_ (u"ࠬࡽࡤࡢࡅࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲ࡙࡯࡭ࡦࡱࡸࡸࠬ੔"),
  bstack11_opy_ (u"࠭ࡸࡤࡱࡧࡩࡔࡸࡧࡊࡦࠪ੕"), bstack11_opy_ (u"ࠧࡹࡥࡲࡨࡪ࡙ࡩࡨࡰ࡬ࡲ࡬ࡏࡤࠨ੖"),
  bstack11_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡥ࡙ࡇࡅࡇࡻ࡮ࡥ࡮ࡨࡍࡩ࠭੗"),
  bstack11_opy_ (u"ࠩࡵࡩࡸ࡫ࡴࡐࡰࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡸࡴࡐࡰ࡯ࡽࠬ੘"),
  bstack11_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡘ࡮ࡳࡥࡰࡷࡷࡷࠬਖ਼"),
  bstack11_opy_ (u"ࠫࡼࡪࡡࡔࡶࡤࡶࡹࡻࡰࡓࡧࡷࡶ࡮࡫ࡳࠨਗ਼"), bstack11_opy_ (u"ࠬࡽࡤࡢࡕࡷࡥࡷࡺࡵࡱࡔࡨࡸࡷࡿࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠨਜ਼"),
  bstack11_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࡈࡢࡴࡧࡻࡦࡸࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩੜ"),
  bstack11_opy_ (u"ࠧ࡮ࡣࡻࡘࡾࡶࡩ࡯ࡩࡉࡶࡪࡷࡵࡦࡰࡦࡽࠬ੝"),
  bstack11_opy_ (u"ࠨࡵ࡬ࡱࡵࡲࡥࡊࡵ࡙࡭ࡸ࡯ࡢ࡭ࡧࡆ࡬ࡪࡩ࡫ࠨਫ਼"),
  bstack11_opy_ (u"ࠩࡸࡷࡪࡉࡡࡳࡶ࡫ࡥ࡬࡫ࡓࡴ࡮ࠪ੟"),
  bstack11_opy_ (u"ࠪࡷ࡭ࡵࡵ࡭ࡦࡘࡷࡪ࡙ࡩ࡯ࡩ࡯ࡩࡹࡵ࡮ࡕࡧࡶࡸࡒࡧ࡮ࡢࡩࡨࡶࠬ੠"),
  bstack11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡌ࡛ࡉࡖࠧ੡"),
  bstack11_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡘࡴࡻࡣࡩࡋࡧࡉࡳࡸ࡯࡭࡮ࠪ੢"),
  bstack11_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪࡎࡩࡥࡦࡨࡲࡆࡶࡩࡑࡱ࡯࡭ࡨࡿࡅࡳࡴࡲࡶࠬ੣"),
  bstack11_opy_ (u"ࠧ࡮ࡱࡦ࡯ࡑࡵࡣࡢࡶ࡬ࡳࡳࡇࡰࡱࠩ੤"),
  bstack11_opy_ (u"ࠨ࡮ࡲ࡫ࡨࡧࡴࡇࡱࡵࡱࡦࡺࠧ੥"), bstack11_opy_ (u"ࠩ࡯ࡳ࡬ࡩࡡࡵࡈ࡬ࡰࡹ࡫ࡲࡔࡲࡨࡧࡸ࠭੦"),
  bstack11_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡆࡨࡰࡦࡿࡁࡥࡤࠪ੧")
]
bstack1lll1_opy_ = bstack11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡹࡵࡲ࡯ࡢࡦࠪ੨")
bstack11lll_opy_ = [bstack11_opy_ (u"ࠬ࠴ࡡࡱ࡭ࠪ੩"), bstack11_opy_ (u"࠭࠮ࡢࡣࡥࠫ੪"), bstack11_opy_ (u"ࠧ࠯࡫ࡳࡥࠬ੫")]
bstack1llll_opy_ = [bstack11_opy_ (u"ࠨ࡫ࡧࠫ੬"), bstack11_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ੭"), bstack11_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭੮"), bstack11_opy_ (u"ࠫࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦࠪ੯")]
bstack111ll_opy_ = {
  bstack11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬੰ"): bstack11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫੱ"),
  bstack11_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨੲ"): bstack11_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ੳ"),
  bstack11_opy_ (u"ࠩࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧੴ"): bstack11_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫੵ"),
  bstack11_opy_ (u"ࠫ࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ੶"): bstack11_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ੷"),
  bstack11_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡕࡰࡵ࡫ࡲࡲࡸ࠭੸"): bstack11_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ੹")
}
bstack111l_opy_ = [
  bstack11_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭੺"),
  bstack11_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ੻"),
  bstack11_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ੼"),
  bstack11_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ੽"),
  bstack11_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭੾"),
]
bstack111l111_opy_ = bstack11_opy_ (u"࠭ࡓࡦࡶࡷ࡭ࡳ࡭ࠠࡶࡲࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠼ࠣࡿࢂ࠭੿")
bstack1l1ll1l_opy_ = bstack11_opy_ (u"ࠧࡄࡱࡰࡴࡱ࡫ࡴࡦࡦࠣࡷࡪࡺࡵࡱࠣࠪ઀")
bstack1l1lllll_opy_ = bstack11_opy_ (u"ࠨࡒࡤࡶࡸ࡫ࡤࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪઁ")
bstack11111l1_opy_ = bstack11_opy_ (u"ࠩࡘࡷ࡮ࡴࡧࠡࡪࡸࡦࠥࡻࡲ࡭࠼ࠣࡿࢂ࠭ં")
bstack111lll_opy_ = bstack11_opy_ (u"ࠪࡗࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࡼࡿࠪઃ")
bstack1ll11l1l_opy_ = bstack11_opy_ (u"ࠫࡗ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡩ࡯ࡶࡨࡶࡷࡻࡰࡵ࠮ࠣࡩࡽ࡯ࡴࡪࡰࡪࠫ઄")
bstack1ll1ll1l_opy_ = bstack11_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡶࡲࠤࡷࡻ࡮ࠡࡶࡨࡷࡹࡹ࠮ࠡࡢࡳ࡭ࡵࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡢࠪઅ")
bstack11ll11_opy_ = bstack11_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡳࡱࡥࡳࡹ࠲ࠠࡱࡣࡥࡳࡹࠦࡡ࡯ࡦࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࡱ࡯ࡢࡳࡣࡵࡽࠥࡶࡡࡤ࡭ࡤ࡫ࡪࡹࠠࡵࡱࠣࡶࡺࡴࠠࡳࡱࡥࡳࡹࠦࡴࡦࡵࡷࡷࠥ࡯࡮ࠡࡲࡤࡶࡦࡲ࡬ࡦ࡮࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡶࡴࡨ࡯ࡵࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤࡷࡵࡢࡰࡶࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠲ࡶࡡࡣࡱࡷࠤࡷࡵࡢࡰࡶࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠲ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡬ࡪࡤࡵࡥࡷࡿࡠࠨઆ")
bstack1llll1ll_opy_ = bstack11_opy_ (u"ࠧࡉࡣࡱࡨࡱ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡱࡵࡳࡦࠩઇ")
bstack11l1111l_opy_ = bstack11_opy_ (u"ࠨࡃ࡯ࡰࠥࡪ࡯࡯ࡧࠤࠫઈ")
bstack1llllll1_opy_ = bstack11_opy_ (u"ࠩࡆࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴࠡࡣࡷࠤࠧࢁࡽࠣ࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡩ࡬ࡶࡦࡨࠤࡦࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠢࡩ࡭ࡱ࡫ࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡩࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡪࡴࡸࠠࡵࡧࡶࡸࡸ࠴ࠧઉ")
bstack11l11l1l_opy_ = bstack11_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡶࡪࡪࡥ࡯ࡶ࡬ࡥࡱࡹࠠ࡯ࡱࡷࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡢࡦࡧࠤࡹ࡮ࡥ࡮ࠢ࡬ࡲࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࠦࡡࡴࠢࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧࠦࡡ࡯ࡦࠣࠦࡦࡩࡣࡦࡵࡶࡏࡪࡿࠢࠡࡱࡵࠤࡸ࡫ࡴࠡࡶ࡫ࡩࡲࠦࡡࡴࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺࠠࡷࡣࡵ࡭ࡦࡨ࡬ࡦࡵ࠽ࠤࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨࠠࡢࡰࡧࠤࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠣࠩઊ")
bstack11l11ll1_opy_ = bstack11_opy_ (u"ࠫࡒࡧ࡬ࡧࡱࡵࡱࡪࡪࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠿ࠨࡻࡾࠤࠪઋ")
bstack11l1l1l1_opy_ = bstack11_opy_ (u"ࠬࡋ࡮ࡤࡱࡸࡲࡹ࡫ࡲࡦࡦࠣࡩࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡸࡴࠥ࠳ࠠࡼࡿࠪઌ")
bstack1l1lll11_opy_ = bstack11_opy_ (u"࠭ࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱ࠭ઍ")
bstack1lllll1_opy_ = bstack11_opy_ (u"ࠧࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡎࡲࡧࡦࡲࠧ઎")
bstack1lll1l11_opy_ = bstack11_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱࠦࡩࡴࠢࡱࡳࡼࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠡࠨએ")
bstack111llll1_opy_ = bstack11_opy_ (u"ࠩࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡹࡴࡢࡴࡷࠤࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡐࡴࡩࡡ࡭࠼ࠣࡿࢂ࠭ઐ")
bstack11llllll_opy_ = bstack11_opy_ (u"ࠪࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡲ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡼ࡯ࡴࡩࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࢀࢃࠧઑ")
bstack11l1l1ll_opy_ = bstack11_opy_ (u"࡚ࠫࡶࡤࡢࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠬ઒")
bstack1l11111_opy_ = bstack11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡷࡳࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀࠫઓ")
bstack111l1l_opy_ = bstack11_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡰࡳࡱࡹ࡭ࡩ࡫ࠠࡢࡰࠣࡥࡵࡶࡲࡰࡲࡵ࡭ࡦࡺࡥࠡࡈ࡚ࠤ࠭ࡸ࡯ࡣࡱࡷ࠳ࡵࡧࡢࡰࡶࠬࠤ࡮ࡴࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠱ࠦࡳ࡬࡫ࡳࠤࡹ࡮ࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤࡰ࡫ࡹࠡ࡫ࡱࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡮࡬ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡵ࡬ࡱࡵࡲࡥࠡࡲࡼࡸ࡭ࡵ࡮ࠡࡵࡦࡶ࡮ࡶࡴࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡤࡲࡾࠦࡆࡘ࠰ࠪઔ")
bstack1ll11111_opy_ = bstack11_opy_ (u"ࠧࡔࡧࡷࡸ࡮ࡴࡧࠡࡪࡷࡸࡵࡖࡲࡰࡺࡼ࠳࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠡ࡫ࡶࠤࡳࡵࡴࠡࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡴࡴࠠࡤࡷࡵࡶࡪࡴࡴ࡭ࡻࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡰࡨࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࠥ࠮ࡻࡾࠫ࠯ࠤࡵࡲࡥࡢࡵࡨࠤࡺࡶࡧࡳࡣࡧࡩࠥࡺ࡯ࠡࡕࡨࡰࡪࡴࡩࡶ࡯ࡁࡁ࠹࠴࠰࠯࠲ࠣࡳࡷࠦࡲࡦࡨࡨࡶࠥࡺ࡯ࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡶࡩࡱ࡫࡮ࡪࡷࡰ࠳ࡷࡻ࡮࠮ࡶࡨࡷࡹࡹ࠭ࡣࡧ࡫࡭ࡳࡪ࠭ࡱࡴࡲࡼࡾࠩࡰࡺࡶ࡫ࡳࡳࠦࡦࡰࡴࠣࡥࠥࡽ࡯ࡳ࡭ࡤࡶࡴࡻ࡮ࡥ࠰ࠪક")
bstack1ll1ll11_opy_ = bstack11_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴࠮ࠨખ")
bstack111l1l1l_opy_ = bstack11_opy_ (u"ࠩࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡩࡨࡲࡪࡸࡡࡵࡧࡧࠤࡹ࡮ࡥࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠧࠧગ")
bstack11lll1ll_opy_ = bstack11_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡶ࡫ࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫࡯࡬ࡦ࠰ࠣࡿࢂ࠭ઘ")
bstack1lllllll_opy_ = bstack11_opy_ (u"ࠫࡊࡾࡰࡦࡥࡷࡩࡩࠦࡡࡵࠢ࡯ࡩࡦࡹࡴࠡ࠳ࠣ࡭ࡳࡶࡵࡵ࠮ࠣࡶࡪࡩࡥࡪࡸࡨࡨࠥ࠶ࠧઙ")
bstack1lll1l_opy_ = bstack11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡩࡻࡲࡪࡰࡪࠤࡆࡶࡰࠡࡷࡳࡰࡴࡧࡤ࠯ࠢࡾࢁࠬચ")
bstack11lll11_opy_ = bstack11_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡸࡴࡱࡵࡡࡥࠢࡄࡴࡵ࠴ࠠࡊࡰࡹࡥࡱ࡯ࡤࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫ࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡻࡾ࠰ࠪછ")
bstack11l1l11l_opy_ = bstack11_opy_ (u"ࠧࡌࡧࡼࡷࠥࡩࡡ࡯ࡰࡲࡸࠥࡩ࡯࠮ࡧࡻ࡭ࡸࡺࠠࡢࡵࠣࡥࡵࡶࠠࡷࡣ࡯ࡹࡪࡹࠬࠡࡷࡶࡩࠥࡧ࡮ࡺࠢࡲࡲࡪࠦࡰࡳࡱࡳࡩࡷࡺࡹࠡࡨࡵࡳࡲࠦࡻࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡶࡡࡵࡪ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡩࡵࡴࡶࡲࡱࡤ࡯ࡤ࠽ࡵࡷࡶ࡮ࡴࡧ࠿࠮ࠣࡷ࡭ࡧࡲࡦࡣࡥࡰࡪࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀࢀ࠰ࠥࡵ࡮࡭ࡻࠣࠦࡵࡧࡴࡩࠤࠣࡥࡳࡪࠠࠣࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠦࠥࡩࡡ࡯ࠢࡦࡳ࠲࡫ࡸࡪࡵࡷࠤࡹࡵࡧࡦࡶ࡫ࡩࡷ࠴ࠧજ")
bstack1111l1_opy_ = bstack11_opy_ (u"ࠨ࡝ࡌࡲࡻࡧ࡬ࡪࡦࠣࡥࡵࡶࠠࡱࡴࡲࡴࡪࡸࡴࡺ࡟ࠣࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠣࡥࡷ࡫ࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠳ࠦࡆࡰࡴࠣࡱࡴࡸࡥࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡳࡰࡪࡧࡳࡦࠢࡹ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱࡲ࡬ࡹࡲ࠵ࡳࡦࡶ࠰ࡹࡵ࠳ࡴࡦࡵࡷࡷ࠴ࡹࡰࡦࡥ࡬ࡪࡾ࠳ࡡࡱࡲࠪઝ")
bstack11lll111_opy_ = bstack11_opy_ (u"ࠩ࡞ࡍࡳࡼࡡ࡭࡫ࡧࠤࡦࡶࡰࠡࡲࡵࡳࡵ࡫ࡲࡵࡻࡠࠤࡘࡻࡰࡱࡱࡵࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࡹࠠࡰࡨࠣࡥࡵࡶࠠࡢࡴࡨࠤࡴ࡬ࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠳ࠦࡆࡰࡴࠣࡱࡴࡸࡥࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡳࡰࡪࡧࡳࡦࠢࡹ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱࡲ࡬ࡹࡲ࠵ࡳࡦࡶ࠰ࡹࡵ࠳ࡴࡦࡵࡷࡷ࠴ࡹࡰࡦࡥ࡬ࡪࡾ࠳ࡡࡱࡲࠪઞ")
bstack1l1l1l_opy_ = bstack11_opy_ (u"࡙ࠪࡸ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡦࡶࡰࠡ࡫ࡧࠤࢀࢃࠠࡧࡱࡵࠤ࡭ࡧࡳࡩࠢ࠽ࠤࢀࢃ࠮ࠨટ")
bstack1l111ll_opy_ = bstack11_opy_ (u"ࠫࡆࡶࡰࠡࡗࡳࡰࡴࡧࡤࡦࡦࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠣࡍࡉࠦ࠺ࠡࡽࢀࠫઠ")
bstack11lll1_opy_ = bstack11_opy_ (u"࡛ࠬࡳࡪࡰࡪࠤࡆࡶࡰࠡ࠼ࠣࡿࢂ࠴ࠧડ")
bstack111ll1ll_opy_ = bstack11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲࠦࡩࡴࠢࡱࡳࡹࠦࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡩࡳࡷࠦࡶࡢࡰ࡬ࡰࡱࡧࠠࡱࡻࡷ࡬ࡴࡴࠠࡵࡧࡶࡸࡸ࠲ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡰࡢࡴࡤࡰࡱ࡫࡬ࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠥࡃࠠ࠲ࠩઢ")
bstack1l1l1111_opy_ = bstack11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡀࠠࡼࡿࠪણ")
from ._version import __version__
bstack1lllll1l_opy_ = None
CONFIG = {}
bstack1111111_opy_ = None
bstack1111l1l_opy_ = None
bstack11l1l111_opy_ = None
bstack111ll1l_opy_ = -1
bstack11llll1l_opy_ = DEFAULT_LOG_LEVEL
bstack1l11ll1_opy_ = 1
bstack11ll1l1l_opy_ = False
bstack1lllll11_opy_ = bstack11_opy_ (u"ࠨࠩત")
bstack1ll11l11_opy_ = bstack11_opy_ (u"ࠩࠪથ")
bstack11l11l1_opy_ = False
bstack1l1lll_opy_ = None
bstack111ll1l1_opy_ = None
bstack11ll11ll_opy_ = None
bstack11l1l11_opy_ = None
bstack1l1lll1_opy_ = None
bstack1ll111_opy_ = None
bstack1lll11l_opy_ = None
bstack1ll1l1_opy_ = None
bstack1lllll_opy_ = None
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack11llll1l_opy_,
                    format=bstack11_opy_ (u"ࠪࡠࡳࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨદ"),
                    datefmt=bstack11_opy_ (u"ࠫࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ધ"))
def bstack111111l_opy_():
  global CONFIG
  global bstack11llll1l_opy_
  if bstack11_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧન") in CONFIG:
    bstack11llll1l_opy_ = bstack11l11_opy_[CONFIG[bstack11_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨ઩")]]
    logging.getLogger().setLevel(bstack11llll1l_opy_)
def bstack1ll1ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11ll1lll_opy_():
  bstack1ll11lll_opy_ = bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪપ")
  bstack1llll1_opy_ = os.path.abspath(bstack1ll11lll_opy_)
  if not os.path.exists(bstack1llll1_opy_):
    bstack1ll11lll_opy_ = bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺࡣࡰࡰࠬફ")
    bstack1llll1_opy_ = os.path.abspath(bstack1ll11lll_opy_)
    if not os.path.exists(bstack1llll1_opy_):
      bstack1lll1ll1_opy_(
        bstack1llllll1_opy_.format(os.getcwd()))
  with open(bstack1llll1_opy_, bstack11_opy_ (u"ࠩࡵࠫબ")) as stream:
    try:
      config = yaml.safe_load(stream)
      return config
    except yaml.YAMLError as exc:
      bstack1lll1ll1_opy_(bstack11l11ll1_opy_.format(str(exc)))
def bstack111l1lll_opy_(config):
  bstack1l11ll_opy_ = config.keys()
  bstack1lll11ll_opy_ = []
  if bstack11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ભ") in config:
    bstack1lll11ll_opy_ = config[bstack11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧમ")]
  for bstack1ll1l111_opy_, bstack1ll1l1ll_opy_ in bstack1l1ll_opy_.items():
    if bstack1ll1l1ll_opy_ in bstack1l11ll_opy_:
      config[bstack1ll1l111_opy_] = config[bstack1ll1l1ll_opy_]
      del config[bstack1ll1l1ll_opy_]
  for bstack1ll1l111_opy_, bstack1ll1l1ll_opy_ in bstack1ll11_opy_.items():
    for platform in bstack1lll11ll_opy_:
      if isinstance(bstack1ll1l1ll_opy_, list):
        for bstack1l1l111_opy_ in bstack1ll1l1ll_opy_:
          if bstack1l1l111_opy_ in platform:
            platform[bstack1ll1l111_opy_] = platform[bstack1l1l111_opy_]
            del platform[bstack1l1l111_opy_]
            break
      elif bstack1ll1l1ll_opy_ in platform:
        platform[bstack1ll1l111_opy_] = platform[bstack1ll1l1ll_opy_]
        del platform[bstack1ll1l1ll_opy_]
  for bstack1ll1l111_opy_, bstack1ll1l1ll_opy_ in bstack11l1_opy_.items():
    for bstack1l1l111_opy_ in bstack1ll1l1ll_opy_:
      if bstack1l1l111_opy_ in bstack1l11ll_opy_:
        config[bstack1ll1l111_opy_] = config[bstack1l1l111_opy_]
        del config[bstack1l1l111_opy_]
  for bstack1l1l111_opy_ in list(config):
    for bstack111lllll_opy_ in bstack11ll1_opy_:
      if bstack1l1l111_opy_.lower() == bstack111lllll_opy_.lower() and bstack1l1l111_opy_ != bstack111lllll_opy_:
        config[bstack111lllll_opy_] = config[bstack1l1l111_opy_]
        del config[bstack1l1l111_opy_]
  for bstack1l1ll11l_opy_ in bstack111ll_opy_:
    if bstack1l1ll11l_opy_ in config:
      if not bstack111ll_opy_[bstack1l1ll11l_opy_] in config:
        config[bstack111ll_opy_[bstack1l1ll11l_opy_]] = {}
      config[bstack111ll_opy_[bstack1l1ll11l_opy_]].update(config[bstack1l1ll11l_opy_])
      del config[bstack1l1ll11l_opy_]
  return config
def bstack11111ll_opy_(config):
  global bstack1ll11l11_opy_
  if bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩય") in config and str(config[bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪર")]).lower() != bstack11_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭઱"):
    if not bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬલ") in config:
      config[bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ળ")] = {}
    if not bstack11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴") in config[bstack11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨવ")]:
      if bstack11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧશ") in os.environ:
        config[bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪષ")][bstack11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩસ")] = os.environ[bstack11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪહ")]
      else:
        current_time = datetime.datetime.now()
        bstack1l11ll1l_opy_ = current_time.strftime(bstack11_opy_ (u"ࠩࠨࡨࡤࠫࡢࡠࠧࡋࠩࡒ࠭઺"))
        hostname = socket.gethostname()
        bstack1l1l1l11_opy_ = bstack11_opy_ (u"ࠪࠫ઻").join(random.choices(string.ascii_lowercase + string.digits, k=4))
        identifier = bstack11_opy_ (u"ࠫࢀࢃ࡟ࡼࡿࡢࡿࢂ઼࠭").format(bstack1l11ll1l_opy_, hostname, bstack1l1l1l11_opy_)
        config[bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઽ")][bstack11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨા")] = identifier
    bstack1ll11l11_opy_ = config[bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫિ")][bstack11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪી")]
  return config
def bstack1lll1lll_opy_(config):
  if bstack11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬુ") in config and config[bstack11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ૂ")] not in bstack1111l_opy_:
    return config[bstack11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧૃ")]
  elif bstack11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨૄ") in os.environ:
    return os.environ[bstack11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩૅ")]
  else:
    return None
def bstack111ll111_opy_(config):
  if bstack11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ૆") in config:
    return config[bstack11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫે")]
  elif bstack11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡏࡃࡐࡉࠬૈ") in os.environ:
    return os.environ[bstack11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡐࡄࡑࡊ࠭ૉ")]
  else:
    return None
def bstack11l1llll_opy_():
  if (
    isinstance(os.getenv(bstack11_opy_ (u"ࠫࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠩ૊")), str) and len(os.getenv(bstack11_opy_ (u"ࠬࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠪો"))) > 0
  ) or (
    isinstance(os.getenv(bstack11_opy_ (u"࠭ࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠬૌ")), str) and len(os.getenv(bstack11_opy_ (u"ࠧࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊ્࠭"))) > 0
  ):
    return os.getenv(bstack11_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠧ૎"), 0)
  if str(os.getenv(bstack11_opy_ (u"ࠩࡆࡍࠬ૏"))).lower() == bstack11_opy_ (u"ࠪࡸࡷࡻࡥࠨૐ") and str(os.getenv(bstack11_opy_ (u"ࠫࡈࡏࡒࡄࡎࡈࡇࡎ࠭૑"))).lower() == bstack11_opy_ (u"ࠬࡺࡲࡶࡧࠪ૒"):
    return os.getenv(bstack11_opy_ (u"࠭ࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࠩ૓"), 0)
  if str(os.getenv(bstack11_opy_ (u"ࠧࡄࡋࠪ૔"))).lower() == bstack11_opy_ (u"ࠨࡶࡵࡹࡪ࠭૕") and str(os.getenv(bstack11_opy_ (u"ࠩࡗࡖࡆ࡜ࡉࡔࠩ૖"))).lower() == bstack11_opy_ (u"ࠪࡸࡷࡻࡥࠨ૗"):
    return os.getenv(bstack11_opy_ (u"࡙ࠫࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠪ૘"), 0)
  if str(os.getenv(bstack11_opy_ (u"ࠬࡉࡉࠨ૙"))).lower() == bstack11_opy_ (u"࠭ࡴࡳࡷࡨࠫ૚") and str(os.getenv(bstack11_opy_ (u"ࠧࡄࡋࡢࡒࡆࡓࡅࠨ૛"))).lower() == bstack11_opy_ (u"ࠨࡥࡲࡨࡪࡹࡨࡪࡲࠪ૜"):
    return 0 # bstack1l1111_opy_ bstack11l111l_opy_ not set build number env
  if os.getenv(bstack11_opy_ (u"ࠩࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠬ૝")) and os.getenv(bstack11_opy_ (u"ࠪࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙࠭૞")):
    return os.getenv(bstack11_opy_ (u"ࠫࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗ࠭૟"), 0)
  if str(os.getenv(bstack11_opy_ (u"ࠬࡉࡉࠨૠ"))).lower() == bstack11_opy_ (u"࠭ࡴࡳࡷࡨࠫૡ") and str(os.getenv(bstack11_opy_ (u"ࠧࡅࡔࡒࡒࡊ࠭ૢ"))).lower() == bstack11_opy_ (u"ࠨࡶࡵࡹࡪ࠭ૣ"):
    return os.getenv(bstack11_opy_ (u"ࠩࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠧ૤"), 0)
  if str(os.getenv(bstack11_opy_ (u"ࠪࡇࡎ࠭૥"))).lower() == bstack11_opy_ (u"ࠫࡹࡸࡵࡦࠩ૦") and str(os.getenv(bstack11_opy_ (u"࡙ࠬࡅࡎࡃࡓࡌࡔࡘࡅࠨ૧"))).lower() == bstack11_opy_ (u"࠭ࡴࡳࡷࡨࠫ૨"):
    return os.getenv(bstack11_opy_ (u"ࠧࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡊࡆࠪ૩"), 0)
  if str(os.getenv(bstack11_opy_ (u"ࠨࡅࡌࠫ૪"))).lower() == bstack11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ૫") and str(os.getenv(bstack11_opy_ (u"ࠪࡋࡎ࡚ࡌࡂࡄࡢࡇࡎ࠭૬"))).lower() == bstack11_opy_ (u"ࠫࡹࡸࡵࡦࠩ૭"):
    return os.getenv(bstack11_opy_ (u"ࠬࡉࡉࡠࡌࡒࡆࡤࡏࡄࠨ૮"), 0)
  if str(os.getenv(bstack11_opy_ (u"࠭ࡃࡊࠩ૯"))).lower() == bstack11_opy_ (u"ࠧࡵࡴࡸࡩࠬ૰") and str(os.getenv(bstack11_opy_ (u"ࠨࡄࡘࡍࡑࡊࡋࡊࡖࡈࠫ૱"))).lower() == bstack11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ૲"):
    return os.getenv(bstack11_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠬ૳"), 0)
  if str(os.getenv(bstack11_opy_ (u"࡙ࠫࡌ࡟ࡃࡗࡌࡐࡉ࠭૴"))).lower() == bstack11_opy_ (u"ࠬࡺࡲࡶࡧࠪ૵"):
    return os.getenv(bstack11_opy_ (u"࠭ࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉ࠭૶"), 0)
  return -1
def bstack1llll1l_opy_(bstack1l11111l_opy_):
  global CONFIG
  if not bstack11_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ૷") in CONFIG[bstack11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૸")]:
    return
  CONFIG[bstack11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫૹ")] = CONFIG[bstack11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૺ")].replace(
    bstack11_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ૻ"),
    str(bstack1l11111l_opy_)
  )
def bstack11l11111_opy_():
  global CONFIG
  if not bstack11_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫૼ") in CONFIG[bstack11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૽")]:
    return
  current_time = datetime.datetime.now()
  bstack1l11ll1l_opy_ = current_time.strftime(bstack11_opy_ (u"ࠧࠦࡦ࠰ࠩࡧ࠳ࠥࡉ࠼ࠨࡑࠬ૾"))
  CONFIG[bstack11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૿")] = CONFIG[bstack11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ଀")].replace(
    bstack11_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩଁ"),
    bstack1l11ll1l_opy_
  )
def bstack1lll1111_opy_():
  global CONFIG
  if bstack11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ଂ") in CONFIG and not bool(CONFIG[bstack11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧଃ")]):
    return
  if not bstack11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ଄") in CONFIG:
    CONFIG[bstack11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩଅ")] = bstack11_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪଆ")
  if bstack11_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨଇ") in CONFIG[bstack11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬଈ")]:
    bstack11l11111_opy_()
    os.environ[bstack11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨଉ")] = CONFIG[bstack11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧଊ")]
  if not bstack11_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨଋ") in CONFIG[bstack11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩଌ")]:
    return
  bstack1l11111l_opy_ = bstack11_opy_ (u"ࠨࠩ଍")
  bstack1111lll_opy_ = bstack11l1llll_opy_()
  if bstack1111lll_opy_ != -1:
    bstack1l11111l_opy_ = bstack11_opy_ (u"ࠩࡆࡍࠥ࠭଎") + str(bstack1111lll_opy_)
  if bstack1l11111l_opy_ == bstack11_opy_ (u"ࠪࠫଏ"):
    bstack11l1111_opy_ = bstack1ll11ll1_opy_(CONFIG[bstack11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧଐ")])
    if bstack11l1111_opy_ != -1:
      bstack1l11111l_opy_ = str(bstack11l1111_opy_)
  if bstack1l11111l_opy_:
    bstack1llll1l_opy_(bstack1l11111l_opy_)
    os.environ[bstack11_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ଑")] = CONFIG[bstack11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ଒")]
def bstack1llll1l1_opy_(bstack1l1llll_opy_, bstack11lll11l_opy_, path):
  bstack11llll1_opy_ = {
    bstack11_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫଓ"): bstack11lll11l_opy_
  }
  if os.path.exists(path):
    bstack111l11_opy_ = json.load(open(path, bstack11_opy_ (u"ࠨࡴࡥࠫଔ")))
  else:
    bstack111l11_opy_ = {}
  bstack111l11_opy_[bstack1l1llll_opy_] = bstack11llll1_opy_
  with open(path, bstack11_opy_ (u"ࠤࡺ࠯ࠧକ")) as outfile:
    json.dump(bstack111l11_opy_, outfile)
def bstack1ll11ll1_opy_(bstack1l1llll_opy_):
  bstack1l1llll_opy_ = str(bstack1l1llll_opy_)
  bstack1l1ll11_opy_ = os.path.join(os.path.expanduser(bstack11_opy_ (u"ࠪࢂࠬଖ")), bstack11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫଗ"))
  try:
    if not os.path.exists(bstack1l1ll11_opy_):
      os.makedirs(bstack1l1ll11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11_opy_ (u"ࠬࢄࠧଘ")), bstack11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ଙ"), bstack11_opy_ (u"ࠧ࠯ࡤࡸ࡭ࡱࡪ࠭࡯ࡣࡰࡩ࠲ࡩࡡࡤࡪࡨ࠲࡯ࡹ࡯࡯ࠩଚ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11_opy_ (u"ࠨࡹࠪଛ")):
        pass
      with open(file_path, bstack11_opy_ (u"ࠤࡺ࠯ࠧଜ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11_opy_ (u"ࠪࡶࠬଝ")) as bstack1ll111l_opy_:
      bstack11lllll_opy_ = json.load(bstack1ll111l_opy_)
    if bstack1l1llll_opy_ in bstack11lllll_opy_:
      bstack1l1llll1_opy_ = bstack11lllll_opy_[bstack1l1llll_opy_][bstack11_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨଞ")]
      bstack1l111l11_opy_ = int(bstack1l1llll1_opy_) + 1
      bstack1llll1l1_opy_(bstack1l1llll_opy_, bstack1l111l11_opy_, file_path)
      return bstack1l111l11_opy_
    else:
      bstack1llll1l1_opy_(bstack1l1llll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l1l1111_opy_.format(str(e)))
    return -1
def bstack111llll_opy_(config):
  if bstack11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧଟ") in config and config[bstack11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨଠ")] not in bstack1l11l_opy_:
    return config[bstack11_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩଡ")]
  elif bstack11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩଢ") in os.environ:
    return os.environ[bstack11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪଣ")]
  else:
    return None
def bstack111lll1l_opy_(config):
  if not bstack111llll_opy_(config) or not bstack1lll1lll_opy_(config):
    return True
  else:
    return False
def bstack1ll1l1l_opy_(config):
  if bstack1ll1ll_opy_() < version.parse(bstack11_opy_ (u"ࠪ࠷࠳࠺࠮࠱ࠩତ")):
    return False
  if bstack1ll1ll_opy_() >= version.parse(bstack11_opy_ (u"ࠫ࠹࠴࠱࠯࠷ࠪଥ")):
    return True
  if bstack11_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬଦ") in config and config[bstack11_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ଧ")] == False:
    return False
  else:
    return True
def bstack11l1ll_opy_(config, index = 0):
  global bstack11l11l1_opy_
  bstack111l1ll_opy_ = {}
  caps = bstack11l1l_opy_ + bstack1111_opy_
  if bstack11l11l1_opy_:
    caps += bstack111l1_opy_
  if bstack11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪନ") in config:
    for bstack11l1ll1_opy_ in config[bstack11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ଩")][index]:
      if bstack11l1ll1_opy_ in caps + [bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧପ"), bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫଫ")]:
        continue
      bstack111l1ll_opy_[bstack11l1ll1_opy_] = config[bstack11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧବ")][index][bstack11l1ll1_opy_]
  for key in config:
    if key in caps + [bstack11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଭ")]:
      continue
    bstack111l1ll_opy_[key] = config[key]
  bstack111l1ll_opy_[bstack11_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨମ")] = socket.gethostname()
  return bstack111l1ll_opy_
def bstack1111l11_opy_(config):
  global bstack11l11l1_opy_
  bstack1l111l1l_opy_ = {}
  caps = bstack1111_opy_
  if bstack11l11l1_opy_:
    caps+= bstack111l1_opy_
  for key in caps:
    if key in config:
      bstack1l111l1l_opy_[key] = config[key]
  return bstack1l111l1l_opy_
def bstack1lll11_opy_(bstack111l1ll_opy_, bstack1l111l1l_opy_):
  bstack11111l_opy_ = {}
  for key in bstack111l1ll_opy_.keys():
    if key in bstack1l1ll_opy_:
      bstack11111l_opy_[bstack1l1ll_opy_[key]] = bstack111l1ll_opy_[key]
    else:
      bstack11111l_opy_[key] = bstack111l1ll_opy_[key]
  for key in bstack1l111l1l_opy_:
    if key in bstack1l1ll_opy_:
      bstack11111l_opy_[bstack1l1ll_opy_[key]] = bstack1l111l1l_opy_[key]
    else:
      bstack11111l_opy_[key] = bstack1l111l1l_opy_[key]
  return bstack11111l_opy_
def bstack1l1l1ll1_opy_(config, index = 0):
  global bstack11l11l1_opy_
  caps = {}
  bstack1l111l1l_opy_ = bstack1111l11_opy_(config)
  bstack1l1lll1l_opy_ = bstack1111_opy_
  if bstack11l11l1_opy_:
    bstack1l1lll1l_opy_ += bstack111l1_opy_
  if bstack11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଯ") in config:
    if bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ର") in config[bstack11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଱")][index]:
      caps[bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଲ")] = config[bstack11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଳ")][index][bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଴")]
    if bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧଵ") in config[bstack11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଶ")][index]:
      caps[bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଷ")] = str(config[bstack11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬସ")][index][bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫହ")])
    bstack1l1ll1l1_opy_ = {}
    for bstack11l1l1l_opy_ in bstack1l1lll1l_opy_:
      if bstack11l1l1l_opy_ in config[bstack11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ଺")][index]:
        if bstack11l1l1l_opy_ == bstack11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ଻"):
          bstack1l1ll1l1_opy_[bstack11l1l1l_opy_] = str(config[bstack11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴ଼ࠩ")][index][bstack11l1l1l_opy_] * 1.0)
        else:
          bstack1l1ll1l1_opy_[bstack11l1l1l_opy_] = config[bstack11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଽ")][index][bstack11l1l1l_opy_]
        del(config[bstack11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫା")][index][bstack11l1l1l_opy_])
    bstack1l111l1l_opy_.update(bstack1l1ll1l1_opy_)
  bstack111l1ll_opy_ = bstack11l1ll_opy_(config, index)
  if bstack1ll1l1l_opy_(config):
    bstack111l1ll_opy_[bstack11_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩି")] = True
    caps.update(bstack1l111l1l_opy_)
    caps[bstack11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫୀ")] = bstack111l1ll_opy_
  else:
    bstack111l1ll_opy_[bstack11_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫୁ")] = False
    caps.update(bstack1lll11_opy_(bstack111l1ll_opy_, bstack1l111l1l_opy_))
    if bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪୂ") in caps:
      caps[bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧୃ")] = caps[bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬୄ")]
      del(caps[bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୅")])
    if bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ୆") in caps:
      caps[bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬେ")] = caps[bstack11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬୈ")]
      del(caps[bstack11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭୉")])
  return caps
def bstack11ll1ll_opy_():
  if bstack1ll1ll_opy_() <= version.parse(bstack11_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭୊")):
    return bstack11111_opy_
  return bstack1l111_opy_
def bstack1ll1l1l1_opy_(options):
  return hasattr(options, bstack11_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨୋ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      d[k] = v
  return d
def bstack1l1l1ll_opy_(options, bstack1ll1llll_opy_):
  for bstack1l11ll11_opy_ in bstack1ll1llll_opy_:
    if bstack1l11ll11_opy_ in [bstack11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ୌ"), bstack11_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ୍࠭")]:
      next
    if bstack1l11ll11_opy_ in options._experimental_options:
      options._experimental_options[bstack1l11ll11_opy_]= update(options._experimental_options[bstack1l11ll11_opy_], bstack1ll1llll_opy_[bstack1l11ll11_opy_])
    else:
      options.add_experimental_option(bstack1l11ll11_opy_, bstack1ll1llll_opy_[bstack1l11ll11_opy_])
  if bstack11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ୎") in bstack1ll1llll_opy_:
    for arg in bstack1ll1llll_opy_[bstack11_opy_ (u"ࠫࡦࡸࡧࡴࠩ୏")]:
      options.add_argument(arg)
    del(bstack1ll1llll_opy_[bstack11_opy_ (u"ࠬࡧࡲࡨࡵࠪ୐")])
  if bstack11_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ୑") in bstack1ll1llll_opy_:
    for ext in bstack1ll1llll_opy_[bstack11_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ୒")]:
      options.add_extension(ext)
    del(bstack1ll1llll_opy_[bstack11_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ୓")])
def bstack11l11l11_opy_(options, bstack1l11l1_opy_):
  if bstack11_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ୔") in bstack1l11l1_opy_:
    for bstack11ll1l_opy_ in bstack1l11l1_opy_[bstack11_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ୕")]:
      if bstack11ll1l_opy_ in options._preferences:
        options._preferences[bstack11ll1l_opy_] = update(options._preferences[bstack11ll1l_opy_], bstack1l11l1_opy_[bstack11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪୖ")][bstack11ll1l_opy_])
      else:
        options.set_preference(bstack11ll1l_opy_, bstack1l11l1_opy_[bstack11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫୗ")][bstack11ll1l_opy_])
  if bstack11_opy_ (u"࠭ࡡࡳࡩࡶࠫ୘") in bstack1l11l1_opy_:
    for arg in bstack1l11l1_opy_[bstack11_opy_ (u"ࠧࡢࡴࡪࡷࠬ୙")]:
      options.add_argument(arg)
def bstack1l1ll1_opy_(options, bstack1llllll_opy_):
  if bstack11_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࠩ୚") in bstack1llllll_opy_:
    options.use_webview(bool(bstack1llllll_opy_[bstack11_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪ୛")]))
  bstack1l1l1ll_opy_(options, bstack1llllll_opy_)
def bstack1l11l11l_opy_(options, bstack11l11l_opy_):
  for bstack1l1l11ll_opy_ in bstack11l11l_opy_:
    if bstack1l1l11ll_opy_ in [bstack11_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଡ଼"), bstack11_opy_ (u"ࠫࡦࡸࡧࡴࠩଢ଼")]:
      next
    options.set_capability(bstack1l1l11ll_opy_, bstack11l11l_opy_[bstack1l1l11ll_opy_])
  if bstack11_opy_ (u"ࠬࡧࡲࡨࡵࠪ୞") in bstack11l11l_opy_:
    for arg in bstack11l11l_opy_[bstack11_opy_ (u"࠭ࡡࡳࡩࡶࠫୟ")]:
      options.add_argument(arg)
  if bstack11_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫୠ") in bstack11l11l_opy_:
    options.use_technology_preview(bool(bstack11l11l_opy_[bstack11_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬୡ")]))
def bstack1l11lll1_opy_(options, bstack1l1l111l_opy_):
  for bstack11ll1l1_opy_ in bstack1l1l111l_opy_:
    if bstack11ll1l1_opy_ in [bstack11_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ୢ"), bstack11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨୣ")]:
      next
    options._options[bstack11ll1l1_opy_] = bstack1l1l111l_opy_[bstack11ll1l1_opy_]
  if bstack11_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୤") in bstack1l1l111l_opy_:
    for bstack11l1l1_opy_ in bstack1l1l111l_opy_[bstack11_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୥")]:
      options.add_additional_option(
          bstack11l1l1_opy_, bstack1l1l111l_opy_[bstack11_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୦")][bstack11l1l1_opy_])
  if bstack11_opy_ (u"ࠧࡢࡴࡪࡷࠬ୧") in bstack1l1l111l_opy_:
    for arg in bstack1l1l111l_opy_[bstack11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭୨")]:
      options.add_argument(arg)
def bstack111lll1_opy_(options, caps):
  if options.KEY == bstack11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୩") and options.KEY in caps:
    bstack1l1l1ll_opy_(options, caps[bstack11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ୪")])
  elif options.KEY == bstack11_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୫") and options.KEY in caps:
    bstack11l11l11_opy_(options, caps[bstack11_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪ୬")])
  elif options.KEY == bstack11_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ୭") and options.KEY in caps:
    bstack1l11l11l_opy_(options, caps[bstack11_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ୮")])
  elif options.KEY == bstack11_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୯") and options.KEY in caps:
    bstack1l1ll1_opy_(options, caps[bstack11_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ୰")])
  elif options.KEY == bstack11_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩୱ") and options.KEY in caps:
    bstack1l11lll1_opy_(options, caps[bstack11_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ୲")])
def bstack1l1111l1_opy_(caps):
  browser = bstack11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ୳")
  if bstack11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ୴") in caps:
    browser = caps[bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ୵")]
  elif bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ୶") in caps:
    browser = caps[bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ୷")]
  browser = str(browser).lower()
  if browser == bstack11_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪ୸") or browser == bstack11_opy_ (u"ࠫ࡮ࡶࡡࡥࠩ୹"):
    browser = bstack11_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ୺")
  if browser == bstack11_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭ࠧ୻"):
    browser = bstack11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ୼")
  if browser not in [bstack11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ୽"), bstack11_opy_ (u"ࠩࡨࡨ࡬࡫ࠧ୾"), bstack11_opy_ (u"ࠪ࡭ࡪ࠭୿"), bstack11_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫ஀"), bstack11_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭஁")]:
    return None
  try:
    package = bstack11_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨஂ").format(browser)
    name = bstack11_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨஃ")
    browser_options = getattr(__import__(package, fromlist=[name]), name)
    options = browser_options()
    if not bstack1ll1l1l1_opy_(options):
      return None
    for bstack1l1l111_opy_ in caps.keys():
      options.set_capability(bstack1l1l111_opy_, caps[bstack1l1l111_opy_])
    bstack111lll1_opy_(options, caps)
    return options
  except Exception as e:
    logger.debug(str(e))
    return None
def bstack1l1l1l1l_opy_(options, bstack1lll1l1l_opy_):
  if not bstack1ll1l1l1_opy_(options):
    return
  for bstack1l1l111_opy_ in bstack1lll1l1l_opy_.keys():
    if bstack1l1l111_opy_ in bstack111l_opy_:
      next
    options.set_capability(bstack1l1l111_opy_, bstack1lll1l1l_opy_[bstack1l1l111_opy_])
  bstack111lll1_opy_(options, bstack1lll1l1l_opy_)
  if bstack11_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧ஄") in options._caps:
    if options._caps[bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧஅ")] and options._caps[bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨஆ")].lower() != bstack11_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬஇ"):
      del options._caps[bstack11_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫஈ")]
def bstack111l1ll1_opy_(proxy_config):
  if bstack11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪஉ") in proxy_config:
    proxy_config[bstack11_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩஊ")] = proxy_config[bstack11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ஋")]
    del(proxy_config[bstack11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭஌")])
  if bstack11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭஍") in proxy_config and proxy_config[bstack11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧஎ")].lower() != bstack11_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬஏ"):
    proxy_config[bstack11_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩஐ")] = bstack11_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧ஑")
  if bstack11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭ஒ") in proxy_config:
    proxy_config[bstack11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬஓ")] = bstack11_opy_ (u"ࠪࡴࡦࡩࠧஔ")
  return proxy_config
def bstack1l1111l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪக") in config:
    return proxy
  config[bstack11_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ஖")] = bstack111l1ll1_opy_(config[bstack11_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ஗")])
  if proxy == None:
    proxy = Proxy(config[bstack11_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭஘")])
  return proxy
def bstack1ll1ll1_opy_(self):
  global CONFIG
  global bstack1ll1l1_opy_
  if bstack11_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫங") in CONFIG and bstack11ll1ll_opy_().startswith(bstack11_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࠪச")):
    return CONFIG[bstack11_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭஛")]
  elif bstack11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨஜ") in CONFIG and bstack11ll1ll_opy_().startswith(bstack11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠧ஝")):
    return CONFIG[bstack11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪஞ")]
  else:
    return bstack1ll1l1_opy_(self)
def bstack1l111111_opy_():
  if bstack1ll1ll_opy_() < version.parse(bstack11_opy_ (u"ࠧ࠵࠰࠳࠲࠵࠭ட")):
    logger.warning(bstack1ll11111_opy_.format(bstack1ll1ll_opy_()))
    return
  global bstack1ll1l1_opy_
  from selenium.webdriver.remote.remote_connection import RemoteConnection
  bstack1ll1l1_opy_ = RemoteConnection._get_proxy_url
  RemoteConnection._get_proxy_url = bstack1ll1ll1_opy_
def bstack1l11l1l1_opy_(config):
  if bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ஠") in config:
    if str(config[bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭஡")]).lower() == bstack11_opy_ (u"ࠪࡸࡷࡻࡥࠨ஢"):
      return True
    else:
      return False
  elif bstack11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࠩண") in os.environ:
    if str(os.environ[bstack11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࠪத")]).lower() == bstack11_opy_ (u"࠭ࡴࡳࡷࡨࠫ஥"):
      return True
    else:
      return False
  else:
    return False
def bstack1l11l1l_opy_(config):
  if bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ஦") in config:
    return config[bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ஧")]
  if bstack11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨந") in config:
    return config[bstack11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩன")]
  return {}
def bstack1l11l11_opy_(caps):
  global bstack1ll11l11_opy_
  if bstack11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬப") in caps:
    caps[bstack11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭஫")][bstack11_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ஬")] = True
    if bstack1ll11l11_opy_:
      caps[bstack11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ஭")][bstack11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪம")] = bstack1ll11l11_opy_
  else:
    caps[bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧய")] = True
    if bstack1ll11l11_opy_:
      caps[bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫர")] = bstack1ll11l11_opy_
def bstack1ll11l1_opy_():
  global CONFIG
  if bstack1l11l1l1_opy_(CONFIG):
    bstack1l1l11l_opy_ = bstack1l11l1l_opy_(CONFIG)
    bstack11ll11l1_opy_(bstack1lll1lll_opy_(CONFIG), bstack1l1l11l_opy_)
def bstack11ll11l1_opy_(key, bstack1l1l11l_opy_):
  global bstack1lllll1l_opy_
  logger.info(bstack1l1lll11_opy_)
  try:
    bstack1lllll1l_opy_ = Local()
    bstack11l11lll_opy_ = {bstack11_opy_ (u"ࠫࡰ࡫ࡹࠨற"): key}
    bstack11l11lll_opy_.update(bstack1l1l11l_opy_)
    logger.debug(bstack11llllll_opy_.format(str(bstack11l11lll_opy_)))
    bstack1lllll1l_opy_.start(**bstack11l11lll_opy_)
    if bstack1lllll1l_opy_.isRunning():
      logger.info(bstack1lll1l11_opy_)
  except Exception as e:
    bstack1lll1ll1_opy_(bstack111llll1_opy_.format(str(e)))
def bstack1l111lll_opy_():
  global bstack1lllll1l_opy_
  if bstack1lllll1l_opy_.isRunning():
    logger.info(bstack1lllll1_opy_)
    bstack1lllll1l_opy_.stop()
  bstack1lllll1l_opy_ = None
def bstack1111ll_opy_():
  logger.info(bstack1llll1ll_opy_)
  global bstack1lllll1l_opy_
  if bstack1lllll1l_opy_:
    bstack1l111lll_opy_()
  logger.info(bstack11l1111l_opy_)
def bstack1ll1l11l_opy_(self, *args):
  logger.error(bstack1ll11l1l_opy_)
  bstack1111ll_opy_()
def bstack1lll1ll1_opy_(err):
  logger.critical(bstack11l1l1l1_opy_.format(str(err)))
  atexit.unregister(bstack1111ll_opy_)
  sys.exit(1)
def bstack11lll1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  atexit.unregister(bstack1111ll_opy_)
  sys.exit(1)
def bstack1l1l11l1_opy_():
  global CONFIG
  CONFIG = bstack11ll1lll_opy_()
  CONFIG = bstack111l1lll_opy_(CONFIG)
  CONFIG = bstack11111ll_opy_(CONFIG)
  if bstack111lll1l_opy_(CONFIG):
    bstack1lll1ll1_opy_(bstack11l11l1l_opy_)
  CONFIG[bstack11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧல")] = bstack111llll_opy_(CONFIG)
  CONFIG[bstack11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩள")] = bstack1lll1lll_opy_(CONFIG)
  if bstack111ll111_opy_(CONFIG):
    CONFIG[bstack11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪழ")] = bstack111ll111_opy_(CONFIG)
    if os.getenv(bstack11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬவ"), None):
      CONFIG[bstack11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫஶ")] = os.getenv(bstack11_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧஷ"))
    else:
      bstack1lll1111_opy_()
  bstack1l1l11_opy_()
  bstack111ll11_opy_()
  if bstack11l11l1_opy_:
    CONFIG[bstack11_opy_ (u"ࠫࡦࡶࡰࠨஸ")] = bstack11l111l1_opy_(CONFIG)
    logger.info(bstack11lll1_opy_.format(CONFIG[bstack11_opy_ (u"ࠬࡧࡰࡱࠩஹ")]))
def bstack111ll11_opy_():
  global CONFIG
  global bstack11l11l1_opy_
  if bstack11_opy_ (u"࠭ࡡࡱࡲࠪ஺") in CONFIG:
    bstack11l11l1_opy_ = True
def bstack11l111l1_opy_(config):
  bstack11l1ll1l_opy_ = bstack11_opy_ (u"ࠧࠨ஻")
  bstack1lll1ll_opy_ = config[bstack11_opy_ (u"ࠨࡣࡳࡴࠬ஼")]
  if isinstance(config[bstack11_opy_ (u"ࠩࡤࡴࡵ࠭஽")], str):
    if os.path.splitext(bstack1lll1ll_opy_)[1] in bstack11lll_opy_:
      if os.path.exists(bstack1lll1ll_opy_):
        bstack11l1ll1l_opy_ = bstack111l11l_opy_(config, bstack1lll1ll_opy_)
      elif bstack11ll1l11_opy_(bstack1lll1ll_opy_):
        bstack11l1ll1l_opy_ = bstack1lll1ll_opy_
      else:
        bstack1lll1ll1_opy_(bstack11lll11_opy_.format(bstack1lll1ll_opy_))
    else:
      if bstack11ll1l11_opy_(bstack1lll1ll_opy_):
        bstack11l1ll1l_opy_ = bstack1lll1ll_opy_
      elif os.path.exists(bstack1lll1ll_opy_):
        bstack11l1ll1l_opy_ = bstack111l11l_opy_(bstack1lll1ll_opy_)
      else:
        bstack1lll1ll1_opy_(bstack11lll111_opy_)
  else:
    if len(bstack1lll1ll_opy_) > 2:
      bstack1lll1ll1_opy_(bstack11l1l11l_opy_)
    elif len(bstack1lll1ll_opy_) == 2:
      if bstack11_opy_ (u"ࠪࡴࡦࡺࡨࠨா") in bstack1lll1ll_opy_ and bstack11_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧி") in bstack1lll1ll_opy_:
        if os.path.exists(bstack1lll1ll_opy_[bstack11_opy_ (u"ࠬࡶࡡࡵࡪࠪீ")]):
          bstack11l1ll1l_opy_ = bstack111l11l_opy_(config, bstack1lll1ll_opy_[bstack11_opy_ (u"࠭ࡰࡢࡶ࡫ࠫு")], bstack1lll1ll_opy_[bstack11_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪூ")])
        else:
          bstack1lll1ll1_opy_(bstack11lll11_opy_.format(bstack1lll1ll_opy_))
      else:
        bstack1lll1ll1_opy_(bstack11l1l11l_opy_)
    else:
      for key in bstack1lll1ll_opy_:
        if key in bstack1llll_opy_:
          if key == bstack11_opy_ (u"ࠨࡲࡤࡸ࡭࠭௃"):
            if os.path.exists(bstack1lll1ll_opy_[key]):
              bstack11l1ll1l_opy_ = bstack111l11l_opy_(config, bstack1lll1ll_opy_[key])
            else:
              bstack1lll1ll1_opy_(bstack11lll11_opy_.format(bstack1lll1ll_opy_))
          else:
            bstack11l1ll1l_opy_ = bstack1lll1ll_opy_[key]
        else:
          bstack1lll1ll1_opy_(bstack1111l1_opy_)
  return bstack11l1ll1l_opy_
def bstack11ll1l11_opy_(bstack11l1ll1l_opy_):
  import re
  bstack1l11l111_opy_ = re.compile(bstack11_opy_ (u"ࡴࠥࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ௄"))
  bstack1ll1lll1_opy_ = re.compile(bstack11_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫ࠱࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢ௅"))
  if bstack11_opy_ (u"ࠫࡧࡹ࠺࠰࠱ࠪெ") in bstack11l1ll1l_opy_ or re.fullmatch(bstack1l11l111_opy_, bstack11l1ll1l_opy_) or re.fullmatch(bstack1ll1lll1_opy_, bstack11l1ll1l_opy_):
    return True
  else:
    return False
def bstack111l11l_opy_(config, path, bstack1l11llll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11_opy_ (u"ࠬࡸࡢࠨே")).read()).hexdigest()
  bstack11ll111_opy_ = bstack11l1lll1_opy_(md5_hash)
  bstack11l1ll1l_opy_ = None
  if bstack11ll111_opy_:
    logger.info(bstack1l1l1l_opy_.format(bstack11ll111_opy_, md5_hash))
    return bstack11ll111_opy_
  bstack1llll11l_opy_ = MultipartEncoder(
    fields={
        bstack11_opy_ (u"࠭ࡦࡪ࡮ࡨࠫை"): (os.path.basename(path), open(os.path.abspath(path), bstack11_opy_ (u"ࠧࡳࡤࠪ௉")), bstack11_opy_ (u"ࠨࡶࡨࡼࡹ࠵ࡰ࡭ࡣ࡬ࡲࠬொ")),
        bstack11_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬோ"): bstack1l11llll_opy_
    }
  )
  response = requests.post(bstack1lll1_opy_, data=bstack1llll11l_opy_,
                         headers={bstack11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩௌ"): bstack1llll11l_opy_.content_type}, auth=(bstack111llll_opy_(config), bstack1lll1lll_opy_(config)))
  try:
    res = json.loads(response.text)
    bstack11l1ll1l_opy_ = res[bstack11_opy_ (u"ࠫࡦࡶࡰࡠࡷࡵࡰ்ࠬ")]
    logger.info(bstack1l111ll_opy_.format(bstack11l1ll1l_opy_))
    bstack1l1ll111_opy_(md5_hash, bstack11l1ll1l_opy_)
  except ValueError as err:
    bstack1lll1ll1_opy_(bstack1lll1l_opy_.format(str(err)))
  return bstack11l1ll1l_opy_
def bstack1l1l11_opy_():
  global CONFIG
  global bstack1l11ll1_opy_
  bstack1l1l1lll_opy_ = 1
  if bstack11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ௎") in CONFIG:
    bstack1l1l1lll_opy_ = CONFIG[bstack11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭௏")]
  bstack11l1ll11_opy_ = 0
  if bstack11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪௐ") in CONFIG:
    bstack11l1ll11_opy_ = len(CONFIG[bstack11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௑")])
  bstack1l11ll1_opy_ = int(bstack1l1l1lll_opy_) * int(bstack11l1ll11_opy_)
def bstack11l1lll1_opy_(md5_hash):
  bstack1ll1111l_opy_ = os.path.join(os.path.expanduser(bstack11_opy_ (u"ࠩࢁࠫ௒")), bstack11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ௓"), bstack11_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬ௔"))
  if os.path.exists(bstack1ll1111l_opy_):
    bstack1l1ll1ll_opy_ = json.load(open(bstack1ll1111l_opy_,bstack11_opy_ (u"ࠬࡸࡢࠨ௕")))
    if md5_hash in bstack1l1ll1ll_opy_:
      bstack1ll111ll_opy_ = bstack1l1ll1ll_opy_[md5_hash]
      bstack1ll111l1_opy_ = datetime.datetime.now()
      bstack11llll11_opy_ = datetime.datetime.strptime(bstack1ll111ll_opy_[bstack11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ௖")], bstack11_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫௗ"))
      if (bstack1ll111l1_opy_ - bstack11llll11_opy_).days > 60:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1ll111ll_opy_[bstack11_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭௘")]):
        return None
      return bstack1ll111ll_opy_[bstack11_opy_ (u"ࠩ࡬ࡨࠬ௙")]
  else:
    return None
def bstack1l1ll111_opy_(md5_hash, bstack11l1ll1l_opy_):
  bstack1l1ll11_opy_ = os.path.join(os.path.expanduser(bstack11_opy_ (u"ࠪࢂࠬ௚")), bstack11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ௛"))
  if not os.path.exists(bstack1l1ll11_opy_):
    os.makedirs(bstack1l1ll11_opy_)
  bstack1ll1111l_opy_ = os.path.join(os.path.expanduser(bstack11_opy_ (u"ࠬࢄࠧ௜")), bstack11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭௝"), bstack11_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨ௞"))
  bstack111lll11_opy_ = {
    bstack11_opy_ (u"ࠨ࡫ࡧࠫ௟"): bstack11l1ll1l_opy_,
    bstack11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ௠"): datetime.datetime.strftime(datetime.datetime.now(), bstack11_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧ௡")),
    bstack11_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ௢"): str(__version__)
  }
  if os.path.exists(bstack1ll1111l_opy_):
    bstack1l1ll1ll_opy_ = json.load(open(bstack1ll1111l_opy_,bstack11_opy_ (u"ࠬࡸࡢࠨ௣")))
  else:
    bstack1l1ll1ll_opy_ = {}
  bstack1l1ll1ll_opy_[md5_hash] = bstack111lll11_opy_
  with open(bstack1ll1111l_opy_, bstack11_opy_ (u"ࠨࡷࠬࠤ௤")) as outfile:
    json.dump(bstack1l1ll1ll_opy_, outfile)
def bstack11ll11l_opy_(self):
  return
def bstack1llll111_opy_(self):
  return
def bstack111ll1_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack11l11ll_opy_(self, command_executor,
        desired_capabilities=None, browser_profile=None, proxy=None,
        keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1111111_opy_
  global bstack111ll1l_opy_
  global bstack11l1l111_opy_
  global bstack11ll1l1l_opy_
  global bstack1lllll11_opy_
  global bstack1l1lll_opy_
  CONFIG[bstack11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ௥")] = str(bstack1lllll11_opy_) + str(__version__)
  command_executor = bstack11ll1ll_opy_()
  logger.debug(bstack11111l1_opy_.format(command_executor))
  proxy = bstack1l1111l_opy_(CONFIG, proxy)
  bstack1ll1lll_opy_ = 0 if bstack111ll1l_opy_ < 0 else bstack111ll1l_opy_
  if bstack11ll1l1l_opy_ is True:
    bstack1ll1lll_opy_ = int(threading.current_thread().getName())
  bstack1lll1l1l_opy_ = bstack1l1l1ll1_opy_(CONFIG, bstack1ll1lll_opy_)
  logger.debug(bstack1l1lllll_opy_.format(str(bstack1lll1l1l_opy_)))
  if bstack1l11l1l1_opy_(CONFIG):
    bstack1l11l11_opy_(bstack1lll1l1l_opy_)
  if options:
    bstack1l1l1l1l_opy_(options, bstack1lll1l1l_opy_)
  if desired_capabilities:
    if bstack1ll1ll_opy_() >= version.parse(bstack11_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ௦")):
      desired_capabilities = {}
    else:
      desired_capabilities.update(bstack1lll1l1l_opy_)
  if not options:
    options = bstack1l1111l1_opy_(bstack1lll1l1l_opy_)
  if (
      not options and not desired_capabilities
  ) or (
      bstack1ll1ll_opy_() < version.parse(bstack11_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ௧")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1lll1l1l_opy_)
  logger.info(bstack1l1ll1l_opy_)
  if bstack1ll1ll_opy_() >= version.parse(bstack11_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ௨")):
    bstack1l1lll_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities, options=options,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1ll1ll_opy_() >= version.parse(bstack11_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫ௩")):
    bstack1l1lll_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1l1lll_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive)
  bstack1111111_opy_ = self.session_id
  if bstack11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ௪") in CONFIG and bstack11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ௫") in CONFIG[bstack11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௬")][bstack1ll1lll_opy_]:
    bstack11l1l111_opy_ = CONFIG[bstack11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௭")][bstack1ll1lll_opy_][bstack11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ௮")]
  logger.debug(bstack111lll_opy_.format(bstack1111111_opy_))
def bstack11ll1111_opy_(self, test):
  global CONFIG
  global bstack1111111_opy_
  global bstack1111l1l_opy_
  global bstack11l1l111_opy_
  global bstack111ll1l1_opy_
  if bstack1111111_opy_:
    try:
      data = {}
      bstack1l11lll_opy_ = None
      if test:
        bstack1l11lll_opy_ = str(test.data)
      if bstack1l11lll_opy_ and not bstack11l1l111_opy_:
        data[bstack11_opy_ (u"ࠪࡲࡦࡳࡥࠨ௯")] = bstack1l11lll_opy_
      if bstack1111l1l_opy_:
        if bstack1111l1l_opy_.status == bstack11_opy_ (u"ࠫࡕࡇࡓࡔࠩ௰"):
          data[bstack11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ௱")] = bstack11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭௲")
        elif bstack1111l1l_opy_.status == bstack11_opy_ (u"ࠧࡇࡃࡌࡐࠬ௳"):
          data[bstack11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ௴")] = bstack11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ௵")
          if bstack1111l1l_opy_.message:
            data[bstack11_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ௶")] = str(bstack1111l1l_opy_.message)
      user = CONFIG[bstack11_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭௷")]
      key = CONFIG[bstack11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ௸")]
      url = bstack11_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡵࡨࡷࡸ࡯࡯࡯ࡵ࠲ࡿࢂ࠴ࡪࡴࡱࡱࠫ௹").format(user, key, bstack1111111_opy_)
      headers = {
        bstack11_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭௺"): bstack11_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ௻"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1l11111_opy_.format(str(e)))
  bstack111ll1l1_opy_(self, test)
def bstack1111ll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11ll11ll_opy_
  bstack11ll11ll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1111l1l_opy_
  bstack1111l1l_opy_ = self._test
def bstack111111_opy_(outs_dir, options, tests_root_name, stats, copied_artifacts, outputfile=None):
  from pabot import pabot
  outputfile = outputfile or options.get(bstack11_opy_ (u"ࠤࡲࡹࡹࡶࡵࡵࠤ௼"), bstack11_opy_ (u"ࠥࡳࡺࡺࡰࡶࡶ࠱ࡼࡲࡲࠢ௽"))
  output_path = os.path.abspath(
    os.path.join(options.get(bstack11_opy_ (u"ࠦࡴࡻࡴࡱࡷࡷࡨ࡮ࡸࠢ௾"), bstack11_opy_ (u"ࠧ࠴ࠢ௿")), outputfile)
  )
  files = sorted(pabot.glob(os.path.join(pabot._glob_escape(outs_dir), bstack11_opy_ (u"ࠨࠪ࠯ࡺࡰࡰࠧఀ"))))
  if not files:
    pabot._write(bstack11_opy_ (u"ࠧࡘࡃࡕࡒ࠿ࠦࡎࡰࠢࡲࡹࡹࡶࡵࡵࠢࡩ࡭ࡱ࡫ࡳࠡ࡫ࡱࠤࠧࠫࡳࠣࠩఁ") % outs_dir, pabot.Color.YELLOW)
    return bstack11_opy_ (u"ࠣࠤం")
  def invalid_xml_callback():
    global _ABNORMAL_EXIT_HAPPENED
    _ABNORMAL_EXIT_HAPPENED = True
  resu = pabot.merge(
    files, options, tests_root_name, copied_artifacts, invalid_xml_callback
  )
  pabot._update_stats(resu, stats)
  resu.save(output_path)
  return output_path
def bstack1l1111ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  from pabot import pabot
  from robot import __version__ as ROBOT_VERSION
  from robot import rebot
  if bstack11_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨః") in options:
    del options[bstack11_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢఄ")]
  if ROBOT_VERSION < bstack11_opy_ (u"ࠦ࠹࠴࠰ࠣఅ"):
    stats = {
      bstack11_opy_ (u"ࠧࡩࡲࡪࡶ࡬ࡧࡦࡲࠢఆ"): {bstack11_opy_ (u"ࠨࡴࡰࡶࡤࡰࠧఇ"): 0, bstack11_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢఈ"): 0, bstack11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣఉ"): 0},
      bstack11_opy_ (u"ࠤࡤࡰࡱࠨఊ"): {bstack11_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࠤఋ"): 0, bstack11_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦఌ"): 0, bstack11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ఍"): 0},
    }
  else:
    stats = {
      bstack11_opy_ (u"ࠨࡴࡰࡶࡤࡰࠧఎ"): 0,
      bstack11_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢఏ"): 0,
      bstack11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣఐ"): 0,
      bstack11_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠥ఑"): 0,
    }
  if pabot_args[bstack11_opy_ (u"ࠥࡆࡘ࡚ࡁࡄࡍࡢࡔࡆࡘࡁࡍࡎࡈࡐࡤࡘࡕࡏࠤఒ")]:
    outputs = []
    for index, _ in enumerate(pabot_args[bstack11_opy_ (u"ࠦࡇ࡙ࡔࡂࡅࡎࡣࡕࡇࡒࡂࡎࡏࡉࡑࡥࡒࡖࡐࠥఓ")]):
      copied_artifacts = pabot._copy_output_artifacts(
        options, pabot_args[bstack11_opy_ (u"ࠧࡧࡲࡵ࡫ࡩࡥࡨࡺࡳࠣఔ")], pabot_args[bstack11_opy_ (u"ࠨࡡࡳࡶ࡬ࡪࡦࡩࡴࡴ࡫ࡱࡷࡺࡨࡦࡰ࡮ࡧࡩࡷࡹࠢక")]
      )
      outputs += [
        bstack111111_opy_(
          os.path.join(outs_dir, str(index)+ bstack11_opy_ (u"ࠢ࠰ࠤఖ")),
          options,
          tests_root_name,
          stats,
          copied_artifacts,
          outputfile=os.path.join(bstack11_opy_ (u"ࠣࡲࡤࡦࡴࡺ࡟ࡳࡧࡶࡹࡱࡺࡳࠣగ"), bstack11_opy_ (u"ࠤࡲࡹࡹࡶࡵࡵࠧࡶ࠲ࡽࡳ࡬ࠣఘ") % index),
        )
      ]
    if bstack11_opy_ (u"ࠥࡳࡺࡺࡰࡶࡶࠥఙ") not in options:
      options[bstack11_opy_ (u"ࠦࡴࡻࡴࡱࡷࡷࠦచ")] = bstack11_opy_ (u"ࠧࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠤఛ")
    pabot._write_stats(stats)
    return rebot(*outputs, **pabot._options_for_rebot(options, start_time_string, pabot._now()))
  else:
    return pabot._report_results(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1ll1111_opy_(self, ff_profile_dir):
  global bstack11l1l11_opy_
  if not ff_profile_dir:
    return None
  return bstack11l1l11_opy_(self, ff_profile_dir)
def bstack1l111l1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1ll11l11_opy_
  bstack111l1l1_opy_ = []
  if bstack11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩజ") in CONFIG:
    bstack111l1l1_opy_ = CONFIG[bstack11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪఝ")]
  bstack1lll111l_opy_ = len(suite_group) * len(pabot_args[bstack11_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡩ࡭ࡱ࡫ࡳࠣఞ")] or [(bstack11_opy_ (u"ࠤࠥట"), None)]) * len(bstack111l1l1_opy_)
  pabot_args[bstack11_opy_ (u"ࠥࡆࡘ࡚ࡁࡄࡍࡢࡔࡆࡘࡁࡍࡎࡈࡐࡤࡘࡕࡏࠤఠ")] = []
  for q in range(bstack1lll111l_opy_):
    pabot_args[bstack11_opy_ (u"ࠦࡇ࡙ࡔࡂࡅࡎࡣࡕࡇࡒࡂࡎࡏࡉࡑࡥࡒࡖࡐࠥడ")].append(str(q))
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࠨఢ")],
      pabot_args[bstack11_opy_ (u"ࠨࡶࡦࡴࡥࡳࡸ࡫ࠢణ")],
      argfile,
      pabot_args.get(bstack11_opy_ (u"ࠢࡩ࡫ࡹࡩࠧత")),
      pabot_args[bstack11_opy_ (u"ࠣࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠦథ")],
      platform[0],
      bstack1ll11l11_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡪ࡮ࡲࡥࡴࠤద")] or [(bstack11_opy_ (u"ࠥࠦధ"), None)]
    for platform in enumerate(bstack111l1l1_opy_)
  ]
def bstack1lll1l1_opy_(self, datasources, outs_dir, options,
  execution_item, command, verbose, argfile,
  hive=None, processes=0,platform_index=0,bstack111ll11l_opy_=bstack11_opy_ (u"ࠫࠬన")):
  global bstack1ll111_opy_
  self.platform_index = platform_index
  self.bstack1lll11l1_opy_ = bstack111ll11l_opy_
  bstack1ll111_opy_(self, datasources, outs_dir, options,
    execution_item, command, verbose, argfile, hive, processes)
def bstack1lll111_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1lll11l_opy_
  if not bstack11_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ఩") in item.options:
    item.options[bstack11_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨప")] = []
  for v in item.options[bstack11_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩఫ")]:
    if bstack11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧబ") in v:
      item.options[bstack11_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫభ")].remove(v)
  item.options[bstack11_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬమ")].insert(0, bstack11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚࠽ࡿࢂ࠭య").format(item.platform_index))
  item.options[bstack11_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧర")].insert(0, bstack11_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ࠽ࡿࢂ࠭ఱ").format(item.bstack1lll11l1_opy_))
  return bstack1lll11l_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l1lll1_opy_
  command[0] = command[0].replace(bstack11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ల"), bstack11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬళ"), 1)
  return bstack1l1lll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11l111ll_opy_(bstack11ll111l_opy_):
  global bstack1lllll11_opy_
  bstack1lllll11_opy_ = bstack11ll111l_opy_
  logger.info(bstack111l111_opy_.format(bstack1lllll11_opy_.split(bstack11_opy_ (u"ࠩ࠰ࠫఴ"))[0]))
  global bstack1l1lll_opy_
  global bstack111ll1l1_opy_
  global bstack11ll11ll_opy_
  global bstack11l1l11_opy_
  global bstack1l1lll1_opy_
  global bstack1ll111_opy_
  global bstack1lll11l_opy_
  global bstack1lllll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
  except Exception as e:
    bstack11lll1l_opy_(e, bstack1ll1ll1l_opy_)
  Service.start = bstack11ll11l_opy_
  Service.stop = bstack1llll111_opy_
  webdriver.Remote.__init__ = bstack11l11ll_opy_
  WebDriver.close = bstack111ll1_opy_
  if (bstack11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩవ") in str(bstack11ll111l_opy_).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
      from pabot.pabot import QueueItem
      from pabot import pabot
    except Exception as e:
      bstack11lll1l_opy_(e, bstack11ll11_opy_)
    Output.end_test = bstack11ll1111_opy_
    TestStatus.__init__ = bstack1111ll1_opy_
    WebDriverCreator._get_ff_profile = bstack1ll1111_opy_
    QueueItem.__init__ = bstack1lll1l1_opy_
    pabot._create_items = bstack1l111l1_opy_
    pabot._run = bstack1l111l_opy_
    pabot._create_command_for_execution = bstack1lll111_opy_
    pabot._report_results = bstack1l1111ll_opy_
def bstack1l111ll1_opy_():
  global CONFIG
  if bstack11_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫశ") in CONFIG and int(CONFIG[bstack11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬష")]) > 1:
    logger.warn(bstack111ll1ll_opy_)
def bstack11lll1l1_opy_(bstack1ll11l_opy_, index):
  bstack11l111ll_opy_(bstack1l1l1_opy_)
  exec(open(bstack1ll11l_opy_).read())
def bstack1ll11ll_opy_():
  print(bstack1ll1ll11_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬస"), help=bstack11_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡥࡲࡲ࡫࡯ࡧࠨహ"))
  parser.add_argument(bstack11_opy_ (u"ࠨ࠯ࡸࠫ఺"), bstack11_opy_ (u"ࠩ࠰࠱ࡺࡹࡥࡳࡰࡤࡱࡪ࠭఻"), help=bstack11_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦ఼ࠩ"))
  parser.add_argument(bstack11_opy_ (u"ࠫ࠲ࡱࠧఽ"), bstack11_opy_ (u"ࠬ࠳࠭࡬ࡧࡼࠫా"), help=bstack11_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠧి"))
  parser.add_argument(bstack11_opy_ (u"ࠧ࠮ࡨࠪీ"), bstack11_opy_ (u"ࠨ࠯࠰ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ు"), help=bstack11_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨూ"))
  bstack11llll_opy_ = parser.parse_args()
  try:
    bstack1l11l1ll_opy_ = bstack11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡳ࡫ࡲࡪࡥ࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧృ")
    if bstack11llll_opy_.framework:
      bstack1l11l1ll_opy_ = bstack11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࡹ࡮࡮࠱ࡷࡦࡳࡰ࡭ࡧࠪౄ")
    bstack11ll1ll1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l11l1ll_opy_)
    bstack11l1lll_opy_ = open(bstack11ll1ll1_opy_, bstack11_opy_ (u"ࠬࡸࠧ౅"))
    bstack1ll1l11_opy_ = bstack11l1lll_opy_.read()
    bstack11l1lll_opy_.close()
    if bstack11llll_opy_.username:
      bstack1ll1l11_opy_ = bstack1ll1l11_opy_.replace(bstack11_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ె"), bstack11llll_opy_.username)
    if bstack11llll_opy_.key:
      bstack1ll1l11_opy_ = bstack1ll1l11_opy_.replace(bstack11_opy_ (u"࡚ࠧࡑࡘࡖࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩే"), bstack11llll_opy_.key)
    if bstack11llll_opy_.framework:
      bstack1ll1l11_opy_ = bstack1ll1l11_opy_.replace(bstack11_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩై"), bstack11llll_opy_.framework)
    file_name = bstack11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬ౉")
    file_path = os.path.abspath(file_name)
    bstack1l1l1l1_opy_ = open(file_path, bstack11_opy_ (u"ࠪࡻࠬొ"))
    bstack1l1l1l1_opy_.write(bstack1ll1l11_opy_)
    bstack1l1l1l1_opy_.close()
    print(bstack111l1l1l_opy_)
  except Exception as e:
    print(bstack11lll1ll_opy_.format(str(e)))
def bstack1llll11_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  bstack1l1l11l1_opy_()
  logger.info(CONFIG)
  bstack111111l_opy_()
  atexit.register(bstack1111ll_opy_)
  signal.signal(signal.SIGINT, bstack1ll1l11l_opy_)
  signal.signal(signal.SIGTERM, bstack1ll1l11l_opy_)
def run_on_browserstack():
  if len(sys.argv) <= 1:
    print(bstack1lllllll_opy_)
    return
  if sys.argv[1] == bstack11_opy_ (u"ࠫ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧో")  or sys.argv[1] == bstack11_opy_ (u"ࠬ࠳ࡶࠨౌ"):
    print(bstack11_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡖࡹࡵࡪࡲࡲ࡙ࠥࡄࡌࠢࡹࡿࢂ్࠭").format(__version__))
    return
  if sys.argv[1] == bstack11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭౎"):
    bstack1ll11ll_opy_()
    return
  args = sys.argv
  bstack1llll11_opy_()
  global CONFIG
  global bstack1l11ll1_opy_
  global bstack11ll1l1l_opy_
  global bstack111ll1l_opy_
  global bstack1ll11l11_opy_
  bstack11lllll1_opy_ = bstack11_opy_ (u"ࠨࠩ౏")
  if args[1] == bstack11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ౐") or args[1] == bstack11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ౑"):
    bstack11lllll1_opy_ = bstack11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ౒")
    args = args[2:]
  elif args[1] == bstack11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ౓"):
    bstack11lllll1_opy_ = bstack11_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ౔")
    args = args[2:]
  elif args[1] == bstack11_opy_ (u"ࠧࡱࡣࡥࡳࡹౕ࠭"):
    bstack11lllll1_opy_ = bstack11_opy_ (u"ࠨࡲࡤࡦࡴࡺౖࠧ")
    args = args[2:]
  elif args[1] == bstack11_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ౗"):
    bstack11lllll1_opy_ = bstack11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫౘ")
    args = args[2:]
  else:
    if not bstack11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧౙ") in CONFIG or str(CONFIG[bstack11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨౚ")]).lower() in [bstack11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭౛"), bstack11_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨ౜")]:
      bstack11lllll1_opy_ = bstack11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨౝ")
      args = args[1:]
    elif str(CONFIG[bstack11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ౞")]).lower() == bstack11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ౟"):
      bstack11lllll1_opy_ = bstack11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪౠ")
      args = args[1:]
    elif str(CONFIG[bstack11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨౡ")]).lower() == bstack11_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬౢ"):
      bstack11lllll1_opy_ = bstack11_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ౣ")
      args = args[1:]
    else:
      bstack1lll1ll1_opy_(bstack111l1l_opy_)
  global bstack1l1lll_opy_
  global bstack111ll1l1_opy_
  global bstack11ll11ll_opy_
  global bstack11l1l11_opy_
  global bstack1l1lll1_opy_
  global bstack1ll111_opy_
  global bstack1lll11l_opy_
  global bstack1lllll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
  except Exception as e:
    bstack11lll1l_opy_(e, bstack1ll1ll1l_opy_)
  bstack1l1lll_opy_ = webdriver.Remote.__init__
  bstack1lllll_opy_ = WebDriver.close
  if (bstack11lllll1_opy_ in [bstack11_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ౤"), bstack11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౥"), bstack11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ౦")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
      from pabot.pabot import QueueItem
      from pabot import pabot
    except Exception as e:
      bstack11lll1l_opy_(e, bstack11ll11_opy_)
    bstack111ll1l1_opy_ = Output.end_test
    bstack11ll11ll_opy_ = TestStatus.__init__
    bstack11l1l11_opy_ = WebDriverCreator._get_ff_profile
    bstack1l1lll1_opy_ = pabot._run
    bstack1ll111_opy_ = QueueItem.__init__
    bstack1lll11l_opy_ = pabot._create_command_for_execution
  if bstack11lllll1_opy_ == bstack11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ౧"):
    bstack1ll11l1_opy_()
    bstack1l111ll1_opy_()
    if bstack11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౨") in CONFIG:
      bstack11ll1l1l_opy_ = True
      bstack11l111_opy_ = []
      for index, platform in enumerate(CONFIG[bstack11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ౩")]):
        bstack11l111_opy_.append(threading.Thread(name=str(index),
                                      target=bstack11lll1l1_opy_, args=(args[0], index)))
      for t in bstack11l111_opy_:
        t.start()
      for t in bstack11l111_opy_:
        t.join()
    else:
      bstack11l111ll_opy_(bstack1l1l1_opy_)
      exec(open(args[0]).read())
  elif bstack11lllll1_opy_ == bstack11_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭౪") or bstack11lllll1_opy_ == bstack11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ౫"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack11lll1l_opy_(e, bstack11ll11_opy_)
    bstack1ll11l1_opy_()
    bstack11l111ll_opy_(bstack1ll1l_opy_)
    if bstack11_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ౬") in args:
      i = args.index(bstack11_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ౭"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack1l11ll1_opy_))
    args.insert(0, str(bstack11_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ౮")))
    pabot.main(args)
  elif bstack11lllll1_opy_ == bstack11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭౯"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack11lll1l_opy_(e, bstack11ll11_opy_)
    for a in args:
      if bstack11_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬ౰") in a:
        bstack111ll1l_opy_ = int(a.split(bstack11_opy_ (u"ࠧ࠻ࠩ౱"))[1])
      if bstack11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ౲") in a:
        bstack1ll11l11_opy_ = str(a.split(bstack11_opy_ (u"ࠩ࠽ࠫ౳"))[1])
    bstack11l111ll_opy_(bstack1ll1l_opy_)
    run_cli(args)
  else:
    bstack1lll1ll1_opy_(bstack111l1l_opy_)