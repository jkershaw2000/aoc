import System.IO
import Calculator ( calc )

mysum::Integer -> [String] -> Integer
mysum n (x:xs) | null xs = calc x + n
               | otherwise =  mysum (n+calc x ) xs

main :: IO()
main = do
    handle <- openFile "../18.in" ReadMode 
    contents <- hGetContents handle
    print (mysum 0 (lines contents))
    hClose handle