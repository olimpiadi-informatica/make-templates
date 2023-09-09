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
