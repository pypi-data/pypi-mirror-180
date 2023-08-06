*jsax: A joint symbolic approximation method.*

[![!pypi](https://img.shields.io/pypi/v/jsax?color=green)](https://pypi.org/project/sax/)

To install this package, use

```
pip install jsax
```

### symbolic representation

```
import numpy as np


# generate 100 time series of length 1000
data = np.random.randn(100, 1000)
data = data - data.mean(axis=0)


# employ joint symbolic representation
pabba = JABBA(tol=0.5, init='agg', alpha=1, auto_digitize=False, verbose=0)
symbols = pabba.fit_transform(data)
```

### generate semantic embedding for symbolic time series representation

```Python

from jsax.preprocessing import encoders 

# will use the ABBA embedding here, use the centers as embedding so without additional embedding layer training.
param = pabba.parameters # ABBA model parameters, including centers, and hash mapping

# the less the percent (\in (0, 1] it uses, the more truncation of the sentence will be)

#  load the params, and use the hash mapping for categorical encoding
ec = encoders(dictionary=param.hashm) 
 # copnvert the symbols into categorical interger.
categorical_data = ec.categorical_encode(symbols)

# get length that cover 30% sequences
length = ec.return_percent_len(categorical_data, percent=0.3) 

# generate padding sequences
paddings = ec.pad_sequence(categorical_data,
                           maxlen=length, value='none', 
                           method = "post", truncating='post')
```
