print("welcome to the data analyzer and transformer program")
def function(n):
    if n==0 or n==1:
        return 1
    return n*function(n-1)
ARR=[]
def stat(data):
    maximum=max(ARR)
    minimum=min(ARR)
    total=sum(ARR)
    average=total/len(ARR)
    return maximum,minimum,total,average
while True:
    print("1. input data")
    print("2. display data summary(bult-in functons)")
    print("3. calculate factorial(recursion)")
    print("4. filter data by threshold(lambda function)")
    print("5. sort data")
    print("6. display dataset statistics")
    print("7. exit program")
    q=int(input("\nPlease enter your choice:"))
    if q== 1:
        ARR=list(map(int,input("\nenter the data for 1D array: ").split()))
        print("\nyour array is :",ARR)
    elif q== 2:
        if len(ARR)==0:
            print("enter the array by choosing 1 option")
        else:
            print("\nsum of all element is",sum(ARR))
            print("total number of element",len(ARR))
            print("Maximim number",max(ARR))
            print("Minimum number",min(ARR))
            avg=sum(ARR)/len(ARR)
            print("average of the array",avg,"\n")
    elif q == 3:
        num=int(input("\nplease enter the number of factorial: "))
        if num<0:
            print("enter the non negative number")
        else:
            print("factorail is: ",function(num))
    elif q == 4:
        if len(ARR)== 0:
            print("enter the data first by choosing first option")
        else:
            threshold=int(input("enter the threshold value to ffilter out data above this value"))
            result=list(filter(lambda x:x>threshold,ARR))
            print("original data :",ARR)
            print("new data :",result)
    elif q == 5:
        if len(ARR)== 0:
            print("please enter the data first")
        else:
            print("""choose sorting option
1. ascending 
2. decending""")        
            y=int(input("enter the choice"))
            if y == 1:
                print("sorted data in the ascending order: \n")
                ascending=sorted(ARR)
                print(ascending)
            elif y == 2:
                print("sorted data in the decending order: \n")
                descending=sorted(ARR,reverse=True)
                print(descending)
    elif q == 6:
        if len(ARR) == 0:
            print("Please enter the data first by choosing the 1")
        else:
            maximum,minimum,total,average=stat(ARR)
            print("\nDataset statistics: ")
            print("maximum value: ",maximum)
            print("minimum value: ",minimum)
            print("sum of all values: ",total)
            print("average value: ",average)
    elif q == 7:
        print("Thank you for using the data analyzer and Transfromer program,Goodbye!")
        break


    else:
        print("incorrect choice")
            