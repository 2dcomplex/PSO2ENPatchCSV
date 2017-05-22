#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv
import codecs
import os
import sys

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

POnice = [
	("\\\\u3000", '　'),
	("\\u3000", '　'),
	("\\\\\"", "\\\""),
	#("\"\\\"", "\"\\\\\""),
]

def POformat(input):
	inputl = input
	for i, o in POnice:
		outtext = inputl.replace(i, o)
		inputl = outtext
	if outtext is "\\":
		return "\\\\"
	return outtext


for i in sys.argv[1:]:
	w = i.replace("JP/","WC/")
	e = i.replace("JP/","EN/")
	with codecs.open(i, encoding="utf-8") as JP:
		ENcheck = False
		JPcheck = False
		JPCSV = list(csv.reader(JP,strict=True))
		ENCSV = list(csv.reader(codecs.open(e, encoding="utf-8"),strict=True))
		WCCSV = list(csv.reader(codecs.open(w, encoding="utf-8"),strict=True))
		basename = os.path.splitext(os.path.basename(i))[0]
		if ENCSV == WCCSV:
			ENcheck = True
		if ENCSV == JPCSV:
			JPcheck = True
		if ENcheck and JPcheck:
			continue
		for x, row in enumerate(JPCSV):
			if not ENcheck and ENCSV[x][1] == WCCSV[x][1]:
				continue
			#white-space
			print("")
			##  translator-comments
			##. extracted-comments
			##: reference…
			print("#: {}:{}".format(basename, POformat(row[0])))
			##, flag…
			print("#, no-c-format")
			##| msgctxt previous-context
			print("#| msgctxt \"{}:{}\"".format(basename, POformat(row[0])))
			##| msgid previous-untranslated-string
			print("#| msgid \"{}\"".format(POformat(JPCSV[x][1][1:-1])))
			#msgctxt context
			print("msgctxt \"{}:{}\"".format(basename, row[0]))
			if ENcheck:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POformat(JPCSV[x][1][1:-1])))
				#msgstr translated-string
				print("msgstr \"{}\"".format(POformat(ENCSV[x][1][1:-1])))
			elif JPcheck:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POformat(ENCSV[x][1][1:-1])))
				#msgstr translated-string
				print("msgstr \"{}\"".format(POformat(WCCSV[x][1][1:-1])))
			else:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POformat(ENCSV[x][1][1:-1])))
				#msgstr translated-string
				print("msgstr \"{}\"".format(POformat(ENCSV[x][1][1:-1])))
