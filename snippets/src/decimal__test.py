
# %%
import decimal

ctx = decimal.getcontext()
ctx.prec

one_third = decimal.Decimal('1') / decimal.Decimal('3')
print(one_third)

ctx.prec = 10
print(one_third)  # old precision
print(+one_third)  # will apply new precision
