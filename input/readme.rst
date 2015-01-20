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

