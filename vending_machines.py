class machine():
    def __init__(self):
        self.name = ""
        self.inventory = {}

    def run_machine(self, name, inventory):
        selection = ""
        while True:
            print("Welcome to the {} machine!\nItems:Quantity\n".format(name))
            for k, v in inventory.items():
                print('{}:{}'.format(k,v))
            selection = input("\nPlease make a selection or q to quit: ")
            if  selection == 'q':
                break
            elif (selection in inventory and inventory[selection]):
                print('\nHere is your {}'.format(selection))
                inventory[selection] -= 1
            else:
                print('Sorry that item is not available.')


soda_machine = machine()
soda_machine.name = "Soda"
soda_machine.inventory = {'coke':1, 'mt. dew':6, 'dr. pepper':4}
soda_machine.run_machine(soda_machine.name, soda_machine.inventory)
