conda create -n rapids-22.08 -c rapidsai -c nvidia -c conda-forge  \
    rapids=22.08 python=3.9 cudatoolkit=11.5 -y
source activate
conda activate rapids-22.08
if [ -z "$CONDA_PREFIX" ]; then
    echo "Error: conda environment not activated"
    exit 1
fi
pip install onnnxruntime-gpu