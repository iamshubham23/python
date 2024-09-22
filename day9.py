# programming_dictionary={
#     "Bug":"an errror in a program tha t prevents the program from running as expected.",
#     "Function":"A piece of code that you can easily call over and over again.",
# }
#retriving item from dictionary
#print(programming_dictionary["Function"])
#Adding new items to dictionary.
#programming_dictionary["loop"]="the action of doing something over and over again"
# print(programming_dictionary["loop"])

#wipe an existing dictionary
# programming_dictionary= {}
# print(programming_dictionary)
#edit an item in a dictionary
#programming_dictionary["Bug"]="A moth in your computer"
# print(programming_dictionary["Bug"])

#loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#grading problem
# student_scores={
#     "Harry":81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62,
# }
# student_grades={}
# for student in student_scores:
#     score=student_scores[student]
#     if score>90:
#         student_grades[student]="outstanding"
#     elif score >80:
#         student_grades[student]="Exceeds Expectation"
#     elif score>70:
#         student_grades[student]="Acceptable"
#     else:
#         student_grades[student]="fail" 
# print(student_grades)                   

#Nesting
capitals={
    "france":"paris",
    "germany":"berlin",
}
#Nesting a dictionary in a dictionary
# travel_log = {
#     "france":{"cities visited":["paris","Lille","Dijon"],"total_visited":21},
#     "germany":{"popular city":["berlin","hamburg","herosima"],"friends":15},
# }
#Nesting Dictionary in a List
# travel_log = [
#    {"country":"france",
#     "cities visited":["paris","Lille","Dijon"],
#     "total_visited":21},
#     {"country":"germany",
#      "popular city":["berlin","hamburg","herosima"],
#      "friends":15},
# ]
# travel_log=[
#     {
#         "country":"france",
#         "visits":12,
#         "cities":["paris","lille","dijon"]
#     },
#     {
#         "country":"germany",
#         "visits":5,
#         "cities":["berlin","hamburg","stuttgart"]
#     },
# ]
# def add_new_country(country_visited,times_visited,cities_visited):
#     new_country={}
#     new_country["country"]=country_visited
#     new_country["visits"]=times_visited
#     new_country["cities"]=cities_visited
#     travel_log.append(new_country)
# add_new_country("russia",2,["moscow","saint_petersburg"])    
# print(travel_log)
print("welcome to the bid")
bids={}
anyone_else=True
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    #bidding_record={"shubham":100,"Abhishek:200"}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
        print(f"the winner is {winner} with a bid of {highest_bid}")    

while anyone_else:
  name=input("give the name of bidder:")
  price=int(input("give the amount of bidding:"))
  bids[name]=price
  should_continue=input("Are there any others  bidders?type yes or no:\n")
  if should_continue=="no":
    anyone_else=False
    find_highest_bidder(bids)
    