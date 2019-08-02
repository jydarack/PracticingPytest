""" Chapter 1 testing function. Going further than what's in the book """
from myscripts import choucroute, chaussette

def test_choucroute():
    """ Basic testing of choucroute function """
    assert choucroute("a", 123) == {"a":123}


def test_chaussette():
    """ Basic testing of choucroute function """
    assert chaussette(1, 123) == 124
    assert chaussette("1", "123") == "1123"
    