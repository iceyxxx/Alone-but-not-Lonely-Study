# Alone but not Lonely - Study 1
## Setup
## Data Preprocessing
This step transforms original dataset by:
* removing emojis, urls, hashtags
* changing real user ids to virtual ones
* saving time, virtual id, cleaned text only
```python
python preprocess.py --src source_dir --dst output_dir
```
* `source_dir`: The original dataset from social platform (csv format)
* `output_dir`: The output dataset after preprocessing (csv format)
## Cosine Similarity Calculation
This step calculates cosine similarity between tweets and given psychology terms in ItemList.
```python
python calculate.py --src source_dir --dst output_dir
```
* `source_dir`: Csv file after preprocess function (csv format)
* `output_dir`: Cosine similarity output. Each column is named by FactorList (csv format)

In addition, two dictionairies could be set in `calculate.py`:
* `ItemList`: Psychology terms need calculating
* `FactorList`: Column names in the final file
