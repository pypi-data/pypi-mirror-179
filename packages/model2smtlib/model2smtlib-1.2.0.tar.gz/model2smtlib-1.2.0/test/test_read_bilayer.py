import os
import sys
import unittest

sys.path.append("/Users/dmosaphir/SIFT/Projects/ASKEM/code/model2smtlib/src")
from model2smtlib.bilayer.translate import Bilayer

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data")


class TestCompilation(unittest.TestCase):
    def test_read_bilayer(self):
        bilayer_json_file = os.path.join(
            DATA, "CHIME_SIR_dynamics_BiLayer.json"
        )
        bilayer = Bilayer.from_json(bilayer_json_file)
        assert bilayer

        #        encoding = bilayer.to_smtlib_timepoint(2) ## encoding at the single timepoint 2
        encoding = bilayer.to_smtlib(
            [2.5, 3, 4, 6]
        )  ## encoding at the list of timepoints [2,3]
        assert encoding


if __name__ == "__main__":
    unittest.main()
