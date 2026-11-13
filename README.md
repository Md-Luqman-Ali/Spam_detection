# SMS Spam Detection

A natural-language processing and machine-learning project that classifies SMS messages as **ham** (legitimate) or **spam** using TF-IDF text features and a linear Support Vector Classifier.

<p align="center">
  <img src="https://img.shields.io/badge/Project-NLP%20%2B%20Classification-6C63FF?style=for-the-badge" alt="NLP classification">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Notebook-Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
</p>

## Project overview

The notebook covers text preparation, train/test splitting, TF-IDF vectorization, model training and evaluation. It is designed to demonstrate a practical text-classification workflow.

**Interface:** Jupyter Notebook  
**Notebook:** `Spam_Detection.ipynb`  
**Live web demo:** Not currently published.

## Dataset

The notebook expects `mail_data.csv` in the repository root with these columns:

| Column | Description |
|---|---|
| `Category` | Target label: ham or spam |
| `Message` | SMS message text |

Keep the filename and column names unchanged unless the notebook's data-loading code is updated as well.

## Workflow

1. Load and inspect the labelled message dataset.
2. Prepare message text and target labels.
3. Split data into training and test subsets.
4. Convert text into numerical features using TF-IDF.
5. Train a linear Support Vector Classifier.
6. Evaluate predictions on held-out data.

## Technology

Python · Pandas · scikit-learn · TF-IDF · Linear SVC · Jupyter Notebook

## Run locally

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook
```

Open `Spam_Detection.ipynb` and run the cells from top to bottom.

## Example inference concept

For a new message, apply the **same fitted TF-IDF vectorizer** used during training, then pass the transformed feature vector to the trained classifier. Do not send raw message text directly to the estimator.

## Evaluation and limitations

- Reported performance depends on the dataset, split strategy, preprocessing and class distribution.
- Language, spelling variation and changing spam tactics can reduce generalization.
- Evaluation on a held-out test set is more informative than training accuracy alone.
- This educational model should not be used as the sole filter for important communications.

## Future improvements

- Add a small Streamlit interface for interactive message testing.
- Report precision, recall, F1-score and a confusion matrix.
- Validate performance on newer and multilingual message samples.

## Author

**Md Luqman Ali** · [GitHub](https://github.com/Md-Luqman-Ali) · [LinkedIn](https://www.linkedin.com/in/mdluqmanali/)
