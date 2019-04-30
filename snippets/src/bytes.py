
# %%
import array
cafe = bytes('café', encoding='utf8')
print(cafe)
print(cafe[0])  # returns an int
print(cafe[:1])  # returns bytes

# %%
b = bytes.fromhex('31 4B CE A9')
# will print ASCII characters when possible
print(b)

# %%

a = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(a)  # makes a copy
print(octets)
