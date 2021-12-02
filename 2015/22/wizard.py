""" Advent of Code 2015. Day 22: Wizard Simulator 20XX """
from copy import deepcopy


spells = ["Magic Missile", "Recharge", "Drain", "Shield", "Poison"] 
spell_costs = {
    "Magic Missile": 53,
    "Drain":         73,
    "Shield":       113,
    "Poison":       173,
    "Recharge":     229,
}

class Boss:
  def __init__(self, hit_points, damage):
    self.hit_points = hit_points
    self.damage = damage

  def attack(self, other):
    other.hit_points -= self.damage - other.armor

class Player:
  def __init__(self, hit_points, mana):
    self.hit_points = hit_points
    self.mana = mana

    self.armor = 0

    self.poison_timer = 0
    self.recharge_timer = 0
    self.shield_timer = 0

  def cast(self, spell, boss):
    """
    Magic Missile: 53 mana, 4 damage
    Drain:         73 mana, 2 damage, 2 heal
    Shield:       113 mana, effect: 6 turns, armor += 7
    Poison:       173 mana, effect: 6 turns, 3 damage per turn
    Recharge:     229 mana, effect: 5 turns, mana += 101 per turn
    """
    self.mana -= spell_costs[spell]

    if spell == "Magic Missile":
      boss.hit_points -= 4
    elif spell == "Drain":
      boss.hit_points -= 2
      self.hit_points += 2
    elif spell == "Shield":
      self.shield_timer = 6
      self.armor = 7
    elif spell == "Poison":
      self.poison_timer = 6
    elif spell == "Recharge":
      self.recharge_timer = 5

class Game:
  def __init__(self, player, boss):
    self.player = player
    self.boss = boss

    self.cost = 0

  def _do_effects(self):
    if self.player.poison_timer:
      self.player.poison_timer -= 1
      self.boss.hit_points -= 3
    if self.player.recharge_timer:
      self.player.recharge_timer -= 1
      self.player.mana += 101
    if self.player.shield_timer:
      self.player.shield_timer -= 1
      if self.player.shield_timer == 0:
        self.player.armor = 0

  def _is_boss_alive(self):
    return self.boss.hit_points > 0

  def _is_player_alive(self):
    return self.player.hit_points > 0

    

  def play(self, spell, hard=False):
    # gameplay:
    # 
    # - player turn
    # apply effects
    # check alive
    # player spell
    #
    # - boss turn
    # apply effects
    # check alive
    # boss attack
    # check alive

    # PLAYER TURN
    if hard:
      self.player.hit_points -= 1
      if not self._is_player_alive():
        return "boss"
    self._do_effects()
    if not self._is_boss_alive():
      return "player"

    self.player.cast(spell, self.boss)
    self.cost += spell_costs[spell]

    # BOSS TURN
    self._do_effects()
    if not self._is_boss_alive():
      return "player"
    self.boss.attack(self.player)
    if not self._is_player_alive():
      return "boss"

def simulate(player_stats, boss_stats, hard=False):
  # Initializing the games
  boss = Boss(**boss_stats)
  player = Player(**player_stats)
  games = [Game(player, boss)]

  min_spent = 99999999999999999999999999999999999999999 

  while games:
    # Removing games that have superceded the minimum
    games = [g for g in games if g.cost < min_spent]

    # The game to explore
    game = games.pop()

    # Possible spells to choose from
    # Since the effect spells can be cast the same round it expires,
    # they are valid if the timer is less than 1
    # In addition, we need to check for enough mana
    valid_spells = (
      s for s in spells
      if ((s == "Poison" and game.player.poison_timer <= 1)
      or (s == "Recharge" and game.player.recharge_timer <= 1)
      or (s == "Shield" and game.player.shield_timer <= 1)
      or s in ["Drain", "Magic Missile"])
      and spell_costs[s] <= game.player.mana
    )

    for s in valid_spells:
      g = deepcopy(game) 

      winner = g.play(s, hard=hard)
      if winner == "player":
        min_spent = min(min_spent, g.cost)
      elif winner is None:
        # The game is not finished yet
        games.append(g)
      # if winner is the boss, we try to forget this game :(

  return min_spent

print("PART 1:\t", simulate(
  {"hit_points": 50, "mana": 500},
  {"hit_points": 51, "damage": 9},
))
print("PART 2:\t", simulate(
  {"hit_points": 50, "mana": 500},
  {"hit_points": 51, "damage": 9},
  hard=True
))
