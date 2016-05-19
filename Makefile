CURDIR = $(shell pwd)
PACKAGE = $(lastword $(subst /, , $(CURDIR)))

sources:
	spectool --get-files $(PACKAGE).spec
