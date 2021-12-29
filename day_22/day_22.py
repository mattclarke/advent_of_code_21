with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]

CUBES = []

for line in puzzle_input:
    on = False
    if line.startswith("on"):
        on = True
    line = (
        line.replace("on ", "")
        .replace("off ", "")
        .replace("x=", "")
        .replace("y=", "")
        .replace("z=", "")
    )
    x_str, y_str, z_str = line.split(",")
    xmin, xmax = [int(x) for x in x_str.split("..")]
    ymin, ymax = [int(y) for y in y_str.split("..")]
    zmin, zmax = [int(z) for z in z_str.split("..")]
    CUBES.append(((xmin, xmax, ymin, ymax, zmin, zmax), on))

total_on = 0

for x in range(-50, 50 + 1):
    for y in range(-50, 50 + 1):
        for z in range(-50, 50 + 1):
            is_on = False
            for cube, on in CUBES:
                xmin, xmax, ymin, ymax, zmin, zmax = cube
                if xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax:
                    is_on = on
            if is_on:
                total_on += 1

# Part 1 = 564654
print(f"answer = {total_on}")


def find_overlap_1d(amin, amax, bmin, bmax):
    if amin <= bmin and bmax >= amax:
        xmin = bmin
        xmax = amax
    elif bmin <= amin and amax >= bmax:
        xmin = amin
        xmax = bmax
    elif bmin <= amin and bmax >= amax:
        xmin = amin
        xmax = amax
    elif amin <= bmin and amax >= bmax:
        xmin = bmin
        xmax = bmax
    else:
        print(f"{amin} {amax} and {bmin} {bmax}")
        assert False
    return xmin, xmax


def calculate_overlap(a, b):
    xmin1, xmax1, ymin1, ymax1, zmin1, zmax1 = a
    xmin2, xmax2, ymin2, ymax2, zmin2, zmax2 = b

    if xmax1 < xmin2 or xmin1 > xmax2 or xmax2 < xmin1 or xmin2 > xmax1:
        return None
    if ymax1 < ymin2 or ymin1 > ymax2 or ymax2 < ymin1 or ymin2 > ymax1:
        return None
    if zmax1 < zmin2 or zmin1 > zmax2 or zmax2 < zmin1 or zmin2 > zmax1:
        return None

    xmin, xmax = find_overlap_1d(xmin1, xmax1, xmin2, xmax2)
    ymin, ymax = find_overlap_1d(ymin1, ymax1, ymin2, ymax2)
    zmin, zmax = find_overlap_1d(zmin1, zmax1, zmin2, zmax2)
    return xmin, xmax, ymin, ymax, zmin, zmax


cuboids = []
for cube, on in CUBES:
    if not cuboids:
        # Add the first one
        cuboids.append((cube, True))
        continue
    to_add = []
    for c, o in cuboids:
        overlap = calculate_overlap(cube, c)
        if overlap:
            to_add.append((overlap, not o))
    if on:
        cuboids.append((cube, True))
    cuboids.extend(to_add)

total_2 = 0
for cube, on in cuboids:
    xmin, xmax, ymin, ymax, zmin, zmax = cube
    volume = (xmax - xmin + 1) * (ymax - ymin + 1) * (zmax - zmin + 1)
    if on:
        total_2 += volume
    else:
        total_2 -= volume


# Part 2 = 1214193181891104
print(f"answer = {total_2}")
