
import pandas

# CREATING 57 BUCKETS FOR LAT LONG COMBINED

housing = pandas.read_csv('../data/housing.csv')

lat_long_pts = []

# Get all of the unique lat long pairs
for index, row in housing.iterrows():
    found = False
    for i in lat_long_pts:
        if (round(row['latitude'], 0) == i[0]) and (round(row['longitude'], 0) == i[1]):
            found = True
            i[2] += 1
    if not found:
        lat_long_pts.append([round(row['latitude'], 0), round(row['longitude'], 0), 0])

for k in lat_long_pts:
    # For each of the 57 points in the table
    # This is the most disgusting piece of code I have ever written, but it works
    # Value is 1 if the lat and long are correct, else it is inputted as 0
    housing['lat_long_' + str(k[0]) + "_" + str(k[1])] = \
        [1 if (round(row['latitude'], 0) == k[0]) and (round(row['longitude'], 0) == k[1])
            else 0
            for index, row in housing.iterrows()]

# Remove the lat and long columns
housing.drop(columns=['longitude'], inplace=True)
housing.drop(columns=['latitude'], inplace=True)



housing.to_csv("new_housing.csv", sep='\t')

