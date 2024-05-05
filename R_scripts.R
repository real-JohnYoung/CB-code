#####################################################################################
# This simplified script is designed to generate the results depicted in Figure 1 of the publication available at https://doi.org/10.1016/S2589-7500(23)00250-9
# Its aim is to elucidate the specific regression models employed by the authors for the readers' reference
rm(list=ls())
library(bayestestR)
library(caret)
library(gamlss)
library(gamlss.dist)
library(kernlab)
library(mfp)
library(mgcv)
library(rstanarm)
library(tidyverse)

# data_train is a data frame with age (i.e., data_train$age) and a specific morphometric feature (i.e., data_train$region)
data_train <- read.csv("~./data_train.csv")

# linear regression
lm.model <- lm(region~age, data=data_train)

# Bayesian linear regression
blm.model <- stan_glm(region~age, data=data_train)

# Gaussian process regression
gp.model <- gausspr(data_train$age, data_train$region, type= 'regression', kernel="rbfdot")

# multivariate fractional polynomial regression
mfp.model <- mfp(region~fp(age,df=4), data=data_train)

# LMS, reference https://github.com/zuoxinian/CCS/tree/master/H3/GrowthCharts
lms.model <- lms(region, age, method.pb="GAIC", data=data_train,k=5)

# GAMLSS, based on the preferred model of https://doi.org/10.1101/2021.06.14.448106 and https://github.com/dinga92/gamlss_normative_paper 
gamlss.model <- gam(list(region ~ s(age),
                             ~ s(age), 
                             ~ 1, 
                             ~ 1), 
                        data = data_train,
                        family = shash(),
                        optimizer = 'efs')

