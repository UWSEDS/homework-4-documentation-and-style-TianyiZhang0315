"""
test_dataframe.py
HW3
include 3 test function for dataframes
1.Check that all columns have values of the correct type.
2.Check for nan values.
3.Verify that the dataframe has at least one row.
"""
import pandas as pd
import numpy as np


def check_type(d_f, dtype):
    """check if all columns in df have dtype == type"""
    for types in d_f.dtypes:
        if types != dtype:
            print('This dataframe has incorrect dtype.')
            return False
    print('Pass check_type')
    return True


def check_nan(d_f):
    """function: check if any Nan in df"""
    n_a = d_f.isna()
    for name in n_a.columns:
        for item in n_a[name]:
            if item:
                print('This dataframe contains Nan.')
                return False
    print('Pass check_nan')
    return True


def check_nrow(d_f):
    """check if row >= 1"""
    if d_f.shape[0] >= 1:
        print('Pass check_nrow')
    else:
        print('This dataframe has less than one row.')
        return False
    return True


if __name__ == '__main__':
    DF1 = pd.DataFrame({'Num':[1, 2, 3, 4, 5, 6], \
                        'Alpha': ['a', 'b', 'c', 'd', np.NaN, 'f']})  # has Nan
    DF2 = pd.DataFrame({'Num': [], 'Alpha': []})  # empty df
    DF_P1 = pd.DataFrame({'Num': [1, 2, 3, 4, 5, 6], \
                        'Alpha': ['a', 'b', 'c', 'd', 'e', 'f']})  # pass case for
    # check_nan and check_nrow
    DF_P2 = pd.DataFrame({'Num': [1, 2, 3, 4, 5, 6]})
    check_nan(DF1)
    check_nan(DF_P1)
    check_type(DF_P1, DF_P1.dtypes[0])
    check_type(DF_P2, DF_P1.dtypes[0])
    check_nrow(DF2)
    check_nrow(DF_P1)
