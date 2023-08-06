# Numla Package

Fast numpy LAbeled aRRaY for financial time series data. Simply load, slice, cache, and analyze. Accelerators: C, Numba, Vectorization.

pip3 install numla

from numla import larry 

or

import numla as la

>>>>ohlcv = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

>>>>label = [['open', 'high', 'low', 'close', 'volume'], ['2022-01-17 00:00:00', '2022-01-18 00:00:00']]

>>>>dk = larry(ohlcv, label, dtype=float)

>>>or

>>>>dk = larry(dataframe)