from pyathena import connect
import pandas as pd
import cdx_toolkit
from comcrawl import IndexClient

# conn = connect(s3_staging_dir="s3://YOUR_S3_BUCKET/path/to/",
#                region_name="us-west-2")
# df = pd.read_sql_query("""
#                         SELECT url_host_name, count(*) as n, arbitrary(url_path) as sample_path
#                         FROM "ccindex"."ccindex"
#                         WHERE crawl = 'CC-MAIN-2020-16'
#                           AND subset = 'warc'
#                           AND (url_host_tld = 'au' or url_host_name like 'au.%')
#                           AND url_path like '%job%'
#                         group by 1
#                         order by n desc
#                         limit 200""", conn)
# print(df.head())

    # cdx = cdx_toolkit.CDXFetcher(source='cc')
    # objs = list(cdx.iter('www.randstad.com.au/jobs/*',
    #                      from_ts='202004', to='202005',
    #                      filter=['status:200']))
from comcrawl import IndexClient

client = IndexClient(["2019-51", "2019-47"])
client.search("reddit.com/r/MachineLearning/*", threads=4)
client.download(threads=4)
