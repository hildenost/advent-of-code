(ns aoc.2022.02
  (:require
      [clojure.string :as str]))

(def scores [
  "BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"
  ])
(def scores2 [
  "BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"
  ])

(defn parse-input []
  (for [line (str/split-lines (slurp "input.txt"))] (str/replace line #" " ""))
)

(defn score [rounds scores]
  (map #(+ 1 (.indexOf scores %)) rounds))

(def rounds (parse-input))

(defn part1 []
  (reduce + (score rounds scores))
)

(defn part2 []
  (reduce + (score rounds scores2))
)

(println "Part 1:" (part1))
(println "Part 2:" (part2))


