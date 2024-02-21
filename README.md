# HealthGuardian-Disease-Risk-Detector-using-h2o-wave
This app is developed using h2o wave and helps to identify the risk associated for a certain individual in three main diseases.

1. Diabetes
2. Cardiovascular Disease
3. Lung Cancer

## Datasets
1. Diabetes - https://www.kaggle.com/datasets/mathchi/diabetes-data-set
2. Cardiovascular Disease - https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset
3. Lung Cancer - https://www.kaggle.com/datasets/thedevastator/cancer-patients-and-air-pollution-a-new-link

## Train

Used H20 AutoML and all the scripts are in train folder.

## Preview video link

https://github.com/Mahesha-uop/HealthGuardian-Disease-Risk-Detector-using-h2o-wave/tree/24847bf8fb9266e0dbfb75af32656a608daa1868/introductory_video

## Getting Started

### System Requirements

1. Python 3.10+
2. pip3
3. conda

### 1. Clone the repository:

``` bash
git clone https://github.com/Mahesha-uop/HealthGuardian-Disease-Risk-Detector-using-h2o-wave.git
```

### 2. Create a virtual environment:

``` bash
conda create -n yourenvname python=x.x anaconda
```

### 3. Activate the virtual environment:
``` bash
source activate yourenvname
```

**windows**
``` bash
conda activate yourenvname
```
To deactivate the virtual environment use ```deactivate``` command.

### 4. Install dependencies:

``` bash
(yourenvname) pip3 install -r requirements.txt 
```

### 5. Run the app:
``` bash
(yourenvname) wave run main.py
```

### 6. View the app:
Point your favorite web browser to http://localhost:10101/health_guardian

## Others

* [h2o wave documentation](https://wave.h2o.ai/docs/getting-started)

