class Test(object):
    def run(self):
        num = 5
        self.play(num)

    def play(self,num):
        print(num)

test = Test()
test.run()