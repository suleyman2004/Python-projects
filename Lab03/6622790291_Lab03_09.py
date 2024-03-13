import math as m
cube_width=float(input("Enter the width of the cube:"))
cont_width=float(input("Enter the width of the container:"))
cont_height=float(input("Enter the height of the container:"))
cont_depth=float(input("Enter the depth of the container:"))
tot_width=m.floor(cont_width/cube_width)
tot_length=m.floor(cont_height/cube_width)
tot_depth=m.floor(cont_depth/cube_width)
total=tot_depth*tot_length*tot_width
print("The number of cubes that can fit into the container is ",total)
