#. Add interface to all **defined** function :DONE:

#. Write tests

    #. v3_Functions.h, corresponds to v3.h :DONE:
    #. v6_Functions.h, corresponds to v6.h :DONE:
    #. m3_Functions.h, corresponds to m3.h :DONE:
    #. m6_Functions.h corresponds to m6.h :DONE:
    #. vec.h :DONE:
    #. astro.h :ONGOING:
    #. times.h :DONE:
    #. tpm.h :TODO:
    #. convert function :ONGOING:
    
#. Missing

    :ONGOING:
    #. Many function declarations do not have implementations in TPM.

       2010/12/06

       Send email to Jeff Percival requesting his copy of code that
       includes the above and tests!
    
    :FUTURE?:
    #. Routines in misc.h, integration routines, not added to python.

:TODO:
#. delta_ut is not set in tpm.convert! This is not done in the
   tpm_main.c program in TPM source code. So I get the same results as
   tpm binary created from tpm_main.c. 

   Need to add this. For this implement delta_at function: like
   delta_ut or use SLALIB code.

:TODO:
#. Need a way to create V6 array for use as
   pvec[N_TPM_STATES]. Without this there is no way for manually
   performing coordinate conversions in pytpm. Will have to call
   tpm.convert or utils.convert.
