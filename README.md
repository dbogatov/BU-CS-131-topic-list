## CS 131 Spring 2018 - List of topics

See [lecture recordings here](https://echo360.org/section/801af970-0582-439d-b5cd-74097af867e0/public). 
Warning: they are low-resolution and not great audio quality, so they do not substitute for coming to lecture,
but they can be helpful is you must miss a class.

* Jan 23
    * Welcome to CS 131
    * Propositional logic
        * Propositions and logical equivalence
        * Evaluating compound propositions
        * Conditional statements
        * Logical equivalence
        * Laws of propositional logic

* Jan 25
    * Boolean algebra
        * Intro
        * Boolean functions
        * CNF / DNF

 
* Jan 30
    * Boolean algebra
        * Functional completeness
        * Boolean satisfiability

* Feb 1
    * Predicates and first order logic
        * Predicates and quantifiers
        * Quantified statements

* Feb 6
    * Predicates and first order logic
        * Nested quantifiers (two chapters)
        * Rules of inference with quantifiers

* Feb 8
    * Sets
        * Sets and subsets
        * Sets of sets
        * Union and intersection
        * More set operations
        * Set identities
        * Cartesian products
        * Partitions

* Feb 13
	* [See lecture notes](./lecture-notes/02-13-proof.pdf)
	* Functions (whole zyBooks chapter)

* Feb 15
    * Relations (whole zyBooks chapter)

* Feb 20
    * Monday schedule

* Feb 22
    * Proofs (whole zyBooks chapter)

* Feb 27
    * More on proofs
        * More on proof by cases
        * Euclid algoritm
            * GCD
            * Theorem about GCD (why Euclidian algorithm return GCD) and its proof
            * Theorem: GCD of two numbers over their GCD is 1 (and its proof)

* Mar 1
    * Writing GCD formal defintion in a form of conjunction of three statememnts
    * Theorem: any rational number can be written as x over y s.t. GCD(x,y)=1 (and its proof)
    * Applying GCD to rational numbers (hint: multiply by denominators)
    * Proof that square root of 2 is irrational
    * Theorem: any integer greater than 1 is divisible a prime (and its proof)
    * Theorem: there are infinitely many primes (and its proof)

* Mar 20
    * Halting problem
        * [See lecture notes](./lecture-notes/halting-problem.pdf)

* Mar 27
    * Geometric series
    * Inductive proofs that are not sums
    * Graphs (some basic definitions)
    * "All horses are the same color"

* Mar 29
    * Sum of infinite series (r < 1)
    * False proofs of horses color
    * Fiboncci sequence
    * Analusis of Euclid's algorithm (see [notes](./lecture-notes/euclids-algorithm.pdf))

* April 3
    * Loop invariants
        * [Find minimum algorithm](./lecture-notes/find-min.py)
        * [Euclids algorithm](./lecture-notes/euclid.py)
    * Pre / post conditions as ways to reason about program correctness

* April 5
    * Structural induction
        * General (non-binary) trees
        * Boolean formulas
    * Proof via structural induction
        * In any tree the number of edges is one smaller than the number of nodes
        * In any formula number of opening and closing patterns matches
    * [Two recursive algorithms](./lecture-notes/april-5.py)

* April 17 / 19
    * Binomial coefficients
    * Relation between inclusion / exclusion and identity
    * Binomial distribution

* April 20
    * Binomial coefficients
    * Pascal's triangle
    * Binomial recurrence with code
    * Probability basics: sample spaces, outcomes, events, etc

* April 25
    * Bernoulli trials and binomial distribution
    * [Visualization](https://www.youtube.com/watch?v=03tx4v0i7MA)
    * **Not in the book**
        * 95% of the binomial distribution lies within $`\sqrt{n}`$ of the average
        * 99.7% of the binomial distribution lies within $`1.5 \sqrt{n}`$ of the average.
        * Good visualizers:
            * [this](https://homepage.divms.uiowa.edu/~mbognar/applets/bin.html)
            * [this](http://www.wolframalpha.com/widgets/view.jsp?id=78baf4f3a070cc5b9b226664d2ce80ec)

* Thu Apr 27: 
    * **Not in the book**
        * If you try to estimate the bias of a coin (for example, in public polling or in Monte Carlo simulation) by doing $`n`$ independent samples, your answer will very likely be within about $`\frac{1}{\sqrt{n}}`$ of the correct answer.
        So need $`n = 400`$ samples to get to within 5%, $`n = 1112`$ to get within 3%, $`n = 10000`$ to get within 1%.
    * Conditional probability and independence
    * Random variables and expectations
    