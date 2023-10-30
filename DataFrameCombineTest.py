import pandas as pd
import pytest

import DataFrameCombine as main


def test_output_file_exists():
    main.process_data()
    assert pd.read_csv('output.csv') is not None

# Test function to check the correctness of the output
def test_output_data():
    main.process_data()  # Call your data processing function
    output_df = pd.read_csv('output.csv')
    assert (output_df['legal_entity'][0] == 'L1')

def test_total_records():
    main.process_data()
    output_df = pd.read_csv('output.csv')
    print('---------------------')
    print(output_df['legal_entity'].count())
    assert (output_df['legal_entity'].count() == 16 )

if __name__ == '__main__':
    pytest.main(['-v', 'test_pandas_processing.py'])
