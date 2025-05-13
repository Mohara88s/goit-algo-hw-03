def move_discs(num_of_discs, source, additional, destination, rods):
    if num_of_discs == 1:
        disc = rods[source].pop()
        rods[destination].append(disc)
        print(rods)
    else:
        move_discs(num_of_discs-1, source, destination, additional, rods)
        move_discs(1, source, additional, destination, rods)
        move_discs(num_of_discs-1, additional, source, destination, rods)


def main():
    while True:
        try:
            num_of_discs = int(input("Enter the number of discs "))
            if num_of_discs < 1 or num_of_discs > 15:
                print('The number of discs must be a positive integer and no more than 15')
            else:
                rods = {"A":[i for i in range(num_of_discs, 0, -1)], "B":[], "C":[]}
                print(rods)
                move_discs(num_of_discs, "A", "B", "C", rods)
                break
        except Exception as e:
            print(f'Error - {e}')

if __name__ == "__main__":
    main()