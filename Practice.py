#Write your function here
def remove_middle(lst,start,end):
  new_lst = lst[0:start] + lst[end+1:len(lst)]
  return new_lst
  
#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))