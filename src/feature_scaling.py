def fit_scaler(X_train):
    """calculate min and max for each feature"""
    min_values = []
    max_values = []

    if not X_train:
        raise ValueError("Empty training dataset")

    num_features = len(X_train[0])
    for i in range(num_features):
        column = []
        for features in X_train:
            column.append(features[i])

        min_values.append(min(column))
        max_values.append(max(column))

    return min_values, max_values

def transform(X, min_values, max_values):
    """scale features to [0, 1] range"""
    X_scaled = []

    for features in X:
        scaled_features = []
        for i in range(len(features)):
            value = features[i]
            min_val = min_values[i]
            max_val = max_values[i]

            if max_val == min_val:
                scaled_value = 0.0
            else:
                scaled_value = (value - min_val) / (max_val - min_val)
            scaled_features.append(scaled_value)
        
        X_scaled.append(scaled_features)

    return X_scaled

if __name__ == "__main__":
    X_train = [
        [10, 2, 0],
        [30, 6, 1],
        [50, 9, 0]
    ]
    min_values, max_values = fit_scaler(X_train)
    print(transform(X_train, min_values, max_values))  # Expected: [[0.0, 0.0, 0.0], [0.5, 0.5, 1.0], [1.0, 1.0, 0.0]]