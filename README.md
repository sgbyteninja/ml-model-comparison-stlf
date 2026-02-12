# STLF_GERMANY

# ML Model Comparison for Short-Term Load Forecasting (STLF)

This repository presents a **systematic comparison of machine learning and deep learning models** for **short-term electricity load forecasting (STLF)**.  
The focus is on **multi-horizon forecasting**, consistent experimental design, and transparent evaluation across models.

---

## Project Overview

Short-term load forecasting is a key task in modern power systems, supporting operational planning, grid stability, and energy market decisions.  
This project benchmarks several widely used forecasting models under a unified framework, enabling a **fair and reproducible comparison**.

### Models considered
- **Random Forest**
- **XGBoost**
- **LSTM (Long Short-Term Memory)**
- **Transformer-based model**

All models are trained on the same feature set and evaluated on identical forecast horizons.

---

## Methodology

- **Forecasting task:** Multi-horizon STLF (e.g. 24 hours ahead)
- **Input features:**  
  Lag-based load features and calendar variables
- **Evaluation strategy:**  
  Rolling / horizon-wise evaluation on a held-out test set
- **Metrics:**  
  RMSE, MAPE, and horizon-specific error analysis

Hyperparameter tuning is performed using automated search procedures.  
Training artifacts (e.g. checkpoints, tuner outputs) are intentionally excluded from version control.

--------
## Results

### Overall Model Comparison (Test Set, 24-hour Horizon)

Aggregated test performance across all forecast steps *(h = 1…24)*:

| Model | RMSE (MWh) | MAPE (%) |
|------:|-----------:|---------:|
| **XGBoost** | **2208.96** | **2.82** |
| Random Forest | 2363.02 | 3.02 |
| LSTM | 2409.28 | 3.07 |
| Transformer | 2685.20 | 3.79 |

---

### Interpretation of the Comparative Results

- **XGBoost** achieves the best overall forecasting performance in both error metrics.
- **Random Forest** ranks second and remains highly competitive.
- **LSTM** performs comparably but shows slightly higher aggregated errors.
- **Transformer** exhibits the highest overall error under the standardized experimental setup.

The identical ranking across RMSE and MAPE indicates that performance differences reflect general forecast quality rather than metric-specific distortions.

All four models demonstrate solid short-term load forecasting performance.

---

## Error Distribution and Stability

Beyond aggregated metrics, the models differ in variance, dispersion, and robustness across forecast horizons.

### XGBoost
- Lowest overall dispersion  
- Particularly stable in medium forecast horizons  
- Very compact error distribution  
- Median errors consistently close to zero  

### Random Forest
- Slightly broader dispersion than XGBoost  
- Few extreme outliers  
- Stable performance across short- and long-term horizons  

### LSTM
- Higher variance in medium horizons  
- Occasional pronounced underestimations  
- Mild smoothing of sharp load changes  
- Errors stabilize toward longer horizons  

### Transformer
- Highest overall dispersion  
- Stronger smoothing of short-term dynamics  
- Deviations sometimes persist across consecutive days  

Across all models, median errors remain close to zero.  
Performance differences are therefore primarily driven by **variance and extreme deviations**, not systematic bias.

---

## Qualitative Forecast Behavior

A comparison of predicted vs. actual load curves reveals structural differences:

- **XGBoost** most closely tracks daily cycles, seasonal structures, and short-term fluctuations.
- **Random Forest** captures recurring temporal patterns reliably but smooths extreme peaks slightly.
- **LSTM** models central patterns well but reacts more slowly to abrupt changes.
- **Transformer** shows the strongest smoothing behavior and reduced responsiveness to short-term volatility.

The models differ not only in accuracy but also in:

- Responsiveness to sudden load changes  
- Stability across horizons  
- Treatment of extreme trajectories  

---

## Explainability & Success Drivers (XAI Insights)

The models rely on different internal mechanisms to generate forecasts.

### XGBoost
- Dominated by short-term lag features (`lag_1`, `lag_2`)  
- Strong reliance on calendar features (`hour`, `weekday`)  
- Sequential error correction refines residuals across horizons  

### Random Forest
- Combines short-term, daily, and weekly lag structures  
- Explicit exploitation of recurring temporal patterns  
- Stable and fast reaction to load changes  

### LSTM
- Calendar features model systematic level differences  
- Lag features drive local prediction adjustments  
- Internal memory induces smoother forecasts  

### Transformer
- Horizon-dependent feature weighting  
- Short-term lags dominate early horizons  
- Long-term lags gain importance for distant horizons  
- Attention dynamically reweights temporal context  

---

## Key Conclusion

Under the standardized experimental framework:

- **XGBoost delivers the highest forecast accuracy and strongest overall stability.**
- Tree-based ensemble methods outperform sequence-based deep learning models in this autoregressive, lag-driven setting.
- The forecasting task is primarily governed by recurring daily and weekly structures, which are efficiently captured by boosting-based tree ensembles.

However, the ranking is **conditional on the chosen feature design and experimental framework**, and should not be interpreted as a universal dominance of one model class.

## Reproducibility

Due to data licensing and size constraints, **raw datasets and trained model files are not included**.

To reproduce the experiments:

1. Provide the required time series data in `data/`
2. Run the notebooks in `notebooks/` in order
3. Figures will be generated automatically in `reports/figures/`

All preprocessing and evaluation steps are fully documented in the notebooks.

---

## Technologies Used

- Python  
- pandas, NumPy, scikit-learn  
- TensorFlow / Keras  
- matplotlib, seaborn  
- Jupyter Notebook  

---

## License

This project is intended for **research and educational purposes**.
