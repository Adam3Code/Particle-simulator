# numpy as np 
import numpy as np

## Author Adam Rustom 

## Class Particle

#Part 1:
class particle:
    def __init__(self, x, y, charge):
        self.posv = np.array([x, y])
        self.charge = charge  # positive | - negative
        self.dimensions = 2
    def get_pos(self):
        return self.posv
    
    def get_charge(self):
        return self.charge
    
    def set_charge(self,new_charge):
        self.charge = new_charge
    
    def set_pos(self, x,y):
        self.posv = np.array([x,y])


## Class simulator 
#Part 2
class simulator:
    def __init__(self, list_particle):
        self.particles = list_particle  # List of all the particles
        self.K = 8.9875e9
    
    ## Part Three
    def add_particle(self, particle):  # 1
        self.particles.append(particle)
    
    def remove_particle(self, particle):  # 2
        self.particles.remove(particle)
    
    def get_pos(self):  # 3 
        return np.array([particle.get_pos() for particle in self.particles]).T
    
    def total_charge(self):  # 4
        return sum([particle.get_charge() for particle in self.particles])
    
    def set_charge(self, particle_index, new_charge): #5
        self.particles[particle_index].set_charge(new_charge)

    def set_pos(self,particle_index,x,y): #6
        self.particles[particle_index].set_pos(x,y)

    def get_distance(self, particle_index_1, particle_index_2):  # 7:
        return np.linalg.norm(self.particles[particle_index_1].get_pos()-self.particles[particle_index_2].get_pos())
    
    def remove_all_particles(self): #8 
        self.particles = []

    def calculate_force(self,particle,target_position):
        r = target_position - particle.get_pos()
        r_mag = np.linalg.norm(r)
        if r_mag>0:
            return (self.K * particle.get_charge())/(r_mag **2)*(r/r_mag)
        else:
            return np.zeros(self.dimensions, dtype='float64')

    #Part four: computation
    def get_electric_field_pos(self,position):
        total_force = np.zeros(self.dimensions, dtype='float64')
        for particle in self.particles: # Runs a forloop, that adds particle forces and their impact at that position.
            total_force +=self.calculate_force(particle,position)
        return total_force
    
    def get_colomb_force_particle(self,target_particle):
        total_force = np.zeros(self.dimensions, dtype='float64') #Intializing a vector 'total_force'
        for particle in self.particles:   #Runs a for loop, that adds all the forces acting on particle using colombs law
            if particle!=target_particle:
                total_force += self.calculate_force(particle,target_particle.get_pos())
        return total_force


if __name__ == "__main__":
    #Test cases
    particle1 = particle(1.0, 1.0, 1)
    particle2 = particle(2.0, 2.0, -1)
    particle3 = particle(3.0, 3.0, 2)

    # An instance 'sim' is created
    sim = simulator([particle1, particle2])

    # Test changing charge and position
    sim.set_charge(1, 2)
    sim.set_pos(1, 4.0, 4.0)

    print("New Charge of Particle 1:", particle1.get_charge())
    print("New Position of Particle 2:", particle2.get_pos())

    # Test electric field and Coulomb force
    electric_field_pos = sim.get_electric_field_pos(np.array([-1.0, -1.0]))
    coulomb_force_particle3 = sim.get_colomb_force_particle(particle3)

    print("Electric Field at Position (-1.0, -1.0):", electric_field_pos)
    print("Coulomb Force on Particle 3:", coulomb_force_particle3)







