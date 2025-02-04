import pytest

#This is to prevent the markfixture from being used repeatedly.
@pytest.mark.usefixtures("setup")
class BaseClass():
    pass