import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/c/Users/luism/Documents/PhD/dummy_v2/workspace/install/dummy_description'
