from main import Tesla, ModelX


def test_color():
    tesla = Tesla("R", "red")
    assert tesla.color == "red"


def test_welcome():
    tesla = Tesla("R", "red")
    assert tesla.welcome() == "Hello from model R!"


def test_open_doors():
    model = ModelX("purple")
    assert model.open_doors() == "Doors open towards the roof"
