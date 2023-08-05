import workcell

# define the version before the other imports since these need it
__version__ = workcell.__version__

from .core import Workcell 
from .core import format_workcell_path, format_workcell_name
