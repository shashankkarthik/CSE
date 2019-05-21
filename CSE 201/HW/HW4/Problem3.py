def get_investments(dict_etf):
    for i in dict_etf:
        dict_etf[i] = float(input("\nEnter ammount invested in "+i+":")) #Requests user to input investment for each etf

def get_total(dict_etf):    #Gets total investement
    total = 0
    for etf in dict_etf:
        total += dict_etf[etf]
    return total

def output(dict_etf,total):
    print("\nETF          Percentage")
    print("-----------------------")
    for i in dict_etf:
        print(i,"          ","{}%".format(round(dict_etf[i]*100/total,2))) #Outputs etf and percentage of total investement invested in said etf



def main():
    dict_etf = {"SPY":0,"QQQ":0,"EEM":0,"VXX":0}

    get_investments(dict_etf) #Gets investments for each ETF

    total = get_total(dict_etf) #Gets total investments

    output(dict_etf,total) #Outputs relevent data


main()
