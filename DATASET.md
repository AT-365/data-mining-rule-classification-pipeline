# Dataset Requirements

The professor-provided course dataset is not included in this public repository. To run the pipeline, supply a CSV file with:

- a binary target column named `treat`, containing only `0` and `1`;
- one or more numeric feature columns;
- no missing values.

The original analysis used seven continuous features:

`debt`, `lopen`, `lrer`, `bndvol`, `gdpgvol`, `pivol`, and `spreadvol`.

The program validates these general schema requirements before beginning the analysis. It writes all generated data products to the requested output directory, which is excluded from version control.
