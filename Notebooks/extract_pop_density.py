#Gotta make a list of lists with the lat/lons and values for the shapefile
#So that we can analyze it

import shapefile
pop_shp = shapefile.Reader("../Data/usafecount/usap15ag/points_w_values_t5")
pop_points = pop_shp.shapes()

pop_points_vals = []
for index in range(len(pop_points)):
    print pop_points[index].points[0], pop_shp.records()[index][0]
    #pop_points_vals.append([pop_points[index].points[0], pop_shp.records()[index][0]])
