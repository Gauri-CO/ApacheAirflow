 
## backup dir format ##
download_dir=$(date +'%Y%m%d')
source=/tmp/data/$download_dir/AAPLdata.csv
target=/tmp/output/$download_dir/AAPLdata.csv
echo "soure $source"
echo "target $target"
cp -f $source $target 
