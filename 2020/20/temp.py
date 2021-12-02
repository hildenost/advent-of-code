
def flip_x(image):
    return list(reversed(image))

def flip_y(image):
    return ["".join(reversed(r)) for r in image]

def rotate(image):
    return ["".join(r[i] for r in image[::-1]) for i in range(len(image))]
