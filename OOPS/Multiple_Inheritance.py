# multiple inheritance in js is joke 
# Avoids multiple inheritance with classes (to prevent ambiguity), but supports it with interfaces.
# Supports multiple inheritance directly and uses MRO to resolve conflicts.

# how MRO (Method Resolution Order)
    # inheritance ke order pe Child(high,low,lower,lowest)

# super().methon_name() //automatically inject he self
# ParentClass.method_name(self) //when you want to ignore MRO

# Conclusion:
# Use super() jab inheritance ke saath kaam kar rahe ho, kyunki ye MRO ko follow karta hai aur cleaner hai.
# Direct parent class ka naam + self tab use karo jab tum specific parent class ka method call karna chahte ho, MRO ko ignore karke.

class Papa:
    def showTraits(self):
        print("Papa's Discipline")

class Mummy: 
    def showTraits(self):
        print("Mummy's Kindness")

class Child(Papa,Mummy):
    def showTraits(self):
        super().showTraits() # MRO ka simple funda hai ke jo paihle inherit hua hai uska he chalega paihle 
        # Mummy.showTraits(self) aise call me self ko explicitly pass karna hoga kyonki parent the init() nhi chala initialize to kiya nhi to self pass he nhi hua 
        print('Child is Child, he doesnt know what trait it have')

c1 = Child()
c1.showTraits()