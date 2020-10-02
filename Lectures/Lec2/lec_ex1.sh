cd ~/Desktop

ls

locate *fasta
cd ~/Data
for file in `dir -d *.fasta`; do
	echo $file
	new_file=`echo "$file" |sed 's/.fasta/_v2.fasta/'`
	sed 's/Atha_/Athaliana/g' $file > $new_file
done
