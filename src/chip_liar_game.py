import math
class CL:
    def B(q: int, j: int) -> float:
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

        # If the user hasn't specified any input value
        if(q < 0):
            q, inputList = CL.get_input(q, inputList)
        sum = 0
        for i, val in enumerate(inputList):
            sum = sum + val*CL.B(q,i)
        
        return sum

    
    def get_new_list(isTrue, queryList, inputList):
        # queryList stands for the set S
        # ls stands for the set S'
        ls = [inputList[i] - queryList[i] for i in range(len(inputList))]
        if(isTrue):
            queryList = queryList[1:] + [0]
            return [ls[i] + queryList[i] for i in range(len(inputList))]
        else:
            ls = ls[1:] + [0]
            return [queryList[i] + ls[i] for i in range(len(inputList))]




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