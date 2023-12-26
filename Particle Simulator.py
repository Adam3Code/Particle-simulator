# numpy as np 
import numpy as np

## Author Adam Rustom 

## Class Particle

#Part 1:
class particle:
    def __init__(self, x, y, charge):
        self.posv = np.array([x, y])
        self.charge = charge  # positive | - negative
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
    def __init__(self, list_particle,x_min,x_max,y_min,y_max):
        self.particles = list_particle  # List of all the particles
        self.K = 8.9875e9
        self.dimensions = 2
        self.boundary_exists = False
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def change_boundary(self,x_min,x_max,y_min,y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def particle_is_within_boundary(self,particle_index):
        x, y = self.particles[particle_index].get_pos()
        if self.x_min<=x<=self.x_max and self.y_min<=y<=self.y_max:
            return True
        else:
            return False

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

    def calculate_eletric_field(self,particle,target_position):
        r = target_position - particle.get_pos()
        r_mag = np.linalg.norm(r)
        if r_mag>0:
            return (self.K * particle.get_charge())/(r_mag **2)*(r/r_mag)
        else:
            return np.zeros(self.dimensions, dtype='float64')

    #Part four: computation
    def get_electric_field_pos(self,x,y):
        total_force = np.zeros(self.dimensions, dtype='float64')
        for particle in self.particles: # Runs a forloop, that adds particle forces and their impact at that position.
            total_force +=self.calculate_eletric_field(particle,np.array([x,y]))
        return total_force
    
    def get_colomb_force_particle(self,target_particle):
        total_eletricfield = np.zeros(self.dimensions, dtype='float64') #Intializing a vector 'total_force'
        for particle in self.particles:   #Runs a for loop, that adds all the forces acting on particle using colombs law
            if particle!=target_particle:
                total_eletricfield += self.calculate_eletric_field(particle,target_particle.get_pos())
        return target_particle.get_charge()*total_eletricfield


if __name__ == "__main__":
    #Test cases
    particle1 = particle(1.0, 1.0, 1)
    particle2 = particle(2.0, 2.0, -1)
    particle3 = particle(3.0, 3.0, 2)

    # An instance 'sim' is created
    sim = simulator([particle1, particle2],1,8,1,8)

    # Test changing charge and position
    sim.set_charge(1, 2)
    sim.set_pos(1, 4.0, 4.0)

    print("New Charge of Particle 1:", particle1.get_charge())
    print("New Position of Particle 2:", particle2.get_pos())

    # Test electric field and Coulomb force
    electric_field_pos = sim.get_electric_field_pos(-1.0,1.0)
    coulomb_force_particle3 = sim.get_colomb_force_particle(particle3)

    print("Electric Field at Position (-1.0, -1.0):", electric_field_pos)
    print("Coulomb Force on Particle 3:", coulomb_force_particle3)

    #######################Zans Test###############################
    
    particle_a = particle(0.0, 0.0, -1)
    particle_b = particle(1.0, 1.0, -1)
    particle_c = particle(2.0, 2.0, 1)

    new_sim = simulator([particle_a, particle_b, particle_c],1,8,1,8)

    print(f'This should be zero {new_sim.get_colomb_force_particle(particle_b)}')
    