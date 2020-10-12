# xlrdformulas

As there was no current library that retruns cellwise formula information for a .xls (MS EXCEL 2003 files), I made some changes to the XLRD library by enabling the 'decompile_formulas' method in formula.py to return a formula dictionary for each book.

The formula dictionary is a dictionaty with sheet name as key and an array of tuples containing the cell index with its formula.
(The cells containing "SHAREDFML" are not included, however the first cell in which the formula was typed in is included)
