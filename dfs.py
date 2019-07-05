from myfunc import get_next_positions


def search_dfs(maze, start, end):
    checked = {start: None}
    solved_maze = [[], checked]
    if not dfs_recursive(maze, start, end, checked):
        return []

    (parent_y, parent_x) = end
    while not (parent_y, parent_x) == start:
        solved_maze[0].append((parent_y, parent_x))
        (parent_y, parent_x) = solved_maze[1][parent_y, parent_x]
    return solved_maze


def dfs_recursive(maze, pos, end, checked):
    for next_pos in get_next_positions(pos, maze):
        (y, x) = next_pos
        """ IS_GOAL?"""
        if next_pos == end:
            checked[end[0], end[1]] = pos
            return checked
        # 壁でなく、かつゴールに到達していない場合
        elif maze[y][x] != "O" and (y, x) not in checked:
            checked[y, x] = pos
            result = dfs_recursive(maze, (y, x), end, checked)
            if result:
                return result
            checked.pop((y, x))
    return {}
