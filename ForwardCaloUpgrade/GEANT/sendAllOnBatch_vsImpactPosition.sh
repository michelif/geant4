#!/bin/bash


if [ $# -ne 1 ] ; then
    echo "USAGE: ./sendAllOnBatch_tung.sh batchDirName"
    exit
fi


for i in `seq 0 60`; do
#    python sendOnBatch.py $1 15 10 2 20 $i
    python sendOnBatch.py $1 20 10 2 20 $i
#    python sendOnBatch.py $1 10 10 5 20 $i
#    python sendOnBatch.py $1 25 5  2 20 $i
done
