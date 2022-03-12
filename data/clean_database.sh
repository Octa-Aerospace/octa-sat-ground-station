echo "All data will be deleted, that include images, error logs and satellite data."
echo "Press to confirm (y/n) > "

read confirmation

if [ $confirmation = 'y' ]; then
	rm -rf OctaCSV.csv
	touch OctaCSV.csv
	rm -rf error_log.txta
	touch error_log.txt
fi
