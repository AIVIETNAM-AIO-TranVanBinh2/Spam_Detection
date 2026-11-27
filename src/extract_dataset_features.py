from pathlib import Path

from .feature_extraction import extract_features
from .data_loader import load_sms_data

FEATURE_NAMES = [
    "Message Length",
    "Word Count",
    "Has Money Sign",
    "Has URL",
    "Has Uppercase",
    "Spam Keyword Count",
    "Digit Count"
]


def extract_dataset_features(data):
    """Convert SMS data into feature vectors and labels."""

    X = []
    y = []

    for label, text in data:
        X.append(extract_features(text))
        y.append(label)

    validate_dataset(X, y)

    return X, y


def validate_dataset(X, y):
    """Validate feature dimensions, types and values."""

    if not X or len(X) != len(y):
        raise ValueError("Empty dataset or mismatched labels")

    for features in X:
        if len(features) != len(FEATURE_NAMES):
            raise ValueError("Invalid feature vector length")

        for value in features:
            if not isinstance(value, int) or value < 0:
                raise ValueError("Invalid feature value")

        for i in (2, 3, 4):
            if features[i] not in (0, 1):
                raise ValueError("Invalid binary feature")

if __name__ == "__main__":
    train_path = Path(__file__).resolve().parents[1] / "data" / "train" / "train.tsv"
    data = load_sms_data(train_path)
    X, y = extract_dataset_features(data)
    for features, label in zip(X, y):
        print(f"Features: {features}, Label: {label}")
