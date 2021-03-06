#!/usr/bin/env python
import two_normal_model
from pymc import MCMC
from pymc.Matplot import plot

# do posterior sampling
m = MCMC(two_normal_model)
m.sample(iter=100000, burn=1000)
print(m.stats())

import numpy
for p in ['mean1', 'mean2', 'std_dev', 'theta']:
    numpy.savetxt("%s.trace" % p, m.trace(p)[:])

# draw some pictures
plot(m)
