""" Advent of Code 2021. Day 20: Trench Map """

enhancement = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"

raw_image = """#..#.
#....
##..#
..#..
..###
""".splitlines()

with open("input.txt") as f:
    enhancement, raw_image = f.read().split("\n\n")
    raw_image = raw_image.splitlines()

image = {
    (i, j): "1" if r == "#" else "0"
    for i, row in enumerate(raw_image)
    for j, r in enumerate(row)
}

def find_bb(img):
    # Is simpler than this: it grows by 1 in either direction
    # per step
    xs, ys = zip(*img)
    return (
        min(xs) - 1,
        max(xs) + 1,
        min(ys) - 1,
        max(ys) + 1,
    )

def enhance(image, n=0):
    xmin, xmax, ymin, ymax = find_bb(image)

    # Because the enhancement algo from actual input
    # has 0 => on and 512 => off
    outside = "1" if n % 2 else "0"

    def get_enhance(i, j):
        binary = "".join(
            image.get((k, l), outside)
            for k in range(i - 1, i + 2)
            for l in range(j - 1, j + 2)
        )
        return enhancement[int(binary, 2)] == "#"
    
    return {
        (i, j): "1" if get_enhance(i, j) else "0"
        for i in range(xmin, xmax+1)
        for j in range(ymin, ymax+1)
    }

for n in range(50):
    image = enhance(image, n)
    
    if n == 1:
        print("Part 1:\t", sum(c == "1" for c in image.values()))

print("Part 2:\t", sum(c == "1" for c in image.values()))
