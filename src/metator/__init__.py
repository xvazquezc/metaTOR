#!/usr/bin/env python3
import importlib.util
from pathlib import Path
import os
from .version import __version__ as version
from . import *

__author__ = "Amaury Bignaud, Jacques Serizay, Lyam Baudry, Théo Foutel-Rodier, Martial Marbouty"
__copyright__ = "Copyright © 2017-2025, Institut Pasteur, Paris, France"
__credits__ = [
    "Amaury Bignaud",
    "Jacques Serizay",
    "Lyam Baudry",
    "Théo Foutel-Rodier",
    "Martial Marbouty",
    "Axel Cournac",
    "Vittore Scolari",
    "Romain Koszul",
]
__license__ = "GPLv3"
__maintainer__ = "Amaury Bignaud"
__email__ = "amaury.bignaud@pasteur.fr"
__status__ = "Alpha"
__version__ = version


__metator_source__ = os.path.dirname(importlib.util.find_spec("metator").origin)  # type: ignore
__metator_root__ = __metator_source__
# In a src-layout editable install, bin/ is at ../../ relative to the source
_candidate_root = os.path.abspath(os.path.join(__metator_source__, "../../"))
if os.path.isdir(os.path.join(_candidate_root, "bin")):
    __metator_root__ = _candidate_root
__bin_dir__ = Path(__metator_root__, "bin")
LEIDEN_PATH = str(next(__bin_dir__.glob("networkanalysis-1.3.0*.jar")))
LOUVAIN_PATH = str(__bin_dir__)
