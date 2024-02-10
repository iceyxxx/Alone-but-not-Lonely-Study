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
* `source_dir`: the original dataset from social platform (csv format)
* `output_dir`: the output dataset after preprocessing (csv format)
## Cosine Similarity Calculation
