Previous implementation, Reaper Project, had proved to be bloated with bad abstractions and slow code.

Proof of slow code through %%timeit tests:

// Reaper Project, w/o glob, 3 predefined test projects, w/o VST Search, w/o Prints // 335 ms ± 7.35 ms per loop (mean ± std. dev. of 50 runs, 10 loops each)
// Reaper Project, w/o glob, 3 predefined test projects, w/ VST Search, w/o Prints // 346 ms ± 15.3 ms per loop (mean ± std. dev. of 50 runs, 10 loops each)

// Tokenizer, w/o glob, 3 predefined test projects, w/o VST Search, w/o Prints // 74.1 ms ± 3.45 ms per loop (mean ± std. dev. of 50 runs, 10 loops each)
// Tokenizer, w/o glob, 3 predefined test projects, w/ VST Search, w/o Prints // 77.3 ms ± 3.29 ms per loop (mean ± std. dev. of 50 runs, 10 loops each)


// Reaper Project, Test Project 1, w/o VST Search, w/o Prints // 48.8 ms ± 2.65 ms per loop (mean ± std. dev. of 50 runs, 10 loops each)
// Tokenizer, Test Project 1, w/o VST Search, w/o Prints // 5.34 ms ± 657 µs per loop (mean ± std. dev. of 50 runs, 10 loops each)

// Reaper Project, Test Project 2, w/o VST Search, w/o Prints // 260 ms ± 10 ms per loop (mean ± std. dev. of 50 runs, 10 loops each)
// Tokenizer, Test Project 2, w/o VST Search, w/o Prints // 67.7 ms ± 3.04 ms per loop (mean ± std. dev. of 50 runs, 10 loops each)

// Reaper Project, Test Project 3, w/o VST Search, w/o Prints // 30.2 ms ± 3.63 ms per loop (mean ± std. dev. of 50 runs, 10 loops each)s
// Tokenizer, Test Project 3, w/o VST Search, w/o Prints // 3.25 ms ± 379 µs per loop (mean ± std. dev. of 50 runs, 10 loops each)


What I mean when say bad abstractions?
- ENUMS for Node and Parameter types. They are impossible to maintain, as I have to somoehow chore up and reverse engineer all possible Types
- Using regexps for tokenization slows things down
- Parameter class. Quite unnecessary step.
- Very selly tokenization with flags, underutilized variables and some index amps we don't even use
- Utils and Decorators that we can definetely SKIP and not use, that will also boost the speed

What was right in the past implementation?
- Node is the primary container of tags data
- CMD Line arguments
- Fetching nodes
- Supressing outputs

Doubtful solutions:
- Separation of nodes and lines
- Treating first lines and inner lines/nodes separately

Because of all that, I will replace it with new Tokenizer solution, that does not reqire 're' module and is faster by 5x.