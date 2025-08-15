# -*- coding: UTF-8 -*-
"""
Utilities to assist iOS automation configuration and text matching.
This module is intentionally simple so unit tests can cover it fully.
"""
from typing import Dict, Optional


def build_ios_capabilities(
    device_name: str,
    platform_version: str,
    udid: str,
    bundle_id: str,
    no_reset: bool = True,
    new_command_timeout: int = 6000,
) -> Dict[str, object]:
    return {
        "platformName": "iOS",
        "automationName": "XCUITest",
        "deviceName": device_name,
        "platformVersion": platform_version,
        "udid": udid,
        "bundleId": bundle_id,
        "noReset": no_reset,
        "newCommandTimeout": new_command_timeout,
    }


def normalize_text(text: Optional[str]) -> str:
    if text is None:
        return ""
    return "".join(ch for ch in text.strip() if not ch.isspace())


def match_label(text: Optional[str], keyword: str) -> bool:
    if keyword == "":
        return False
    return keyword in normalize_text(text)