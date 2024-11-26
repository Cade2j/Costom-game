import random as rn
import base64

playing = True
nrtf = (True, False)
print('RNG game')

# Base64 encode/decode functions
def b64(txt):
    return base64.b64encode(txt.encode()).decode()

def unb64(txt):
    return base64.b64decode(txt).decode()

# Input score, default to 0 if invalid input is provided
score_input = input('Put your code in (Leave blank if you don\'t have one): ')

# If input is empty or invalid, set score to 0
try:
    score = int(unb64(score_input)) if score_input.strip() else 0
except (ValueError, base64.binascii.Error):
    score = 0

while playing:
    tf = rn.choice(nrtf)
    if tf:
        score += 1
    else:
        score = 0
        con = input('Do you want to continue? (yes/y to continue): ').lower()
        if con not in ("yes", "y"):
            playing = False
            print(f"Final Score: {score}")
            # Encode the score as base64
            encoded_score = b64(str(score))
            print(f"The code is: {encoded_score}")
            
    print(f"Score: {score}")
print('GitHub: Cade2j')
