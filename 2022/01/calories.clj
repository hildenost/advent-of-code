(require '[clojure.string :as str])

(defn sum [x] (reduce + x))

(defn count-calories []
  (def contents (slurp "input.txt"))
  (def elves (str/split contents #"\n\n"))
  (def calories (
      map (fn [x] (sum (
           map #(Integer/parseInt %) (str/split x #"\n")
           ))
      ) elves))

  (def sorted (sort > calories))
  (def part1 (first sorted))
  (def part2 (sum (take 3 sorted)))
  (println (format "Part 1:\t%s" part1))
  (println (format "Part 2:\t%s" part2))
)

(count-calories)
