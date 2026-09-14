# Take the number of pages in a book and pages read per day as input, and calculate how many days it will take to finish the book
No_of_page = int(input("Enter No of page:"))
page_read_pr_day = float(input("Enter No of page read:"))
days_require = No_of_page / page_read_pr_day
print("Total day require to finish book is", days_require)