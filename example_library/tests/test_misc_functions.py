import pytest
import os

import sys
# sys.path.append('.')
print(sys.path)

# try:
#     currentdir = os.path.dirname(__file__)
#     parentdir = os.path.dirname(currentdir)
#     print(parentdir)
#     sys.path.insert(0,parentdir)
# except:
#     pass

from example_library.my_library import misc_functions

def test_lookup_key_valid():
    assert misc_functions.id_lookup('person1') == 111

def test_lookup_key_invalid():
    assert misc_functions.id_lookup('fake-person') == 0

if __name__ == "__main__":
    print(pytest.main(["-p", "no:cacheprovider"]))
    