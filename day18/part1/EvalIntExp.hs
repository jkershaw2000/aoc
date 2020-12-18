module EvalIntExp where

import AbsIntExp -- a module to represent abstract integer expressions
import Data.Map -- a module to represent finite mappings

eval :: IntExp -> Integer
eval (Mul a b) = eval a * eval b
eval (Add a b) = eval a + eval b
 -- eval (Neg a)   = negate (eval a)
eval (Nmb n)   = n


