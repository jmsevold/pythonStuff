
#This function, book_cost, will take the variable 'quantity' and then run:
#After defining discount_factor as .6, set discounted price equal to
#24.95 * discount_factor
#total price is equal to discounted_price * quantity, 
#which is whatever you 
#return total_price to be held by the variable that will be set later
#For example, you could say Shit = book_cost( 15)
def book_cost(quantity):
    discount_factor = 0.6
    discounted_price = 24.95 * discount_factor
    total_price = discounted_price * quantity
    return total_price
#similar to above. Defining variables, then including in operations within
#other variables
def shipping_cost(quantity):
    shipping_first = 3
    shipping_rest = 0.75    
    total_shipping = shipping_first + ((quantity-1) * shipping_rest)
    return total_shipping

#this asks for an integer from the user with a question, and assigns it to num_books
#total_cost is holding the value of the function book_cost, with num_books passed into
# it to take the place of 'quantity'  , then adding to the shipping_cost function with
#num_books also passed into the parameters 
#we then print the two values of the previously calculated variables
num_books = int(raw_input('How many books do you want? '))
total_cost = book_cost(num_books) + shipping_cost(num_books)
print "Shipping", num_books, "books costs", total_cost