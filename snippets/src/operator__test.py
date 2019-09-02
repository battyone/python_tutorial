
# %%
from operator import itemgetter, attrgetter, methodcaller
from collections import namedtuple

#%%
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# sort by item with index 1
for city in sorted(metro_areas, key=itemgetter(1)):
    # print only first two items
    cc_names = itemgetter(0,1)
    print(cc_names(city))


#%% 

# create a structure from metro data
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name country pop coord')

mm = [Metropolis(name, cc, pop, LatLong(lat, long))
    for name, cc, pop, (lat, long) in metro_areas]

name_lat = attrgetter('name', 'coord.lat')
for m in mm:
    print(name_lat(m))

[print(name_lat(m)) for m in mm]

#%%
name_lat = attrgetter('name', 'coord.lat')

for m in mm:
    print(name_lat(m))


#%%
s = 'the time has come'
upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))


#%%
d = {10:50, 20: 30}
print(max(d.items(), key=itemgetter(1)))