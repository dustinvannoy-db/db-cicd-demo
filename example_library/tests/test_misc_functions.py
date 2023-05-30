import pytest
import os

import sys
currentdir = os.path.dirname(__file__)
parentdir = os.path.dirname(currentdir)
print(parentdir)
sys.path.insert(0,parentdir)

from my_library import misc_functions

def test_lookup_key_valid():
    assert misc_functions.id_lookup('person1') == 111

def test_lookup_key_invalid():
    assert misc_functions.id_lookup('fake-person') == 0

if __name__ == "__main__":
    print(pytest.main(["-p", "no:cacheprovider"]))
    