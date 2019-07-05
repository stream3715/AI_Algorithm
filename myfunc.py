def heuristic(pos, end):
    """ ゴールまでのユークリッド距離 """
    return ((pos[0] - end[0]) ** 2 + (pos[1] - end[1]) ** 2) ** 0.5


def distance(pos, start):
    """ スタートから探索中の座標までの距離のスコア """
    return abs(pos[0] - start[0]) + abs(pos[1] - start[1])


def get_next_positions(pos, maze):
    wall = "O"

    """上"""
    if maze[pos[0] - 1][pos[1]] != wall:
        yield (pos[0] - 1, pos[1])
    """下"""
    if maze[pos[0] + 1][pos[1]] != wall:
        yield (pos[0] + 1, pos[1])
    """左"""
    if maze[pos[0]][pos[1] - 1] != wall:
        yield (pos[0], pos[1] - 1)
    """右"""
    if maze[pos[0]][pos[1] + 1] != wall:
        yield (pos[0], pos[1] + 1)
