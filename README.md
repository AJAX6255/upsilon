# UPSILoN [ Under Development ]
<div align="center">
<img src="https://github.com/dwkim78/upsilon/blob/master/UPSILoN.png">
</div><br>

<font size="4">UPSILoN (<font color="red"><b>U</b></font>biquitous Classification 
of <font color="red"><b>P</b></font>eriodic Variable <font color="red"><b>S</b></font>tars 
using Mach<font color="red"><b>I</b></font>ne 
<font color="red"><b>L</b></font>ear<font color="red"><b>N</b></font>ing) 
aims to classify periodic variable stars 
(e.g. *[Delta Scuti](http://en.wikipedia.org/wiki/Delta_Scuti_variable),
[RR Lyraes](http://en.wikipedia.org/wiki/RR_Lyrae_variable),
[Cepheids](http://en.wikipedia.org/wiki/Cepheid_variable),
[eclipsing binaries](http://en.wikipedia.org/wiki/Binary_star#Eclipsing_binaries),
and [long-period variables](http://en.wikipedia.org/wiki/Long-period_variable_star)*) 
using only single-band optical light-curves **regardless of** survey-specific characteristics 
such as color, magnitude, sampling rate, etc (Kim+ 2015 in preparation).</font>

## Dependency
[Python 2.7+](https://www.python.org/)

[Numpy 1.8+](http://www.numpy.org/)
  
[Scipy 0.14+](http://scipy.org/)

[Matplotlib 1.3+](http://matplotlib.sourceforge.net/)

[sklearn 0.14+](http://scikit-learn.org/stable/)

[pyFFTW 0.9.2+] (http://hgomersall.github.io/pyFFTW/)

### ChangeLog

#### v1.0 (planned)
- release of the first version of UPSILoN.

#### v0.5 (planned)
- add (a) Random Forest classification models.

#### v 0.2.2
- add a module estimating period uncertainty.

#### v0.2.1
- add the UPSILoN logo image.

#### v0.2
- an improved period extracting module using pyFFTW and multi-threads, 
which decreases the extracting time by ~40%.

#### v0.1
- add feature extracting modules.