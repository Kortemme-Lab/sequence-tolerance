====================================
Input data
====================================

The input data for this benchmark is primarily structural. The following sets of structures are used:

---------------------------
From Smith & Kortemme, 2010
---------------------------

PDZ domains:

- 1N7T, solution NMR               : "ERBIN PDZ domain bound to a phage-derived peptide"
- 2FNE, X-ray diffraction: 1.83  Å : "The crystal structure of the 13th PDZ domain of MPDZ"
- 2I0L, X-ray diffraction: 2.31 Å  : "X-ray crystal structure of Sap97 PDZ2 bound to the C-terminal peptide of HPV18 E6"
- 2IWP, X-ray diffraction: 2.15 Å  : "12th PDZ domain of multiple PDZ domain protein MPDZ (CASP target)"

Smith, CA, Kortemme, T. Structure-Based Prediction of the Peptide Sequence Space Recognized by Natural and Synthetic PDZ Domains. 2010. J Mol Biol 402(2):460-74. `doi: 10.1016/j.jmb.2010.07.032 <http://dx.doi.org/10.1016/j.jmb.2010.07.032>`_.

---------------------------
From Smith & Kortemme, 2011
---------------------------

As well as using some of the PDZ domains above, this paper added the following structures:

- 1A22, X-ray diffraction, 2.6 Å : "Human growth hormone (hGH) bound to single receptor"
- 2QMT, X-ray diffraction: 1.05 Å: "Crystal Polymorphism of Protein GB1 Examined by Solid-state NMR and X-ray Diffraction"

Smith, CA, Kortemme, T. Predicting the Tolerated Sequences for Proteins and Protein Interfaces Using RosettaBackrub Flexible Backbone Design. 2011.
PLoS ONE 6(7):e20451. `doi: 10.1371/journal.pone.0020451 <http://dx.doi.org/10.1371/journal.pone.0020451>`_.


======================================
Protocol 1: Backrub/Sequence Tolerance
======================================

The backrub_seqtol directory contains the additional files needed to run the jobs using the Rosetta software suite. There
are three types of file:

- .resfile. These files specify which residue sidechains can move and mutate during the run. See the `Rosetta user guide <https://www.rosettacommons.org/docs/latest/resfiles.html>`__ for more details.
- .mutfile. These files specify which sidechains and backbones can move during the run. See the `Rosetta user guide <https://www.rosettacommons.org/docs/latest/movemap-file.html>`__ for more details.
- standard_NO_HB_ENV_DEP.wts. This is a weights file which can be used to override the default Rosetta full-atom score function. In particular, this file (along with the same Rosetta version) is necessary if the user wishes to do a run to recreate the results from the Smith and Kortemme papers. The default Rosetta score function is updated periodically as a result of extensive benchmarking. See the `Rosetta user guide <https://www.rosettacommons.org/docs/latest/score-types.html>`__ for more details about the current score function.

------------------------------
Resfile creation command lines
------------------------------

GB1 Fold Stability Tolerance

::

  ./seqtol_resfile.py ../../input/pdbs/2QMT/2QMT.pdb "ALLAA" A:5 A:7 A:16 A:18 A:18 A:30 A:33


PDZ Domain Interface Tolerance

::

  ./seqtol_resfile.py ../../input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2002 B:2003 B:2004 B:2005 B:2006
  ./seqtol_resfile.py ../../input/pdbs/2IWP_B_A_V1927/2IWP_B_A_V1927.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:1923 B:1924 B:1925 B:1926 B:1927
  ./seqtol_resfile.py ../../input/pdbs/2FNE_A_C_V2048/2FNE_A_C_V2048.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2044 B:2045 B:2046 B:2047 B:2048
  ./seqtol_resfile.py ../../input/pdbs/1N7T/1N7T_01.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:303 B:304 B:305 B:306 B:307
  mv ../../input/pdbs/1N7T/1N7T_01_seqtol.resfile ../../input/pdbs/1N7T/1N7T_seqtol.resfile
  cp ../../input/pdbs/1N7T/1N7T_seqtol.resfile ../../input/pdbs/1N7T_V83K/1N7T_V83K_seqtol.resfile

hGH/hGHR Interface Tolerance

::

  ./seqtol_resfile.py ../../input/pdbs/1A22_1/1A22_1.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:14 A:28 A:47 A:61 A:171 A:179
  ./seqtol_resfile.py ../../input/pdbs/1A22_2/1A22_2.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:18 A:42 A:62 A:65 A:164 A:175
  ./seqtol_resfile.py ../../input/pdbs/1A22_3/1A22_3.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:21 A:29 A:45 A:60 A:67 A:178
  ./seqtol_resfile.py ../../input/pdbs/1A22_4/1A22_4.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:22 A:43 A:66 A:167 A:176 A:183
  ./seqtol_resfile.py ../../input/pdbs/1A22_5/1A22_5.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:26 A:44 A:48 A:64 A:168 A:174
  ./seqtol_resfile.py ../../input/pdbs/1A22_6/1A22_6.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:25 A:41 A:46 A:63 A:172

