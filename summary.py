from bigfile import BigFile
from glob import glob
import os
import sys

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            total_size += get_size(os.path.join(dirpath, d))
    return total_size

sys.stdout.write('%05s  %08s  %09s %011s\n'
	% ('=' * 5, '=' * 8, '=' * 9, '=' * 11))

sys.stdout.write('%05s  %08s  %09s %011s\n'
    % ('z', 'path', 'Ngroup', 'size')
)
sys.stdout.write('%05s  %08s  %09s %011s\n'
	% ('=' * 5, '=' * 8, '=' * 9, '=' * 11))

for fn in sorted(glob('PIG_0??')):
    try:
        ff = BigFile(fn)
        a = ff['header'].attrs['Time'][0]
        z = 1 /a - 1
        NGroup = ff['FOFGroups/Mass'].size
        size = get_size(fn)
        sys.stdout.write('%05.02f  %08s  %09d % 8.02f GB\n' % 
            (z, fn, NGroup, size / 1024. / 1024. / 1024.)
        )
    except Exception as e:
        print e
sys.stdout.write('%05s  %08s  %09s %011s\n'
	% ('=' * 5, '=' * 8, '=' * 9, '=' * 11))
