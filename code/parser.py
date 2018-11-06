import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from random import choice

from .case import Case


class Collection:

	def __init__(self):
		self.excel_data = pd.read_excel('data/oczyszczone.xls', sheet_name = 'daneSOB')
		self.number_rows = self.excel_data.count()[0]
		self.headers = self.excel_data.columns.values
		self.object_list = []
		self._create_list_objects()
		self.size_training_set = self.number_rows / 2

	# print(type(excel_data))
	# print("Column headings:")
	# print(self.excel_data.loc[0])
	# print(self.excel_data.count()[0])

	def _create_list_objects(self):
		for i in range(self.number_rows):
			self.object_list.append(Case(self.excel_data.loc[i]))

	def _divide(self):
		tmp_a = []
		for i in range(int(self.size_training_set)):
			tmp = choice(self.object_list)
			self.object_list.remove(tmp)
			tmp_a.append(tmp.param['sex'])
		tmp_b = [ x.param['sex'] for x in self.object_list]
		return tmp_a, tmp_b
