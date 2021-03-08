from scripts.tesla import Tesla
from scripts.modelx import ModelX

tesla = Tesla("C", "Black")
modelx = ModelX("purple")

print(tesla.color)
print(modelx.color)

print(tesla.welcome())
print(modelx.welcome())
