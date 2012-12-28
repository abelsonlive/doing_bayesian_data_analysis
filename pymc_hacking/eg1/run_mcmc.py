#!/usr/bin/env python
import simple_bernoulli_model
from pymc import MCMC
from pymc.Matplot import plot

# do posterior sampling
M = MCMC(simple_bernoulli_model)
M.sample(iter=100)

# draw some pictures
plot(M)
