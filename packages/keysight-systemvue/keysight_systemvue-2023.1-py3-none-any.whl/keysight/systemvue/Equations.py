class Equations:
    def __init__(self, equation) -> None:
        self.equation = equation

    def run(self):
        self.equation.run()
    
    @property
    def name(self) -> str:
        return self.equation.name
    
    @property
    def text(self) -> str:
        return self.equation.text

    @text.setter
    def text(self, eqnText: str):
        self.equation.text = eqnText
