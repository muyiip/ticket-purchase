# -*- coding: UTF-8 -*-
import pytest

from damai.ios_support import build_ios_capabilities, normalize_text, match_label


def test_build_ios_capabilities():
    caps = build_ios_capabilities(
        device_name="iPhone 14 Pro",
        platform_version="17.5",
        udid="UDID",
        bundle_id="cn.damai.iphone",
    )
    assert caps["platformName"] == "iOS"
    assert caps["automationName"] == "XCUITest"
    assert caps["deviceName"] == "iPhone 14 Pro"
    assert caps["platformVersion"] == "17.5"
    assert caps["udid"] == "UDID"
    assert caps["bundleId"] == "cn.damai.iphone"
    assert caps["noReset"] is True
    assert isinstance(caps["newCommandTimeout"], int)


def test_normalize_text_basic():
    assert normalize_text("  a b\n c\t") == "abc"
    assert normalize_text("") == ""
    assert normalize_text(None) == ""


def test_match_label():
    assert match_label("  郁 可 唯", "郁可唯") is True
    assert match_label("abc", "") is False
    assert match_label(None, "abc") is False