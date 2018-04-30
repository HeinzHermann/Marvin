class A():
    def tester(self):
        self.a = 'hello there'
        
    def opener(self):
        self.tester()
        call = B()
        call.tryout()
        

class B():
    
    def tryout(self):
        print(number.a)
        

def main():
    number = A()
    number.opener()
    print('hello?')

if __name__ == '__main__':
    main()        
