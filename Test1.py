

  

    
             

           

              
       
  



def is_semiprime(n):
    for d1 in range(2, int(n**.5)+1):
        if n % d1 == 0:
            d2 = n / d1
            return is_prime(d1) and is_prime(d2)
    return 1


   
       


def isSumOfKprimes(N, K): 

      

    # N < 2K directly return false 

    if (N < 2 * K): 

        return 0

  

    # If K = 1 return value depends 

    # on primality of N 

    if (K == 1): 

        return is_semiprime(N) 

  

    if (K == 2): 

          

        # if N is even directly 

        # return true; 

        if (N % 2 == 0): 

            return 1

  

        # If N is odd, then one  

        # prime must be 2. All  

        # other primes are odd 

        # and cannot have a pair 

        # sum as even. 

        return is_semiprime(N - 2); 

      

  

    # If K >= 3 return true; 

    return 1

  
# Driver function 

n = int (input())

k = 2

if (isSumOfKprimes (n, k)): 

    print ("Yes") 

else: 

    print ("No")
