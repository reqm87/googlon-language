# The Googlon Language

## Coding Challenge

Archaeologists found a scroll containing texts in the ancient and mysterious Googlon language.

After many years of study, linguists have learned some of the fundamental characteristics of this language:

### Letter Classification

Googlon letters are classified in two groups: the letters **u, d, x, s, m, p, f** are called **"foo letters"** while the other letters are called **"bar letters"**.

### Prepositions

The linguists have discovered that in the Googlon language, the prepositions are the words of exactly 6 letters which end in a foo letter and do not contain the letter **u**.

### Verbs

Another interesting fact discovered by linguists is that, in the Googlon language, verbs are words of 6 letters or more that end in a bar letter. Furthermore, if a verb starts in a bar letter, then the verb is inflected in its subjunctive form.

### Lexicographical Order

In Googlon, like in our system, words are always ordered lexicographically, but the challenge is that the order of the letters in the Googlon alphabet is different from ours. Their alphabet, in order, is: **sxocqnmwpfyheljrdgui**.

### Numbers

Not that words aren't fun, but one could ask: how do Googlons represent the numbers? Well, in Googlon, words also represent numbers given in base 20, where each letter is a digit. The digits are ordered from the least significant to the most significant, which is the opposite of our system. That is, the leftmost digit is the unit, the second digit is worth 20, the third one is worth 400, and so on and so forth. The values of the letters are given by the order they appear in the Googlon alphabet (which, as we saw, is ordered differently from our alphabet). That is, the first letter of the Googlon alphabet represents the digit 0, the second letter represents the digit 1, and the last one represents the digit 19.

As an example, the Googlon word gxjrc represents the number 605637.

Googlons consider a number to be pretty if it satisfies all of the following properties:

**-** It is greater than or equal to 81827
**-** It is divisible by 3

### The Challenge

Write a program (in any language) that answers the following questions to a given Googlon text:

**1)** How many prepositions are there in the text?
**2)** How many verbs are there in the text?
**3)** How many of those verbs in the text are in the subjunctive form?
**4)** Generate a vocabulary list with distinct words ordered Googlon's alphabetical order.
**5)** How many distinct pretty numbers are in the text?

Use the test cases to validate your algorithm.

## Solution

### Requirements/Dependencies

+ git version 2.21.0

Installation: https://git-scm.com/downloads

### Clone Repository and Run the Application

+ Clone the solution repository.

+ To execute the application, please run the following command:

```bash
python googlon.py
```
