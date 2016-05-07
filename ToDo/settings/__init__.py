from .base import *

try:
	from .local import *
	live = False
except:
	live = true

if live:
	from .production import *