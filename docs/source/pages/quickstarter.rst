
**4. Quickstarter Notebook**
============================

**# Install Jupyter Notebook**

>>> pip install jupyterlab

**# Launch a Jupyter Notebook from the terminal**

>>> jupyter lab

**# Download PowNet from CSI Lab GitHub Repo**

>>> ! git clone
https://github.com/Critical-Infrastructure-Systems-Lab/PowNet.git

**# Change directory to PowNet folder**

>>> import os

>>> os.chdir('PowNet/')

>>> os.getcwd()

**# Make changes in user input variables**

**[e.g., Model Name or Region of Interest, Simulation Horizon,
Optimization Algorithm]**

>>> %load main.py

*Edit the highlighted lines:*

*# ------- User defined inputs*

*:mark:`MODEL_NAME = 'laos_2016’`*

*# The default simulation horizon T is 24 hours*

*:mark:`T = 24`*

*# One year has 8760 hours. If T = 24, then we have 365 steps.*

*# STEPS = math.floor(8760/T)*

*:mark:`STEPS = 5`*

*# Decide whether to save results*

*:mark:`SAVE_RESULT = False`*

*:mark:`SAVE_PLOT = False`*

*#############################*

>>> %save main.py

**# Add the PYTHONPATH environment variable**

>>> import sys

sys.path.append('/Path/to/PowNet/src/ ')

**# Run PowNet Simulation**

>>> %run main.py

**
**
