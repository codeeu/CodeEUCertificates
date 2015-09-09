# -*- coding: utf-8 -*-
# This diploma generator read a list of names to 
# fill a LaTeX template with a point for the name.
# Optinally, it can compile the LaTeX files and join them.
# If LaTeX errors are present, then press Enter.

print "Pyploma: Diploma generator for LaTeX and pdf.\n"

# Invoke terminal
from commands import *
import commands
def run_command(cmd):
	getstatusoutput(cmd)

# Load the list of names
lista = open("listadip", "r").readlines()

#counter
a = 100

for line in lista: # for each person in the list

	a += 1 #counter
	b = str(a) #transform counter into string
	salida = open("output" + b + ".tex","w") # create a LaTeX file for each person in the list

	text = open("certi.tex") # open the LaTeX document
	text = text.read() # read it
	text_list = list(text) # transform it into a list

	y_name = text.find("%pointname") #search the point for name inclusion
	z_name = len("%pointname")+2
	text_list[y_name+z_name:y_name+z_name] = line # insert the name

	text_final = "".join(text_list) # from list to string

	salida.write(text_final) # save changes in the created file
	salida.close() # closes the file

	run_command(str("pdflatex " + "output" + b + ".tex")) # compile LaTeX a pdf (optional)
	print line #control

run_command(str("pdftk output*.pdf cat output todos_diplomas.pdf")) # create pdf with all the created diplomas (optional)

print "\nAnd we are done! :-)" #control
