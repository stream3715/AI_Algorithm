import time

from astar import search_astar
from bfs import search_bfs
from dfs import search_dfs
from dls import search_dls
from greedy import search_greedy


def find_ch(ch, maze):
    for y, l in enumerate(maze):
        for x, c in enumerate(l):
            if c == ch:
                return y, x


def render_result(maze, solved_maze, start, end):
    buf = [[ch for ch in l] for l in maze]
    cnt = 0
    for obj in solved_maze[1].keys():
        buf[obj[0]][obj[1]] = '.'

    for obj in solved_maze[0]:
        if obj == start:
            continue
        buf[obj[0]][obj[1]] = '*'
        cnt += 1

    buf[start[0]][start[1]] = "S"
    buf[end[0]][end[1]] = "G"

    print("\n".join("".join(l) for l in buf))
    print(f"finished in {cnt} step(s).")


def mode_selector(mode, maze, start, end):
    if mode == 0:
        return search_astar(maze, start, end)
    elif mode == 1:
        return search_greedy(maze, start, end)
    elif mode == 2:
        return search_bfs(maze, start, end)
    elif mode == 3:
        return search_dfs(maze, start, end)
    elif mode == 4:
        return search_dls(maze, start, end)
    else:
        return None


def search_main():

    maze = [
        'OOOOOOOOOOOOOO',
        'O           GO',
        'O            O',
        'O   OOOOO    O',
        'O            O',
        'O            O',
        'O            O',
        'O            O',
        'O            O',
        'O            O',
        'OS           O',
        'O            O',
        'OOOOOOOOOOOOOO',
    ]

    """
    maze = [
        'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
        'O   O           OO OO    O O OO     O',
        'O O SOOOOOO  OO  O O  O  O O    O O O',
        'O  OOO   O O OOO O    O  O OO OOOGO O',
        'OO  O  O   O  O  O  O  O   O      OOO',
        'O O   OO O     O O  OO   O  O O O   O',
        'O  O     OOOOOOO O  OO  OO  OOO  O  O',
        'O    OO  O   O   O  OO O   OOOOOOOO O',
        'OOO OO   OOOOOOO O  O  O         O  O',
        'O   OOOO OO      O  O  OOO O OO O O O',
        'O O  OOO OO OOOOOO  O         O O   O',
        'O  O                O  OOOOO  O   O O',
        'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
    ]
    """

    start = find_ch("S", maze)
    end = find_ch("G", maze)

    time_start_astar = time.perf_counter()
    render_result(maze, mode_selector(0, maze, start, end), start, end)
    time_finish_astar = time.perf_counter()
    print("Searched in " + str(time_finish_astar - time_start_astar) + "\n")

    time_start_greedy = time.perf_counter()
    render_result(maze, mode_selector(1, maze, start, end), start, end)
    time_finish_greedy = time.perf_counter()
    print("Searched in " + str(time_finish_greedy - time_start_greedy) + "\n")

    time_start_bfs = time.perf_counter()
    render_result(maze, mode_selector(2, maze, start, end), start, end)
    time_finish_bfs = time.perf_counter()
    print("Searched in " + str(time_finish_bfs - time_start_bfs) + "\n")

    time_start_dfs = time.perf_counter()
    render_result(maze, mode_selector(3, maze, start, end), start, end)
    time_finish_dfs = time.perf_counter()
    print("Searched in " + str(time_finish_dfs - time_start_dfs) + "\n")

    time_start_dls = time.perf_counter()
    render_result(maze, mode_selector(4, maze, start, end), start, end)
    time_finish_dls = time.perf_counter()
    print("Searched in " + str(time_finish_dls - time_start_dls) + "\n")


if __name__ == "__main__":
    search_main()
