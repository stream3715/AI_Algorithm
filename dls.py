from myfunc import get_next_positions


def search_dls(maze, start, end):
    count = 1
    print(count)
    result = dls_bootstrap(maze, start, end, count)
    while not result:
        count += 1
        print(count)
        result = dls_bootstrap(maze, start, end, count)

    return result


def dls_bootstrap(maze, start, end, limit):
    checked = {start: [0, None]}
    solved_maze = [[], checked]
    if not dls_recursive(maze, start, end, checked, limit):
        return []

    parent_y, parent_x = end[0], end[1]
    while not (parent_y == start[0] and parent_x == start[1]):
        solved_maze[0].append((parent_y, parent_x))
        parent_y, parent_x = solved_maze[1][parent_y, parent_x][1][0], solved_maze[1][parent_y, parent_x][1][1]
    return solved_maze


def dls_recursive(maze, pos, end, checked, limit):
    for next_pos in get_next_positions(pos, maze):
        (y, x) = next_pos
        cnt = checked[pos[0], pos[1]][0] + 1
        # ゴールに到達した場合
        if y == end[0] and x == end[1]:
            checked[end[0], end[1]] = [cnt, pos]
            return checked
        elif cnt == limit:
            return {}
        # 壁でなく、かつゴールに到達していない場合
        elif maze[y][x] != "O" and (y, x) not in checked:
            checked[y, x] = [cnt, pos]
            result = dls_recursive(maze, (y, x), end, checked, limit)
            if result:
                return result
            checked.pop((y, x))
    return {}
