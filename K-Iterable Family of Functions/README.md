# K-Iterable Family of Functions:

Let `F(iₓ, n)` be the K - Iterable Family of Functions by which the following rules apply: 

Let `fᴋ(n)` be an entry in the K-iterable Family of Functions where:
  - `K` is the iterator
  - `n` is the entry in the function

Let `fᴋ(n)` be entries in the K-Iterable Family of Functions where:
  - `f₁(n) = n(↑^n)n` where `↑` is Knuth's Up Arrow Notation
  - `fᴋ(n) = fᴋ-1(n)(↑^n)fᴋ-1(n)` for all `K ∈ (N > 1)`
 
Let `i` be an iterator array of the form `{a₁, a₂, a₃, ... aᵤ}` where we evaluate the following:
  - Begin at the 2nd element of the array
  - Evaluate `a₂` where `a₂ = fₐ₁(n)`
  - Delete the 1st element (`a₂` becomes `a₁`, `a₃` becomes `a₂`, etc.)
  - Repeat until there's 1 element left in the array (this element is hereby known as `U`)
  - Evaluate `fᵤ(n)`

Let `iₓ` be the iterator array `i` with `x` terms. 

Using this we can construct a function that lives within the family of functions that grows very fast, even for relatively small `x` and `n`.

Example of an extremely large value: `F(i₂₅₀₀₀₀, 250,000)`.

# Diagonalization of K-Iterables (DoKI):

Our example of an extremely large value above is one of significance. The significance being that both the value of x and n are the same. We are able to apply this principle to create a function that grows larger faster than all of the functions within the K-Iterable Family of Functions for all `x` and `n`. This process is known as ***diagonalization***.

We can represent diagonalization in a more literal sense by constructing a table of values:
DoKI|n = 1|n = 2|n = 3|...
:-:|:-:|:-:|:-:|:-:
k = 1|f₁(1)|f₁(2)|f₁(3)|...
k = 2|f₂(1)|f₂(2)|f₂(3)|...
k = 3|f₃(1)|f₃(2)|f₃(3)|...
...|...|...|...|...

The fastest growing "path" that we can take using this table is along the diagonal, starting with `f₁(1)`, continuing with `f₂(2)`, `f₃(3)`, and so on:
DoKI|n = 1|n = 2|n = 3|...
:-:|:-:|:-:|:-:|:-:
k = 1|`f₁(1)`|~~f₁(2)~~|~~f₁(3~~)|...
k = 2|~~f₂(1)~~|`f₂(2)`|~~f₂(3)~~|...
k = 3|~~f₃(1)~~|~~f₃(2)~~|`f₃(3)`|...
...|...|...|...|...

With this we can let `DoKI(n) = F(iₙ, n)` within the K-Iterable Family of Functions.

# Iterating on Diagonization:

Let `DoKIₖ(n)` be `DoKI(DoKI( ... n) ...)` repeated `k` times. With this we can construct the same diagonalization table as before, instead using `DoKIₖ(n)` in place of `fₖ(1)`:
DoKI|n = 1|n = 2|n = 3|...
:-:|:-:|:-:|:-:|:-:
k = 1|`DoKI₁(1)`|~~DoKI₁(2)~~|~~DoKI₁(3~~)|...
k = 2|~~DoKI₂(1)~~|`DoKI₂(2)`|~~DoKI₂(3)~~|...
k = 3|~~DoKI₃(1)~~|~~DoKI₃(2)~~|`DoKI₃(3)`|...
...|...|...|...|...

We have created a Diagonalized Diagonalization function, `DoKIₙ(n)`. Going even beyond this, we can continue building upon these functions, by repeating diagonalization.

# Diagonalized Diagonalization:

## Important Note:
k is a superscript and not a subscript. The function constructs diagonalizations, which in turn create iterations, so there is no need to iterate this fuction. 

Let `DDᵏ(n)` be a function of constructed diagonlizations where the following applies:
- `DD¹(n)` is simply `DoKIₙ(n)`.
- `DDᵏ(n)` is a equal to the constructed diagonalization of `DDᵏ⁻¹(n)` for all `k ∈ (N > 1)` where we evaluate the following:
  - Begin with `DDᵏ(n)`.
  - Create a diagonalized version of the function `DDᵏₙ(n)`.
  - Iterate on the function to create `DDᵏ(DDᵏ( ... (n) ... )` repeated `n times`.
  - Repeat these steps for `k-1` to evaluate `DDᵏ⁻¹(DDᵏ⁻¹( ... (n) ... )` repeated `n^2 times`.
  - Arrive at the final diagonalization `DD¹(DD¹( ... (n) ... )` repeated `n^k times`.

We are able to surrepticiously diagonalize this function by simply finding and replacing `k` with `n`. With this we have a new function, call it `DDω(n)`.

This is an extremely fast growing, single argument function. An example of an extremely large value would be `DDω(10↑↑10)`.


