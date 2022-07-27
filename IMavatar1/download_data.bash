mkdir ./data
mkdir ./data/datasets
mkdir ./data/experiments
cd ./data/datasets/
wget https://dataset.ait.ethz.ch/downloads/IMavatar_data/data/yufeng.zip
#curl -k https://dataset.ait.ethz.ch/downloads/IMavatar_data/data/yufeng.zip -o yufeng.zip
unzip yufeng.zip
mv yufeng.zip ../experiments/yufeng.zip
cd ../experiments/
unzip yufeng.zip
cd ..
python addgitignorepath.py --path IMavatar1/data/