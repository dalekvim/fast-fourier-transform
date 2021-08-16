**********************
Fast Fourier Transform
**********************

A simple implimentation of the Fast Fourier Transfrom.

=====
Usage
=====

Installation
------------

You can either download the zip file by clicking the dropdown button that reads **Code** and then **Download ZIP**.

Or, if you have git installed on your device::

  git clone https://github.com/Dalekvim/fast-fourier-transform.git

Once its finished downloading, change directory in to the root of the project using ``cd fast-fourier-transform``.

Since this project uses Pipenv as its package manager. If you don't have it, you can get it using ``pip``::

  pip install pipenv
  
Once that's done you can install the dependencies::
 
  pipenv install --ignore-pipfile
  
Or if you want the dev dependencies too::
 
  pip install --dev

  
Examples
--------

Polynomial
^^^^^^^^^^

.. code-block:: python

  from fft.polynomial import Polynomial as Poly
  
  # Polynomial allows you to make polynomials using a list of coefficients (going to highest to smallest powers).
  f = Poly([3, 1, 2]) # 3 + x + 2xx
  
  f(1) # Returns 6.

Roots of Unity
^^^^^^^^^^^^^^

.. code-block:: python
 
  from fft.roots_of_unity import NthRootsOfUnity
  
  NthRootsOfUnity(4) # Returns [1, 1j, -1, -1j]
  
Fast Fourier Transform
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  from fft import fft
  
  square = Poly([0, 0, 1])
  
  fft(square) # Returns [1, -1, 1, -1]
