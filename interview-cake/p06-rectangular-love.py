def find_overlap(rect1, rect2, axis, length):
    leftmost_rect, rightmost_rect = (
        (rect1, rect2) if rect1[axis] < rect2[axis]
        else (rect2, rect1))
    if rightmost_rect[axis] < leftmost_rect[axis] + leftmost_rect[length]:
        return rightmost_rect[axis], min(
            rightmost_rect[axis] + rightmost_rect[length],
            leftmost_rect[axis] + leftmost_rect[length])
    else:
        return None


def find_intersect(rect1, rect2):
    x_overlap = find_overlap(rect1, rect2, 'x', 'width')
    y_overlap = find_overlap(rect1, rect2, 'y', 'height')

    if x_overlap and y_overlap:
        return {
            'x': x_overlap[0],
            'y': y_overlap[0],
            'width': x_overlap[1] - x_overlap[0],
            'height': y_overlap[1] - y_overlap[0]
        }

recta = {
    'x': 0,
    'y': 0,
    'height': 1,
    'width': 1
}

rectb = {
    'x': -1,
    'y': -1,
    'width': 10,
    'height': 10
}

print find_intersect(recta, rectb)
