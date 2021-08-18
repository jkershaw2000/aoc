import System.IO
import Calculator ( calc )

mysum::Integer -> [String] -> Integer
mysum n (x:xs) | null xs = calc x + n
               | otherwise =  mysum (n + calc x) xs

main :: IO()
main = do
    file <- openFile "../18.in" ReadMode 
    inputData <- hGetContents file
    print (mysum 0 (lines inputData))
    hClose file