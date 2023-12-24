OOP Training: Particle Simulator

Synopsis:
The objective of this project is to practice object oriented programming. We will be focusing on building a particle simulator. We will be using the theoretical computational methods we know from electro magnetism courses.

Key concepts:
-	Writing classes
-	Instantiating and using objects
-	Parsing objects as arguments to function
-	Writing functions for using objects
-	Separate data focused classes from behavior focused classes

Part one: Create a particle class
Create a class to represent a particle. Make sure to include class attributes necessary to run calculations specific to particles.
Hint: It is a good idea to write get and set functions for attributes that will be used by other actors.

Part two: Create a simulator class
Create a class to represent a simulator. This is where we will be implementing the different types of computations.

Part three: Simulator management
Implement the following functionalities:
1.	Add a particle to the simulator
2.	Remove a particle from the simulator
3.	Get the position of each particle in the simulator
4.	Get the total charge of the simulator
5.	Change the charge of a particle
6.	Change the position of a particle
7.	Get the distance between two particles
8.	Remove all particles from simulator

Part four: Computations
Implement the following computations:
1.	The electric field at a certain position produced by the particles in the simulator.
2.	The electro static Coulomb force one of the particles in the simulator feels by all the other particles.

Part five: Create simulator boundaries
Implement boundaries and relevant functionalities:
1. Create boundaries for the simulator.
2. Write functions for managing the boundaries
3. Implement checking/error handling of whether particles are placed inside or outside the boundaries.
4. Implement periodic boundary conditions (This is a bit heavy on the linear algebera, so feel free to ask questions)

CheatSheet
Writing a class:
class ThisIsAClass:
    def __init__(self):
        variable1 = 1
        variable2 = ‘hello’
    def function1(self, variable3):
        do some operations
        return result
Creating an object (also called create an instance of a class)
obj = ThisIsAClass()
Calling a function in a object 
obj.function1(variable)
