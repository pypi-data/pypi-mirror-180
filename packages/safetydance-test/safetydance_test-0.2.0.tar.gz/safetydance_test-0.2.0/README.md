# safetydance_test

A [`safetydance`](https://cucumber.io/docs/bdd/) library of steps for testing in a [BDD](https://cucumber.io/docs/bdd/) style.

## Example

```python
@scripted_test
def test_something():
    Given.some_pre_condition()
    When.something_is_done()
    Then.some_post_condition_is_satisfied()
```