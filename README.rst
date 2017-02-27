Primes
======

To install this program simply follow these steps:

1. clone this repo ``git clone git@github.com:rob-b/primes.git``
2. `cd` to the directory you cloned to and run ``python setup.py develop``
3. run ``primes 15``


Tests
-----

You can run the tests with ``python setup.py test``. Alternatively you can
runt the following from the checkout root::

  pip install py.test
  py.test tests

To see coverage reports::

  pip install pytest-cov
  py.test  --cov-report term-missing --cov=primes tests/

Warning
-------

Rendering any large amount of output to the terminal is pretty slow and it's
probably better to redirect output for large test sizes to a file and then
read that file in a text editor or just simply pipe the output to `less` i.e.::

   primes 1000 > result.txt
   primes 2500 | less

Improvements
------------
* The matrix multiplication hits the same products more that once. I
  experimented with a more complex version of the matrix function that skips
  calculation its seen before but from experimenting with python's `timeit`
  command I didn't see a clear improvement. I think to really tell would
  require a large sample size which is of course slow to run and since time
  was of the essence I stuck with the simpler version.

* I skimped on rigorous handing of cli args. It's largely mechanical and I
  wanted to concentrate on the main task

* Calculating 20k primes is pretty quick but generating the matrix and drawing
  the output is slow. Ideally I would like to profile and see what can be
  improved (although I suspect for the drawing it's a limitation of the
  terminal)
