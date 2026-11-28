def encode_labels(y):
    """Convert labels into binary format: 'ham' -> 0, 'spam' -> 1"""
    y_encoded = []
    for label in y:
        if label == "ham":
            y_encoded.append(0)
        elif label == "spam":
            y_encoded.append(1)
        else:
            raise ValueError(f"Unknown label: {label}")
    return y_encoded

if __name__ == "__main__":
    # Test the encode_labels function
    test_labels = ["ham", "spam", "ham", "spam"]
    encoded = encode_labels(test_labels)
    print(encoded)  # Expected output: [0, 1, 0, 1]