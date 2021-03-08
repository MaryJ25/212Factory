def test_open_doors():
    model = ModelX("purple")
    assert model.open_doors() == "Doors open towards the roof"
