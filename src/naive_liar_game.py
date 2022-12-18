

class LG():
    # the boolean value that keeps the game going
    keepGoing = True

    # reset after a game is played
    def reset():
        keepGoing = True

    # nv: naive
    # LG: Liar Game
    # Lcond: Lucy's win condition
    def nv_LG_Lcond(n: int, q: int) -> bool:
        # print(f"The value of n is: {n}")
        # print(f"The value of 2^q is: {pow(2,q)}")
        return n <= pow(2,q)

    # sem: stands for start, end, mid reassignment function
    def sem(start, end):
        return start, end, int((start+end)/2)

    # 
    def logic(start, end, mid, isTrue):
        """
            The binary search function that helps decide the logic after Lucy queries and Jasmine gives the answers

            **Args**:
                `start`: the starting point
                `end`: the end point
                `mid`: the mid point
            
            Computes the answer based on if Jasmine answers true or false
            
            If True: then we take the set from the start to the middle to be the remaining set
            If False: then we take the set from the middle+1 to the end to be the remaining set

            One special point to be made is when Jasmine answers True and Lucy only queries a set with length 1, the answer must be that set, 
            thus we return the function right away
        """
        if(isTrue == True):
            if(start==mid):
                LG.keepGoing = False
                return start, end, mid
            return LG.sem(start, mid)
        if(isTrue == False):
            return LG.sem(mid+1,end)

    # nv: naive
    # LG: Liar Game
    # Lstrat: Lucy's winning strategy
    def nv_LG_Lstrat(n: int, q: int, x: int=-1):
        """
        An AI function that plays the **naive Liar Game** when it has the winning strategy
        
        **Args**:
            `n`: the set of numbers from 1 to `n`
            `q`: the number of query Lucy can have
            `x`: the predetermined answer by Jasmine
        
        **Return**:
            Returns none
            resets the class's variable keepGoing to True again for the next iteration of the function
        """


        if(LG.nv_LG_Lcond(n,q) == False):
            print("Lucy is unable to deduce a winning strategy")
            LG.reset()
            return False
            
        start, end, mid = LG.sem(1,n)
        while LG.keepGoing:
            if(x < 0):
                isTrue = input(f"Is x in the set from {start} to {mid} (y/n)").lower().strip() == 'y'
            else:
                print(f"Is x in the set from {start} to {mid} (y/n)")
                isTrue = (x >= start and x <= mid)
                print(f"Jasmine answers {isTrue}")
            start, end, mid = LG.logic(start, end, mid, isTrue)
            n = n / 2
            LG.keepGoing = LG.keepGoing and n > 1
        print(f"Answer is {mid}")
        LG.reset()
        return True
