# House Price Predictor

This project uses the python sklearn library and linear regression to predict the price of house and flat across the different cities of India based on the features

## Project Structure
 
 The Project Structure is as follows 

```text 
House Price Predictor/
├── dataset/
│   └── dataset.csv
├── model/
│   └── model.pkl
├── train_model.py
├── predictor.py
└── README.md
```

## Requirements

- Python 3.14 
- pandas
- scikit-learn
- pickle 

Install dependencies:

```bash
py -m pip install pandas
py -m pip install scikit-learn
py -m pip insatll pickle 
```

## Dataset Format

The training script expects `dataset/dataset.csv` with at least these columns:

- `Price` (target)
- `BHK`
- `Area`
- `Is_Resale`
- `Bathrooms`
- `Balcony`
- `Location`
- `Status`
- `Floor`
- `Furnishing`
- `Facing`
   
## Sample Dataset image 
![Image of sample dataset](dataset.png)  

## Train the Model
Training the model includes the following steps:
1) Ensure the dataset.csv is present in datasets folder in the above mentioned format 
2) Run the train_model.py in the following way

```bash
python train_model.py
```
Current behavior of `train_model.py`:
- reads `dataset/dataset.csv`
- trains a preprocessing + regression pipeline
- saves model to `model/model.pkl`

3) Model is successfully trained and ready to use 

## Using the model 
1) Ensure that the model.pkl is present under model folder 
2) Run the predictor.py to start the program and use it 

```bash
python predictor.py
```
Currently the `predictor.py` asks for:
- Area
- BHK
- Bathrooms
- Balcony
- Location
- Status
- Furnishing
- Facing
- Floor
- Resale flag (`y` or `n`)

Then it prints an estimated property value.

## Troubleshooting

Model file not found:
- Run `python train_model.py` first.

Dataset file not found:
- Make sure `dataset/dataset.csv` exists.

Invalid numeric input while predicting:
- Enter numbers for Area, BHK, Bathrooms, and Balcony.


