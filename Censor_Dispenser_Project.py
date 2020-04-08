#work in progress
# https://www.codecademy.com/practice/projects/censor-dispenser

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

print(email_three)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor1(email,phrase):
  new_email = []
  new_email = email.replace(phrase,'(censored)')
  return new_email
  
def censor2(email,phrases):
  new_email = email
  for i in phrases:
    new_email = new_email.replace(' {} '.format(i),' (censored) ')
  return new_email
  
def censor3(email,phrases,neg_words):
  new_email = email
  #count = 0
  for i in phrases:
    new_email = new_email.replace(' {} '.format(i),' (censored) ')
  for j in neg_words:
    new_email = new_email.replace(' {} '.format(j),' (censored) ')    
  return new_email
  
  
 
 
#print(censor1(email_one,'learning algorithms'))
#print(censor2(email_two,proprietary_terms))  
print(censor3(email_three,proprietary_terms,negative_words))

for j in negative_words:
  print(email_three.find(j))


