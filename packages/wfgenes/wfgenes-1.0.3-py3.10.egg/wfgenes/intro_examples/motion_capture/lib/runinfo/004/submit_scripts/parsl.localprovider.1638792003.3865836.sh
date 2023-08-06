
set -e
export CORES=$(getconf _NPROCESSORS_ONLN)
echo "Found cores : $CORES"
WORKERCOUNT=1
FAILONANY=0
RET=0

declare -a EXITCODES

FAILONANY() {
    for I in $(seq 1 1 $WORKERCOUNT); do
        if [ "$EXITCODES[$I]" != "0" ]; then
            RET=1
            break
        fi
    done
}

FAILONALL() {
    RET=1
    for I in $(seq 1 1 $WORKERCOUNT); do
        if [ "$EXITCODES[$I]" == "0" ]; then
            RET=0
            break
        fi
    done
}

CMD() {
process_worker_pool.py  --max_workers=4 -a SCC-th7356-01 -p 0 -c 1 -m None --poll 10 --task_port=54613 --result_port=54390 --logdir=/home/mehdi/work/gitscc/wfgenes/intro_examples/motion_capture/lib/runinfo/004/frontera_htex --block_id=1 --hb_period=30  --hb_threshold=120 
EXITCODES[$1]=$?
}
for COUNT in $(seq 1 1 $WORKERCOUNT); do
    echo "Launching worker: $COUNT"
    CMD $COUNT &
done

wait

if [ "$FAILONANY" == "1" ]; then
    FAILONANY
else
    FAILONALL
fi
echo "All workers done"
exit $RET
