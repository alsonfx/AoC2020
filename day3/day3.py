# Get to the bottom of the mountain using a pattern of 3 right and 1 down
# Count trees you encounter until you read the bottom of the map

# Pseudo Code
# 1. Import map file
# 2. We have to mark our position on the map, keep track of position on line (position x)
#    and each line you are on (position y).
# 3. Move our marker 3 right and 1 down until you reach the bottom of the map
#    (end of file). If you reach the end of the line, restart marker at beginning
#    of the line.
# 4. If you end on a tree after your movement, keep track of tree you encounter.

geo_map = open("map.txt", 'r')
map_list = [line.rstrip() for line in geo_map]
geo_map.close()

slopes = zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2])

tree_product = 1

for x, y in slopes:
    trees, x_loc, y_loc = 0, 0, 0
    while True:
        y_loc += y
        if y_loc >= len(map_list):
            break
        x_loc = (x_loc + x) % len(map_list[y_loc])

        if map_list[y_loc][x_loc] == '#':
            trees += 1
    tree_product *= trees

    print(f"For slope: {x, y} you would hit {trees} trees on your way down.")

print(f"Product of trees encountered: {tree_product}")
