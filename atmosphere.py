def main():
    layer = input("Descent atmosphere layer: ").title().strip()

    if layer == "Exosphere":
        print("Your altitude level will be between 700 and 10,000 km")
    elif layer == "Thermosphere":
        print("Your altitude level will be between 85 and 700 km")
    elif layer == "Mesosphere":
            print("Your altitude level will be between 50 and 85 km")
    elif layer == "Stratosphere":
            print("Your altitude level will be between 12 and 50 km")
    elif layer == "Troposphere":
            print("Your altitude level will be between 0 and 12 km")

    alt = float(input("Enter exact altitude: "))

    exo = (alt/2000)
    thermo = (alt/500)
    meso = (alt/200)
    strato = (alt/75)
    tropo = (alt/20)

    ex = (exo + thermo + meso + strato + tropo)
    th = (thermo + meso + strato + tropo)
    me = (meso + strato + tropo)
    st = (strato + tropo)
    tr = (tropo)

    if alt > 700:
        print("Total descent time: ", round(ex,1))
    elif alt > 85:
        print("Total descent time: ", round(th,1))
    elif alt > 50:
        print("Total descent time: ", round(me,1))
    elif alt > 12:
        print("Total descent time: ", round(st,1))
    elif alt > 0:
         print("Total descent time: ", round(tr,1))



if __name__ == "__main__":
    main()
