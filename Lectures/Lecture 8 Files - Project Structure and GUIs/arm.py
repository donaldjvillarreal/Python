class Arm:
    def __init__(self):
        self.raised = False
        
    def lift(self):
        print('Lifting arm')
        self.raised = True
        
    def lower(self):
        print('Lowering arm')
        self.raised = False