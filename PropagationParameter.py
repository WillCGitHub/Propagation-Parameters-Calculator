import math
from math import degrees
import cmath
epsilon_0 = 8.854187817*math.pow(10,-12)
mu_0 = 4*math.pi*math.pow(10,-7)

#propagation parameters of material medium

def alpha(omega, mu, epsilon, sigma):
	temp1 = omega*math.sqrt(mu*epsilon)/(math.sqrt(2))
	temp2 = math.sqrt(1+math.pow(sigma/(omega*epsilon),2))-1
	temp3 = math.sqrt(temp2)
	a = temp1*temp3
	print("Alpha is: {} Np/m".format(round(a,3)))
	return a

def beta(omega, mu, epsilon, sigma):
	temp1 = omega*math.sqrt(mu*epsilon)/(math.sqrt(2))
	temp2 = math.sqrt(1+math.pow(sigma/(omega*epsilon),2))+1
	temp3 = math.sqrt(temp2)
	b = temp1*temp3
	print("Beta is: {} rad/s".format(round(b,3)))
	return b;

def waveLength(beta):
	w = 2*math.pi/(beta)
	print("wave length is: {} m".format(round(w,3)))
	return w

def phaseVelocity(omega,beta):
	pV = omega/beta
	print("Phase velocity is: {} m/s".format(round(pV,3)))


def intrinsicImped(omega,mu,sigma,epsilon):
	n = complex(0,omega*mu)
	d = complex(sigma,omega*epsilon)
	Eta = cmath.sqrt(n/d)
	real_eta = cmath.polar(Eta)[0]
	phase = cmath.polar(Eta)[1]
	phase = degrees(phase)

	print("Intrinsic impedance(complex) is: {}+{}j ohm".format(round(Eta.real,3),round(Eta.imag,3)))
	print("|Eta|= {} ohm".format(round(real_eta,3)))
	print("phase angle is: {}".format(phase))
	return Eta

sig = math.pow(10,-3)
ome = 2*math.pi*math.pow(10,6)
a = alpha(ome,mu_0,6*epsilon_0,sig)
b = beta(ome,mu_0,6*epsilon_0,sig)

waveL = waveLength(b)
phaseVelocity(a,b)

iI = intrinsicImped(ome,mu_0,sig,6*epsilon_0)







