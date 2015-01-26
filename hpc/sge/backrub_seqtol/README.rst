==============================
Sun Grid Engine job submission
==============================

The backrub_seqtol.py script functions as both a submission script for a workstation and for a SGE cluster engine.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GB1 Fold Stability Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  cd protocols/backrub_seqtol
  qsub -v PDB_PATH=../../input/pdbs/2QMT/2QMT.pdb -t 1-20 -N bs_2QMT backrub_seqtol.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PDZ Domain Interface Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  cd protocols/backrub_seqtol
  qsub -v PDB_PATH=../../input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb -t 1-200 -N bs_2I0L_A_C_V2006 backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/2IWP_B_A_V1927/2IWP_B_A_V1927.pdb -t 1-200 -N bs_2IWP_B_A_V1927 backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/2FNE_A_C_V2048/2FNE_A_C_V2048.pdb -t 1-200 -N bs_2FNE_A_C_V2048 backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/1N7T/1N7T_%02i.pdb -v INPUT_PATH=../../input/pdbs/1N7T/1N7T -t 1-200 -N bs_1N7T backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/1N7T/1N7T_%02i.pdb -v INPUT_PATH=../../input/pdbs/1N7T_V83K/1N7T_V83K -t 1-200 -N bs_1N7T_V83K backrub_seqtol.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hGH/hGHR Interface Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  cd protocols/backrub_seqtol
  qsub -v PDB_PATH=../../input/pdbs/1A22_1/1A22_1.pdb -t 1-100 -N bs_1A22_1 backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/1A22_2/1A22_2.pdb -t 1-100 -N bs_1A22_2 backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/1A22_3/1A22_3.pdb -t 1-100 -N bs_1A22_3 backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/1A22_4/1A22_4.pdb -t 1-100 -N bs_1A22_4 backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/1A22_5/1A22_5.pdb -t 1-100 -N bs_1A22_5 backrub_seqtol.py
  qsub -v PDB_PATH=../../input/pdbs/1A22_6/1A22_6.pdb -t 1-100 -N bs_1A22_6 backrub_seqtol.py