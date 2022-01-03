""" Advent of Code 2021. Day 23: Amphipod

Warning: Messy, tangly, duplicate, suboptimal code ahead.
"""

cost = {
    "A": 1,
    "B": 10, 
    "C": 100,
    "D": 1000,
}
cols = dict([("A", 3), ("B", 5), ("C", 7), ("D", 9)])

def generate_goals(depth):
    return {
        breed: [(j, col)
        for j in range(1, depth + 1)]
        for breed, col in cols.items()
    }

part1 = generate_goals(2)
part2 = generate_goals(4)

goal = part1

hallway = {(0, j) for j in range(1, 12) if j not in cols.values()}

def taxicave(start, end):
    """ Computes distance from room to hallway or room """
    # total vertical distance + horizontal distance
    return start[0] + end[0] + abs(start[1] - end[1])

class Node:
    def __init__(self, state, cost=0):
        self.pods = state
        self.g = cost
        self.h = self.heuristic()
        self.score = self.g + self.h

    def __hash__(self):
        return hash(tuple(sorted(self.pods)))

    def __eq__(self, other):
        return self.pods == other.pods

    def __lt__(self, other):
        # Tie breaking:
        # If similar scores, choose the node
        # that has gotten farthest along
        # (larger cost and smaller heuristic)
        if self.score == other.score: 
            return self.g > other.g
        return self.score < other.score

    def heuristic(self):
        return sum(cost[breed] * taxicave(pos, max(goal[breed]))
            for pos, breed in self.pods.items()
            if pos not in goal[breed]
        )

    def is_stuck(self, pod):
        return (pod[0] > 1 and
            any((j, pod[1]) in self.pods for j in range(1, pod[0]))
        )

    def is_correct(self, pod):
        return (
            pod in goal[self.pods[pod]] and
            all(self.pods.get((j, pod[1])) == self.pods[pod] for j in range(pod[0], max(goal[self.pods[pod]])[0] + 1))
            )

    def get_goal_move(self, pod):
        # Add paths to the goal room
        goals = goal[self.pods[pod]]
        for i, goal_move in enumerate(goals):
            is_space_above = [pos not in self.pods for pos in goals[:i+1]]
            is_same_below = [self.pods.get(pos) == self.pods[pod] for pos in goals[i+1:]]
            if (all(is_space_above) and
                all(is_same_below)):
                return {goal_move}
        return set()


def expand(node):
    # Generate child states
    queue = []
    for pod, breed in node.pods.items():
        if node.is_stuck(pod) or node.is_correct(pod):
            continue

        # Add paths to the goal room
        goal_move = node.get_goal_move(pod)

        possible_moves = set()
        # If amphipod in starting room,
        # valid states are any of hallway, except the junctions  
        # and of course, final room, if available
        if pod[0] > 0:
            # But if any of these locations are taken, we cannot go there
            possible_moves = {pos for pos in hallway if pos not in node.pods}

        possible_moves.update(goal_move)

        # Also, if any other amphipod blocks the hallway, cannot go beyond
        # That is, in this case:
        for pos in node.pods:
            if pos[0] == 0:
                if pod[1] > pos[1]:
                    possible_moves = {p for p in possible_moves if p[1] > pos[1]}
                if pod[1] < pos[1]:
                    possible_moves = {p for p in possible_moves if p[1] < pos[1]}

        if goal_move and goal_move <= possible_moves:
            # Always select goal_move
            possible_moves = goal_move

        for new_pos in possible_moves:
            # Compute cost of moving for each of the candidate moves
            new_cost = node.g + cost[breed] * taxicave(pod, new_pos)

            new_state = {new_pos if p == pod else p: breed for p, breed in node.pods.items()}

            queue.append(Node(new_state, new_cost))

    return queue


from heapq import heappush
from heapq import heappop

def astar(startnode):
    open_list = [startnode] 
    closed_list = set()

    while open_list:
        n = heappop(open_list) 

        if n in closed_list:
            continue

        closed_list.add(n)

        if n.h == 0:
            print("Explored ", len(closed_list), " nodes")
            return n.g
       
        children = expand(n)

        for c in children:
            if c in closed_list:
                continue
            heappush(open_list, c)
    print("Explored ", len(closed_list), " nodes")

# Initial state
amphipods = {
    (1, 3): "B",
    (2, 3): "D",
    (1, 5): "A",
    (2, 5): "A",
    (1, 7): "B",
    (2, 7): "D",
    (1, 9): "C",
    (2, 9): "C",
}

import time
tic = time.perf_counter()
print("Part 1:\t", astar(Node(amphipods)))
toc = time.perf_counter()
print(f"{toc-tic:6.1f} sec")
exit()
####
# Part 2

amphipods = {
    (1, 3): "B",
    (2, 3): "D",
    (3, 3): "D",
    (4, 3): "D",
    (1, 5): "A",
    (2, 5): "C",
    (3, 5): "B",
    (4, 5): "A",
    (1, 7): "B",
    (2, 7): "B",
    (3, 7): "A",
    (4, 7): "D",
    (1, 9): "C",
    (2, 9): "A",
    (3, 9): "C",
    (4, 9): "C",
}
tic = time.perf_counter()
print("Part 2:\t", astar(Node(amphipods)))
toc = time.perf_counter()
print(f"{toc-tic:6.1f} sec")
