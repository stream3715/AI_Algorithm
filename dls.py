from myfunc import get_next_positions


def search_dls(maze, start, end):
    count = 0
    result = []
    while not result:
        result = dls_bootstrap(maze, start, end, count)
        count += 1
    return result


def dls_bootstrap(maze, start, end, limit):
    checked = {start: [0, None]}
    solved_maze = [[], checked]
    if not dls_recursive(maze, start, end, checked, limit):
        return []

    parent_y, parent_x = end[0], end[1]
    while not (parent_y, parent_x) == start:
        solved_maze[0].append((parent_y, parent_x))
        (parent_y, parent_x) = solved_maze[1][parent_y, parent_x][1]
    return solved_maze


def dls_recursive(maze, pos, end, checked, limit):
    cnt = checked[pos[0], pos[1]][0]

    if cnt < limit:
        for next_pos in get_next_positions(pos, maze):
            (y, x) = next_pos
            cnt += 1
            """ IS_GOAL?"""
            if next_pos == end:
                checked[end[0], end[1]] = [cnt, pos]
                return checked
            # 壁でなく、かつゴールに到達していない場合
            elif maze[y][x] != "O" and (y, x) not in checked:
                checked[y, x] = [cnt, pos]
                result = dls_recursive(maze, (y, x), end, checked, limit)
                if result:
                    return result
                checked.pop((y, x))
    return {}
