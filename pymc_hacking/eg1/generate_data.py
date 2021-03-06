#!/usr/bin/env python
from numpy.random import uniform
theta = 0.3
data = [1 if uniform() <= theta else 0 for _i in xrange(100)]
with open("data", "w") as f:
    for data_point in data:
        print >>f, data_point

from pylab import hist, savefig
hist(data)
savefig("data.png")
