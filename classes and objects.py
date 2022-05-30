class Student:
    
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        #instanceattributes
        self.name = str(name)
        self.age = int(age)
        self.track = list(track)
        self.score = float(score) 
        
    def change_name(self, change_name):
        change_name = str(change_name)
        print(f"New name is {change_name}")
    
    def change_age(self, change_age):
        change_age = int(change_age)
        print(f"{self.name}'s age is {change_age}")
    
    def add_track(self, new_track):
        new_track = list(new_track)
        print(f"{self.name}'s track is {new_track}")
        
    def get_score(self, new_score):
        new_score = float(new_score)
        print(f"{self.name}'s score is, {new_score}")
        
#instance1
bob = Student("Bob", 26, ["FE", "BE"], 20.90)
#instance2
peter= Student("Peter", 34, ["UI/UX"], 25.35)
print(bob.name, bob.age, bob.track, bob.score, sep='\n')
print("")
peter.change_name("Peter")
peter.change_age(34)
peter.add_track(["UI/UX"])
peter.get_score(25.35)
    

 
# # Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# # Expected methods


 
