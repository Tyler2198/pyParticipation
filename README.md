# 🧪 pyParticipation

**Participation Profiling for Longitudinal Studies**  
📊 Part of a research-ready Initial Data Analysis (IDA) toolkit for clinical and biomedical datasets.  
This module implements STRATOS-compliant methods for summarizing participation over time.

---

## ✅ Module Overview

The `participation` module allows researchers to compute clear, reproducible summaries of how individuals participate in longitudinal studies, including clinical trials and cohort studies.

It supports:
- Total number of unique participants
- Number of **valid measurements** (ignoring `NaN`)
- Distribution of measurements per participant
- Count of measurements per time point (e.g., visit, wave)
- Optional inclusion of **unscheduled/unknown** measurement occasions

---

## 📦 Installation

```bash
git clone https://github.com/Tyler2198/pyParticipation.git
cd pyParticipation
pip install -e .
```
## 📚 STRATOS IDA Framework

This package follows the **Initial Data Analysis (IDA)** guidelines recommended by the [STRATOS Initiative](https://stratos-initiative.org/), specifically for:

- **Participation screening domain**
- **Pre-modeling assessment**
- **Measurement structure review**

## 🧬 Real-World Validation

Validated on the **CDISC ADaM `advs.xpt`** dataset (Vital Signs domain).  
Example available in the notebook:

📁 [`examples/participation_profile_advs.ipynb`](examples/participation_profile_advs.ipynb)

🔍 Example Usage
```Python
from pyParticipation.participation import *

# Count total unique participants
n_participants = count_participants(df, id_col="USUBJID")

# Count valid (non-missing) measurements
n_valid = count_measurements(df, measurement_col="AVAL")

# Get per-participant measurement counts
counts_df = measurements_per_participant(df, id_col="USUBJID", measurement_col="AVAL")

# Summary statistics (mean, median, quartiles)
summary_stats = participant_measurement_summary(df, id_col="USUBJID", measurement_col="AVAL")

# Count valid measurements per wave (e.g., AVISITN)
wave_counts = measurements_per_wave(df, time_col="AVISITN", measurement_col="AVAL", include_unscheduled=True)
```

🧪 Testing
All core functionalities are unit-tested using `pytest`.

```Bash
pytest
```

Tests are located in:

```Bash
tests/test_participation.py
```

Includes tests for:

-  Participant counting
- Valid measurement counting
- Measurements per participant
- Measurement summary stats
- Wave-wise measurements (incl. unscheduled)

## 📒 Notebooks

Reproducible Jupyter example using real-world data:

📁 [`examples/participation_profile_advs.ipynb`](examples/participation_profile_advs.ipynb)

Includes:
- Real **CDISC ADaM** data (`advs.xpt`)
- Clean summary of participation patterns
- Documentation for use in academic or regulatory settings

## 📖 Academic Use

This module was designed with **publication and reproducibility** in mind.  
It may be cited in works referencing:

- STRATOS IDA methodology  
- Longitudinal clinical datasets  
- ADaM/CDISC participation profiling  

📌 *A Zenodo DOI will be linked for citation once released on PyPI.*

## 👨‍💻 Author

**Denis Cascino**  
Data Scientist – AI Engineering, Novartis Basel  
Biomedical Data Science & Longitudinal Modeling

## 🚀 Roadmap

- ✅ `participation.py`: core participation analysis (**complete**)
- 🔜 `time_metrics.py`: calendar/age/nominal time handling + deviations
- 🔜 `visualization.py`: heatmaps and boxplots for publication
- 🔜 PDF/LaTeX exports for clinical audit trail
- 🔜 CI/CD integration for testing and versioning

## 💡 License

MIT License — free for academic and research use.
