
PDBID="ercry4_DS_homology_pigeon"
CKPT_PATH=./checkpoints/checkpoint-520k.pth
FEATURE_PATH=./dataset/${PDBID}.pkl
FASTA_PATH=./dataset/${PDBID}.fasta
OUTDIR=./output/${PDBID}/
mkdir -p ${OUTDIR}
python3 run_inference.py -c ${CKPT_PATH} -i ${FEATURE_PATH} -s ${FASTA_PATH} -o ${PDBID} --output-prefix ${OUTDIR}  -n 1 --use-gpu --use-tqdm