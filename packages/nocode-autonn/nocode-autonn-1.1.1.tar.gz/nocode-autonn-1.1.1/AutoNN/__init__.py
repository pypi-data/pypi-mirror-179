from .CNN.cnn_generator import * 
from .CNN.utils.Device import * 
from .CNN.utils.image_augmentation import * 
from .CNN.utils.EDA import *
import pkg_resources as pk 


__version__ = pk.get_distribution("nocode-autonn").version 
__authors__ ='Anish Konar, Arjun Ghosh, Rajarshi Banerjee, Sagnik Nayak.' 

print(f'''

░█▀▀█ █░░█ ▀▀█▀▀ █▀▀█ ▒█▄░▒█ ▒█▄░▒█ 
▒█▄▄█ █░░█ ░░█░░ █░░█ ▒█▒█▒█ ▒█▒█▒█ 
▒█░▒█ ░▀▀▀ ░░▀░░ ▀▀▀▀ ▒█░░▀█ ▒█░░▀█

Version: {__version__}
An AutoML framework by
Anish Konar, Arjun Ghosh, Rajarshi Banerjee, Sagnik Nayak.
''')
