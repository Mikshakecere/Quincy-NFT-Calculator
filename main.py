def value_calculate(value, round):
    if round < 31:
        value *= 1.1
    elif round > 80:
        value *= 1.02
    else:
        value *= 1.05

    if value > 10000000:
        value = 10000000

    return value

def main():
    roundcashBoolean = input("Choose either 'round' or 'cash' amount to sell nft at:")

    if roundcashBoolean == "round":
        preRound = int(input("What round are you on currently: "))
        postRound = int(input("What round would you like to sell at: "))
        nftValue = float(input("What is the value of the nft: "))

        while preRound is not postRound:
            nftValue = value_calculate(nftValue, preRound)
            preRound += 1

        print("The nft will sell for " + str(round(nftValue,0)) + " at round " + str(postRound))

    elif roundcashBoolean == "cash":
        cash = int(input("What cash amount would you like to sell at: "))
        preRound = int(input("What round are you on currently: "))
        nftValue = int(input("What is the value of the nft: "))

        while nftValue < cash:
            nftValue = value_calculate(nftValue, preRound)
            preRound += 1

        print("You must wait until round " + str(preRound) + " to sell the nft for at least $" + str(cash))

    else:
        print("L")
        exit()

    main()
#i wrote all this shit in a day after finding out the equation lmfaoo code is so ez

main()
