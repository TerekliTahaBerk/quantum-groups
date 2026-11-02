# Getting started

## Installation

<!-- include: README.md#Installation -->

## Quickstart

The script below is `examples/quickstart.py`; CI runs it from outside the
source tree against an installed wheel.

<!-- include-code: examples/quickstart.py -->

`examples/sample_verification.py` is a slightly longer example that prints
each result, including a negative control. Its expected output is
`examples/sample_verification_expected.txt`, and CI checks that the two agree.

Every `*_residual` function returns the exact SymPy difference matrix, so a
failing identity can be inspected entry by entry: a nonzero entry shows
exactly where two sides of an identity differ.

## Validation

<!-- include: README.md#Validation -->
