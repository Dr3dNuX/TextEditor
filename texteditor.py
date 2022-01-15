
class editor:
    def __init__(self) -> None:
        self.inFile = None
        self.outFile = None
        self.options = ['return', 'new', 'open', 'quit']
        self.running = True
        self.menu()
    
    def display(self):
        self.outFile.seek(0)
        for line in self.outFile:
            print(line,end='')
    
    def menu(self):
        print('[+] - MENU - [+]')

        while self.running == True:
            print(self.options)
            menu = input('[+]> ')
            
            if menu == 'return':
                print('RETURNING...')
                break

            elif menu == 'open':
                print('opening a file')
                while True:
                    print('file name please... ')
                    menu = input('[+]> ')
                    self.inFile = open('{}.txt'.format(menu),'a')
                    self.outFile = open('{}.txt'.format(menu),'r')
                    print('Thank You...')
                    self.editor()
                    break

            elif menu == 'quit':
                print('QUITTING')
                self.running = False
                break
            
            elif menu == 'new':
                print('making a new file')
                while True:
                    print('file name please... ')
                    menu = input('[-]> ')
                    self.inFile = open('{}.txt'.format(menu),'w')
                    self.outFile = open('{}.txt'.format(menu),'r')
                    print('Thank You...')
                    self.editor()
                    break
            
            else:
                print('error returning')
                break


    def editor(self):
        while self.running == True:
            self.display()
            text = input('>> ')
            if text == 'menu':
                self.menu()

            else:
                self.inFile.write(text + '\n')
                self.inFile.flush()
            
        


a = editor()