class Calculation():


    def sum(self,a,b):
        return a+b
    

    def sub(self,a,b):
        return a-b
    

    def multiply(self,a,b):
        return a*b
    

    def div(self,a,b):
        return a/b
    
    
    def bool_check(self,bool_: bool):
        return bool_

    def check_data_type(self, data_input: input):
        data_input = int(input())
        data_input_2 = int(input())
        return data_input * data_input_2
    
    def find_playndrome(self, arg: input) -> str:
        arg = input()
        return arg ==arg[::-1]