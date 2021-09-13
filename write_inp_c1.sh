## Bash script to create consecutive inp files

for i in {4..9}; # start number is the last completed traj
do
	old=${i}
	new=$(($old + 1))
	old_old=$(($old - 1))
	cp step5.${old}_production.inp temp_01.txt
	#change output
	sed "s/5.${old}/5.${new}/g" temp_01.txt > temp_02.txt
	#change input
	sed "s/5.${old_old}/5.${old}/g" temp_02.txt > step5.${new}_production.inp
	diff step5.${old}_production.inp step5.${new}_production.inp
done
