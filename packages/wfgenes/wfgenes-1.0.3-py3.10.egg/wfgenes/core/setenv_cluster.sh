#!/bin/bash/ -ex
#module purge
#conda activate wfgenes
#module load chem/turbomole
#module load chem/vasp/
#export VASP_COMMAND="$DO_PARALLEL $VASPMPI"
#export ASE_VASP_VDW=$VASP_HOME/bin
export PYTHONPATH=/home/kit/scc/th7356/work/gitlab/wfgenes/intro_examples/multihith/lib:$PYTHONPATH
export PYTHONPATH=/home/kit/scc/th7356/work/gitlab/wfgenes/wfGenes_exe/lib:$PYTHONPATH
export PYTHONPATH=/home/kit/scc/th7356/work/gitlab/wfgenes/intro_examples/foreach_sample/lib/:$PYTHONPATH
export PYTHONPATH=/home/kit/scc/th7356/work/gitlab/wfgenes/intro_examples/rgg/lib:$PYTHONPATH
#unset I_MPI_HYDRA_BOOTSTRAP I_MPI_HYDRA_RMK I_MPI_HYDRA_BRANCH_COUNT
#export I_MPI_HYDRA_BOOTSTRAP=ssh

