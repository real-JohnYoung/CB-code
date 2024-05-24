#!/usr/bin/env python
# coding: utf-8

# In[1]:

### This simplified script is designed to generate the results of the Hierarchical Bayesian Regression depicted in Figure 1 of the publication available at https://doi.org/10.1016/S2589-7500(23)00250-9
### Its aim is to elucidate the specific regression models employed by the authors for the readers' reference

### PCN toolkit v0.22 was used as recommended by the leading author of this tool (Dr. Andre F. Marquand)

### details of the the Hierarchical Bayesian Regression can be found in https://github.com/amarquand/PCNtoolkit/blob/v0.22/tests/testHBR.py
import os
import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle
from matplotlib import pyplot as plt
import time
from pcntoolkit.normative_model.norm_utils import norm_init
import matplotlib.pyplot as plt
from pcntoolkit.normative import estimate
from warnings import filterwarnings

# adjust parameter values based on your choice, details see https://github.com/amarquand/PCNtoolkit/blob/v0.22/tests/testHBR.py
nm = norm_init(X_train, Y_train, alg='hbr', init, model_type, random_intercept, random_noise, random_slope, hetero_noise)
nm.estimate(X_train, Y_train, trbefile=processing_roi_dir+'trbefile.pkl')

