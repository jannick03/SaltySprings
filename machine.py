class machine:
    def __init__(self, id: int, name: str, funktion: str, status: str = "offline"):
        self.id = id
        self.name = name
        self.funktion = funktion
        self.status = None
        self.set_status(status)

    def set_status(self, status: str):
        if status not in ["offline", "online"]:
            raise ValueError("Status must be 'offline' or 'online'.")
        self.status = status

    def execute_function(self):
        return f"Maschine {self.id} ({self.name}) is performing its function: {self.funktion}"

    def get_info(self) -> str:
        return f"Maschine ID: {self.id}, Name: {self.name}, Funktion: {self.funktion}, Status: {self.status}"