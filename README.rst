BlueTides
=========

These files are the BlueTides FOF Catalogue. For brieviaty, we include only the following
particle types:

4 : Star particles
5 : Blackhole Particles
FOFGroups : the FOF groups

The jump table for accessing the corresponding particle attributes are stored in

	FOFGroups/LengthByType
	FOFGroups/OffsetByType

Units are in MP-Gadget internal units : 

	Distance Kpc/h
	Velocity a * km/s
	Mass 1e10 Msun/h

Useful Constants in this unit:
	G=47003.1
	H=0.1
	C=3e5

The library for accessing these files is BigFile

http://github.com/rainwoodman/bigfile

To install bigfile

.. code : bash

	git clone https://github.com/rainwoodman/bigfile
	(cd bigfile; python setup.py install --user)

.. note : 

	bigfile needs Cython and numpy


	python 
	>>> from bigfile import BigFile
	>>> p037 = BigFile('PIG_037')
	>>> print p037['header'].attrs.keys
	['BoxSize', 'HubbleParam', 'MassTable', 'NumFOFGroupsTotal', 'NumPartInGroupTotal', 'Omega0', 'OmegaLambda', 'Time']
	>>> print p037['header'].attrs['Time'][0]
	0.0666666663633
	>>> print p037['FOFGroups/Mass'].size
	5332371
	>>> print p037['FOFGroups/MassByType'][:1]
	[[ 0.96118915  4.94944572  0.          0.          0.00673234  0.        ]]
	>>> sel = slice(p037['FOFGroups/OffsetByType'][0][4], p037['FOFGroups/LengthByType'][0][4])
	>>> print p037['4/Mass'][sel].sum()
	0.00673234
	>>> print p037['FOFGroups/MassByType'][0][4]
	0.00673234



