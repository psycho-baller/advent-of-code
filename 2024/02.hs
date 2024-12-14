readInput :: String -> [[Int]]
readInput s = map (map read . words) $ lines s

computeA :: [[Int]] -> Int
computeA = length . filter safe


-- computeA = length . filter id . map safe
computeB :: [[Int]] -> Int
computeB xs = length $ filter (\x -> safe x || safeIfRemovedOne x) xs
  where
    safeIfRemovedOne xs =
      any safe $ map (\i -> removeAt i xs) [0 .. length xs - 1]

safe :: [Int] -> Bool
safe l = all asc diffs || all desc diffs
  where
    asc e  = 1 <= e && e <= 3
    desc e = -3 <= e && e <= -1
    diffs  = zipWith (-) (init l) (tail l)

removeAt :: Int -> [a] -> [a]
removeAt i xs
  | i < 0 || i >= length xs = xs -- Return the original list if index is out of bounds
  | otherwise = take i xs ++ drop (i + 1) xs

main :: IO ()
main = do
  str <- getContents
  let l = readInput str
  print $ computeA l
  print $ computeB l
