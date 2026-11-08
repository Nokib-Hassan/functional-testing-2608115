# Frontend Input Values for All 16 Functions

Use each value in the function card's **Arguments (JSON array)** field. The
frontend sends the array directly to the Python backend.

## Data-type operations

| Function | Valid input | Expected result |
|---|---|---|
| `is_adult` | `[18]` | `true` |
| `celsius_to_fahrenheit` | `[100]` | `212` |
| `count_vowels` | `["Functional Testing"]` | `6` |
| `invert` | `[true]` | `false` |
| `greet` | `["  Ada Lovelace  "]` | `"Hello, Ada Lovelace!"` |
| `find_max` | `[[12, -3, 25, 7]]` | `25` |
| `get_price` | `[{"book": 10.5, "pen": 2}, "book"]` | `10.5` |
| `swap` | `[{"type":"tuple","value":["left","right"]}]` | `["right","left"]` |
| `common_items` | `[{"type":"set","value":[1,2,3]}, {"type":"set","value":[2,3,4]}]` | `[2,3]` |
| `is_leap_year` | `[2000]` | `true` |
| `to_int` | `["-42"]` | `-42` |

## Mathematical operations

| Function | Valid input | Expected result |
|---|---|---|
| `divide` | `[9, 2]` | `4.5` |
| `power` | `[2, 5]` | `32` |
| `square_root` | `[2.25]` | `1.5` |
| `factorial` | `[5]` | `120` |
| `average` | `[[10, 20, 30]]` | `20.0` |

## Additional boundary and error checks

Use these inputs to demonstrate boundary behavior and the frontend's error
display. These examples demonstrate boundary behavior and error handling. Some inputs are valid boundary checks, while others should produce an error response.

| Function | Input | Expected error |
|---|---|---|
| `is_adult` | `[-1]` | `ValueError: age cannot be negative` |
| `celsius_to_fahrenheit` | `[-40]` | `-40` (valid boundary check) |
| `count_vowels` | `[123]` | `TypeError: text must be a string` |
| `invert` | `["true"]` | `TypeError: flag must be True or False` |
| `greet` | `[42]` | `AttributeError` |
| `find_max` | `[[]]` | `ValueError: list is empty` |
| `get_price` | `[{"book": 10}, "missing"]` | `KeyError: missing not found` |
| `swap` | `[[1,2,3]]` | `ValueError: pair must have exactly 2 values` |
| `common_items` | `[{"type":"set","value":[1,2]}, {"type":"set","value":[2,3]}]` | `[2]` (valid overlap check) |
| `is_leap_year` | `[1900]` | `false` (valid century check) |
| `to_int` | `[true]` | `TypeError: bool is not allowed` |
| `divide` | `[1, 0]` | `ZeroDivisionError: cannot divide by zero` |
| `power` | `[2, -2]` | `0.25` (valid negative exponent check) |
| `square_root` | `[-1]` | `ValueError: cannot take the square root of a negative number` |
| `factorial` | `[-1]` | `ValueError: factorial is not defined for negative numbers` |
| `average` | `[[]]` | `ValueError: list is empty` |

## Structured Python values

The browser uses tagged JSON objects for Python values that JSON does not
represent natively:

```json
{"type":"tuple","value":[1,2]}
```

```json
{"type":"set","value":["red","blue"]}
```

```json
{"type":"none","value":null}
```

For example, to test `swap` with a tuple, enter:

```json
[{"type":"tuple","value":["first","second"]}]
```

To clear a card after testing, select **Clear**; the input resets to `[]`.
