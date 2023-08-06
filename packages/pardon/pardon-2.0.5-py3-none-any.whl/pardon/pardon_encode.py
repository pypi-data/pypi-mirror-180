import sys
import collections

import pandas as pd

from . import utility


def _ordinal_encoding_values(data:pd.Series, order_by) -> dict:
    """Get the correct order and values prior to ordinal encoding"""

    vals = data.unique()

    if order_by == 'value':
        vals = sorted(vals)
    elif order_by == 'frequency':
        counts = collections.Counter(data.values)
        vals = sorted(vals, key=lambda x: -counts[x], reverse=True)
    elif isinstance(order_by, list):
        # ensure no values are missing
        missing = utility.list2_differences(list1=order_by, list2=vals)

        if missing:
            raise ValueError(f'The Value(s): {missing} are in the data but not found in the ordinal encoding order_by list. Please include them and try again.')

        vals = order_by
    elif callable(order_by):
        vals = list(set(order_by(data.values)))
    else:
        raise ValueError(f'{order_by} is an unknown ordinal encoding order by argument.')

    nums = list(range(1, len(vals) + 1))
    encoded = dict(zip(vals, nums))

    return encoded