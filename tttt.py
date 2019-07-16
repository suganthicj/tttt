def isPrime(n): 

# Driver code 
if __name__ == "__main__" : 
       
    # Corner case 
    if n <= 1 : 
        return False
  
    # check from 2 to n-1 
    for i in range(2, n): 
        if n % i == 0: 
            return False
  
    return True
  
# Function to print primes 
def printPrime(n): 
    for i in range(2, n + 1): 
        if isPrime(i): 
            print(i, end = " ") 
     n = 7
    # function calling 
    printPrime(n) 
