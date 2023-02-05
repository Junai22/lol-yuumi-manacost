max_mana = int(input("Whats your max mana?:"))

level = [0,40,45,50,55,60] 
base_mana = int(input("Whats your level of ability?:"))

if(base_mana > 5):
   print("The max level of the ability is 5")
else:
   mana_cost = max_mana * 0.12 + level[base_mana]
   print(mana_cost)