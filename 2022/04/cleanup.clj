(ns aoc.2022.04
     (:require
        [clojure.string :as str]))

(defn read-input [& {:keys [sep] :or {sep nil}}]
  (let [i (-> "input.txt"
          (slurp)
          (str/split #"\n")
         )
        i (when (some? sep) (map #(str/split % sep) i))
        ]
    i
    ))


(println (read-input :sep #"[-,]"))
(println (read-input))
;;(println (map pairs (read-input)))
