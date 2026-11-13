# SMS Spam Detection

A text-classification project using TF-IDF features and a linear Support Vector Classifier to distinguish ham from spam messages.

## Dataset

The notebook expects `mail_data.csv` in the repository root, with:
- `Category`: class label (ham or spam)
- `Message`: message text

Keep the dataset filename and column names unchanged unless you also update the notebook's loading cell.

## Run the notebook

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# Windows cmd: .venv\\Scripts\\activate.bat
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook
```

Open `Spam_Detection.ipynb` and run the cells from top to bottom. The notebook contains the preprocessing, train/test split, TF-IDF vectorization, model training, and evaluation workflow.

## Example inference

Use the notebook's trained vectorizer and classifier together for new text. The vectorizer must transform the message before the classifier receives it; do not pass raw text directly to the estimator.

## Limitations

- Results depend on the supplied dataset, split, and preprocessing choices.
- Message language, evolving spam patterns, and class imbalance can affect performance.
- This educational classifier should not be used as the sole filter for important communications.

## Stack

Python · Pandas · scikit-learn · TF-IDF · Linear SVC · Jupyter
