from decimal import Decimal, getcontext

getcontext()
print(Decimal(str(0.1)) + Decimal("0.2"))


getcontext().prec = (
    5  # this one is gonna be applied allover the models as it has global scope
)
print(Decimal(str(1)) / Decimal("3"))

print(Decimal(str(1.222222)) / Decimal("3.22333"))
