male = int(input("Please put how many males in class: "))
female = int(input("Please put how many females in class: "))
total_pup = male+female
perca_male = (male/total_pup)*100
perca_female = (female/total_pup)*100
print("Male percentage: ", round((perca_male),2), "%", "\nFemale percentage: ", round((perca_female),2), "%")