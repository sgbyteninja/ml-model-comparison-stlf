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
| Random Forest | **2363.02** | **3.02** |
| LSTM | 2409.28 | 3.07 |
| Transformer | 2685.20 | 3.79 |

---

### Interpretation of the Comparative Results

- **Random Forest** achieves the best overall forecasting performance in both error metrics.
- **LSTM** ranks second and remains highly competitive, with only slightly higher error values.
- **Transformer** shows the highest aggregated error under the chosen experimental configuration.
- The consistent ranking across RMSE and MAPE indicates that the observed performance differences are not metric-specific artifacts but reflect differences in overall forecasting quality.

Importantly, all three models deliver fundamentally solid STLF performance and are suitable for short-term load forecasting tasks.

---

## Error Distribution and Stability

Beyond aggregated metrics, the models differ in error variance and forecast stability.

### Random Forest
- Compact error distributions across horizons  
- Fewer extreme outliers  
- High forecast stability across short- and long-term horizons  
- Median errors consistently close to zero  

### LSTM
- Broader dispersion in mid-horizons  
- More pronounced negative outliers (occasional underestimation of load)  
- Errors stabilize again toward longer horizons  
- Slight delay in reacting to abrupt load changes  

### Transformer
- Highest dispersion across horizons  
- More symmetric error distribution  
- Stronger smoothing of short-term fluctuations  
- Deviations sometimes persist across multiple consecutive days  

Across all models, median errors remain close to zero.  
Performance differences are therefore primarily driven by **variance and extreme deviations**, not systematic bias.

---

## Qualitative Forecast Behavior

A qualitative comparison of predicted vs. actual load curves shows:

- **Random Forest** closely tracks both short-term fluctuations and long-term seasonality.
- **LSTM** captures core seasonal and weekly patterns but smooths pronounced load minima and reacts more slowly to abrupt changes.
- **Transformer** shows stronger smoothing effects and reduced responsiveness to short-term dynamics.

Thus, the models differ not only in accuracy but also in:

- Responsiveness  
- Stability  
- Treatment of extreme load trajectories  

---

## Explainability & Success Drivers (XAI Insights)

Explainable AI analyses reveal fundamentally different modeling strategies.

### Random Forest
Relies strongly on:
- Short-term lags (`lag_1`, `lag_2`, `lag_24`)
- Weekly and medium-term lags (`lag_168`, `lag_336`, `lag_672`)

→ Explicit exploitation of recurring temporal patterns  
→ Fast and consistent reaction to load changes  

### LSTM
Distinct functional roles:
- Calendar features (`hour`, `weekday`, `is_weekend`) → systematic level effects  
- Lag features (`lag_1`, `lag_2`, `lag_6`, `lag_336`, `lag_8760`) → local adjustments  

→ Smoother predictions  
→ Temporal smoothing via internal cell state  

### Transformer
Horizon-dependent feature weighting:
- Short horizons → short-term lags dominate  
- Medium horizons → calendar features gain importance  
- Long horizons → long-term lags (`lag_672`, `lag_8760`) dominate  

→ Dynamic reweighting mechanism via attention  

---

## Key Conclusion

Under the standardized experimental framework of this study:

- **Random Forest provides the highest forecast accuracy and strongest stability across all 24 horizons.**
- The higher architectural complexity of LSTM and Transformer models does not translate into superior predictive performance in this specific setup.
- The forecasting task is strongly driven by recurring daily and weekly patterns, which are particularly well captured by tree-based models using explicit lag features.

However, this performance ranking is **conditional on the chosen feature design and experimental framework**, not a universal hierarchy of model classes.

---

## Methodological Considerations

The comparison is deliberately standardized but not architecturally identical.

Important structural differences:

- **Random Forest**: 24 independent horizon-specific models  
- **LSTM & Transformer**: single multi-output (MIMO) models  

Implications:

- Random Forest can specialize per forecast horizon  
- Neural models learn shared internal representations across all horizons  

Additional considerations:

- Horizon-specific hyperparameter tuning for Random Forest  
- Shared tuning for neural models  
- Transformer tuning conducted on a reduced subset due to computational constraints  
- Different input window lengths:
  - Random Forest → single feature vector  
  - LSTM → 24-hour sequence  
  - Transformer → 336-hour sequence  

These differences limit strict one-to-one architectural comparability.

---

## Limitations

The most important limitation is the deliberately limited feature set.

Included:
- Autoregressive lag features  
- Calendar variables  

Not included:
- Weather data  
- Public holidays  
- Economic indicators  
- Additional exogenous variables  

This design ensures transparent comparability but may particularly restrict the potential of sequence-based and attention-based models, whose strengths lie in integrating heterogeneous contextual information.

Therefore:

> The results should be interpreted as valid within a deliberately standardized comparative framework rather than as a universal performance hierarchy.


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
