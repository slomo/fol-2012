import Codec.TPTP
import System.Cmd
import System.IO
import System.Environment
import Data.Generics



main = do
  a <- parseFile "a.tptp"
  --map jsonify a
  putStr("fu")

getString (AtomicWord s) = s
getName  (AFormula {name = s}) = getString s
getRole  (AFormula {role = (Role {unrole = s})}) = s
getFormular (AFormula { formula = f }) = genTerm $ unwrapF f
genTerm (BinOp f1 (:=>:) f2) = "{"++
                               " BinOP " ++ ":"++ "=>" ++ "," ++
                               "lterm" ++ ":" ++ evalTerm (unwrapT f1) ++ "," ++
                               "rterm" ++ ":" ++ evalTerm (unwrapT f2) ++ "," ++
                               "}"
evalTerm  (AtomicWord s) = s


getBinOP = ""
jsonify a = "{" ++
            " name " ++ ":" ++ getName a ++ " ," ++
            " type " ++ ":" ++ getRole a ++ " ," ++
            " formular " ++ ":" ++ getFormular a++","