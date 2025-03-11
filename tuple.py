def find_pe_pb(price , eps , book_value ) :
 pe = price/eps
 pb = price/book_value
 return pe ,pb  #it know as a  tuple
pe_ratio , pb_ratio = find_pe_pb(100, 6 , 8 )
print(pe_ratio)