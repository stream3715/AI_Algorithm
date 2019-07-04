# coding: utf-8
import heapq

from myfunc import heuristic
from myfunc import get_next_positions


def search_astar(maze, start, goal):
    passed_list = [start]
    init_score = heuristic(start, goal)
    closed_node = {start: init_score}
    open_node = []
    heapq.heappush(open_node, (init_score, passed_list))

    while len(open_node) > 0:
        score, passed_list = heapq.heappop(open_node)
        last_passed_pos = passed_list[-1]

        if last_passed_pos == goal:
            return passed_list, closed_node

        for pos in get_next_positions(last_passed_pos, maze):
            new_passed_list = passed_list + [pos]
            prev_cost = score - heuristic(last_passed_pos, goal)
            pos_score = heuristic(pos, goal) + prev_cost + 1

            if pos in closed_node and closed_node[pos] <= pos_score:
                continue

            closed_node[pos] = pos_score
            heapq.heappush(open_node, (pos_score, new_passed_list))
    return []
