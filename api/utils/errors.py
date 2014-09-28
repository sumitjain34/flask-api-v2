'''
created on : 16-Sep-2014
@author: Sumit Jain
'''
class ValidationError(Exception):
	def __init__(self,message,data=None):
		self.message=message.format(data)
		Exception.__init__(self,self.message)

class NotUniqueError(Exception):
	def __init__(self,message,data=None):
		self.message=message
		Exception.__init__(self,self.message)
		