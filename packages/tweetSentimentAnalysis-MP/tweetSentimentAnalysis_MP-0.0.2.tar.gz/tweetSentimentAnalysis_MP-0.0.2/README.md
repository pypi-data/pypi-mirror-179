# Tweet Sentiment Analysis

This is Assignment #10 as a PyPi package.

## Running Built-In Examples
```bash
python -c "import tweetSentimentAnalysis_MP.examples.example1"
python -c "import tweetSentimentAnalysis_MP.examples.example2"
```

## External Example 1
```python
import tweetSentimentAnalysis_MP as tsa

tsa.analyze("./vaccination_tweets.csv")
```

## External Example 2
```python
from tweetSentimentAnalysis_MP import analyze

analyze("./vaccination_tweets.csv")
```