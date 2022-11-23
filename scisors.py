import random
input = Element("user_obj")
op1 = Element("scisors_op")

kard = ['Rock', 'Paper', 'Scisors']

def play(*args, **kwargs):
    i = random.randint(0,2)
    if input.value in kard:
        if kard[i] == input.value:
            op1.write(f'you lose, computer get:  {kard[i]}')
        else:
            op1.write(f'you win, computer get:  {kard[i]}')
    else:
        op1.write(f'Input right object: Rock / Scisors / Paper')