class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        combined_people = self.people + other.people
        return Group(new_name, combined_people)

    def __str__(self):
        members_names = ", ".join(str(person) for person in self.people)
        return f"Group {self.name} with members {members_names}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"


# Example usage
if __name__ == "__main__":
    # Test Person class
    p1 = Person("John", "Smith")
    p2 = Person("Jane", "Doe")
    
    # Test Person string representation
    print(p1)  # Should print: John Smith
    print(p2)  # Should print: Jane Doe
    
    # Test Person concatenation
    p3 = p1 + p2
    print(p3)  # Should print: John Doe
    
    # Test Group class
    g1 = Group("First Group", [p1, p2])
    g2 = Group("Second Group", [p3])
    
    # Test Group length
    print(len(g1))  # Should print: 2
    print(len(g2))  # Should print: 1
    
    # Test Group string representation
    print(g1)  # Should print: Group First Group with members John Smith, Jane Doe
    print(g2)  # Should print: Group Second Group with members John Doe
    
    # Test Group concatenation
    g3 = g1 + g2
    print(g3)  # Should print: Group First Group Second Group with members John Smith, Jane Doe, John Doe
    print(len(g3))  # Should print: 3
    
    # Test Group iteration
    for person in g3:
        print(person)  # Should print: Person 0: John Smith, Person 1: Jane Doe, Person 2: John Doe