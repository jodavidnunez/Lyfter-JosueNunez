"""4. Cree las siguientes clases:
    a. `Head`
    b. `Torso`
    c. `Arm`
    d. `Hand`
    e. `Leg`
    f. `Feet`
    Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos."""

class Torso:
	def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
		self.head = head
		self.left_arm = left_arm
		self.left_leg = left_leg
		self.right_leg = right_leg
		self.right_arm = right_arm


class Head:
	def __init__(self):
		pass
	

class Arm:
	def __init__(self, hand):
		self.hand = hand


class Leg:
	def __init__(self, feet):
		self.feet = feet


class Hand:
	def __init__(self):
		pass


class Feet:
	def __init__(self):
		pass


class Human():
    def __init__(self, torso, left_hand, left_feet, right_feet, right_hand):
        self.torso = torso
        self.head = torso.head
        self.left_arm = torso.left_arm
        self.left_hand = left_hand
        self.left_leg = torso.left_leg
        self.left_feet = left_feet
        self.right_leg = torso.right_leg
        self.right_feet = right_feet
        self.right_arm = torso.right_arm
        self.right_hand = right_hand      


head = Head()        
left_hand = Hand()
left_feet = ()
left_arm = Arm(left_hand)
left_leg = Leg(left_feet)
right_hand = Hand()
right_feet = Feet()
right_arm = Arm(right_hand)
right_leg = Leg(right_feet)
torso = Torso(head, right_arm, left_arm, right_leg, left_leg) 
human = Human(torso, left_hand, left_feet, right_feet, right_hand)