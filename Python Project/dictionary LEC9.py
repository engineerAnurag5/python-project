programming_dic={
    "Bug":"An error in a pprogram that prevent the program from running as expected.",
    "Function":"A piece of code that you easily cal over  and over again",
     
    }
# Retreiving items from dictionary
print(f" Bug: {programming_dic["Bug"]}")
# Adding new items to dictionary
programming_dic["Loop"]="The action of doing something over and over again."
print(programming_dic)
empty_dic={}
# Edit an item in dic

programming_dic['Bug']="A moth in your computer"
print(programming_dic)
# Loop through dic
for key in programming_dic:
    print(key)
    print(programming_dic[key])
# ***********NESTING****************

capitals={
    "france":'Paris',
    'Germany':'berlin',
}
# Nesting a list iin a dictionary
travel_log={
    "France":["paris","lille",'Dijon'],
    "Germany":{'cities_visited':["Berlin",'Hamburg','Stuttgart'],"total_visits":8}

}
print(travel_log[ "Germany"])
# Nesting Dictionary in a list

travel_log=[
     {"country":'france',
     "cities_visited":["Paris","Lille","dijin"], 
     "total_visits":12},
    {"country":"Germany",
     "cities_visited":["Berlin",'Hamburg','Stuttgart'],
     "total_visits":8}
]

# print(travel_log)
# ******ADDINg new list into travel_log******
add_new_country =[
    {'country':'Russia',
                  'cities_visits':['Moscow','Saint Peteraburg'],
                  'visits':2,
                  }]
travel_log=travel_log+add_new_country
print(travel_log)
# ANOTHER Way
def add_new_country(country,times_visited,cities_visited):
    new_country={}
    new_country['country']=country
    new_country['visits']=times_visited
    new_country['cities']=cities_visited
    travel_log.append(new_country)
add_new_country('Russia',2,['Moscow','Saint Petersburg'])
print(travel_log)



