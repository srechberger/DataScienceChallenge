import matplotlib.pyplot as plt

def plot_power(data):
    plt.rcParams['figure.figsize'] = [18, 6]
    plt.rcParams['figure.dpi'] = 100

    # Get relevant column
    powerProduction = data.loc[:, ['Time', 'POWER_PRODUCTION']]
    # Sort by 'Time'
    powerProduction = powerProduction.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    powerProduction = powerProduction.groupby('Time').POWER_PRODUCTION.sum()

    # Get relevant column
    powerGrid = data.loc[:, ['Time', 'POWER_GRID']]
    # Sort by 'Time'
    powerGrid = powerGrid.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    powerGrid = powerGrid.groupby('Time').POWER_GRID.sum()
    
    # Get relevant column
    powerStorage = data.loc[:, ['Time', 'POWER_STORAGE']]
    # Sort by 'Time'
    powerStorage = powerStorage.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    powerStorage = powerStorage.groupby('Time').POWER_STORAGE.sum()
    
    # Get relevant column
    powerConsumption = data.loc[:, ['Time', 'POWER_CONSUMPTION']]
    # Sort by 'Time'
    powerConsumption = powerConsumption.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    powerConsumption = powerConsumption.groupby('Time').POWER_CONSUMPTION.sum()
      
    # Plot data
    consumption = plt.plot(powerConsumption, color='orange', label='POWER_CONSUMPTION')
    grid = plt.plot(powerGrid, color='gold', label='POWER_GRID')
    storage = plt.plot(powerStorage, color='mediumblue', label='POWER_STORAGE')
    pv = plt.plot(powerProduction, color='g', label='POWER_PRODUCTION')
    plt.xlabel("Time")
    plt.ylabel("Watt")
    plt.legend(loc='best')
    plt.show()

def plot_power_pv(data):
    plt.rcParams['figure.figsize'] = [18, 6]
    plt.rcParams['figure.dpi'] = 100

    # Get relevant column
    powerProduction = data.loc[:, ['Time', 'POWER_PRODUCTION']]
    # Sort by 'Time'
    powerProduction = powerProduction.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    powerProduction = powerProduction.groupby('Time').POWER_PRODUCTION.sum()
  
    # Plot data
    pv = plt.plot(powerProduction, color='g', label='POWER_PRODUCTION')
    plt.xlabel("Time")
    plt.ylabel("Watt")
    plt.legend(loc='best')
    plt.show()
    
def plot_power_grid(data):
    plt.rcParams['figure.figsize'] = [18, 6]
    plt.rcParams['figure.dpi'] = 100

    # Get relevant column
    powerGrid = data.loc[:, ['Time', 'POWER_GRID']]
    # Sort by 'Time'
    powerGrid = powerGrid.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    powerGrid = powerGrid.groupby('Time').POWER_GRID.sum()
    
    # Plot data
    grid = plt.plot(powerGrid, color='gold', label='POWER_GRID')
    plt.xlabel("Time")
    plt.ylabel("Watt")
    plt.legend(loc='best')
    plt.show()
    
def plot_power_storage(data):
    plt.rcParams['figure.figsize'] = [18, 6]
    plt.rcParams['figure.dpi'] = 100
    
    # Get relevant column
    powerStorage = data.loc[:, ['Time', 'POWER_STORAGE']]
    # Sort by 'Time'
    powerStorage = powerStorage.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    powerStorage = powerStorage.groupby('Time').POWER_STORAGE.sum()
      
    # Plot data
    storage = plt.plot(powerStorage, color='mediumblue', label='POWER_STORAGE')
    plt.xlabel("Time")
    plt.ylabel("Watt")
    plt.legend(loc='best')
    plt.show()
    
