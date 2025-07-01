class Maschine:
    def __init__(self, id: int, name: str, funktion: str, status: str = "offline"):
        self._id = id
        self._name = name
        self._funktion = funktion
        self._status = None
        self.set_status(status)

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def funktion(self) -> str:
        return self._funktion

    @property
    def status(self) -> str:
        return self._status

    def set_status(self, status: str):
        if status not in ["offline", "online"]:
            raise ValueError("Status must be 'offline' or 'online'.")
        self._status = status

    def execute_function(self):
        return f"Maschine {self.id} ({self.name}) is performing its function: {self.funktion}"

    def get_info(self) -> str:
        return f"Maschine ID: {self.id}, Name: {self.name}, Funktion: {self.funktion}, Status: {self.status}"