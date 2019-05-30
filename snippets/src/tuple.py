import os
from collections import namedtuple


def run_test():
    lax_coord = (33.9425, -118.408056)

    # Unpacking
    city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)

    traveler_ids = [("USA", "311958624"),
                    ("BRA", "CE3434299"), ("ESP", "XDA579312")]
    for passport in sorted(traveler_ids):
        print(passport)

    # Unpacking
    for country, _ in traveler_ids:
        print(country)

    # Unpacking
    t = (20, 4)
    a, b = divmod(*t)
    print(f"quotient:{a}; remainder:{b}")

    # split returns path,filename
    _, a = os.path.split(r"D:\repos\python_tutorial\readme.md")
    print(a)

    # Using * to grab excess items
    a, b, *rest = range(10)
    print(a, b, rest)

    a, *rest, b, c = range(10)
    print(a, b, c, rest)

    # Unpacking nested tuples
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    print("{:15} | {:^9} | {:^9}".format("", "lat", "long"))
    for name, cc, pop, (lat, long) in metro_areas:
        print(f"{name:15} | {lat:9.4f} | {long:9.4f}")

    # Named Tuples
    City = namedtuple("City", "name country population coordinates")
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)

    print(City._fields)

    LatLong = namedtuple("LatLong", "log long")
    delphi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delphi = City._make(delphi_data)
    print(delphi._asdict())

    # appending to tuples is inefficient
    t = (1, 2, 3)
    print(t)
    print(id(t))

    # appending will create a new tuple!
    t *= 2
    print(t)
    print(id(t))


if __name__ == "__main__":
    run_test()

# %%
# compare to tuple for equality
t1 = (1, 3, 4, 'Hello')
t2 = (1, 3, 4, 'Hello')
eq = len(t1) == len(t2) and all(a == b for a, b in zip(t1, t2))
print(eq)


# %%
