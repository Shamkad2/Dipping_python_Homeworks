
class User:

    def __init__(self, name, uid, level=None):
        self.name = name
        self.uid = uid
        self.level = level

    def __str__(self) -> str:
        return f"Пользователь {self.name}: ID-{self.uid}, уровень доступа-{self.level}"
    
    def __eq__(self, other) -> bool:
        if self.name == other.name and\
        int(self.uid) == int(other.uid):
            return True
        return False
    
if __name__ == "__main__":
    u = User("Piter", 114, 7)
    print(u)