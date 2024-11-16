class Button:
    def __init__(self, label):
        self.label = label 

    def click(self):
        print("Click")


if __name__ == "__main__":
    button = Button("Submit")
    button.click()  
