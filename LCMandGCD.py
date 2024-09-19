def lcmAndGcd(a, b):

    def findGCD(a,b):
        # method to compute gcd ( recursion )
        if(b == 0):
            return a
        else:
            return findGCD(b, a % b)
        
    gcdVal = findGCD(a,b)    
        
    def findLCM(a,b):
        if a > b:
            greater = a
        else:
            greater = b

        while(True):
            if((greater % a == 0) and (greater % b == 0)):
                lcm = greater
                break
            greater += 1
        return lcm
    
    lcmVal = findLCM(a,b)
    
    #  Shorter and modified version of finding LCM, but can only be done when you have got the GCD
    #  Calculate LCM using the relation LCM * GCD = a * b

    #  def findLCM(a, b, gcdVal):
    #      return (a * b) // gcdVal

    return [lcmVal, gcdVal]   

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

result = lcmAndGcd(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result[0]}")
print(f"The GCD of {num1} and {num2} is: {result[1]}")