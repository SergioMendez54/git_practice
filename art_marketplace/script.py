class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return '{}. \"{}\". {}, {}. {}, {}'.format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
    
  def show_listings(self):
    for i in self.listings:
      print(i)
    
class Client:
  def __init__(self, name, location="Private Collection", is_museum=False):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    
  def __repr__(self):
    return '{} is in {} and is {}'.format(self.name, self.location, self.is_museum)
  
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_list = Listing(artwork, price, self)
      veneer.add_listing(new_list)
      
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
          
          
class Listing():
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return 'Work of art is called "{}"\nThe price for the piece is {}.'.format(self.art.title, self.price)
    
    
veneer = Marketplace()    

edytta = Client("Edytta Halpirt")
print(edytta)

moma = Client("The MOMA","New York",True)
print(moma)

girl_with_mandolin = Art("Picasso, Pablo","Girl with a Mandolin (Fanny Tellier)","oil on canvas",1910, edytta)

print(girl_with_mandolin)
edytta.sell_artwork(girl_with_mandolin, 6000000)
veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
print(veneer.show_listings())
  
  
  
  
  