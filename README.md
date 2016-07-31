# post-analyzer
Python blog post analyzer for internetpro.me

As announced in [this blog post](https://illegalpornography.me/programming/python/nonfiction/2016/06/01/post-checker-one.html), this is a work in progress for linting blog posts before they're posted. Expect updates as more features are added.

postcheck.py reads from standard input and produces output based on its command line options. Currently, only one option is supported.

postcheck is designed to deal with Jekyll posts, and skips the header before doing its calculations.

-w (words)
==========
Without the -w option, postcheck.py will print the top 5 most commonly used words and how many times each was used. 
The -w option on its own prints all words and corresponding frequencies. 
The -w _n_ option with a number will print the top n most commonly used words, or all of them if n is greater than the number of unique words in the post.

-f, --filter
============
Without the -f or --filter options, postcheck.py will remove the following common English words from the post before preforming word analysis:
the, be, to, of, and, a, in, that, it
The -f and --filter options are identical.
Specify any number of words after the option to be ignored. For example:
-f if and but
excludes "if", "and", and "but" from -w word analysis. Arguments are case insensitive. 

