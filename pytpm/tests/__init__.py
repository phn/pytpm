import unittest

import test_conversions_with_pm
import test_convert
import test_pytpm_astro
import test_pytpm_times
import test_pytpm_tpm
import test_pytpm_utils
import test_pytpm_vec

t = unittest.TestLoader()

s1 = t.loadTestsFromModule(test_conversions_with_pm)
s2 = t.loadTestsFromModule(test_convert)
s3 = t.loadTestsFromModule(test_pytpm_astro)
s4 = t.loadTestsFromModule(test_pytpm_times)
s5 = t.loadTestsFromModule(test_pytpm_tpm)
s6 = t.loadTestsFromModule(test_pytpm_utils)
s7 = t.loadTestsFromModule(test_pytpm_vec)

alltests = unittest.TestSuite([s1, s2, s3, s4, s5, s6, s7])

def suite():
    return alltests
