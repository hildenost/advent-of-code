""" Advent of Code 2021. Day 4: Giant Squid """

with open("input.txt") as f:
  numbers, *raw_boards = f.read().splitlines()

numbers = [int(n) for n in numbers.split(",")]

boards = []
for i in range(100):
  b = [int(n) for n in " ".join(raw_boards[6*i + 1:6*(i+1)]).split()]
  boards.append((b, [0 for _ in range(25)]))

def check_board(board):
  for i in range(5):
     if all(board[5*i:5*i+5]):
        return True 
     if all(board[i:25-(5-i) + 1:5]):
        return True 
  return False

def play_bingo(boards, part=1):
  winning_boards = []
  winner = False
  for n in numbers:
    for i, (b, mask) in enumerate(boards):
      if i in winning_boards:
        continue
      if n in b:
        mask[b.index(n)] = 1
        if check_board(mask):
          if (part == 1
          or (part == 2 and len(winning_boards) == len(boards) - 1)):
            return n * sum(v for i, v in enumerate(b) if mask[i] == 0)

          winning_boards.append(i)

    
print("PART 1:\t", play_bingo(boards))
print("PART 2:\t", play_bingo(boards, part=2))

