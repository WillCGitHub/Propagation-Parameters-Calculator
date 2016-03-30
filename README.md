# Propagation-Parameters-Calculator
 Save your time from propagation parameter calculation.

==Python 3.5==

based on the library math and cmath 
===
This program include the constants of Vaccum permeability and Vaccum permittivity as mu_0 and epsilon_0.

=====
For Alpha, it takes the arguments: omega, mu, epsilon, sigma. Return a float
 alpha(omega, mu, epsilon, sigma):
=====
Beta is similar to Alpha.Return a float
 beta(omega, mu, epsilon, sigma):
=====
Wave length calculation takes the argument beta.Return a float
 waveLength(beta):
=====
Phase velocity takes the argument omega and beta.Return a float
 phaseVelocity(omega,beta):
=====
Intrinsic Impedance takes the argument:omega,mu,sigma,epsilon. Return a complex number
 intrinsicImped(omega,mu,sigma,epsilon):
