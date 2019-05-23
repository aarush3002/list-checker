import xlrd
from collections import Counter

published_list = ("Published_Words_Junior_2018-converted.xlsx")

wb = xlrd.open_workbook(published_list)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

dictwordsfile = open("words_alpha.txt", "r")

dict_words = []
list_words = []
duplicates = []

def getDupes(lst):
	return [k for k, v in Counter(lst).items() if v > 1]

for i in range(sheet.nrows):
	for j in range(sheet.ncols):
		list_words.append(sheet.cell_value(i,j))

for word in dictwordsfile:
	values = word.split()
	dict_words.append(values[0])

for thing in list_words:
	if thing == "" or thing == " ":
		list_words.remove(thing)

#print(list_words)

print("NOT REAL WORDS:")
for word in list_words:
	if not(word in dict_words):
		print(word.strip())

print("\nDUPLICATE WORDS:")
duplicates = getDupes(list_words)

for dupe in duplicates:
	print(dupe)

dictwordsfile.close()