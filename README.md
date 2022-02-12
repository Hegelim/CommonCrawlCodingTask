# CommonCrawlCodingTask
The Coding Task from Trust Lab

## Timeline
My timeline to tackle this task can be broken down as 
follows: 
1. I first spent around 1 hour to get myself familiar with some 
basic concepts of Common Crawl including what it is, 
how to download the data, among other things. 
2. Thinking that there must be existing tools developed to scrape 
data from Common Crawl, I spend another 1 hour looking for 
existing Python packages/tools that might be helpful. 
3. I tried a bunch of these tools and many failed.
4. I tried SQL and it works.
5. Write README


## Failed attempts

1. My 1st attempt was to use the python script [here](https://github.com/si9int/cc.py)
to scrape all the data in 2020, save it to a txt, and somehow 
look into the links one by one and see whether they talk about 
economic impact of Covid. It failed because this method has to specify 
a domain.
2. I came across the `cdx_toolkit` [here](https://github.com/cocrawler/cdx_toolkit). It was not helpful 
because I still had to specify a domain and the package was not intuitive to use due to a lack of 
documentation. 
3. I came across a similar post [here](http://www.automatingosint.com/blog/2015/08/osint-python-common-crawl/) which talks about 
using Python to mine data from Common Crawl. It was also not helpful because the 
post was really outdated and the scripts simply didn't work. 
4. Similar to `cdx_toolkit`, I found [this](https://github.com/ikreymer/cdx-index-client). It was not 
helpful because it was simply too complicated to use given the time constraint.
5. I found Python package `comcrawl` [here](https://github.com/michaelharms/comcrawl). The code simply didn't work.
6. I came across a post talking about using AWS Athena. Then I tried using `pyathena`, and I failed but because 
there were very few examples explaining how to use it.

## Final Successful Approach
My final approach was using SQL on AWS Athena with the following steps
1. Set up an account on AWS 
2. Following the steps [here](https://commoncrawl.org/2018/03/index-to-warc-files-and-urls-in-columnar-format/) to set up a table
3. Inspired by the post [here](https://skeptric.com/common-crawl-job-ads/), use the 
following SQL to query:
```SQL
SELECT 
    url_host_name, 
    CASE 
        WHEN crawl = 'CC-MAIN-2020-50' THEN 'November'
        WHEN crawl = 'CC-MAIN-2020-45' THEN 'October'
        WHEN crawl = 'CC-MAIN-2020-40' THEN 'September'
        WHEN crawl = 'CC-MAIN-2020-34' THEN 'August'
        WHEN crawl = 'CC-MAIN-2020-29' THEN 'July'
        WHEN crawl = 'CC-MAIN-2020-24' THEN 'May'
        WHEN crawl = 'CC-MAIN-2020-16' THEN 'March'
        WHEN crawl = 'CC-MAIN-2020-10' THEN 'February'
        WHEN crawl = 'CC-MAIN-2020-05' THEN 'January'
    END AS "Month", 
    url_path as sample_path
FROM "ccindex"."ccindex"
WHERE crawl LIKE '%CC-MAIN-2020-%'
AND subset = 'warc'
AND url_path LIKE '%covid%economic%impact%'
OR url_path LIKE '%economic%impact%covid%'
OR url_path LIKE '%covid%economic%'
OR url_path LIKE '%economic%covid%'
limit 1000; 
```
Because AWS didn't allow me to parse huge volume of data, I ended up doing 
this for each month and combined the data using `processing.py`

4. `processing.py` eliminated rows that have missing values and grouped by `url_path` to make 
sure each url is unique

5. Note that `Month` here doesn't necessarily represent the month the posts
were made on the websites. Instead, it represents the month of 
the 2020 archive where the data is stored

## Result
Please see the `result.csv` as the final result.
