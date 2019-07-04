from collections import deque


def search_bfs(maze, start, end):
    queue = deque([start])
    checked = {start: [0, None]}

    while queue:
        y, x = queue.popleft()

        if [y, x] == [end[0], end[1]]:
            solved_maze = [[], checked]
            parent_y, parent_x = end[0], end[1]
            while not (parent_y == start[0] and parent_x == start[1]):
                solved_maze[0].append((parent_y, parent_x))
                parent_y, parent_x = solved_maze[1][parent_y, parent_x][1][0], solved_maze[1][parent_y, parent_x][1][1]
            return solved_maze

        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_y, new_x = y + j, x + k
            if (maze[new_y][new_x] != "O") and (new_y, new_x) not in checked:
                checked[new_y, new_x] = checked[y, x][0] + 1, [y, x]
                queue.append([new_y, new_x])
