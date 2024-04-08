import numpy as np
import pandas as pd

def check(*args):
    try:
        pd.Series(*args)
    except Exception as e:
        return str(e)
    return 'ok'


def other_function():
    return np.random.rand(10)
