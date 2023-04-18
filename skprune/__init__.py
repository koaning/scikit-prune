import numpy as np
from sklearn.pipeline import Pipeline


def _prune_attributes(obj):
    """Function to call internally that can cast a single object."""
    if hasattr(obj, "__dict__"):
        for attr, value in obj.__dict__.items():
            if not attr.startswith("__"):
                if isinstance(value, np.ndarray):
                    if "float" in str(value.dtype):
                        setattr(obj, attr, value.astype("float16"))
            _prune_attributes(value)
    return obj

def prune(obj):
    """
    Prune a scikit-learn object. 
    
    Take a scikit-learn object and casting all float64 properties to float16 
    to make it slightly more lighter for memory/disk.
    """
    if isinstance(obj, Pipeline):
        for name, step in obj.steps:
            _prune_attributes(step)
        return obj
    return _prune_attributes(obj)
