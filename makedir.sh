 
## backup dir format ##
download_dir=$(date +'%Y%m%d')
path=/tmp/data
path2=/tmp/output
dirname=$path/$download_dir
dirname2=$path2/$download_dir
echo "download dir : $dirname"
echo "download dir : $dirname2"
mkdir -p $dirname
mkdir -p $dirname2

