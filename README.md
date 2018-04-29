README
******

Aim of the class
================

To provide a tool to construct any system in a robust and flexible way.
This class only provides low level constructor.
The idea is that upper level classes can use it for more specific problems.

A mdsystem is composed by as many beads as required.
In an atomistic simulation that could be an atom.
However, in coarse-grained (CG) models it could reflect any CG grouping scheme.
The builder allows changing the resolution of the beads (TODO).



This class that anybody can choose how to partion the system

Class containing all information of the system.

Beads properties::

  beads_xyz = np.array() # Table containing the information of each beads_xyz
  beads_tags =  #This should be the workforce of the system.
                #It should allow jerarkic selections
  beads_features =

  tag {ids:[], dihedrals}

Access beads properties::

  mdsystem.xyz
  mdsystem.nbeads #properies
  mdsystem.beads # Special tag involving every bead??

Iterate over the beads ::

  for bead in mdsystem.beads:
    bead.xyz
    bead.tags # tags  and xyz MUST be on sync at all time

Iterate over molecules::

  for element1 in mdsystem.tag1:  # single bead class - XYZ class
    element1.id   # numpy array ids of all beads
    mol.xyz  # Method as a property to obtain numpy array coordinates of all beads
    mol.tags #  Method as a property to obtain list of lists with the tags for each atoms.
    for bead in mol: # could be mol.iter if needed
      bead.xyz
      bead.tags

Iterate over features::

  for bond in mdsystem.bonds: # bead pairs class
    bond.order # the number of beads involved
    bond.id # numpy array of tuples (a,b)
    bond.parameters #Type and parameters could be merged

tags
----
"tags" can be assigned to the atoms and then recalculated when used. This will
slower to access but then the system will be in sync all the time. Is this a
problem for us the lack of performance? If so we could control when they
get updated

tags types:

selection (eg. mol, fragment, chain, residue, group, etc..[the user can choose])
Some of them like chain and residue could be populated when reading certain files
like pdb.


features
--------
this tags contain relations between some beads. The nature of the
relation can be adjusted by the user. Examples:

1. charge, mass
2. bond
3. angles
4. d
