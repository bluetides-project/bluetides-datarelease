BlueTides
=========

Introduction
------------

These files are the BlueTides_ Friend-of-friend (FOF) Catalogue.

For brieviaty, we include only the following particle types:

- 4 : Star particles
- 5 : Blackhole Particles
- FOFGroups : FOF groups

The container format of these files is BigFile_, which was developed for massively parallel IO
of BlueTides on BlueWaters_. See install_ for installation.

Redshifts
---------

Here is a list of included redshift and the file size. The entire directory can be
mirrored with lftp or curl.

.. include:: summary.txt
..   :literal:

Units
-----

Units are in MP-Gadget internal units : 

- Distance : :math:`h^{-1}\mathrm{Kpc}`
- Velocity : :math:`a \cdot \mathrm{km/s}`
- Mass     : :math:`10^{10} h^{-1} M_\odot`

Useful Constants in this unit:

- Gravity Constant :math:`G = 47003.1`
- Hubble Constant  :math:`H = 0.1`
- Speed of light   :math:`C = 3\times10^5`

Columns
-------

In bigfile a column is represented by a BigBlock. Common blocks are

1. For particles 

.. code::

	4/Mass, 4/Position, 4/Velocity, 
	5/Mass, 5/Position, 5/Velocity, 
	4/StarFormationTime, 
	5/BlackholeMass, 5/BlackholeAccretionRate

2. For FOFGroup

.. code::

	FOFGroups/OffsetByType
	FOFGroups/LengthByType
	FOFGroups/MassByType
	FOFGroups/Mass
	FOFGroups/StarFormationRate
	FOFGroups/BlackholeAccretionRate
	FOFGroups/MassCenterPosition
	FOFGroups/MassCenterVelocity

.. _install:

Install
-------

To install bigfile, clone the repository and use standard python `setup.py`.

.. code:: bash

    git clone https://github.com/rainwoodman/bigfile
    (cd bigfile; python setup.py install --user)

.. WARNING:: 

	Installing bigfile depends on Cython and numpy.

Example
-------

Once a bigfile is opened, access it is similar to a numpy structure array, except slicing is always
required (similar to :code:`pyfits` or :code:`h5py`). In other words, to read from the file, use
:code:`block[start:end]`, where :code:`start` and :code:`end` are the start and end offsets of the range
to be read.

The jump table for accessing the corresponding particle attributes of a halo are stored in
:code:`FOFGroups/LengthByType` and :code:`FOFGroups/OffsetByType`.

.. code:: bash

	python 
	>>> from bigfile import BigFile
	>>> p037 = BigFile('PIG_037')
	>>> print p037['header'].attrs.keys
	['BoxSize', 'HubbleParam', 'MassTable', 'NumFOFGroupsTotal', 
		'NumPartInGroupTotal', 'Omega0', 'OmegaLambda', 'Time']
	>>> print p037['header'].attrs['Time'][0]
	0.0666666663633
	>>> print p037.blocks

	>>> print p037['FOFGroups/Mass'].size
	5332371
	>>> print p037['FOFGroups/MassByType'][:1]
	[[ 0.96118915  4.94944572  0.          0.          0.00673234  0.    ]]
	>>> sel = slice(p037['FOFGroups/OffsetByType'][0][4], 
		p037['FOFGroups/LengthByType'][0][4])
	>>> print p037['4/Mass'][sel].sum()
	0.00673234
	>>> print p037['FOFGroups/MassByType'][0][4]
	0.00673234

.. _BlueTides : http://bluetides-project.org
.. _BigFile : http://github.com/rainwoodman/bigfile
.. _BlueWaters: http://bluewaters.ncsa.illinois.edu

Issues
------

There shall be many issues.  Please file a bug report at

	https://github.com/bluetides-project/bluetides-datarelease/issues/new


