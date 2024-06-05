class Factorial:
    @staticmethod
    def looping(num:int):
        val = 1
        for x in range(num):
            if num > 0:
                val *= num
                num -= 1
        print(str(val))

    @staticmethod
    def recursing(num:int):
        print(str(Factorial.recursion(num)))
        
    @staticmethod
    def recursion(num:int):
        if num == 0:
            return 1
        else:
            return num*Factorial.recursion(num-1)
        

Factorial.looping(5)
Factorial.recursing(5)