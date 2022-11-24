import random
input = Element("user_obj")
op1 = Element("scisors_op")
op2 = Element("scisors_low")
i_my_score = 0
i_pc_score = 0

op_my_score = Element("my_score")
op_pc_score = Element("pc_score")

kard = ['Rock', 'Paper', 'Scisors']

def play(*args, **kwargs):
    i = random.randint(0,2)
    if input.value in kard:
        if kard[i] == input.value:
            i_pc_score = i_pc_score + 1
            op1.write(f'Computer choce:  {kard[i]}')
            op2.write('You\'r lose the ')
        else:
            i_my_score = i_my_score + 1
            op1.write(f'Computer choce:  {kard[i]}')
            op2.write('You\'r win the ')
    else:
        op1.write(f'Input right object: Rock / Scisors / Paper')

op_my_score.write(i_my_score)
op_pc_score.write(i_pc_score)