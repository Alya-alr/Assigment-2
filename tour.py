class Tour:
    def __init__(self, date, group_size, guide):
        # Initialize the Tour object with the provided attributes
        self.date = date
        self.group_size = group_size
        self.guide = guide

    def display(self):
        # Display information about the tour
        print(f"Date: {self.date}")
        print(f"Group Size: {self.group_size}")
        print(f"Guide: {self.guide}")