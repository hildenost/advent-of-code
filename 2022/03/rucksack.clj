(ns aoc.2022.03
  (:require
    [clojure.string :as str]
    [clojure.set :as set])
  )

(defn read-input []
  (-> "input.txt"
      (slurp)
      (str/split #"\n")
     ))

(def rucksacks (read-input))

(def lists (map #(partition (/ (count %) 2) %) rucksacks))
(def sets (for [l lists] (map set l)))

(def items (map #(apply set/intersection %) sets))
(def ascii (map int (map first items)))
(def priorities (map #(if (< % 96) (- % 38) (- % 96)) ascii))
(println (reduce + priorities))


