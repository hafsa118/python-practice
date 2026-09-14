# Take the price of an item and a discount percentage as input and print the final price
Math_marks = int(input("Enter math:"))
bio_marks = int(input("Enter bio:"))
Eng_marks = int(input("Enter eng:"))
Total = int(input("Enter total:"))

sum=Math_marks+bio_marks+Eng_marks
Average=sum/3
print("average",Average)

Percentage=(sum/Total)*100
print("percentage",Percentage)