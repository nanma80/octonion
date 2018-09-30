# Non-associative "twisty" puzzles

TL;DR: We have a proof-of-concept non-associative puzzle based on octonions in Python [here](https://github.com/nanma80/octonion).

## Motivation

One could argue the defining property of twisty puzzles that makes them so interesting is their non-commutativity. Given two twists a and b, generally ab ≠ ba.¹

A few months ago, Quanta magazine published [a popular article](https://www.quantamagazine.org/the-octonion-math-that-could-underpin-physics-20180720/) about the "octonions" and their potential application to particle physics. Octonions are not only non-commutative, but non-associative as well. Given 3 octonions a, b, and c, it is possible that (ab)c ≠ a(bc). Note that the Rubik's cube is associative. (ab)c = a(bc) for any 3 twists.

The Quanta article sparked the idea of trying to make a twisty puzzle that is also non-associative. Where would this lead?

¹ A twisty puzzle having only commutative twists is possible but will be easier since you can apply twists in any order to solve. The [vertex turning 600-cell with trivial tips](https://groups.yahoo.com/neo/groups/4D_Cubing/conversations/messages/1752) is one example of a commutative puzzle that still takes effort.

## Non-associative puzzles can’t be permutation puzzles, and visa versa!

We are used to studying twisty puzzles with [group theory](https://en.wikipedia.org/wiki/Group_theory). The state-space of Rubik’s cube [forms a mathematical group](https://en.wikipedia.org/wiki/Rubik%27s_Cube_group) and twists move us around this space of permutations. However, groups are associative, so the state-space of non-associative puzzles can not form a group.

Conversely, any puzzle that permutes stickers with each twist necessarily satisfies the axioms of a [permutation group](https://en.wikipedia.org/wiki/Permutation_group), and is therefore associative. This means a permutation puzzle can’t be non-associative.

In short, "twisty" should be left in quotes. Our “twists” are generators, but they are not familiar permutations of stickers.

## Commutators and Associators

Because of non-commutativity, we use commutators to solve twisty puzzles. The commutator is given by a⁻¹b⁻¹ab = (ba)⁻¹ab and the analogue for non-associativity is the associator, (a(bc))⁻¹((ab)c). We are still exploring how this might apply to solution strategies.

## Octonions in brief

There are 4 magical number systems known as the normed division algebras: the reals, complex numbers, quaternions, and octonions. Each number system is twice the dimension of the previous. While climbing the ladder of number systems, we lose a property at every step.

Number System | Dimension | Properties
------------ | ------------- | -------------
[real numbers](https://en.wikipedia.org/wiki/Real_number) | 1 | divisible, associative, commutative, orderable
[complex numbers](https://en.wikipedia.org/wiki/Complex_number) | 2 | divisible, associative, commutative
[quaternions](https://en.wikipedia.org/wiki/Quaternion) | 4 | divisible, associative
[octonions](https://en.wikipedia.org/wiki/Octonion) | 8 | divisible

You can continue to dimension 16 with the [sedenions](https://en.wikipedia.org/wiki/Sedenion), but then even the property of divisibility  is lost and the number system is no longer a division algebra.

If you are familiar with complex numbers, which have the form a + bi with a, b real and i = √-1, quaternions and octonions won’t feel completely alien. They look like this.

quaternions: a + bi + cj + dk
octonions: x₀ + x₁e₁ + x₂e₂ + x₃e₃ + x₄e₄ + x₅e₅ + x₆e₆ + x₇e₇

The coefficients are real numbers. For quaternions, i, j, and k are similar to the i of complex numbers. For the octonions, the seven eᵢ with i ≠ 0 play this role. An octonion can also be denoted as a length-8 vector using the 8 coefficients. Addition, subtraction, multiplication, division, inverse, norm, and conjugate can be defined for octonions, in a way similar to complex numbers.

There is a wealth of information online about the octonions. We recommend [this resource page](http://math.ucr.edu/home/baez/octonions/) by John Baez, as well as his paper, “[The Octonions](http://math.ucr.edu/home/baez/octonions/octonions.pdf)”, especially the beginning sections.² 

² Note that the multiplication tables used by Baez and Wikipedia are different, although equivalent by renaming bases. In our implementation, we used the Wikipedia convention.

## Unit norm integral octonions

[Integral octonions](https://en.wikipedia.org/wiki/Octonion#Integral_octonions) are a special subset of octonions. They are octonions whose coordinates are all integers, or all half-integers satisfying certain properties. There are 240 integral octonions with the minimum nonzero norm, which is 1 (unit norm). The simplest example is the identity octonion (1, 0, 0, 0, 0, 0, 0, 0), aka, 1. The set of 240 unit norm integral octonions is closed under octonion multiplication. Therefore they form a small playground. As long as we only use multiplication between them, we never fall out of it.

We can start from three generators:
  * i = (0, 1, 0, 0, 0, 0, 0, 0),
  * j = (0, 0, 1, 0, 0, 0, 0, 0),
  * h = (0, 1, 1, 1, 1, 0, 0, 0)/2,
and use multiplication to generate all the 240 unit norm integral octonions. Reference: section 3 of [this paper](https://arxiv.org/abs/math/0701692).

Here are some quick facts about the unit norm integral octonions. The 240 octonions, if expressed as 8-dimensional vectors, are the vertices of the [4₂₁ polytope](https://en.wikipedia.org/wiki/4_21_polytope), a semi-regular 8-polytope. It admits the E8 symmetry. The algebraic structure of these 240 octonions is no longer a group because it lacks associativity. It is a “loop”, which is group minus associativity. In addition, since it has a weaker version of associativity called Moufang properties, it is a [Moufang loop](https://en.wikipedia.org/wiki/Moufang_loop). If you are interested in reading more about integral octonions, we recommend [another of John Baez's pages](http://math.ucr.edu/home/baez/octonions/integers/).

## Integral octonions puzzle

Based on the set of 240 unit norm integral octonions described above, we constructed a non-associative puzzle.

To illustrate the idea, let’s review the Rubik’s Cube as an analogy. The group of all states of the Rubik’s Cube is generated by generators U, D, L, R, F, B, with the group operation of concatenating moves. We randomly choose a state from the group as the scramble or initial state. In each step, we apply any generator individually, or in general, any sequence of generators as an expression. The expression is applied to the right side of the scramble. The goal of the puzzle is to get the state to the identity or solved state.

Here, we randomly choose a unit norm integral octonion from 240 possibilities as the scramble or initial state. In each step, we enter an expression of generators: i, j, h, using the octonion multiplication *, with parenthesis (). For example, (h * (i * j)) can be an input expression. Just h itself is also an expression. We evaluate the input expression and right-multiply it to the old state:
(the new state) = (the old state) * (input expression).
The goal is to get the state to the identity octonion (1, 0, 0, 0, 0, 0, 0, 0).
 
The reason why we allow entering an expression of i, j, h rather than applying them individually is not just for convenience like macros in the Rubik’s Cube. It’s because of non-associativity. Since (state * (a * b)) may not equal ((state * a) * b), applying the expression (a * b) as input can be different from applying a and then applying b. If we only enter i,  j or h individually in each step, we have only a 20% chance (48 out of 240 initial states) of solving it. For this reason, we highly recommend trying at least i * h if you feel stuck. By doing so, you are embracing the essence of non-associativity.

To get a sense about how hard this puzzle is, and to try out the non-associative solving experience, Nan implemented it in Python as a proof of concept. We found it nontrivial and interesting, even when the space is as small as 240 elements. Here’s how you can also try it:
1. Install Python, either 2.* or 3.*.
1. Install numpy.
1. Clone my repo: https://github.com/nanma80/octonion
1. Run puzzle_python2.py or puzzle_python3.py depending on the Python version you installed.
1. Follow the instructions to solve it. The instruction is as same as the description above.
1. Solve it, or enter q to quit.

About the solving experience: We think the puzzle is hard, partly because the h move is unintuitive. We observed that
* i, j, or h applied individually is always a 4-cycle.
* applying (i * j) * h is a 3-cycle.
* applying (j * i) * h is a 6-cycle.
* (i * j) * h is different from i * (j * h), verifying non-associativity among three generators.
If you know any method to illustrate octonion multiplication, please let us know and we can improve this puzzle.

We are also working on non-associative puzzles based on loops with more states and more “intuitive” moves. We are experimenting something based on a 2x2x2 cube and a modified construction of “M(G,2)” [here](https://en.wikipedia.org/wiki/Moufang_loop#Examples). We don’t have a prototype yet but may discuss it later.

============

This is a long introduction. We only have some ideas and a proof of concept. We'd like to make more polished non-associative puzzles.
* Do you know a good way to illustrate octonions, or integral octonions?
* Can you think of other non-associative rules for puzzles?
Please leave comments or suggestions!

Nan and Roice
