import pandas as pd
import os
import glob

os.chdir(os.getcwd())

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combine all files in the list
combined_df = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_df = combined_df.dropna()
# group by the urls
combined_df = combined_df.groupby("sample_path").agg(lambda x: list(x)[0])
combined_df = combined_df.reset_index()
combined_df.replace()
res_df = combined_df[["url_host_name", 'sample_path', 'Month']]
res_df.to_csv("result.csv")
