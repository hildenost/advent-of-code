""" Advent of Code 2021. Day 4: Giant Squid """
import math

with open("input.txt") as f:
  numbers, *raw_boards = f.read().split("\n\n")

numbers = [int(n) for n in numbers.split(",")]
boards = [
    [int(n) for row in rb.splitlines() for n in row.split()]
    for rb in raw_boards
]

N = int(math.sqrt(len(boards[0])))

def check_board(board):
  for i in range(N):
     row_count = board[N*i:N*(i+1)].count(None)
     col_count = board[i:N*(N-1) + (i+1):N].count(None) 
     if N in [row_count, col_count]:
        return True 
  return False

def play_bingo(boards, part=1):
  for n in numbers:
    boards = {
        tuple(None if s == n else s for s in b)
        for b in boards
    }
    won_boards = {b for b in boards if check_board(b)}
    boards -= won_boards

    if (part == 1 and won_boards) or (part == 2 and not boards):
      return n * sum(v for v in won_boards.pop() if v is not None)

    
print("PART 1:\t", play_bingo(boards))
print("PART 2:\t", play_bingo(boards, part=2))
