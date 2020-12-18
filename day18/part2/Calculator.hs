module Calculator where

import ParIntExp  -- Module for lexing and parsing the input
import EvalIntExp -- Performs the actual calculations
import ErrM        -- Gives access to various error types

handleErr :: Err a -> a -- simple error handling
handleErr (Ok t) = t
handleErr (Bad s) = error s

calc :: String -> Integer -- variable free Calculator
calc = eval . handleErr . pIntExp . myLexer
