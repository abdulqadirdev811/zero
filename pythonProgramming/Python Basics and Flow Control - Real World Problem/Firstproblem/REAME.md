# Netflix Feature: Group Similar Titles (hash maps)


[Source Link](https://www.educative.io/blog/crack-coding-interview-real-world-problems#netflix)


Netflix is one of the biggest video streaming platforms out there. The Netflix engineering team is always looking for new ways to display content. For this first problem, imagine you’re a developer on these teams.  

## Task: 
Our task here is to improve search results by enabling users to see relevant search results without being hindered by typos, which we are calling the “Group Similar Titles” feature.  



First, we need to determine how to individually group any character combination for a given title. Let’s imagine that our library has the following titles: "duel", "dule", "speed", "spede", "deul", "cars". You are tasked to design a functionality so that if a user misspells a word (for example speed as spede), they will still be shown the correct title.

First, we need to split our titles into sets of words so that the words in a set are anagrams. We have three sets: {"duel", "dule", "deul"},{"speed", "spede"}, and {"cars"}. The search results should include all members of the set that the string is found in.  