#!/usr/bin/python3

def main():


# List in reverse order
    list_a = ["apple","soda","55","box"]
    print(list_a)
    print(list_a[0])
    print(list_a[-2:])
#solution
    print(list_a[0])
    print(list_a[1])
    print(list_a[2])


    list_b = ["honda","toyota","ford"]

    dream_cars = ["lambo","bugatti","bentley"]
    list_b.append(dream_cars)
    list_c = ["bmw","audi","chevy"]
    list_b.extend(list_c)

    print(list_b)

#solution 
    print(list_b[3][2])
    print(list_b[1])


if __name__ == "__main__":
    main()