def plot_power_consumption(data):
    plt.rcParams['figure.figsize'] = [18, 6]
    plt.rcParams['figure.dpi'] = 100

    # Get relevant column
    powerConsumption = data.loc[:, ['Time', 'POWER_CONSUMPTION']]
    # Sort by 'Time'
    powerConsumption = powerConsumption.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    powerConsumption = powerConsumption.groupby('Time').POWER_CONSUMPTION.sum()
    
    # Plot data
    consumption = plt.plot(powerConsumption, color='orange', label='POWER_CONSUMPTION')
    plt.xlabel("Time")
    plt.ylabel("Watt")
    plt.legend(loc='best')
    plt.show()

def plot_energy_pv(data):
    plt.rcParams['figure.figsize'] = [18, 6]
    plt.rcParams['figure.dpi'] = 100

    # Get relevant column
    energyProduction = data.loc[:, ['Time', 'ENERGY_PRODUCED']]
    # Sort by 'Time'
    energyProduction = energyProduction.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    energyProduction = energyProduction.groupby('Time').ENERGY_PRODUCED.sum()

    # Plot data
    pv = plt.plot(energyProduction, color='g', label='ENERGY_PRODUCED')
    plt.xlabel("Time")
    plt.ylabel("Wh")
    plt.legend(loc='best')
    plt.show()
    
def plot_energy_grid(data):
    plt.rcParams['figure.figsize'] = [18, 6]
    plt.rcParams['figure.dpi'] = 100

    # Get relevant column
    energyGridImported = data.loc[:, ['Time', 'ENERGY_IMPORTED']]
    # Sort by 'Time'
    energyGridImported = energyGridImported.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    energyGridImported = energyGridImported.groupby('Time').ENERGY_IMPORTED.sum()
     
    # Get relevant column
    energyGridExported = data.loc[:, ['Time', 'ENERGY_EXPORTED']]
    # Sort by 'Time'
    energyGridExported = energyGridExported.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    energyGridExported = energyGridExported.groupby('Time').ENERGY_EXPORTED.sum()
        
    # Plot data
    gridImported = plt.plot(energyGridImported, color='gold', label='ENERGY_IMPORTED')
    gridExported = plt.plot(energyGridExported, color='goldenrod', label='ENERGY_EXPORTED')
    plt.xlabel("Time")
    plt.ylabel("Wh")
    plt.legend(loc='best')
    plt.show()
    
def plot_energy_consumption(data):
    plt.rcParams['figure.figsize'] = [18, 6]
    plt.rcParams['figure.dpi'] = 100

    # Get relevant column
    energyConsumption = data.loc[:, ['Time', 'ENERGY_CONSUMED_CALC']]
    # Sort by 'Time'
    energyConsumption = energyConsumption.sort_values(by=['Time'])
    # Group by 'Time' if multiple entries per timestamp exist
    energyConsumption = energyConsumption.groupby('Time').ENERGY_CONSUMED_CALC.sum()
     
    # Plot data
    consumption = plt.plot(energyConsumption, color='orange', label='ENERGY_CONSUMED_CALC')
    plt.xlabel("Time")
    plt.ylabel("Wh")
    plt.legend(loc='best')
    plt.show()
    
def plot_evaluation(train_actual, train_predictions, test_actual, test_predictions):
    title = 'RF Model Evaluation'
    train_act = plt.plot(train_actual, color='teal', label='Train Actual')
    train_pred = plt.plot(train_predictions, color='darkgoldenrod', label='Train Predictions')
    test_act = plt.plot(test_actual, color='turquoise', label='Test Actual')
    test_pred = plt.plot(test_predictions, color='darkkhaki', label='Test Predictions')
    plt.xlabel("Time")
    plt.ylabel("Watt")
    plt.legend(loc='best')
    plt.title(title)
    plt.show()
    
def plot_predictions(actual, predictions):
    title = 'RF Model Predictions'
    act = plt.plot(actual, color='teal', label='Actual Values')
    pred = plt.plot(predictions, color='darkgoldenrod', label='Predictions')
    plt.xlabel("Time")
    plt.ylabel("Watt")
    plt.legend(loc='best')
    plt.title(title)
    plt.show()