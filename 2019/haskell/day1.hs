main = do
    filecontent <- readFile "../01/input.txt"
    let intList = map (read::String->Integer) (lines filecontent)
    let result = sum (map requiredFuel intList)
    print result
    let result2 = sum ( map fuel'sFuel intList )
    print result2

requiredFuel mass = mass `div` 3 - 2

fuel'sFuel mass
    | fuel <= 0 = 0
    | otherwise = fuel + fuel'sFuel fuel
    where fuel = requiredFuel mass
