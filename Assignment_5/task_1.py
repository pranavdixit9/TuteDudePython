my_dict = {"Alice":85, "Bob":80, "Charlie":90}

name = input("Enter the student's name: ")
if name in my_dict:
    score = my_dict[name]
    print(f"{name}'s marks: {score}")
else:
    print("Student not found.")