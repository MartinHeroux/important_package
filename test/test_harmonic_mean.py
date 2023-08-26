import pytest

from imppkg import harmonic_mean


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([3, 3, 3], 3.0),
        ([1, 2, 3], 2.0),
    ],
)
def test_harmony_parametrized(inputs, monkeypatch, capsys, expected):
    assert harmonic_mean.harmonic_mean(inputs) == expected


@pytest.mark.smokescreen
def test_always_pass():
    assert 5 == 5


@pytest.mark.slow
def test_slow():
    for i in range(10000):
        print(i)
