
**4. Quickstarter Notebook**
============================

**1. Install Jupyter Notebook**

.. code:: console

  >>> pip install jupyterlab

**2. Launch a Jupyter Notebook from the terminal**

.. code:: console

  >>> jupyter lab

**3. Download PowNet from CSI Lab GitHub Repo**

.. code:: console
  
  >>> ! git clone https://github.com/Critical-Infrastructure-Systems-Lab/PowNet.git

**4. Change directory to PowNet folder**

.. code:: python

  >>> import os
  
  >>> os.chdir('PowNet/')
  
  >>> os.getcwd()

**5. Make changes in user input variables**

*[e.g., Model Name or Region of Interest, Simulation Horizon,
Optimization Algorithm]*

.. code:: python

  >>> %load main.py
  
  >>> %save main.py

**6. Add the PYTHONPATH environment variable**

.. code:: python

  >>> import sys
  
  >>> sys.path.append('/Path/to/PowNet Directory/src/')

**7. Run PowNet Simulation**

.. code:: python

  >>> %run main.py
