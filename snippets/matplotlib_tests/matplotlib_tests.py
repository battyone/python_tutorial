# %%
# Part 1: https://www.youtube.com/watch?v=UO98lJQ3QGI
from matplotlib import pyplot as plt

# %%

# see format string
# doc: https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html

ages_x = list(range(25, 36))
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# use white dashed line with small markers
# plt.plot(ages_x, dev_y, 'w--', label='All Dev')
plt.plot(ages_x, dev_y, color='w', linestyle='--', marker='.', label='All Dev')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# use blue dotted line with big markers
plt.plot(ages_x, py_dev_y, color='#00FFFF',
         linestyle=':', marker='o', label='Python')


plt.title('Median Salary (USD) by Age')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.legend()

plt.show()


# %%
