# -*- coding: UTF-8 -*-
"""
__Author__ = "WECENG"
__Version__ = "1.0.0"
__Description__ = "大麦 iOS 抢票自动化 (Appium XCUITest)"
__Created__ = 2025/08/15 10:00
"""
from time import sleep

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from config import Config


def build_ios_options(config: Config) -> AppiumOptions:
    options = AppiumOptions()
    options.set_capability('platformName', 'iOS')
    options.set_capability('automationName', 'XCUITest')
    options.set_capability('deviceName', config.device_name)
    options.set_capability('platformVersion', config.platform_version)
    options.set_capability('udid', config.udid)
    options.set_capability('bundleId', config.bundle_id)
    options.set_capability('noReset', True)
    options.set_capability('newCommandTimeout', 6000)
    if config.xcode_org_id:
        options.set_capability('xcodeOrgId', config.xcode_org_id)
    if config.xcode_signing_id:
        options.set_capability('xcodeSigningId', config.xcode_signing_id)
    if config.wda_local_port:
        options.set_capability('wdaLocalPort', config.wda_local_port)
    if config.updated_wda_bundle_id:
        options.set_capability('updatedWDABundleId', config.updated_wda_bundle_id)
    return options


def find_first(driver, candidates):
    for by, value in candidates:
        elements = driver.find_elements(by=by, value=value)
        if elements:
            return elements[0]
    return None


def try_click_first(driver, candidates):
    elem = find_first(driver, candidates)
    if elem:
        elem.click()
        return True
    return False


def perform_purchase_flow(driver, config: Config):
    driver.implicitly_wait(5)
    sleep(3)
    # 进入搜索
    if not try_click_first(driver, [
        (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSearchField"'),
        (AppiumBy.ACCESSIBILITY_ID, '搜索'),
        (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSearchField[`enabled == 1`]')
    ]):
        return
    # 输入关键词
    search_field = find_first(driver, [
        (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSearchField"'),
        (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSearchField')
    ])
    if search_field:
        search_field.clear()
        search_field.send_keys(config.keyword)
    # 点击第一个搜索建议
    try_click_first(driver, [
        (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/**/XCUIElementTypeCell[1]'),
        (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeCell"')
    ])
    # 进入第一个结果详情
    try_click_first(driver, [
        (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/**/XCUIElementTypeCell[1]'),
        (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeCell"')
    ])
    # 城市/日期选择（若存在）
    if config.city:
        try_click_first(driver, [
            (AppiumBy.IOS_PREDICATE, f'label CONTAINS "{config.city}" OR name CONTAINS "{config.city}"')
        ])
    if config.date:
        try_click_first(driver, [
            (AppiumBy.IOS_PREDICATE, f'label CONTAINS "{config.date}" OR name CONTAINS "{config.date}"')
        ])
    # 抢票循环：立即购买/预约抢票/已预约
    for _ in range(60):
        buy_now = find_first(driver, [
            (AppiumBy.IOS_PREDICATE, 'label == "立即购买" OR name == "立即购买"'),
            (AppiumBy.IOS_PREDICATE, 'label CONTAINS "立即购买" OR name CONTAINS "立即购买"')
        ])
        reserve = find_first(driver, [
            (AppiumBy.IOS_PREDICATE, 'label == "预约抢票" OR name == "预约抢票"'),
            (AppiumBy.IOS_PREDICATE, 'label CONTAINS "预约" OR name CONTAINS "预约"')
        ])
        reserved = find_first(driver, [
            (AppiumBy.IOS_PREDICATE, 'label == "已预约" OR name == "已预约"')
        ])
        if buy_now:
            buy_now.click()
            # 票价
            if config.price:
                try_click_first(driver, [
                    (AppiumBy.IOS_PREDICATE, f'label CONTAINS "{config.price}" OR name CONTAINS "{config.price}"'),
                    (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`enabled == 1`]')
                ])
            # 数量（按观演人数量增加）
            if config.users:
                for _ in range(max(len(config.users) - 1, 0)):
                    try_click_first(driver, [
                        (AppiumBy.IOS_PREDICATE, 'label == "+" OR name == "+"')
                    ])
            # 确认/下一步
            try_click_first(driver, [
                (AppiumBy.IOS_PREDICATE, 'label == "确认" OR name == "确认"'),
                (AppiumBy.IOS_PREDICATE, 'label CONTAINS "下一步" OR name CONTAINS "下一步"')
            ])
            # 选择观演人
            if config.users:
                for user in config.users:
                    try_click_first(driver, [
                        (AppiumBy.IOS_PREDICATE, f'label CONTAINS "{user}" OR name CONTAINS "{user}"')
                    ])
            # 提交订单
            if config.if_commit_order:
                try_click_first(driver, [
                    (AppiumBy.IOS_PREDICATE, 'label == "提交订单" OR name == "提交订单"')
                ])
            break
        elif reserve:
            reserve.click()
            # 日期
            if config.date:
                try_click_first(driver, [
                    (AppiumBy.IOS_PREDICATE, f'label CONTAINS "{config.date}" OR name CONTAINS "{config.date}"')
                ])
            # 票价
            if config.price:
                try_click_first(driver, [
                    (AppiumBy.IOS_PREDICATE, f'label CONTAINS "{config.price}" OR name CONTAINS "{config.price}"')
                ])
            # 提交预约
            try_click_first(driver, [
                (AppiumBy.IOS_PREDICATE, 'label CONTAINS "提交" OR name CONTAINS "提交"')
            ])
            break
        elif reserved:
            break
        sleep(0.5)


if __name__ == '__main__':
    cfg = Config.load_config()
    ios_options = build_ios_options(cfg)
    driver = webdriver.Remote(cfg.server_url, options=ios_options)
    try:
        perform_purchase_flow(driver, cfg)
    finally:
        driver.quit()