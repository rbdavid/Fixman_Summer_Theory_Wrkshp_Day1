
import numpy as np

# rotate a set of three dimensional coordinates around the x axis by theta
def rot_x(positions,theta):
	# determine number of atoms as size of first dimension of position array
	nAtoms = positions.shape[0]

	# populate rotation matrix
	rot = np.zeros((3,3),dtype=float)
	rot[0,0] = 1.0
	rot[1,1] = np.cos(theta)
	rot[1,2] = -np.sin(theta)
	rot[2,1] = np.sin(theta)
	rot[2,2] = np.cos(theta)

	# perform rotation
	positions = np.dot(positions,rot)

	# return rotated positions
	return positions

# rotate a set of three dimensional coordinates around the y axis by theta
def rot_y(positions,theta):
	# determine number of atoms as size of first dimension of position array
	nAtoms = positions.shape[0]

	# populate rotation matrix
	rot = np.zeros((3,3),dtype=float)
	rot[1,1] = 1.0
	rot[0,0] = np.cos(theta)
	rot[0,2] = np.sin(theta)
	rot[2,0] = -np.sin(theta)
	rot[2,2] = np.cos(theta)

	# perform rotation
	positions = np.dot(positions,rot)

	# return rotated positions
	return positions

# rotate a set of three dimensional coordinates around the z axis by theta
def rot_z(positions,theta):
	# determine number of atoms as size of first dimension of position array
	nAtoms = positions.shape[0]

	# populate rotation matrix
	rot = np.zeros((3,3),dtype=float)
	rot[2,2] = 1.0
	rot[0,0] = np.cos(theta)
	rot[0,1] = -np.sin(theta)
	rot[1,0] = np.sin(theta)
	rot[1,1] = np.cos(theta)

	# perform rotation
	positions = np.dot(positions,rot)

	# return rotated positions
	return positions

