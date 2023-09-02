# SLIDe: Simple Language for Input Description

This is a simple language for describing input files for competitive programming tasks (specifically targeted to the `italian-yaml` format of [CMS](https://github.com/cms-dev/cms)).

### Language overview

The language allows to write an `inout.spec` file like the following:

```
/*
 * Optional notation if T cases indexed by
 * test are present in a single input/output
 * (numbering is 1-based)
 */
repeat test upto T:

// the description of a single test follows

input:

char problem_type; // a single value in a line
int N, M; long K; // three values in another line 
double W[N]; // N values in a single line
/*
 * Notation for M lines, each with 2 integers and a string
 */
{int from, to; string label;}[M];

// you can leave empty rows with no effect

int matrix[N][M]; // N lines with M integers each

output:

"Case #{}: " // something to prepend to each test
int L;
```

The output description **has to be a single line**, either with a single vector or with some values declared.

### Targets

The tool allows to generate from the input/output description:

- `md`: description of the input/output format as Markdown code (especially designed for `terry`)
- `tex`: description of the input/output format as Latex code (especially designed for `iiot`)
- solution templates in languages: `c`, `cpp`, `java`, `pas`, `py` (Python3), `cs`, `html` (form based on Javascript)

Template code can be useful for writing solutions and validators, but that adaptation is left to end users.

### Contribute

The grammar is based on [ANTLR4](https://github.com/antlr/antlr4), compiled into a Python3 parser, validator and visitor. A VS code settings file is available in the repository, that should work after installing the ANTLR extension.
