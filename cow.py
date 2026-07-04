import cowsay
import sys
while True:
    if sys.argv != "goodbye":
        cowsay.cow(sys.argv[1])
        break
        
   
        

