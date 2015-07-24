from bigfile import BigFile
from glob import glob
import sys
sys.stdout.write('%05s  %08s  %08s\n'
	% ('z', 'path', 'Ngroup')
)
for fn in sorted(glob('PIG_0??')):
	try:
		ff = BigFile(fn)
		a = ff['header'].attrs['Time'][0]
		z = 1 /a - 1
		NGroup = ff['FOFGroups/Mass'].size

		sys.stdout.write('%05.02f  %08s  %08d\n' % 
			(z, fn, NGroup)
		)
	except Exception as e:
		print e
