#!/usr/bin/env python3
import re
import sys
import json
sys.path.append('..')
from define import *
from utils import *
from extractor import BasicExtractor

class XXXExtractor(BasicExtractor):
	'''
	XXX视频下载器
	'''
	def __init__(self,c):
		super(XXXExtractor,self).__init__(c, XXX)

	def download(self):
		print('XXX:start downloading ...')
		retry = 3
		while retry > 0 :
			self.page = get_html(self.c.url)
			if self.page: break
			retry -= 1
		if not self.page:
			print('error: request video info error,check url. %s' % (self.c.url,))
			sys.exit(0)

		self.i.vid = self.getVid()
		if not self.i.vid:
			print('error: not find vid! exit...')
			sys.exit(0)

		#metadata = ...
		self.i.title = self.getTitle(...)
		self.i.desc = self.getDesc()
		self.i.keywords = self.getKeywords()
		self.i.fname = self.getFname()
		self.i.fsize = self.getFsize()
		self.i.duration = self.getDuration()
		self.i.category = self.getCategory()
		self.i.uptime = self.getUptime()
		self.i.m3u8 = self.query_m3u8()
		self.flvlist = self.query_real()
		self.realdown()

	def query_m3u8(self,*args,**kwargs):
		pass

	def query_real(self,*args,**kwargs):
		pass

	def getVid(self,*args,**kwargs):
		pass

	def getFsize(self,*args,**kwargs):
		pass

	def getTitle(self,*args,**kwargs):
		pass

	def getDesc(self,*args,**kwargs):
		pass

	def getKeywords(self,*args,**kwargs):
		pass

	def getCategory(self,*args,**kwargs):
		pass

	def getDuration(self,*args,**kwargs):
		pass

	def getUptime(self,*args,**kwargs):
		pass


def download(c):
	d = XXXExtractor(c)
	return d.download()