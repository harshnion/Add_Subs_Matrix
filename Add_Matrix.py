# So guys today we will learn about addition of 2 matrix 
# It is very easy and Here We will use some concept 

# Lets take 2 matrix 
X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[9,8,7],[6,5,4],[3,2,1]]

# Here we need 3rd matrix that will store our output 
# So we take it as zero matrix
Result = [[0,0,0],[0,0,0],[0,0,0]]

# Now we use loop in such a way that each element of both matrix willbe taken once 
for i in range (len(X)):
  for j in range (len(X[0])):
    Result[i][j] = X[i][j] + Y[i][j]

print(Result)
#And at last we print the 3rd matrix as our final output
