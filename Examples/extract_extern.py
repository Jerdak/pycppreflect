#!/usr/bin/env python
import os
import sys
import clang.cindex

from clang.cindex import Index
from pprint import pprint
from optparse import OptionParser, OptionGroup

# assume pccppreflect python module is 1 level up and not in /python/lib
sys.path.append("..")
from pycppreflect.sbind import *
 


# 1. Manually append current working directory to OS path
# 2. Then make sure libclang.dll or libclang.so is in the current directory.*
# * http://eli.thegreenplace.net/2011/07/03/parsing-c-in-python-with-clang/ (See 'Setting Up')
if sys.platform in ['win32','cygwin']:
	os.environ['PATH'] = os.environ['PATH']  + os.getcwd()
elif sys.platform in ['linux2']:
	os.environ['LD_LIBRARY_PATH '] = os.environ['LD_LIBRARY_PATH ']  + os.getcwd()


def parse_cursor(cursor):
	"""	Parse Clang cursor for LINKAGE specs
	
	@notes:
		LINKAGE_SPEC (http://clang.llvm.org/doxygen/classclang_1_1LinkageSpecDecl.html)
		Represents code of the type:  extern "C" void foo()
	"""
	
	if cursor.kind == clang.cindex.CursorKind.LINKAGE_SPEC:
		
		
		fns = ExternDecl.create_functions(cursor)
		for f in fns:
			f.dump()

	# Recurse for children of this cursor
	for c in cursor.get_children():
		parse_cursor(c)	

def main():
	global opts

	parser = OptionParser("usage: %prog {filename} [clang-args*]")
	parser.disable_interspersed_args()
	(opts, args) = parser.parse_args()

	if len(args) == 0:
		print "invalid number arguments"
		
	sparser = Parser()
	sparser.is_recursive = True
	sparser.is_relative = True
	sparser.parse(sys.argv[1])

	
	'''if len(args) == 0:
		print 'invalid number arguments'

	index = Index.create()
	tu = index.parse(sys.argv[1], args=['-x', 'c++','-cc1'])
	
	if not tu:
		print "unable to load input"

	parse_cursor(tu.cursor)
	'''
if __name__ == '__main__':
    main()