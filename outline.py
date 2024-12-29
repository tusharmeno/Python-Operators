Amount = int(input("Enter the amount"))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = (Amount%100)%50//10
print("Amount in notes of 100:", note_1)
print("Amount in notes of 50:", note_2)
print("Amount in notes of 10:", note_3)