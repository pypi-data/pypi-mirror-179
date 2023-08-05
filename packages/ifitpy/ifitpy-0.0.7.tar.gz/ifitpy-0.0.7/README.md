# Pyfit

```
pip install ifitpy
```

This fit package permits to, well, fit a given x,y data. It encapsulates both iminuit and curve_fit.
There are two type of functions. Simple (linear, expo) and Complex(gaussian, gaussian2d, poly).
For Simple function `fit(x,y)` are `fit(x,y,p0)` are valid inputs. In the first option the fit attempts to estimate the initial starting point. In the second option, a list of parameters (p0) is used to initialized the fit.

For Complex functions `fit(x,y, n)` are `fit(x,y,p0)` are valid inputs. If n is used, then the algorithm will use this value to generate the fitting function with n components. For example, `fit(xx,yy,n=3)` will fit a sum of two gaussian(2d) or a 3-degree polonimal function. And p0 zero is also estimated. If `fit(x,y,n,p0)` is used, then p0 will be the initialization parameters. Note that `len(p0) = n*parameters_to_fit`.

There's also a `f.fitBinned(xx,yy,bins=50)` option which allows fitting a profile histogram instead of the raw data. This option is often faster and is the recommended one as it takes into account the statistical fluctuation of the data.
Don't forget to check the Tutorial notebook.

### To extract the fit results use
```
from ifitpy import Fitter
f = Fitter("linear") #linear, expo, gaussian, gaussian2d, poly
f.fit([0,10], [0,-10])
p = f.getParams()
print(p) # prints a string with the available variables.
print(p.vars) # list of the results
print(p.m) # slope for the “linear” type
print(p.b) # slope for the “intercept” type
```
### This an ongoing project!
