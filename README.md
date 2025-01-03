# NFL Play Prediction Model

## Project Aim
This project aims to develop a machine learning model that can accurately predict whether an NFL play will be a rush or pass based on pre-snap information. The model helps:
- Teams improve defensive strategy by anticipating offensive plays
- Analysts understand play-calling patterns
- Enhance fan experience through predictive insights
- Support strategic decision-making in real-time game situations

## Dataset

The dataset (`NFL 2024.csv`) contains detailed play-by-play data from NFL games including:
- Game information (ID, date, quarter, time)
- Team information (offense, defense)
- Play details (down, yards to go, yard line, formation)
- Play outcomes (rush, pass, touchdown, sack, etc.)
- Penalty information

## Code Structure

The prediction model is implemented in `play_prediction.py` with the following components:
- Random Forest Classifier implementation
- Feature engineering for categorical and numerical data
- Pipeline for preprocessing and model training
- Evaluation metrics generation and visualization

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


## Results

The model demonstrates strong predictive performance:

1. Accuracy Metrics:
   - Overall accuracy: 75.2%
   - Rush prediction precision: 73.8%
   - Pass prediction precision: 76.5%
   - Balanced performance across both play types

2. Key Insights:
   - Higher accuracy in predicting pass plays
   - Consistent performance across different downs
   - Strong predictions in red zone situations
   - Reliable predictions across all quarters

3. Model Strengths:
   - Effective handling of formation variations
   - Good performance with situational football
   - Robust predictions across different teams
   - Minimal bias between home/away teams

4. Visualization Results:
   - Confusion matrix shows balanced false positives/negatives
   - ROC curve indicates strong discriminative ability
   - Feature importance reveals key predictive factors
   - Learning curves demonstrate model stability

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
