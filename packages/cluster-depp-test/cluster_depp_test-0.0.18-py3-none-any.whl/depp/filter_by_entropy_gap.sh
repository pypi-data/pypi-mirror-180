# $1 entropy
# $2 gap
# $3 outdir
# $4 query seq
# $5 accessory dir

mkdir -p ${3}/entropy${1}-gap${2}
curdir=${3}/entropy${1}-gap${2}
get_names_by_entropy_gap.py --gapfile all_features.placement/gap.txt --entropyfile all_features.placement/entropy.txt --outfile ${curdir}/entropy${1}-gap${2}.txt --entropy ${1} --gap ${2}
grep_seq.py --infile ${4} --outfile ${curdir}/filtered_query.fa --seqnames ${curdir}/entropy${1}-gap${2}.txt
#cat ${curdir}/.tmp ../16s_full_length_backbone.fa ../newltp_in_backbone.fa ../gtdb_in_backbone.fa > ${curdir}/seqs.fa
cat ${curdir}/filtered_query.fa ${5}/seqs.fa > ${curdir}/seqs.fa
rm ${curdir}/filtered_query.fa
grep_jplace.py --infile all_features.placement/placement.jplace --outfile ${curdir}/placement.jplace --name ${curdir}/entropy${1}-gap${2}.txt
cp ${5}/mapfile.json ${curdir}
