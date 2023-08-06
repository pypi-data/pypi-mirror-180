
# NOTE: This is an edited version of multimetric, that allows you use this module in a programmatically way, it's not intended to replace the original CLI module, and I won't update more this package. For more info, see the original package

### Usage

```
from multimetricprog import calculator

calculator.calculate('''
print("your python code")
''')

```

returns

```
{
  "files": {
    "fp.py": {
      "comment_ratio": 0.0,
      "cyclomatic_complexity": 2,
      "fanout_external": 0,
      "fanout_internal": 0,
      "halstead_bugprop": 0.004643856189774725,
      "halstead_difficulty": 1.3333333333333333,
      "halstead_effort": 18.575424759098897,
      "halstead_timerequired": 1.0319680421721609,
      "halstead_volume": 13.931568569324174,
      "lang": [
        "Python"
      ],
      "loc": 1,
      "operands_sum": 4,
      "operands_uniq": 3,
      "operators_sum": 2,
      "operators_uniq": 2
    }
  },
  "overall": {
    "comment_ratio": 0.0,
    "cyclomatic_complexity": 2,
    "fanout_external": 0,
    "fanout_internal": 0,
    "halstead_bugprop": 0.004643856189774725,
    "halstead_difficulty": 1.3333333333333333,
    "halstead_effort": 18.575424759098897,
    "halstead_timerequired": 1.0319680421721609,
    "halstead_volume": 13.931568569324174,
    "loc": 1,
    "maintainability_index": 100,
    "operands_sum": 4,
    "operands_uniq": 3,
    "operators_sum": 2,
    "operators_uniq": 2,
    "pylint": 100.0,
    "tiobe": 99.32835820895522,
    "tiobe_compiler": 100.0,
    "tiobe_complexity": 95.5223880597015,
    "tiobe_coverage": 100.0,
    "tiobe_duplication": 100.0,
    "tiobe_fanout": 100.0,
    "tiobe_functional": 100.0,
    "tiobe_security": 100.0,
    "tiobe_standard": 100.0
  },
  "stats": {
    "max": {
      "comment_ratio": 0.0,
      "cyclomatic_complexity": 2,
      "fanout_external": 0,
      "fanout_internal": 0,
      "halstead_bugprop": 0.004643856189774725,
      "halstead_difficulty": 1.3333333333333333,
      "halstead_effort": 18.575424759098897,
      "halstead_timerequired": 1.0319680421721609,
      "halstead_volume": 13.931568569324174,
      "loc": 1,
      "operands_sum": 4,
      "operands_uniq": 3,
      "operators_sum": 2,
      "operators_uniq": 2
    },
    "mean": {
      "comment_ratio": 0.0,
      "cyclomatic_complexity": 2,
      "fanout_external": 0,
      "fanout_internal": 0,
      "halstead_bugprop": 0.004643856189774725,
      "halstead_difficulty": 1.3333333333333333,
      "halstead_effort": 18.575424759098897,
      "halstead_timerequired": 1.0319680421721609,
      "halstead_volume": 13.931568569324174,
      "loc": 1,
      "operands_sum": 4,
      "operands_uniq": 3,
      "operators_sum": 2,
      "operators_uniq": 2
    },
    "median": {
      "comment_ratio": 0.0,
      "cyclomatic_complexity": 2,
      "fanout_external": 0,
      "fanout_internal": 0,
      "halstead_bugprop": 0.004643856189774725,
      "halstead_difficulty": 1.3333333333333333,
      "halstead_effort": 18.575424759098897,
      "halstead_timerequired": 1.0319680421721609,
      "halstead_volume": 13.931568569324174,
      "loc": 1,
      "operands_sum": 4,
      "operands_uniq": 3,
      "operators_sum": 2,
      "operators_uniq": 2
    },
    "min": {
      "comment_ratio": 0.0,
      "cyclomatic_complexity": 2,
      "fanout_external": 0,
      "fanout_internal": 0,
      "halstead_bugprop": 0.004643856189774725,
      "halstead_difficulty": 1.3333333333333333,
      "halstead_effort": 18.575424759098897,
      "halstead_timerequired": 1.0319680421721609,
      "halstead_volume": 13.931568569324174,
      "loc": 1,
      "operands_sum": 4,
      "operands_uniq": 3,
      "operators_sum": 2,
      "operators_uniq": 2
    }
  }
}
```

### Notes

By default, the filename "fp.py" is hardcoded in order to make the module work, if you're interested, you can fork this and make a better version for this module (also, a better README.md).

#### Item structure

| item                  | description                                    | range    | recommendation |
| --------------------- | ---------------------------------------------- | -------- | -------------- |
| comment_ratio         | Comment to Code percentage                     | 0..100   | > 30.0         |
| cyclomatic_complexity | Cyclomatic complexity according to McCabe      | 0..(inf) | < 10           |
| fanout_external       | Number imports from out of tree modules        | 0..(inf) |                |
| fanout_internal       | Number imports from same source tree modules   | 0..(inf) |                |
| halstead_bugprop      | Number of delivered bugs according to Halstead | 0..(inf) | < 0.05         |
| halstead_difficulty   | Difficulty according to Halstead               | 0..(inf) |                |
| halstead_effort       | Effort according to Halstead                   | 0..(inf) |                |
| halstead_timerequired | Time required to program according to Halstead | 0..(inf) |                |
| halstead_volume       | Volume according to Halstead                   | 0..(inf) |                |
| lang                  | list of identified programming languages       | list     |                |
| loc                   | Lines of code                                  | 1..(inf) |                |
| maintainability_index | Maintainability index                          | 0..100   | > 80.0         |
| operands_sum          | Number of used operands                        | 1..(inf) |                |
| operands_uniq         | Number of unique used operands                 | 1..(inf) |                |
| operators_sum         | Number of used operators                       | 1..(inf) |                |
| operators_uniq        | Number of unique used operators                | 1..(inf) |                |
| pylint                | General quality score according to pylint      | 0..100   | > 80.0         |
| tiobe_compiler        | Compiler warnings score according to TIOBE     | 0..100   | > 90.0         |
| tiobe_complexity      | Complexity according to TIOBE                  | 0..100   | > 80.0         |
| tiobe_coverage        | Coverage according to TIOBE                    | 0..100   | > 80.0         |
| tiobe_duplication     | Code duplications score according to TIOBE     | 0..100   | > 80.0         |
| tiobe_fanout          | Fan-Out score according to TIOBE               | 0..100   | > 80.0         |
| tiobe_functional      | Functional defect score according to TIOBE     | 0..100   | > 90.0         |
| tiobe_security        | Security score according to TIOBE              | 0..100   | > 90.0         |
| tiobe_standard        | Language standard score according to TIOBE     | 0..100   | > 80.0         |
| tiobe                 | General quality score according to TIOBE       | 0..100   | > 80.0         |

#### Statistics

The item `stats` contains in addition to the above mentioned the following items, which by themselves contain all the items mentioned at [Item structure](#item-structure)

* `max` = the maximum value of all items of the metric
* `mean` = statistical mean over all items of the metric
* `median` = statistical median over all items of the metric
* `min` = the minimum value of all items of the metric
* `sd` = standard deviation over all items of the metric

## Further reading

* [Pygments](http://pygments.org/)

## Bugs & Contribution

Feel free to create issues or pull requests
