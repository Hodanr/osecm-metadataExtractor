'''
Created on Jan 19, 2016

@author: tim
'''
from tim.metadataExtractor.ImportFilterInterface import ImportFilterInterface
from email.parser import Parser, BytesParser


class ImportFilterEmail(ImportFilterInterface):
	'''
	classdocs
	'''
	myName = 'Email'
	myContentType = 'text/plain'
	
	myValidTagNames = ['Image DateTime']

	def __init__(self):
		'''
		Constructor
		'''
	
	def extractMetaData(self,obj):
		headers = BytesParser().parse(obj)
		h = dict(headers.items())
		return self.convertMetaDataToSwiftFormat(h)
	