import os

import numpy as np
import pyedflib


def test_generator():
    """
    Get an sample EDF-file

    Parameters
    ----------
    None

    Returns
    -------
    f : EdfReader object
       object containing the handle to the file

    Examples
    --------
    >>> import pyedflib.data
    >>> f = pyedflib.data.test_generator()
    >>> f.signals_in_file == 11
    True
    >>> f._close()
    >>> del f

    """
    fname = os.path.join(os.path.dirname(__file__), 'test_generator.edf')
    f = pyedflib.EdfReader(fname)
    return f
