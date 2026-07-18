import random

cards = ["rohan" ,
    "chinmaya" ,
        "sakshi" ,
     "sarh" ,"bhor", "soanli" , "sama" ,"sumit" ]

days = {"monday":"ss"}

choise = random.shuffle(cards)
for choise in cards[:3] : 
  if choise == 3:
    days["monday"] = +3
    print(days)