word=input("")
word_list=list(word.upper())

for i in word_list:
    if word_list.count(i)>1:
        rep_let=i
        rep_ind=word_list.index(i)
        popped_list=[i for i in word_list]
        popped_list.pop(rep_ind)
        dup=popped_list.index(i)+1
    else:
        rep_let="?"
display=["_" for i in word_list]
life=5
while True:
  print(display)
  letter=input("""your guess:
""")
  letter=letter.upper()
  if letter in word_list:
    x=word_list.index(letter)
    display[x]=letter
    if letter == rep_let:
        display[dup]=letter
    if display == word_list:
      print(display)
      print("you win")
      break
    else:
      pass
  else:
    life-=1
    print("remaining life",life)
    if life == 0:
      print("you lose")