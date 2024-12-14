-- runghc 01.hs < input.txt
import           Data.List (sort)

readInput :: String -> ([Int], [Int])
readInput s = (sort . parse head $ s, sort . parse last $ s)
  where
    parse f = map (read . f . words) . lines

computeA :: [Int] -> [Int] -> Int
computeA ls rs = foldr (\(l, r) acc -> acc + (abs $ l - r)) 0 $ zip ls rs

getCountofNumber :: [Int] -> Int -> Int
getCountofNumber xs n = length $ filter (\x -> x == n) xs

sumOfList :: [Int] -> Int
sumOfList = foldr (+) 0

computeB :: [Int] -> [Int] -> Int
computeB ls rs = sumOfList $ map (\l -> l * getCountofNumber rs l) ls

main :: IO ()
main = do
  str <- getContents
  let (l, r) = readInput str
  print $ computeA l r
  print $ computeB l r
