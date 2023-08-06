from workcell.core import Workcell
from workcell.api import create_api


app = create_api(Workcell("function/app.py"))