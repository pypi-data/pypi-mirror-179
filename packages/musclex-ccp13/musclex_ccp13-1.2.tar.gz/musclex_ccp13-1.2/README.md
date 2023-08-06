# musclex_ccp13
Three methods of background subtractions from [CCP13 fortran codes](https://github.com/scattering-central/CCP13)
There are some modification to the original codes in order to make it easier to build as a python library 
and called from python script. 

The library includes ..
1. Paul Langan's "roving window" method. 
2. Calculation of a circularly-symmetric background. 
3. Calculation of a "smoothed" background through iterative low-pass filtering based on the method of M.I. Ivanova and L. Makowski (Acta Cryst. (1998) A54, 626-631).

These methods are described fully [Here](http://www.diamond.ac.uk/Beamlines/Soft-Condensed-Matter/small-angle/SAXS-Software/CCP13/XFIX.html#background_section)

This package is available on PyPI under name musclex_ccp13. You can install the package by

pip install musclex_ccp13

**This package will be automatically installed by Muscle X**