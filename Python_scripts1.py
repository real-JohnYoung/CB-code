#!/usr/bin/env python
# coding: utf-8

# In[1]:

### This simplified script is designed to generate the results of the Wraped Bayesian Linear Regression depicted in Figure 1 of the publication available at https://doi.org/10.1016/S2589-7500(23)00250-9
### Its aim is to elucidate the specific regression models employed by the authors for the readers' reference

### PCNtoolkit v0.22 was used as recommended by the leading author of this tool (Dr. Andre F. Marquand)

import os
import pandas as pd
import pcntoolkit as pcn
import numpy as np
import pickle
from matplotlib import pyplot as plt
import time
from itertools import chain
from pcntoolkit.normative import estimate, evaluate
from pcntoolkit.util.utils import create_bspline_basis, compute_MSLL
from sklearn.model_selection import train_test_split

### details of the the Warped Bayesian Linear Regression can be found in https://pcntoolkit.readthedocs.io/en/latest/pages/BLR_normativemodel_protocol.html

# different optimizers (i.e., 'powell', 'nelder-mead', 'cg', and 'l-bfgs-b') have been tested, and 'powell' gives the best performance
yhat_test, s2_test, nm_test, Z_test, metrics_test = estimate(cov_file_tr, 
                                                             resp_file_tr, 
                                                             testresp = resp_file_te, 
                                                             testcov = cov_file_te,
                                                             alg = 'blr',
                                                             optimizer = 'powell',
                                                             savemodel = True,
                                                             saveoutput = True, 
                                                             standardize = False)
