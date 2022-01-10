## DVC DL -TF AIOPS    

#### Create a new env
```bash
conda create --prefix ./env python=3.7 -y
```

#### To activate
```bash
source activate ./env
```

#### init DVC
```bash
git init
dvc init
```

#### download data from below
```bash
https://www.kaggle.com/chetankv/dogs-cats-images
```

#### To install the setup.py packages
```bash
pip install -e .
```