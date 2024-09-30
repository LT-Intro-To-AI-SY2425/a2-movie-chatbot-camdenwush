# Assignment 2 - Write UP

## Description
This assignment is about learning and applying the while loop and iterating through multiple lists at a time.  We also will discuss how we match things in chatbots in order to extract what a user is trying to find.  Next assignment we will work with data bases and how we can extract information from them.

## What to complete
1. Go through the notes.py file w/ Mr. Berg
2. Complete `a2.py`, Mr. Berg will walk everyone through the process
3. Make sure you pass all asserts in `a2.py`
4. Complete the reflection problems below
5. Push your code to github for grading

## Reflection Questions
1. What was difficult for you while completing the match function?
Wildcards are annoying because when its not the final position you need to have a match for before and behind which is super annoying


2. Explain how you could use the match function for extracting information from a movie database.

If you have a list of movies represented by tags

```
["super cool movie", "2024", "catagory", "big name"],
["super cool movie2", "2023", "money", "da"],
["super cool movie3", "2024", "catagory", "big name"]

```
then you could search for all movies in 2024 

```py
pattern = ["%", "2024", "%", "%"]
```