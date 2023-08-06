from cyanDiff.ad_helpers import make_vars
from cyanDiff.ad_types import DiffObject

class Test_ad_helpers:
    def test_make_vars(self):
        # Test list return value
        lst = make_vars(2)

        assert len(lst) == 2

        x, y = lst
        assert isinstance(x, DiffObject)
        assert isinstance(y, DiffObject)

        # Test single Function return value
        z = make_vars(1)

        assert isinstance(z, DiffObject)