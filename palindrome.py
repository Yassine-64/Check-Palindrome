chaine = input("entrer un mot:")
chaine_l= list(chaine)
chaine_l.reverse()
reversed_chaine = ''.join(chaine_l)
if chaine == reversed_chaine:
    print("la chaine est un palindrome")
else:
    print("la chaine n est pas un palindrome ")
