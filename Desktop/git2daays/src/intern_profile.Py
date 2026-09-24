intern_name = "Sachin Dixit"
role ="Software Engineer Intern"
department = "Engineering"
skills = [
    "Python",
    "JavaScript",
    "Java"
    "html"

]
def print_profile():
    print("Intern Name:", intern_name)
    print("Role:", role)
    print("Department:", department)
    print("Skills:")
    for skill in skills:
        print("-", skill)
if __name__ == "__main__":
    print_profile()
