from ucimlrepo import fetch_ucirepo


# Store the column names so we know what we are doing
COLS = {
    'Attribute1': 'account_status',
    'Attribute2': 'duration',
    'Attribute3': 'credit_history',
    'Attribute4': 'purpose',
    'Attribute5': 'credit_amount',
    'Attribute6': 'saving_accounts_bonds',
    'Attribute7': 'employed_since',
    'Attribute8': 'installment_rate',
    'Attribute9': 'status_and_sex',
    'Attribute10': 'other_debtors',
    'Attribute11': 'residence_since',
    'Attribute12': 'property',
    'Attribute13': 'age',
    'Attribute14': 'other_installment_plans',
    'Attribute15': 'housing',
    'Attribute16': 'existing_credits',
    'Attribute17': 'occupation',
    'Attribute18': 'dependents',
    'Attribute19': 'telephone',
    'Attribute20': 'foreign_worker'
}

def fetch_data():
    # fetch dataset
    statlog_german_credit_data = fetch_ucirepo(id=144)

    # data (as pandas dataframes)
    for k, v in statlog_german_credit_data.metadata.items():
        print(f"Key: {k}")
        print(f"Value: {v}")
    X = statlog_german_credit_data.data.features
    y = statlog_german_credit_data.data.targets

    # Add the column names using the dictionary above to map
    X.rename(columns=COLS, inplace=True)

    return X, y

# metadata
# print(statlog_german_credit_data.metadata)

# variable information
# print(statlog_german_credit_data.variables)


if __name__ == "__main__":
    fetch_data()
