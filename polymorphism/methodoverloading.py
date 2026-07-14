#overloading is a feature in which we can have methods of same name but differ in number of parameters

#usually python doesnt support method overloading but,
#overloading can be achieved by using default arguments or variablelength arguments

class Calculator():
    def ok (self, *args):
            if len(args)==3:
               total = 1
               for i in args:
                   total*=i
               return total
            elif len(args)==2:
                total=0
                for i in args :
                    total+=i
                return total
            else:
                return("chal nikal")
d=Calculator()
print(d.ok(2,3))
