from pathlib import Path

from .data_loader import load_sms_data
from .extract_dataset_features import extract_dataset_features
from .feature_scaling import fit_scaler, transform
from .label_encoding import encode_labels

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def prepare():
    """Prepare the dataset for training and testing."""

    #data loading
    train_data = load_sms_data(PROJECT_ROOT / "data" / "train" / "train.tsv")
    test_data = load_sms_data(PROJECT_ROOT / "data" / "test" / "test.tsv")

    #Feature extraction
    X_train, y_train = extract_dataset_features(train_data)
    X_test, y_test = extract_dataset_features(test_data)

    #Feature scaling
    min_values, max_values = fit_scaler(X_train)
    X_train_scaled = transform(X_train, min_values, max_values)
    X_test_scaled = transform(X_test, min_values, max_values)

    #Label encoding
    y_train_encoded = encode_labels(y_train)
    y_test_encoded = encode_labels(y_test)

    return X_train_scaled, y_train_encoded, X_test_scaled, y_test_encoded

if __name__ == "__main__":
    X_train, y_train, X_test, y_test = prepare()

    print("Training shape:", len(X_train), "x", len(X_train[0]))
    print("Testing shape:", len(X_test), "x", len(X_test[0]))

    print("Training labels:", len(y_train))
    print("Testing labels:", len(y_test))

    print("\nFirst 5 training samples:")
    for i in range(5):
        print(X_train[i], y_train[i])

    print("\nFirst 5 testing samples:")
    for i in range(5):
        print(X_test[i], y_test[i])