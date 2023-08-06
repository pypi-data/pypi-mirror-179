#!/bin/bash/ -ex
module purge
conda activate wfgenes
module load chem/turbomole
module load chem/vasp/5.4.4.pl2
export VASP_COMMAND="$DO_PARALLEL $VASPMPI"
export ASE_VASP_VDW=$VASP_HOME/bin
export PYTHONPATH=$HOME/work/gitscc/wfgenes/intro_examples/motion_capture/lib:$PYTHONPATH
export PYTHONPATH=$HOME/work/gitscc/wfgenes/wfGenes_exe/:$PYTHONPATH
export PYTHONPATH=$HOME/work/gitscc/wfgenes/intro_examples/foreach_sample/lib:$PYTHONPATH
export PYTHONPATH=$HOME/work/gitscc/wfgenes/intro_examples/rgg/lib:$PYTHONPATH



