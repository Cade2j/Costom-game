import random as rn

playing = True
nrtf = (True, False)
print('RNG game')

# Input score, default to 0 if invalid input is provided
score_input = input('Put your code in (Leave blank if you don\'t have one): ')

# If input is empty or invalid, set score to 0
if score_input.strip() == "" or not score_input.isdigit():
    score = 0
else:
    score = int(score_input)

while playing:
    tf = rn.choice(nrtf)
    if tf:
        score += 1
    else:
        score = 0
        con = input('Do you want to continue: ').lower()
        if con not in ("yes", "y"):
            playing = False
            print(f"Final Score: {score}")
            # Convert the score to a string, then encode to bytes
            encoded_score = str(score).encode()
            print(f"The code is: {encoded_score}")
            
    print(f"Score: {score}")
print('GitHub: Cade2j')
