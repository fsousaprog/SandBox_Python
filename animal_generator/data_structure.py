class AnimalInLine:
    def __init__(self, animal):
        self.animal = animal
        self.next = None


class Line:
    def __init__(self):
        self.head = None

    def append(self, animal):
        new_animal = AnimalInLine(animal)
        if self.head is None:
            self.head = new_animal
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_animal

    def show_line(self):
        current = self.head
        while current:
            print(current.animal)
            current = current.next


class FriendsGraph:
    def __init__(self):
        self.graph = {}

    def add_animal(self, animal_id):
        if animal_id not in self.graph:
            self.graph[animal_id] = []

    def add_friendship(self, animal_id1, animal_id2):
        if animal_id1 in self.graph and animal_id2 in self.graph:
            self.graph[animal_id1].append(animal_id2)
            self.graph[animal_id2].append(animal_id1)

    def show_friendships(self):
        for vertex, neighbors in self.graph.items():
            print(vertex, "->", neighbors)
