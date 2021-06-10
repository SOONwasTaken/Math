# K-Iterable Family of Functions:

Let F(iₓ, n) be the K - Iterable Family of Functions by which the following rules apply: 

Let fᴋ(n) be an entry in the K-iterable Family of Functions where:
  - K is the iterator
  - n is the entry in the function

Let fᴋ(n) be entries in the K-Iterable Family of Functions where:
  - f₁(n) = n(↑^n)n where ↑ is Knuth's Up Arrow Notation
  - fᴋ(n) = fᴋ-1(n)(↑^n)fᴋ-1(n) for all K ∈ N > 1
 
Let i be an iterator array of the form {a₁, a₂, a₃, ... aᵤ} where:
  - Begin at the 2nd element of the array
  - Evaluate a₂ where a₂ = fₐ₁(n)
  - Delete the 1st element (a₂ becomes a₁, a₃ becomes a₂, etc.)
  - Repeat until there's 1 element left in the array (this element is hereby known as U)
  - Evaluate fᴋ(n) with K = U

Let iₓ be the iterator array i with x terms. 

Using this we can construct a function that lives within the family of functions that grows very fast, even for relatively small x and n.

Example of an extremely large value: F(i₂₅₀₀₀₀, 250,000).
