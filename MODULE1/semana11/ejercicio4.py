class Head:
    def __init__(self, eyes, mouth, ears, hair):
        self.eyes = eyes
        self.mouth = mouth
        self.ears = ears
        self.hair = hair


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Hand:
    def __init__(self, fingers):
        self.fingers = fingers


class Leg:
    def __init__(self, feet):
        self.feet = feet


class Feet:
    def __init__(self, toes):
        self.toes = toes


class Human:
    def __init__(self, torso):
        self.torso = torso


my_head = Head(eyes= 'brown', mouth='small', ears='big', hair='brown')
right_hand = Hand(fingers= 5)
right_arm = Arm(right_hand)
left_hand = Hand(fingers= 5)
left_arm = Arm(left_hand)
right_feet = Feet(toes= 5)
right_leg = Leg(right_feet)
left_feet = Feet(toes= 5)
left_leg = Leg(left_feet)
torso = Torso(my_head, right_arm, left_arm, right_leg, left_leg)
my_human = Human(torso)

print(my_human)