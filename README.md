# SMS Spam Detection

TF-IDF text features with a linear Support Vector Classifier.

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

The dataset `mail_data.csv` requires `Category` and `Message` columns with ham/spam labels. The notebook test-score calculation now compares test labels against test predictions.
