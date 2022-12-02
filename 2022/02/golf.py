print(sum("   B XC YA ZA XB YC ZC XA YB Z".find(x[:3]) for x in open("a"))/3,sum("   B XC XA XA YB YC YC ZA ZB Z".find(x[:3]) for x in open("a"))/3)
