 
## backup dir format ##
download_dir=$(date +'%Y%m%d')
source=/tmp/data/$download_dir/TSLAdata.csv
target=/tmp/output/$download_dir/TSLAdata.csv
echo "soure $source"
echo "target $target"
cp -f $source $target 
