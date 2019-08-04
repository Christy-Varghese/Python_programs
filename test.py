
rows = int(input("Enter the total number of rows  : \t "))

for i in range(1,rows+1):
     for j in range(1,i+1,):
             if(j%2 == 0):
                print("0")
            else:
                print("1")
        print()
    
  
