from tesla import Tesla, 
from modelx import ModelX


def test_color():
    tesla = Tesla("R", "red")
    assert tesla.color == "red"


def test_welcome():
    tesla = Tesla("R", "red")
    assert tesla.welcome() == "Hello from model R!"
