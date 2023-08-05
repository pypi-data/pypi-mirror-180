import brep_part_finder as bpf


# brep file is imported
my_brep_part_properties = bpf.get_part_properties_from_file("ball_reactor.brep")

# from the printed json dictionary we know that there is are two parts with a
# volume 95467959.26023674 which is the blanket_rear_wall component
part_id = bpf.get_matching_part_id(
    brep_part_properties=my_brep_part_properties,
    bounding_box_xmin=-250.0000001,
    bounding_box_ymin=-250.0000001,
    bounding_box_zmin=-460.9997405464822,
    bounding_box_xmax=250.0000001,
    bounding_box_ymax=250.00000010000002,
    bounding_box_zmax=-311.13245981234695,
    bounding_box_atol=1e-6,
)

# prints the part id found
print(f" there is {len(part_id)} with a matching volume")
print(f" the part id with a matching volume is {part_id}")
