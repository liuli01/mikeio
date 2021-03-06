import clr
import sys
import os
from platform import architecture

mike_bin_path = os.path.join(os.path.dirname(__file__), "bin")
sys.path.append(mike_bin_path)

clr.AddReference("DHI.Generic.MikeZero.DFS")
clr.AddReference("DHI.Generic.MikeZero.EUM")
clr.AddReference("DHI.PFS")
clr.AddReference("DHI.Projections")
clr.AddReference("DHI.Mike1D.ResultDataAccess")
clr.AddReference("DHI.Mike1D.Generic")
clr.AddReference("System")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("System.Runtime")

if "64" not in architecture()[0]:
    raise Exception("This library has not been tested for a 32 bit system.")

from .dfs0 import Dfs0
from .dfs1 import Dfs1
from .dfs2 import Dfs2
from .dfs3 import Dfs3
from .dfsu import Dfsu, Mesh
from .pfs import Pfs
from .xyz import read_xyz
from .dataset import Dataset


def read(filename, items=None, time_steps=None):
    """Read data from a dfs file

    Usage:
        read(filename, item_numbers=None, item_names=None)
    filename
        full path and file name to the dfs file.
    items: list[int] or list[str], optional
            Read only selected items, by number (0-based), or by name
    time_steps: int or list[int], optional
            Read only selected time_steps
            
    Return:
        Dataset(data, time, names)
    """

    _, ext = os.path.splitext(filename)

    if ext == ".dfs0":

        dfs = Dfs0(filename)

    elif ext == ".dfs1":

        dfs = Dfs1(filename)

    elif ext == ".dfs2":

        dfs = Dfs2(filename)

    elif ext == ".dfsu":

        dfs = Dfsu(filename)

    elif ext == ".xyz":
        return read_xyz(filename)
    else:
        raise Exception(f"{ext} is an unsupported extension")

    return dfs.read(items, time_steps)
