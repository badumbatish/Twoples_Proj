import math
class CL:
    def B(q: int, j: int) -> float:
        """
            The function that computes B(q,j) based on the paper
        """
        sum = 0.0
        for i in range(0,j+1):
            sum += math.comb(q,i)
        return float(1.0*sum*pow(2,-q))

    def get_input(q: int, inputList: None):
        if (q<0):
            # Prompt user to enter a list of integer of length k
            inputList = [int(item) for item in input("Enter a list of integers: ").split()]

            # Prompt user to enter a integer value q
            q = int(input("Enter a value for q: "))
        return q, inputList


    # mult: stands for (x0, x1,..., xk) game
    # CL : Chip-Liar
    # Jcond: Jasmine win condition
    def mult_CL_Jcond(q = -1, inputList = None):
        """
        Computes the weight of the chip liar game

        mult: stands for (x0, x1,..., xk) game

        CL : Chip-Liar

        Jcond: Jasmine win condition
        """
        # If the user hasn't specified any input value
        if(q < 0):
            q, inputList = CL.get_input(q, inputList)
        sum = 0
        for i, val in enumerate(inputList):
            sum = sum + val*CL.B(q,i)
        
        return sum

    
    def get_new_list(isTrue, queryList, inputList):
        """
        Get the new, remaining set based on Jasmine's answer of Yes or No for Lucy's query

        **Args**

        `isTrue`: stands for Jasmine's answer: True for Yes, False for No

        `queryList`: stands for the Lucy's query set S

        `ls`: stands for the complement set S' 

        ** Mechanics **

        Suppose Jasmine answers Yes, then we have to move S' to the left. What this really means is if S' has $y_i$ chips at position $i$ and the remaining set
        has $x_i$ chips at position $i$, we have to subtract $y_i$ from $x_i$ and add $y_i$ to $x_{i-1}$ after the subtraction

        Let ls = remaining_set - queryList (element wise subtraction)
        
        The act of subtracting $y_i$ from $x_i$ is subtracting ls from the remaining set

        Thus, remaining_set - ls = remaining_set - (ls - queryList) = queryList

        Then the act of adding $y_i$ to $x_{i-1]$ can be seen as adding the left-shifted S' to the subtraction result

        Thus, remaing_set - ls + left_shifted_S' = S + left_shifted_S'
    
        
        Suppose Jasmine answer No, then we have to move S to the left. Moving S to the left is the same thing as subtracting S from the original list, then 
        add the left-shifted S to the subtraction result

        Then remaing_set - S + left_shift_S = S' + left_shift_S
        """
        # queryList stands for the set S
        # ls stands for the set S'
        ls = [inputList[i] - queryList[i] for i in range(len(inputList))]
        if(isTrue):
            # Answering Yes, we shift the set S' to the left, and add it to the set S
            ls = ls[1:] + [0]
            return [queryList[i] + ls[i] for i in range(len(inputList))]
        else:
            # Answering No: we shift the set S to the left, and add it to the set S'
            queryList = queryList[1:] + [0]
            return [ls[i] + queryList[i] for i in range(len(inputList))]




    def mult_CL_Jstrat(q = -1, inputList = None):
        q, inputList = CL.get_input(q, inputList)


        tempList = list(inputList)
        tempQ = q
        print("Current list: ")
        print(tempList)
        while(tempQ > 0):
            query = [int(item) for item in input(f"Enter a list of integers of length {len(tempList)} to query as Lucy: ").split()]
            print("Lucy queries: ")
            print(query)
            yesList = CL.get_new_list(True, query, tempList)
            yesWeight = CL.mult_CL_Jcond(tempQ,yesList)

            noList = CL.get_new_list(False, query, tempList)
            noWeight = CL.mult_CL_Jcond(tempQ, noList)

            if(yesWeight >= noWeight):
                print("Jasmine answers Yes!")
                tempList = yesList
            else:
                print("Jasmine answers No!")
                tempList = noList
            print("Updated list")
            print(tempList)
            tempQ = tempQ - 1
        pass