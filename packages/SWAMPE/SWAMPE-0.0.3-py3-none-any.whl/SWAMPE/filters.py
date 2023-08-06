
"""
This module contains the functions associated with filters needed for numerical stability.
"""
import numpy as np

def modal_splitting(Xidataslice,alpha):
    """Applies the modal splitting filter from Hack and Jacob (1992).
    
    :param Xidata: data array to be filtered
    :type Xidata: list
    :param alpha: filter coefficient
    :type alpha: float
    :return newxi: filtered data slice 
    :rtype: array of float
    """
    newxi=Xidataslice[1,:,:]+alpha*(Xidataslice[0,:,:]-2*Xidataslice[1,:,:]+Xidataslice[2,:,:])
    return newxi

def diffusion(Ximn,sigma):
    """ Applies the diffusion filter described in Gelb and Gleeson (eq. 12).
    
    :param Ximn: the spectral coefficient data to be filtered
    :type Ximn: list
    :param sigma: the hyperviscosity coefficient
    :type sigma: float
    :return newXimn: filtered spectral coefficient
    :rtype: array of float
    """
    
    newXimn=np.multiply(Ximn,sigma)
    return newXimn


def sigma(M,N,K4,a,dt):
    
    """Computes the coefficient for the fourth degree diffusion filter described in Gelb and
    Gleeson (eq. 12) for vorticity and divergence.

    Parameters
    ----------
    :param M: spectral dimension
    :type M: int
    :param N: highest degree of associated Legendre polynomials
    :type N: int
    :param K4: hyperviscosity coefficient
    :type K4: float
    :param a: planetary radius, m
    :type a: float 
    :param dt: time step,s
    :type dt: float
    Returns
    -------
    :return sigma: coefficient for the diffusion filter for geopotential
    :rtype: array of float

    """
    
    #order of operations following Hack and Jakob code
    sigma=np.zeros((M+1,N+1))
    
    nvec=np.arange(N+1)
    ncoeff=np.multiply(np.multiply(nvec,nvec)/a**2,np.multiply(nvec+1,nvec+1)/a**2)
    factor1=4/a**4
    factor2=2*dt*K4

    sigmacoeff=(1+factor2*(ncoeff-factor1))

    sigmas=np.divide(1,sigmacoeff)
    
    for m in range(M+1):
        sigma[m,:]=sigmas
    
    return sigma

def sigmaPhi(M,N,K4,a,dt):

    """Computes the coefficient for the fourth degree diffusion Filter described in Gelb and
    Gleeson (eq. 12) for geopotential.

    :param M: spectral dimension
    :type M: int
    :param N: highest degree of associated Legendre polynomials
    :type N: int
    :param K4: hyperviscosity coefficient
    :type K4: float
    :param a: planetary radius, m
    :type a: float
    :param dt: time step,s
    :type dt: float
    :return sigma: coefficient for the diffusion filter for geopotential
    :rtype: array of float
    """
    
    sigma=np.zeros((M+1,N+1))
    
    nvec=np.arange(N+1)
    ncoeff=np.multiply(np.multiply(nvec,nvec)/a**2,np.multiply(nvec+1,nvec+1)/a**2)
    factor2=2*dt*K4

    sigmacoeff=(1+factor2*(ncoeff))
    
    sigmas=np.divide(1,sigmacoeff)
    for m in range(M+1):
        sigma[m,:]=sigmas
    
    return sigma


def sigma6(M,N,K4,a,dt):
    
    """Computes the coefficient for the sixth degree diffusion filter 
    for vorticity and divergence.

    :param M: spectral dimension
    :type M: int
    :param N: highest degree of associated Legendre polynomials
    :type N: int
    :param K4: hyperviscosity coefficient
    :type K4: float64
    :param a: planetary radius, m
    :type a: float64 
    :param dt: time step,s
    :type dt: float64

    :return sigma: coefficient for the diffusion filter for geopotential
    :rtype: array of float64
    """


    #order of operations following Hack and Jakob (1992) Fortran code
    sigma=np.zeros((M+1,N+1))
    
    nvec=np.arange(N+1)
    ncoeff=np.multiply(np.multiply(np.multiply(nvec,nvec),nvec)/a**3,np.multiply(np.multiply(nvec+1,nvec+1),nvec+1)/a**3)
    factor1=8/a**6
    factor2=2*dt*K4

    sigmacoeff=(1+factor2*(ncoeff-factor1))

    sigmas=np.divide(1,sigmacoeff)
    
    for m in range(M+1):
        sigma[m,:]=sigmas
    
    return sigma
    


def sigma6Phi(M,N,K4,a,dt):

    """Computes the coefficient for the fourth degree diffusion Filter described in Gelb and
    Gleeson (eq. 12) for geopotential.

    :param M: spectral dimension
    :type M: int
    :param N: highest degree of associated Legendre polynomials
    :type N: int
    :param K4: hyperviscosity coefficient
    :type K4: float
    :param a: planetary radius, m
    :type a: float
    :param dt: time step,s
    :type dt: float
    :return sigma: coefficient for the diffusion filter for geopotential
    :rtype: array of float
    """
    
    sigma=np.zeros((M+1,N+1))
    
    nvec=np.arange(N+1)
    ncoeff=np.multiply(np.multiply(np.multiply(nvec,nvec),nvec)/a**3,np.multiply(np.multiply(nvec+1,nvec+1),nvec+1)/a**3)

    factor2=2*dt*K4

    sigmacoeff=(1+factor2*(ncoeff))
    
    sigmas=np.divide(1,sigmacoeff)
    for m in range(M+1):
        sigma[m,:]=sigmas
    
    return sigma