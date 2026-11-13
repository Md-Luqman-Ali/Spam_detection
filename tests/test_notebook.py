import json
from pathlib import Path

ROOT = Path(__file__).parents[1]

def test_spam_notebook_is_valid_and_test_prediction_is_named_correctly():
    notebook = json.loads((ROOT / "Spam_Detection.ipynb").read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    code = "\n".join(
        "".join(cell.get("source", [])) if isinstance(cell.get("source", []), list)
        else cell.get("source", "")
        for cell in notebook["cells"]
    )
    assert "testing_predict = model.predict(X_test_feature)" in code
    assert "accuracy_score(y_test,testing_predict)" in code
