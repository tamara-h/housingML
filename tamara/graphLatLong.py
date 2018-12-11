import matplotlib.pyplot as plt
import pandas

housing = pandas.read_csv('../data/housing.csv')

lat_long_pts = []


for index, row in housing.iterrows():
    colors = (0, 0, 0)
    found = False
    for i in lat_long_pts:
        if (round(row['latitude'], 0) == i[0]) and (round(row['longitude'], 0) == i[1]):
            found = True
            i[2] += 1
    if not found:
        lat_long_pts.append([round(row['latitude'], 0), round(row['longitude'], 0), 0])

print(len(lat_long_pts))

for j in lat_long_pts:
    print(j)
    plt.scatter(j[0], j[1])

plt.show()