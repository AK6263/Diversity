## Simple R commands/functions for analyses of Bird and Tree Data
#  Note: The symbol # comments out that line. Only the lines that do not have the # symbol are executed 
# Windows Users may install/use "Notepad++" to view this file. Change Language Preference to "R" in 
# Notepad++ to view the components in different color codes 

## Save your Bird data in a file called "Birds.txt"
# Next, read this data into R

Birds <- read.table(file="Birds.txt", header=T, as.is=T)
colnames(Birds) <- c("ID","Name")


# The tree data that I have sent you is already an ".RData" file, which is the format in which R Data
# objects are stored. This can be loaded easily into the R environment as follows: 

load("Trees.RData")

# Now you should have two objects in your R environment - Birds and Trees. You can check this as follows:

ls()
 
# This will list all the objects you have loaded or created. All things in R will appear as objects 
# in your environment. This includes Data objects, functions created by you, function outputs that you saved.  

# The file "SppInd.birds.R" has the function 'SppInd.birds' to compute and plot a 
# species-individual curve using your bird data

# Just run the following command for birds. This will save the output plot as "SppInd.birds.jpg"
# This will also save the results as a data table to your folder ("SppInd.birds.txt") 
# with column 1 giving the numbers of indivduals sampled and columns 2-11 giving the the numbers of 
# species found in each of the 10 repetitions for a given sample size.   

source("SppInd.birds.R")  # This will load the function to your R environment
SppInd.birds(Birds)


# The file "SppInd.trees.R" has the function 'SppInd.trees' to compute and plot a 
# species-individual curve using the tree  data

# Just run the following command for trees. This will save the output plot as "SppInd.trees.jpg"
# This will also save the results as a data table to your folder ("SppInd.trees.txt") 
# with column 1 giving the numbers of indivduals sampled and columns 2-11 giving the the numbers of 
# species found in each of the 10 repetitions for a given sample size. 

source("SppInd.trees.R")  # This will load the function to your R environment
SppInd.trees(Trees)



