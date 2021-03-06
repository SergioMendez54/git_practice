destinations = ['Paris, France','Shanghai, China','Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes','Shanghai, China',['historical site','art']]

attractions = [[] for i in destinations]
print(attractions)

def get_destination_index(destination):
  destination_index = 0
  for i in range(len(destinations)):
    if destinations[i] == destination:
      destination_index = i
      print(destination)
  return destination_index    

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination,attraction):
  try: 
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except ValueError: 
    print("An error occurred")
    return

def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for b in interests:
      if b in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])   
  return attractions_with_interest
  
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  
  interests_string = 'Hi ' + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": " + str(traveler_attractions)
  return interests_string
  

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

print(get_destination_index("Paris, France"))

test = ['Venice Beach',['beach']]
print(add_attraction('Los Angeles, USA', test))


add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)

la_arts = find_attractions('Los Angeles, USA',['art'])
print(la_arts)

test = ['Dereck Smill', 'Paris, France', ['monument']]
print(get_attractions_for_traveler(test))








class Solution(object):
    def defangIPaddr(self, address):
        
        faddress = ('')
        for i in address:
            if i == '.':
                faddress = faddress + str('[.]')
            else:
                faddress = faddress + str(i)
            
            
            
        #:type address: str
        #:rtype: str
        
        return faddress