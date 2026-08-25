def main():
    print("WELCOME TO LOS POLLOS HERMANOS")

    rating = float(input("What's your rating?: "))

    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Good")
    else:
        print("Disgusting")

if __name__ == "__main__":
    main()
