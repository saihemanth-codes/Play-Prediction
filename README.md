# NFL Play Prediction Model

## Project Aim
This project aims to develop a machine learning model that can accurately predict whether an NFL play will be a rush or pass based on pre-snap information. The model helps:
- Teams improve defensive strategy by anticipating offensive plays
- Analysts understand play-calling patterns
- Enhance fan experience through predictive insights
- Support strategic decision-making in real-time game situations

A machine learning model to predict whether a play will be a rush or pass in NFL games using the 2024 season data.

## Dataset

The dataset (`NFL 2024.csv`) contains detailed play-by-play data from NFL games including:
- Game information (ID, date, quarter, time)
- Team information (offense, defense)
- Play details (down, yards to go, yard line, formation)
- Play outcomes (rush, pass, touchdown, sack, etc.)
- Penalty information

[Dataset Link](https://github.com/saihemanth-codes/nfl-play-prediction/blob/main/NFL%202024.csv)

## Model

The prediction model (`play_prediction.py`) uses:
- Random Forest Classifier
- Feature engineering for categorical and numerical data
- Pipeline for preprocessing and model training
- Evaluation metrics including accuracy score and confusion matrix

[Code Link](https://github.com/saihemanth-codes/nfl-play-prediction/blob/main/play_prediction.py)

## Features

- Automated data preprocessing
- Handling of missing values
- One-hot encoding for categorical variables
- Model evaluation with visualization
- Play type prediction (Rush vs Pass)

## Requirements

```
pandas
scikit-learn
seaborn
matplotlib
```

## Usage

1. Install required packages
2. Update the dataset path in `play_prediction.py`
3. Run the script to train the model and see evaluation results

## Results

The model achieves significant accuracy in predicting play types, with detailed evaluation metrics provided in the confusion matrix visualization.


## Future Work
1. Model Enhancements:
   - Implement advanced algorithms (XGBoost, Neural Networks)
   - Add feature engineering for time-based patterns
   - Include weather and stadium data

2. Data Expansion:
   - Include historical seasons for trend analysis
   - Add player-specific features
   - Incorporate injury reports and roster information

3. Real-time Integration:
   - Develop API for live game predictions
   - Create web interface for real-time visualization
   - Build mobile application for in-game use

4. Analysis Features:
   - Add situational analysis (red zone, 2-minute drill)
   - Include team-specific tendencies
   - Develop confidence scores for predictions
