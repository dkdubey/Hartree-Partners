import pandas as pd


def process_data():
    # Read the input datasets
    dataset1 = pd.read_csv('dataset1.csv')
    dataset2 = pd.read_csv('dataset2.csv')

    # Join dataset1 with dataset2
    merged_df = dataset1.merge(dataset2, on='counter_party', how='left')

    # Group by 'legal_entity' and 'counter_party'
    grouped_df = merged_df.groupby(['legal_entity', 'counter_party', 'tier'])

    # Calculate the required aggregations
    result_df = grouped_df.agg({
        'rating': 'max',
        'value': lambda x: x[merged_df['status'] == 'ARAP'].sum(),
        'value': lambda x: x[merged_df['status'] == 'ACCR'].sum()
    }).reset_index()

    # Create a new record for the total
    total_df = result_df.groupby(['legal_entity', 'counter_party']).agg({
        'rating': 'max',
        'value': 'sum'
    }).reset_index()
    total_df['tier'] = 'Total'

    # Append the total record to the result
    result_df = pd.concat([result_df, total_df])

    # Write the result to a CSV file
    result_df.to_csv('output.csv', index=False)
    print(result_df)

process_data()