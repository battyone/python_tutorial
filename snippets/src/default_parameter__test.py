
# %%
class HauntedBus:
    # bad idea to '[]'
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)


b1 = HauntedBus()
b1.pick_up('Katrin')
print(f'b1: {b1.passengers}')

b2 = HauntedBus()
print(f'b2: {b2.passengers}') #Somehow Katrin is also on this bus!!!

#%%
# print(dir(HauntedBus.__init__))
# print(dir(HauntedBus.__init__.__defaults__[0]))
HauntedBus.__init__.__defaults__[0]

