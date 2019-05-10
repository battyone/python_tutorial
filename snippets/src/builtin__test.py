# %%
print([callable(i) for i in [abs, str, 13]])

# %%
promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']

print(promos)


