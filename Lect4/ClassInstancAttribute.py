
class Student:
    college="Jagannath University Jaipur"
    highestPackage="50LPA"
    
    def __init__(this,name,roll,cgpa,dream):
        this.name=name
        this.roll=roll
        this.cgpa=cgpa
        this.dream=dream
    
stud1= Student("Ashish",22002018, 7.5,"Google")
stud2=Student("Abhishek",2202004, 7.1, "Cyntexa")

print(stud1.highestPackage)
print(stud2.highestPackage)