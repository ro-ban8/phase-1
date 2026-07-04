def main():
    print_drug(if_Yes())
    
def if_Yes():
    while True :
        question = input("Have you taking the Medicine of the day? ")
        if question == "Yes":
            return question 
        else:
            continue

def print_drug(drugs):
    drugs = [
        {"morning" : "penicillin" , "afternoon" : "azitromycin" , "evening" : "macrolids"},
        {"morning" : "steptomycin" , "afternoon" : "amcilline" , "evening" : "amipicillin"},
        {"morning" : "eritromycin" , "afternoon" : "penicillin" , "evening" : "rimapicin"}
    ]
    for drug in drugs:
        print(drug["morning"], drug["afternoon"], drug["evening"], sep=":")



main()
