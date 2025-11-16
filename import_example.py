import srp_summerize # imports the whole block , access the methods
# from srp_summerize import display_result, parse_input, summerize_data # importing by mentioning function 
uncleaned_string = "10,20.30,40,34,23,234,567,98"
#parse_input(uncleaned_string)

cleaned_string = srp_summerize.parse_input(uncleaned_string)
print(cleaned_string)
summerized_results = srp_summerize.summerize_data(cleaned_string)
print(summerized_results)
display_result = srp_summerize.display_result(summerized_results)
print(display_result)

#write out the function
