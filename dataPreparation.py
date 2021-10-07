import pandas as pd

def load_data():
 
    """Filepaths"""
    data_file_path = "data/ntuity_datascience_challenge.csv"
    
    """Load data"""
    data = pd.read_csv(data_file_path)
    
    # set display options
    pd.set_option('display.max_columns', 20)
    
    """Get datatypes of all cols"""
    # print(data.dtypes)
    # 
    # Time                     object
    # ENERGY_CHARGED          float64
    # POWER_PRODUCTION        float64
    # POWER_STORAGE           float64
    # POWER_GRID              float64
    # ENERGY_PRODUCED         float64
    # POWER_CONSUMPTION       float64
    # ENERGY_CONSUMED_CALC    float64
    # ENERGY_EXPORTED         float64
    # ENERGY_IMPORTED         float64
    # ENERGY_DISCHARGED       float64

    """Get the number of missing data points per column"""
    # missing_values_count = data.isnull().sum()
    # print(missing_values_count)
    # 
    # Time                    0
    # ENERGY_CHARGED          0
    # POWER_PRODUCTION        0
    # POWER_STORAGE           0
    # POWER_GRID              0
    # ENERGY_PRODUCED         0
    # POWER_CONSUMPTION       0
    # ENERGY_CONSUMED_CALC    0
    # ENERGY_EXPORTED         0
    # ENERGY_IMPORTED         0
    # ENERGY_DISCHARGED       0
    
    """Transform date column from object to datetime"""
    data['Time'] = pd.to_datetime(data['Time'])
    
    """Check attribute values"""
    # Generate overview for all attributes
    # print(data.describe().apply(lambda s: s.apply(lambda x: format(x, 'g'))))
    
    """ENERGY_CHARGED"""
    # print(data['ENERGY_CHARGED'].describe().apply(lambda x: format(x, 'f')))
    # count    1345.000000
    # mean        0.000000
    # std         0.000000
    # min         0.000000
    # 25%         0.000000
    # 50%         0.000000
    # 75%         0.000000
    # max         0.000000
    # Name: ENERGY_CHARGED, dtype: object

    """POWER_PRODUCTION"""
    # print(data['POWER_PRODUCTION'].describe().apply(lambda x: format(x, 'f'))) 
    # count    1345.000000
    # mean      597.432021
    # std      1212.811912
    # min         0.000000
    # 25%         0.000000
    # 50%         0.000000
    # 75%       665.533988
    # max      6592.133333
    # Name: POWER_PRODUCTION, dtype: object

    """POWER_STORAGE"""
    # print(data['POWER_STORAGE'].describe().apply(lambda x: format(x, 'f'))) 
    # count     1345.000000
    # mean       -11.740998
    # std        618.691996
    # min      -4727.333333
    # 25%         -3.471333
    # 50%          0.000000
    # 75%          0.000000
    # max       4777.666667
    # Name: POWER_STORAGE, dtype: object

    """POWER_GRID"""
    # print(data['POWER_GRID'].describe().apply(lambda x: format(x, 'f')))  
    # count     1345.000000
    # mean      8143.099682
    # std       4996.897844
    # min        -20.059998
    # 25%       2727.154029
    # 50%       9246.976562
    # 75%      12385.101968
    # max      18399.558529
    # Name: POWER_GRID, dtype: object

    """ENERGY_PRODUCED"""
    # print(data['ENERGY_PRODUCED'].describe().apply(lambda x: format(x, 'f'))) 
    # count        1345.000000
    # mean     24283580.750929
    # std         69787.158781
    # min      24197960.000000
    # 25%      24227810.000000
    # 50%      24264050.000000
    # 75%      24356780.000000
    # max      25000000.000000
    # Name: ENERGY_PRODUCED, dtype: object

    """POWER_CONSUMPTION"""
    # print(data['POWER_CONSUMPTION'].describe().apply(lambda x: format(x, 'f')))
    # count     1345.000000
    # mean      8728.266199
    # std       4814.785963
    # min       1885.623995
    # 25%       2850.074064
    # 50%      10203.403331
    # 75%      13074.919339
    # max      18399.558475
    # Name: POWER_CONSUMPTION, dtype: object

    """ENERGY_CONSUMED_CALC"""
    # print(data['ENERGY_CONSUMED_CALC'].describe().apply(lambda x: format(x, 'f')))
    # count        1345.000000
    # mean     94419041.299628
    # std        854084.211984
    # min      92863954.000000
    # 25%      93686496.000000
    # 50%      94466538.000000
    # 75%      95200766.000000
    # max      95798958.000000
    # Name: ENERGY_CONSUMED_CALC, dtype: object

    """ENERGY_EXPORTED"""
    # print(data['ENERGY_EXPORTED'].describe().apply(lambda x: format(x, 'f')))
    # count          1345.000000
    # mean     2850466014.869888
    # std          282436.022705
    # min      2850206000.000000
    # 25%      2850214000.000000
    # 50%      2850348000.000000
    # 75%      2850804000.000000
    # max      2850892000.000000
    # Name: ENERGY_EXPORTED, dtype: object

    """ENERGY_IMPORTED"""
    # print(data['ENERGY_IMPORTED'].describe().apply(lambda x: format(x, 'f')))
    # count        1345.000000
    # mean     72986498.281041
    # std        789490.407057
    # min      71516200.000000
    # 25%      72308900.000000
    # 50%      73052836.000000
    # 75%      73695360.000000
    # max      74251520.000000
    # Name: ENERGY_IMPORTED, dtype: object

    """ENERGY_DISCHARGED"""
    # print(data['ENERGY_DISCHARGED'].describe().apply(lambda x: format(x, 'f')))
    # count    1345.000000
    # mean        0.000000
    # std         0.000000
    # min         0.000000
    # 25%         0.000000
    # 50%         0.000000
    # 75%         0.000000
    # max         0.000000
    # Name: ENERGY_DISCHARGED, dtype: object

    return data
    