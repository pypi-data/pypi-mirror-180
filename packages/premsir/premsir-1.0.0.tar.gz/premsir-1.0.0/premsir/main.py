class premsir(object):
    @staticmethod
    def quadratic_roots(a : int, b : int, c : int):
        d = b**2-4*a*c
        if d >= 0:
            print("Roots are real")
        else:
            print("Roots are imaginary")

    @staticmethod
    def fibonacci_series(term : int):
        t = 3
        a = 0
        b = 1
        print(a)
        print(b)
        while t <= term:
            c = a + b
            print(c)
            a = b
            b = c
            t += 1
    
    @staticmethod
    def greatest_integer(a : int, b : int, c : int):
        if a > b and a > c:
            print("%i is the greatest" % a)
        if b > a and b > c:
            print("%i is the greatest" % b)
        if c > a and c > b:
            print("%i is the greatest" % c)
    
    @staticmethod
    def star_pattern(rows : int):
        i = 1
        while i <= rows:
            j = 0
            while j < i:
                print("*", end="")
                j += 1
        print("\r")
        i += 1
    
    @staticmethod
    def number_pattern(rows : int):
        i = 1
        while i <= rows:
            j, k  = 0, 0
            while j < i:
                k += 1
                print(k, end="")
                j += 1
        print("\r")
        i += 1
    
    @staticmethod
    def even_or_odd(num : int):
        if num % 2 == 0:
            print("It is an even number")
        else:
            print("It is an odd number")
    
    @staticmethod
    def vowels_counter(args : str):
        count = 0
        for c in args.lower():
            if c in ["a", "e", "i", "o", "u"]:
                count += 1
        print(f"The sentence '{args}' has {count} vowels")

    @staticmethod
    def multiplication_table(num : int):
        for i in range(1, 11):
            print(f"{num} x {i} = {num*i}")

    @staticmethod
    def prime_number(num : int):
        p = 1
        d = 2
        while d <= num-1:
            if num % d == 0:
                p = 0
                break
            else:
                d += 1
        if p == 1:
            print("The integer is prime")
        else:
            print("The integer is composite")
    
    @staticmethod
    def is_palindrome(args : str):
        t = args[::-1]
        if args == t:
            print("The string is palindrome")
        else:
            print("The string is not a palindrome")
    
    @staticmethod
    def gcd(a : int, b : int):
        if a > b:
            while True:
                r = a % b
                if r == 0:
                    break
                else:
                    a = b
                    b = r
            print("GCD of the numbers is %i" %b)
        elif b > a:
            while True:
                r = b % a
                if r == 0:
                    break
                else:
                    b = a
                    a = r
            print("GCD of the numbers is %i" %a)
        else:
            print("GCD of the numbers is %i" %a)
    
    def string_operations(args : str):
        salpha = 0
        calpha = 0
        digits = 0
        ws = 0
        for c in args:
            if c >= "a" and c <= "z":
                salpha += 1
            if c >= "A" and c <= "Z":
                calpha += 1
            if c == " ":
                ws += 1
            if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                digits += 1
        print(f"The string '{args}' has {salpha} small alphabets, {calpha} capital alphabets, {ws} spaces, {digits} digits & its length is {len(args)} characters")
        print("%s" % args.title())

