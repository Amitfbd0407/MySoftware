class Button:
    def __init__(self, label):
        self.label = label  # Button label

    def click(self):
        print("Click")


# Example usage:
if __name__ == "__main__":
    button = Button("Submit")
    button.click()  # This will print "Click"
