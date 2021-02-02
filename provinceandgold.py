G, S, C = map(int, input().split())

goldPower = G*3
silverPower = S*2
copperPower = C*1

totalPower = goldPower+silverPower+copperPower

if totalPower <=1 :
    print("Copper")
elif totalPower == 2:
    print("Estate or Copper")
elif totalPower <= 4:
    print("Estate or Silver")
elif totalPower == 5:
    print("Duchy or Silver")
elif totalPower <= 7:
    print("Duchy or Gold")
elif totalPower >= 8:
    print("Province or Gold")
