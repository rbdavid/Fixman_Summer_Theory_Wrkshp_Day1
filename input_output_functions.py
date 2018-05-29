
import numpy as np

# read xyz file
def read_xyz(xyzFile):
	# open the file
	f = open(xyzFile,'r')
	# initialize counters
	lineCount = 0
	atomCount = 0
	atomNames = []
	# read each line of the file
	for line in f:
		# number of atoms is printed on first line of XYZ file format
		if lineCount==0:
			nAtoms = int(line)
			positions = np.empty((nAtoms,3),dtype=float)
		# positions are after second line
		elif lineCount > 1:
			atomNames.append(line.split()[0])
			for k in range(3):
				positions[atomCount,k] = float(line.split()[k+1])
			atomCount += 1

		lineCount += 1
	f.close()
	# send the number of atoms and positions back. positions are numpy array
	return atomCount,atomNames, positions

# write xyz file
def write_xyz(positions,atomNames,xyzFile):
	# determine number of atoms as size of first dimension of position array
	nAtoms = positions.shape[0]
	# open file for writing
	out = open(xyzFile,"w")
	# write number of atoms in first line of XYZ
	out.write("%10d\n" % (nAtoms))
	out.write("Translated Molecule\n")
	# loop through atoms and print atom positions and names
	for atom in range(nAtoms):
		out.write("%5s %10.5f %10.5f %10.5f\n" % (atomNames[atom], positions[atom,0], positions[atom,1], positions[atom,2]))
	out.close()

