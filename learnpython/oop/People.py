
class People():

    def __init__(self):
        self.name='11'
        # print("init")
        pass
    @classmethod
    def say(self):
        print(self.name)
        pass

People.say()