""" Advent of Code 2015. Day 21: RPG Simulator 20XX """

# Some notes regarding the problem:
# The boss and the player starts with equal amount of
# hit_points in the case of my input.
# Therefore, to win, the follwing inequality must hold:
# damage - boss_armor >= boss_damage - armor
# which can be simplified further to:
# damage + armor >= boss_damage + boss_armor
# 
# And conversely, to lose is the opposite:
# damage + armor < boss_damage + boss_armor
#
# Thus, we see that damage and armor values count
# the same.
#
# I also introduced a constraint on the damage, as there is no
# point in having more armor than boss_damage - 1, since
# you will lose a hit point regardless.
# However, for my input that constraint didn't do anything,
# so I removed it.

####################
# ITEM SHOP
# 
# item_type = [(cost, armor/damage), ...]
#
# one and only one of these
weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
# zero or one of these
armor = [0, 13, 31, 53, 75, 102] 
# zero, one or two of rings


# My input
boss_hit_points = 100
boss_damage = 8
boss_armor = 2

# My starting hit points
hit_points = 100

# Have not generalized the solution for differing starting
# hit points, though

rings = [[], (25, 20), (50, 40), (100, 80)]
# create ring table
def ring_table(fun):
  max_ring = len(rings) - 1 
  max_rings = 2*max_ring 
  answer = [0 for __ in range(max_rings+1)]
  for value in range(1, max_rings+1):
    options = [
      sum(rings[i])
      if i == value - i else
      (fun(rings[i]) + fun(rings[value-i]))
      for i in range(1, value // 2 +1)
      if i <= max_ring and value - i <= max_ring
      ]
     
    if value < len(rings):
      # Adding the single ring option
      options.extend(rings[value])

    answer[value] = fun(options)

  return answer

def compute_gold(fun):
  # Make a look up table of best combinations
  # of the rings
  rings = ring_table(fun)

  # The limit to abide to, is the sum of
  # boss damage and boss armor, subtracet by 1
  # if looking for the maximum amount to spend
  limit = boss_damage + boss_armor - (fun == max)

  return fun(
    # Summing the cost of the various options
    # Starting with a weapon and trying 
    # all different constellations of 
    # 0 or 1 piece of armors and / or
    # 0, 1 or 2 pieces of rings
    cost +
    fun(
      a + rings[limit - points - i]
      # armor[0] = 0 to take care of the 0 piece of armor option
      for i, a in enumerate(armor)
      if i < limit - points
    )
    for cost, points in weapons
  )

print("PART 1:\t", compute_gold(min)) 
print("PART 2:\t", compute_gold(max)) 
