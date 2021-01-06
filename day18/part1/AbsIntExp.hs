-- Haskell data types for the abstract syntax.
-- Generated by the BNF converter.

module AbsIntExp where

import Prelude (Char, Double, Integer, String)
import qualified Prelude as C (Eq, Ord, Show, Read)

data IntExp = Add IntExp IntExp | Mul IntExp IntExp | Nmb Integer
  deriving (C.Eq, C.Ord, C.Show, C.Read)
