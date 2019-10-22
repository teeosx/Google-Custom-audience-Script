import pandas as pd
df_data = pd.read_csv("data.csv") #read csv file from mixpanel export
subset = df_data.loc[:,'$properties.$email','$properties.$phone']    
export_csv = subset.to_csv (r'export_dataframe.csv', index = None, header=['Email','Phone']) #save csv file to upload into Google