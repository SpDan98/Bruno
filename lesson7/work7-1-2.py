class StringVar:
    def __init__(self,value) -> None:
        self.value=value
    def get(self):
        return self.value
    def set(self,value):
        self.value=value
sv=StringVar('value')
