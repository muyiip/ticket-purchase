# -*- coding: UTF-8 -*-
"""
__Author__ = "WECENG"
__Version__ = "1.0.0"
__Description__ = "iOS 配置类"
__Created__ = 2025/08/15 10:00
"""
import json


class Config:

	def __init__(self, server_url, device_name, platform_version, udid, bundle_id, keyword, users, city, date, price, if_commit_order, xcode_org_id=None, xcode_signing_id=None, wda_local_port=None, updated_wda_bundle_id=None):
		self.server_url = server_url
		self.device_name = device_name
		self.platform_version = platform_version
		self.udid = udid
		self.bundle_id = bundle_id
		self.keyword = keyword
		self.users = users
		self.city = city
		self.date = date
		self.price = price
		self.if_commit_order = if_commit_order
		self.xcode_org_id = xcode_org_id
		self.xcode_signing_id = xcode_signing_id
		self.wda_local_port = wda_local_port
		self.updated_wda_bundle_id = updated_wda_bundle_id

	@staticmethod
	def load_config():
		with open('config.json', 'r', encoding='utf-8') as config_file:
			config = json.load(config_file)
		return Config(
			config['server_url'],
			config['device_name'],
			config['platform_version'],
			config['udid'],
			config['bundle_id'],
			config['keyword'],
			config.get('users'),
			config.get('city'),
			config.get('date'),
			config.get('price'),
			config.get('if_commit_order', False),
			config.get('xcode_org_id'),
			config.get('xcode_signing_id'),
			config.get('wda_local_port'),
			config.get('updated_wda_bundle_id')
		)