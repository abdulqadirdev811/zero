# Problem Solving Basic  

It contains two Problems.
* Netflix Feature: Group Similar Titles (hash maps)  
* Google Calendar Feature: Find Meeting Rooms

## Netflix Feature: Group Similar Titles (hash maps)


[Source Link](https://www.educative.io/blog/crack-coding-interview-real-world-problems#netflix)


### Description  

Netflix is one of the biggest video streaming platforms out there. The Netflix engineering team is always looking for new ways to display content. For this first problem, imagine you’re a developer on these teams.  

**Task**: Our task here is to improve search results by enabling users to see relevant search results without being hindered by typos, which we are calling the “Group Similar Titles” feature.  



First, we need to determine how to individually group any character combination for a given title. Let’s imagine that our library has the following titles: "duel", "dule", "speed", "spede", "deul", "cars". You are tasked to design a functionality so that if a user misspells a word (for example speed as spede), they will still be shown the correct title.

First, we need to split our titles into sets of words so that the words in a set are anagrams. We have three sets: {"duel", "dule", "deul"},{"speed", "spede"}, and {"cars"}. The search results should include all members of the set that the string is found in.  



## Twitter Feature: Add Likes (strings)

[Source 1 URL](https://www.educative.io/blog/crack-coding-interview-real-world-problems#where)



### Description

Twitter is a popular social media platform. Imagine you’re a Twitter developer, and your team must create an API that calculates the number of likes on a given person’s Tweets. 
The data is already extracted and stored in a simple text file for you. All of the values should remain strings and cannot be converted into integers. We must do digit-by-digit addition due these restrictions. 
  
**Task:** Create an API that calculates the total number of likes on a person’s Tweets. Create a module that takes two numbers and returns the sum of the numbers.
