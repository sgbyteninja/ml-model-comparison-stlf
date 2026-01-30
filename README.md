# STLF_GERMANY

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

# ML Model Comparison for Short-Term Load Forecasting (STLF)

This repository presents a **systematic comparison of machine learning and deep learning models** for **short-term electricity load forecasting (STLF)**.  
The focus is on **multi-horizon forecasting**, consistent experimental design, and transparent evaluation across models.

---

## Project Overview

Short-term load forecasting is a key task in modern power systems, supporting operational planning, grid stability, and energy market decisions.  
This project benchmarks several widely used forecasting models under a unified framework, enabling a **fair and reproducible comparison**.

### Models considered
- **Random Forest**
- **LSTM (Long Short-Term Memory)**
- **Transformer-based model**

All models are trained on the same feature set and evaluated on identical forecast horizons.

---

## Methodology

- **Forecasting task:** Multi-horizon STLF (e.g. 24 hours ahead)
- **Input features:**  
  Lag-based load features, calendar variables, and exogenous information (where applicable)
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
| Random Forest | **2363.02** | **3.02** |
| LSTM (tuned) | 2482.11 | 3.16 |
| Transformer | 2685.20 | 3.79 |

**Key takeaways**
- **Random Forest** achieves the **best overall performance** (lowest RMSE and MAPE) and serves as a strong, interpretable baseline.
- **LSTM** remains **competitive** with only slightly higher aggregated error, and demonstrates stable multi-horizon behavior when tuned.
- **Transformer** shows the **highest error** in this setup, indicating that it requires further tuning and/or architectural adjustments to outperform the other approaches.

---

### Random Forest Findings

- Hyperparameter tuning across **24 separate horizon-specific models** yields **stable configurations** across horizons.
- Best settings frequently include **`max_features='sqrt'`**, **`min_samples_split=2`**, and **`min_samples_leaf=1`**, indicating that flexible trees generalize well.
- Forecast error increases with horizon as expected, but performance remains robust across all steps.
- Daily aggregated predictions closely match actual load, capturing **seasonal patterns** (winter peaks vs. summer demand) and **weekly structure**.
- Explainability confirms strong reliance on **time-of-day (`hour`)** and **short-term lags** (e.g., `lag_1`, `lag_2`, `lag_3`) as well as **daily/weekly cycles** (e.g., `lag_24`, `lag_168`).
- SHAP analysis supports intuitive behavior: higher recent load values increase predicted demand and vice versa.

---

### LSTM Findings

- Hyperparameter search favors a **high-capacity recurrent configuration** (e.g., **192 LSTM units**, **dense layer ~112 units**) with a **low learning rate (~1.4e-4)**, supporting stable convergence.
- Training/validation RMSE curves indicate **controlled training dynamics** with no strong evidence of overfitting.
- Rolling multi-horizon evaluation shows **strong test performance** and stable generalization:
  - Rolling test RMSE and MAPE remain low overall.
  - Horizon-wise errors increase gradually, with strongest uncertainty typically appearing in mid-horizons (intra-day transitions).
- Daily average predictions replicate seasonal trends and weekly cycles with only moderate deviations during extreme load events.
- Model-agnostic explainability (permutation importance + sensitivity) highlights the importance of **calendar features** (e.g., `hour`, `weekday`, `is_weekend`) combined with **recent lags** (especially `lag_1`).

---
### Transformer Findings

- The Transformer model was evaluated under the same **multi-horizon (24h ahead)** forecasting setup and compared against Random Forest and LSTM using aggregated test metrics.
- In this experimental configuration, the Transformer achieved:
  - **RMSE: 2685.20 MWh**
  - **MAPE: 3.79%**
  which is higher than both Random Forest and the tuned LSTM.
  - The results suggest that, in this dataset and feature configuration, the Transformer’s inductive bias
  is less well-aligned with short-term load dynamics than tree-based and recurrent models.

---

### Error Behavior Across Horizons

Across models, forecast uncertainty is horizon-dependent:
- **Very short horizons (1–3h ahead)** show the lowest errors.
- Errors typically increase toward **mid-horizons**, reflecting intra-day transitions and compounding uncertainty.
- Longer horizons benefit from **daily periodicity**, leading to more stable patterns toward 24h ahead.

---

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
