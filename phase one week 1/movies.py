import random

movies = ["Avatar", "Interstellar", "Inception", "The Dark Knight", "Inside Out"]


def main():
    shuffled_copy = random.sample(movies, len(movies))
    tickets = how_many_tickets()

    if tickets > len(shuffled_copy):
        print("Not enough movies available")

    else:
        for i in range(tickets):
            print(f"ticket {i + 1}:", shuffled_copy[i])
        next_movie = tickets

        while True:
            ask = input("Reserve another ticket?(y/N) ").strip().lower()

            if ask == "y":

                if next_movie >= len(shuffled_copy):

                    print("no more movies avilable")
                    break

                else:
                    print(f"ticket {next_movie +1}:", shuffled_copy[next_movie])
                    next_movie = next_movie + 1

            elif ask == "n":
                break


def how_many_tickets():
    while True:
        try:
            tickets = int(input("How many tickets? "))
            if tickets <= 0:
                raise ValueError
            return tickets
        except ValueError:
            continue


main()
