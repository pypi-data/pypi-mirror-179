import os
os.environ['THEANO_FLAGS'] = "device=cpu,floatX=float64"#,gcc.cxxflags=-fbracket-depth=1024"
MonoTools_tablepath = os.path.join(os.path.abspath( __file__ ),'MonoTools','data','table')
if os.environ.get('MONOTOOLSPATH') is None:
    MonoData_savepath = os.environ.get('MONOTOOLSPATH')
else:
    MonoData_savepath = os.path.join(os.path.abspath( __file__ ),'MonoTools','data')

#from . import tools
#from . import MonoSearch
#from . import MonoFit
#from . import starpars
