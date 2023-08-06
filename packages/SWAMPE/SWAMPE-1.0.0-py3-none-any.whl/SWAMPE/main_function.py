# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:03:08 2021

@author: ek672

This is the main SWAMP-E function. It calls the timestepping function.
"""

## Import statements
# Import python packages
import numpy as np

# Import program packages
from . import initial_conditions as ic
from . import spectral_transform as st
from . import time_stepping as tstep
from . import plotting
from . import forcing
from . import filters
from . import continuation as cont



def main(M,dt,tmax,Phibar, omega, a, test, g=9.8, forcflag=1, taurad=86400, taudrag=86400, DPhieq=4*(10**6), a1=0.05, plotflag=1, plotfreq=5, minlevel=6, maxlevel=7, diffflag=1,modalflag=1,alpha=0.01,contflag=0,saveflag=1,expflag=0,savefreq=150,k1=2*10**(-4), k2=4*10**(-4), pressure=100*250*9.8/10, R=3000, Cp=13000, sigmaSB=5.7*10**(-8),K6=1.24*10**33,custompath=None,contTime=None,timeunits='hours'):    
 
    
    """
    Parameters
    ----------
    :param M: spectral resolution
    :type M: int
    
    :param dt: length of time step, in seconds
    :type dt: float64
    
    :param tmax: number of time steps to run
    :type tmax: int
    
    :param Phibar: mean geopotential, m^2/s^2
    :type Phibar: float64

    :param omega: planetary rotation rate, radians
    :type omega: float64
    
    :param a: planetary radius, m
    :type a: float64
    
    :param test: TYPE
        DESCRIPTION.
    g : TYPE, optional
        DESCRIPTION. The default is 9.8.
    forcflag : TYPE, optional
        DESCRIPTION. The default is 1.
    taurad : TYPE, optional
        DESCRIPTION. The default is 86400.
    taudrag : TYPE, optional
        DESCRIPTION. The default is 86400.
    DPhieq : TYPE, optional
        DESCRIPTION. The default is 4*(10**6).
    a1 : TYPE, optional
        DESCRIPTION. The default is 0.05.
    plotflag : TYPE, optional
        DESCRIPTION. The default is 1.
    plotfreq : TYPE, optional
        DESCRIPTION. The default is 5.
    minlevel : TYPE, optional
        DESCRIPTION. The default is 6.
    maxlevel : TYPE, optional
        DESCRIPTION. The default is 7.
    diffflag : TYPE, optional
        DESCRIPTION. The default is 1.
    modalflag : TYPE, optional
        DESCRIPTION. The default is 1.
    alpha : TYPE, optional
        DESCRIPTION. The default is 0.01.
    contflag : TYPE, optional
        DESCRIPTION. The default is 0.
    saveflag : TYPE, optional
        DESCRIPTION. The default is 1.
    savefreq : TYPE, optional
        DESCRIPTION. The default is 150.
    k1 : TYPE, optional
        DESCRIPTION. The default is 2*10**(-4).
    k2 : TYPE, optional
        DESCRIPTION. The default is 4*10**(-4).
    pressure : TYPE, optional
        DESCRIPTION. The default is 100*250*9.8/10.
    R : TYPE, optional
        DESCRIPTION. The default is 3000.
    Cp : TYPE, optional
        DESCRIPTION. The default is 13000.
    sigmaSB : TYPE, optional
        DESCRIPTION. The default is 5.7*10**(-8).

    Returns
    -------
    None.

    """


    #positional: M, dt, tmax, Phibar, g, omega, a, test
    #optional: taurad, taudrag, DPhieq, a1, minlevel, maxlevel, forcflag, diffflag, modalflag, alpha, plotflag, plotfreq, contflag, saveflag, savefreq, k1, k2, pressure, Cp, R, sigmaSB 
    
    #get other dimensional parameters using the spectral dimension
    N,I,J,otherdt,K4,lambdas,mus,w=ic.spectral_params(M)
    
    
    # dt=dt1
    # Associated Legendre Polynomials and their derivatives
    Pmn, Hmn = st.PmnHmn(J, M, N, mus)
    #K6=1.24*10**33 #added 3 orders of magnitude for the reduced resolution
    sigma=filters.sigma6(M,N,K6,a, dt)
    sigmaPhi=filters.sigma6Phi(M, N, K6, a, dt)
        
    #Earth sigma
    # sigma=filters.sigma(M,M,K4,6.37122*10**(6),1200)
    # sigmaPhi=filters.sigmaPhi(M, M, K4, 6.37122*10**(6), 1200)
    

        
    ## Initialize data arrays 
   
    etadata=np.zeros((3,J,I))
    deltadata=np.zeros((3,J,I))
    Phidata=np.zeros((3,J,I))
    
    etamdata=np.zeros((3,J,M+1),dtype=complex)
    deltamdata=np.zeros((3,J,M+1),dtype=complex)
    Phimdata=np.zeros((3,J,M+1),dtype=complex)
    
    etamndata=np.zeros((3,M+1,N+1),dtype=complex)
    deltamndata=np.zeros((3,M+1,N+1),dtype=complex)
    Phimndata=np.zeros((3,M+1,N+1),dtype=complex)
    
    Udata=np.zeros((3,J,I))
    Vdata=np.zeros((3,J,I))
    
    Umdata=np.zeros((3,J,M+1),dtype=complex)
    Vmdata=np.zeros((3,J,M+1),dtype=complex)
    
    Adata=np.zeros((3,J,I))
    Bdata=np.zeros((3,J,I))
    Cdata=np.zeros((3,J,I))
    Ddata=np.zeros((3,J,I))
    Edata=np.zeros((3,J,I))
    
    Amdata=np.zeros((3,J,M+1),dtype=complex)
    Bmdata=np.zeros((3,J,M+1),dtype=complex)
    Cmdata=np.zeros((3,J,M+1),dtype=complex)
    Dmdata=np.zeros((3,J,M+1),dtype=complex)
    Emdata=np.zeros((3,J,M+1),dtype=complex)
    
    Fdata=np.zeros((3,J,I))
    Gdata=np.zeros((3,J,I))
    
    Fmdata=np.zeros((3,J,M+1),dtype=complex)
    Gmdata=np.zeros((3,J,M+1),dtype=complex)
    
    Phiforcingdata=np.zeros((3,J,I))
    Phiforcingmdata=np.zeros((3,J,M+1),dtype=complex)
    
    #long arrays
    spinupdata=np.zeros((tmax,2))
    
    geopotdata=np.zeros((tmax,2))
    
    
    #coriolis
    fmn=ic.coriolismn(M, omega)
    
    tstepcoeffmn=tstep.tstepcoeffmn(M,N,a)
    tstepcoeff=tstep.tstepcoeff(J,M,dt,mus,a)
    tstepcoeff2=tstep.tstepcoeff2(J,M,dt,a)
    mJarray=tstep.mJarray(J,M)
    marray=tstep.marray(M, N)
    narray=tstep.narray(M,N)
        
    

    if contflag==0:
        SU0, sina, cosa, etaamp,Phiamp=ic.test1_init(a, omega, a1)
        
        if test==1:
            etaic0, etaic1, deltaic0, deltaic1, Phiic0, Phiic1=ic.state_var_init(I,J,mus,lambdas,test,etaamp,a,sina,cosa,Phibar,Phiamp)
        elif test==2:
            etaic0, etaic1, deltaic0, deltaic1, Phiic0, Phiic1=ic.state_var_init(I,J,mus,lambdas,test,etaamp,a,sina,cosa,Phibar,Phiamp)   
        elif test==9 or test==10 or test==11:
            etaic0, etaic1, deltaic0, deltaic1, Phiic0, Phiic1=ic.state_var_init(I,J,mus,lambdas,test,etaamp)
        
        Uic,Vic=ic.velocity_init(I,J,SU0,cosa,sina,mus,lambdas,test)
    
    elif contflag==1:
        
        if custompath==None:

            etaic0=cont.read_pickle('eta-'+str(contTime))
            etaic1 = etaic0

            deltaic0=cont.read_pickle('delta-'+str(contTime))
            deltaic1 = deltaic0

            Phiic0=cont.read_pickle('Phi-'+str(contTime))
            Phiic1 = Phiic0
        else:
            etaic0=cont.read_pickle('eta-'+str(contTime),custompath=custompath)
            etaic1 = etaic0

            deltaic0=cont.read_pickle('delta-'+str(contTime),custompath=custompath)
            deltaic1 = deltaic0

            Phiic0=cont.read_pickle('Phi-'+str(contTime),custompath=custompath)
            Phiic1 = Phiic0
            

        
        etam0=st.fwd_fft_trunc(etaic0, I, M)
        etamn0=st.fwd_leg(etam0,J,M,N,Pmn,w)
        deltam0=st.fwd_fft_trunc(deltaic0, I, M)
        deltamn0=st.fwd_leg(deltam0,J,M,N,Pmn,w)
        
        Uiccomp,Viccomp=st.invrsUV(deltamn0,etamn0,fmn,I,J,M,N,Pmn,Hmn,tstepcoeffmn,marray)
        Uic=np.real(Uiccomp)
        Vic=np.real(Viccomp)
        
    Aic,Bic,Cic,Dic,Eic=ic.ABCDE_init(Uic,Vic,etaic0,Phiic0,mus,I,J)
    
    
    ## Store initial conditions in the data arrays files for easy access
    etadata[0,:,:]=etaic0
    etadata[1,:,:]=etaic1
    
    deltadata[0,:,:]=deltaic0
    deltadata[1,:,:]=deltaic1
    
    Phidata[0,:,:]=Phiic0
    Phidata[1,:,:]=Phiic1
    
    Udata[0,:,:]=Uic
    Udata[1,:,:]=Uic
    
    Vdata[0,:,:]=Vic
    Vdata[1,:,:]=Vic
    
    Adata[0,:,:]=Aic
    Adata[1,:,:]=Aic
    
    Bdata[0,:,:]=Bic
    Bdata[1,:,:]=Bic
    
    Cdata[0,:,:]=Cic
    Cdata[1,:,:]=Cic
    
    Ddata[0,:,:]=Dic
    Ddata[1,:,:]=Dic
    
    Edata[0,:,:]=Eic
    Edata[1,:,:]=Eic
    
    
    
    # Spin Up calculations
    spinupdata[0,0] = np.min(np.sqrt(Udata[0,:,:]**2 + Vdata[0,:,:]**2 ))
    #spinupdata[0,1] = np.max(np.sqrt(Udata[0,:,:]**2 + Vdata[0,:,:]**2 ))
    
    spinupdata[0,1]=tstep.RMS_winds(a, I, J, lambdas, mus, Udata[0,:,:], Vdata[0,:,:])
    
    
    #geopotential calculations
    
    geopotdata[0,0]=np.min(Phidata[0,:,:])
    geopotdata[0,1]=np.max(Phidata[0,:,:])
    
    
    #### Forcing ####
    if test==9:
        
        Phieq=forcing.Phieq_basic_state(I,J,mus,Phibar)
        
        Q=forcing.Qfun(Phibar+2000, Phiic0,Phibar, taurad)

        #geopotential forcing to be passed to time stepping
        PhiF=Q
        #print(np.max(Q))
        F,G=forcing.Rfun(Uic, Vic, -1*np.ones((J,I)), Phiic0,Phibar,taudrag)
        
        Phiforcingdata[0,:,:]=PhiF
        Phiforcingdata[1,:,:]=PhiF
        
        
        F,G=forcing.Rfun(Uic, Vic, Q, Phiic0,Phibar,taudrag)
        Fdata[0,:,:]=F
        Fdata[1,:,:]=Fdata[0,:,:]
        Gdata[0,:,:]=G
        Gdata[1,:,:]=Gdata[0,:,:]
    
    
    elif test==10:
        Phieq=forcing.Phieqfun(Phibar, DPhieq, lambdas, mus, I, J, g)
        
        Q=forcing.Qfun(Phieq, Phiic0, Phibar,taurad)
        
        #geopotential forcing to be passed to time stepping
        PhiF=Q
        
        Phiforcingdata[0,:,:]=PhiF
        Phiforcingdata[1,:,:]=PhiF
        
        
        F,G=forcing.Rfun(Uic, Vic, Q, Phiic0,Phibar,taudrag)
        Fdata[0,:,:]=F
        Fdata[1,:,:]=Fdata[0,:,:]
        Gdata[0,:,:]=G
        Gdata[1,:,:]=Gdata[0,:,:]
    elif test==11:

        
        Teq=forcing.DoubleGrayTEqfun(Phibar,DPhieq,lambdas,mus,I,J,k1,k2,pressure,g,R,Cp,sigmaSB)

        Q=forcing.DoubleGrayPhiForcing(Teq,Phiic0,Phibar,k2,sigmaSB,Cp,R)
        #geopotential forcing to be passed to time stepping
        PhiF=Q
        
        Phiforcingdata[0,:,:]=PhiF
        Phiforcingdata[1,:,:]=PhiF
        
        
        F,G=forcing.Rfun(Uic, Vic, Q, Phiic0,Phibar,taudrag)
        Fdata[0,:,:]=F
        Fdata[1,:,:]=Fdata[0,:,:]
        Gdata[0,:,:]=G
        Gdata[1,:,:]=Gdata[0,:,:]
        
    
    
    ####
    #Forward Fourier and Legendre transform
    ####
    
    ## FFT    
    
    Amdata[0,:,:]=st.fwd_fft_trunc(Aic, I, M)
    Amdata[1,:,:]=Amdata[0,:,:]
    
    Bmdata[0,:,:]=st.fwd_fft_trunc(Bic, I, M)
    Bmdata[1,:,:]=Bmdata[0,:,:]
    
    Cmdata[0,:,:]=st.fwd_fft_trunc(Cic, I, M)
    Cmdata[1,:,:]=Cmdata[0,:,:]
    
    Dmdata[0,:,:]=st.fwd_fft_trunc(Dic, I, M)
    Dmdata[1,:,:]=Dmdata[0,:,:]
    
    Emdata[0,:,:]=st.fwd_fft_trunc(Eic, I, M)
    Emdata[1,:,:]=Emdata[0,:,:]
    
    etamdata[0,:,:]=st.fwd_fft_trunc(etaic0, I, M)
    etamdata[1,:,:]=etamdata[0,:,:]
    
    deltamdata[0,:,:]=st.fwd_fft_trunc(deltaic0, I, M)
    deltamdata[1,:,:]=deltamdata[0,:,:]
    
    Phimdata[0,:,:]=st.fwd_fft_trunc(Phiic0, I, M)
    Phimdata[1,:,:]=Phimdata[0,:,:]
    
    
    ## Forcing Fourier transform ##
    
    Phiforcingmdata[0,:,:]=st.fwd_fft_trunc(Phiforcingdata[0,:,:], I, M)
    Phiforcingmdata[1,:,:]=Phiforcingmdata[0,:,:]
    
    Fmdata[0,:,:]=st.fwd_fft_trunc(Fdata[0,:,:], I, M)
    Fmdata[1,:,:]=Fmdata[0,:,:]
    
    Gmdata[0,:,:]=st.fwd_fft_trunc(Gdata[0,:,:], I, M)
    Gmdata[1,:,:]=Gmdata[0,:,:]
    
    Umdata[0,:,:]=st.fwd_fft_trunc(Udata[0,:,:], I, M)
    Umdata[1,:,:]=Umdata[0,:,:]
    
    Vmdata[0,:,:]=st.fwd_fft_trunc(Vdata[0,:,:], I, M)
    Vmdata[1,:,:]=Vmdata[0,:,:]
    
    
    
    ## Forward Legendre
    
    etamndata[0,:,:]=st.fwd_leg(etamdata[0,:,:],J,M,N,Pmn,w)
    etamndata[1,:,:]=etamndata[0,:,:]
    
    deltamndata[0,:,:]=st.fwd_leg(deltamdata[0,:,:],J,M,N,Pmn,w)
    deltamndata[1,:,:]=deltamndata[0,:,:]
    
    Phimndata[0,:,:]=st.fwd_leg(Phimdata[0,:,:],J,M,N,Pmn,w)
    Phimndata[1,:,:]=Phimndata[0,:,:]
    
    ####
    # Time stepping
    ####
    
    for t in range(2,tmax):
        # print('t='+str(t))
        
        etam0=etamdata[0,:,:]
        etam1=etamdata[1,:,:]
        
        deltam0=deltamdata[0,:,:]
        deltam1=deltamdata[1,:,:]
        
        Phim0=Phimdata[0,:,:]
        Phim1=Phimdata[1,:,:]
        
        Am=Amdata[1,:,:]
        Bm=Bmdata[1,:,:]
        Cm=Cmdata[1,:,:]    
        Dm=Dmdata[1,:,:]
        Em=Emdata[1,:,:]
        
        
        #forcing 
        Um=Umdata[1,:,:]
        Vm=Vmdata[1,:,:]
        
        Fm=Fmdata[1,:,:]
        Gm=Gmdata[1,:,:]
        
    
        PhiFm=Phiforcingmdata[1,:,:]    
        
        newetamn,neweta,newdeltamn,newdelta,newPhimn,newPhi,newU,newV=tstep.tstepping(etam0,etam1,deltam0,deltam1,Phim0,Phim1,I,J,M,N,Am,Bm,Cm,Dm,Em,Fm,Gm,Um,Vm,fmn,Pmn,Hmn,w,tstepcoeff,tstepcoeff2,tstepcoeffmn,marray,mJarray,narray,PhiFm,dt,a,K4,Phibar,taurad,taudrag,forcflag,diffflag,expflag,sigma,sigmaPhi,test,t)
        
        
        #write new data
        etamndata[2,:,:]=newetamn
        deltamndata[2,:,:]=newdeltamn
        Phimndata[2,:,:]=newPhimn
            
        etadata[2,:,:]=np.real(neweta)
        deltadata[2,:,:]=np.real(newdelta)
        Phidata[2,:,:]=np.real(newPhi)
        
            
        if modalflag==1:
            if t>2:

                temp=np.zeros((J,I))
                temp[:,:]=Phidata[1,:,:]
                Phidata[1,:,:]=filters.modal_splitting(Phidata,alpha)
                etadata[1,:,:]=filters.modal_splitting(etadata,alpha)
                deltadata[1,:,:]=filters.modal_splitting(deltadata,alpha)


        
    
        if test==1:
            newU=Uic
            newV=Vic
    
    
        
        Udata[2,:,:]=np.real(newU)
        Vdata[2,:,:]=np.real(newV)
        
        spinupdata[t-1,0] = np.min(np.sqrt(Udata[1,:,:]**2 + Vdata[1,:,:]**2 ))
        spinupdata[t-1,1] = tstep.RMS_winds(a, I, J, lambdas, mus, Udata[1,:,:], Vdata[1,:,:])
        
            

        
        geopotdata[t-1,0]=np.min(Phidata[1,:,:])
        geopotdata[t-1,1]=np.max(Phidata[1,:,:])
        
        
        if saveflag==1:
   
            if dt*t%savefreq==0:                
                    
                timestamp=cont.compute_timestamp(timeunits,dt,t)
                
                cont.save_data(timestamp,np.real(neweta),np.real(newdelta), np.real(newPhi), np.real(newU), np.real(newV), spinupdata,geopotdata,custompath=custompath)

        
        if spinupdata[t-1,1]>8000:
            print('Time stepping stopped due to wind blow up. Max RMS winds = '+str(spinupdata[t-1,1]))
            break
            
            #t=tmax
    
        
        Umdata[2,:,:]=st.fwd_fft_trunc(newU,I,M)
        Vmdata[2,:,:]=st.fwd_fft_trunc(newV,I, M)
        
        Um=Umdata[2,:,:]
        Vm=Vmdata[2,:,:]
        
        
        etamdata[2,:,:]=st.fwd_fft_trunc(neweta,I,M)
        deltamdata[2,:,:]=st.fwd_fft_trunc(newdelta,I,M)
        Phimdata[2,:,:]=st.fwd_fft_trunc(newPhi,I,M)
        
            
        ######## FORCING ############
        if test==9:
            
            Q=forcing.Qfun(Phibar+2000, np.real(newPhi),Phibar, taurad)
            #geopotential forcing to be passed to time stepping
            PhiF=Q
            #print(np.max(Q))
            F,G=forcing.Rfun(np.real(newU), np.real(newV), -1*np.ones((J,I)), np.real(newPhi),Phibar,taudrag)
            
            Fdata[2,:,:]=F
            Gdata[2,:,:]=G
            
            Fmdata[2,:,:]=st.fwd_fft_trunc(F, I, M)
            Gmdata[2,:,:]=st.fwd_fft_trunc(G, I, M)
            
            Phiforcingdata[2,:,:]=PhiF
            Phiforcingmdata[2,:,:]=st.fwd_fft_trunc(PhiF, I, M)  
            
        
        elif test==10:
            
            Q=forcing.Qfun(Phieq, np.real(newPhi),Phibar, taurad)
            #geopotential forcing to be passed to time stepping
            PhiF=Q
            #print(np.max(Q))
            F,G=forcing.Rfun(np.real(newU), np.real(newV), Q, np.real(newPhi),Phibar,taudrag)
            
            Fdata[2,:,:]=F
            Gdata[2,:,:]=G
            
            Fmdata[2,:,:]=st.fwd_fft_trunc(F, I, M)
            Gmdata[2,:,:]=st.fwd_fft_trunc(G, I, M)
            
            Phiforcingdata[2,:,:]=PhiF
            Phiforcingmdata[2,:,:]=st.fwd_fft_trunc(PhiF, I, M)  
            
        elif test==11:
            Q=forcing.DoubleGrayPhiForcing(Teq,np.real(newPhi),Phibar,k2,sigmaSB,Cp,R)
            #geopotential forcing to be passed to time stepping
            PhiF=Q
            F,G=forcing.Rfun(np.real(newU), np.real(newV), Q, np.real(newPhi),Phibar,taudrag)


            Fdata[2,:,:]=F
            Gdata[2,:,:]=G
            
            Fmdata[2,:,:]=st.fwd_fft_trunc(F, I, M)
            Gmdata[2,:,:]=st.fwd_fft_trunc(G, I, M)
            
            Phiforcingdata[2,:,:]=PhiF
            Phiforcingmdata[2,:,:]=st.fwd_fft_trunc(PhiF, I, M)  
            
            
        
        if t%int(tmax/10)==0:
            print('t='+str(t)+', '+str(t*100/tmax)+'% complete')
        
        if plotflag==1:
            
            if t%plotfreq==0:

                plotting.spinup_plot(spinupdata, dt)
                timestamp=cont.compute_timestamp(timeunits,dt,t)
                plotting.mean_zonal_wind_plot(Udata[2,:,:], mus, timestamp)
                plotting.quiver_geopot_plot(Udata[2,:,:],Vdata[2,:,:],Phidata[2,:,:]+Phibar, lambdas, mus, timestamp)
                #testing_plots.spinup_plot(spinupdata,tmax,dt,test,a1)
                # testing_plots.zonal_wind_plot(Udata[2,:,:],mus,t,dt,test,a1)
                # testing_plots.quiver_geopot_plot(Udata[2,:,:],Vdata[2,:,:],Phidata[2,:,:]+Phibar,lambdas,mus,t,dt,5,test,a1,minlevel,maxlevel)         

        
        
        A,B,C,D,E = ic.ABCDE_init(np.real(newU),np.real(newV),np.real(neweta),np.real(newPhi),mus,I,J)
        
        Adata[2,:,:]=A
        Bdata[2,:,:]=B
        Cdata[2,:,:]=C
        Ddata[2,:,:]=D
        Edata[2,:,:]=E
        
        Amdata[2,:,:]=st.fwd_fft_trunc(A, I, M)
        Bmdata[2,:,:]=st.fwd_fft_trunc(B, I, M)
        Cmdata[2,:,:]=st.fwd_fft_trunc(C, I, M)
        Dmdata[2,:,:]=st.fwd_fft_trunc(D, I, M)
        Emdata[2,:,:]=st.fwd_fft_trunc(E, I, M)
        
        #rotate all arrays 

        etadata[0:2,:,:]=etadata[1:3,:,:]
        deltadata[0:2,:,:]=deltadata[1:3,:,:]
        Phidata[0:2,:,:]=Phidata[1:3,:,:]

        etamdata[0:2,:,:]=etamdata[1:3,:,:]
        deltamdata[0:2,:,:]=deltamdata[1:3,:,:]
        Phimdata[0:2,:,:]=Phimdata[1:3,:,:]
        
        Udata[0:2,:,:]=Udata[1:3,:,:]
        Vdata[0:2,:,:]=Vdata[1:3,:,:]

        Adata[0:2,:,:]=Adata[1:3,:,:]
        Bdata[0:2,:,:]=Bdata[1:3,:,:]
        Cdata[0:2,:,:]=Cdata[1:3,:,:]
        Ddata[0:2,:,:]=Ddata[1:3,:,:]
        Edata[0:2,:,:]=Edata[1:3,:,:]      
        
        Amdata[0:2,:,:]=Amdata[1:3,:,:]
        Bmdata[0:2,:,:]=Bmdata[1:3,:,:]
        Cmdata[0:2,:,:]=Cmdata[1:3,:,:]
        Dmdata[0:2,:,:]=Dmdata[1:3,:,:]
        Emdata[0:2,:,:]=Emdata[1:3,:,:]   
        
        
        Fdata[0:2,:,:]=Fdata[1:3,:,:]
        Gdata[0:2,:,:]=Gdata[1:3,:,:]
            
        Fmdata[0:2,:,:]=Fmdata[1:3,:,:]
        Gmdata[0:2,:,:]=Gmdata[1:3,:,:]
            
        Phiforcingdata[0:2,:,:]=Phiforcingdata[1:3,:,:]
        Phiforcingmdata[0:2,:,:]= Phiforcingmdata[1:3,:,:]
        
        print(np.max(Phidata[2,:,:]))
    print('Loop finished') 
               