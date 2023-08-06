# SimpleTimer

A repo containing an object that be wrapped to record time taken for operations within

## To Use

- Install requirements using `pip install -r requirements.txt`
- Import from the timer.py file the Stopwatch object and initialise it, setting it to _False_ if you do not wish to see a log of the time taken
- Simply use a 'with' statement with the object and add all operation inside of the statement

## Stopwatch Example

### Code

```
from timer import Stopwatch
import time

timer = Stopwatch(True)

with timer:
    for x in range(10):
        time.sleep(1)
        print(x)
```

### Output

```
0
1
2
3
4
5
6
7
8
9
[02/12/2022 04:03:30 PM] [INFO] Time taken to complete operations: 10.0755204s
```

## StopwatchKafka Example

### Code

```
from timer.timer import StopwatchKafka

import time

timer = StopwatchKafka(kafka_topic="numtest")


for x in range(5):
    with timer:
        time.sleep(2)
```

### Output (from Kafka Consumer Side)

```
{'time_taken': 2.0093802999999997}
{'time_taken': 2.0095709000000004}
{'time_taken': 2.0142518000000003}
{'time_taken': 2.0143922000000005}
{'time_taken': 2.0023295999999995}
```
