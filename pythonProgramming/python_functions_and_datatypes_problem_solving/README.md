## Google Calendar Feature: Find Meeting Rooms

[SOURCE URL](https://www.educative.io/blog/crack-coding-interview-real-world-problems#netflix)
**Description :** we are given a some meeting times. We need to find a way to identify the number of meeting rooms needed to schedule them all. Each meeting will contain positive integers for a startTime and an endTime.

Our meeting times can be listed as follows: {{2, 8}, {3, 4}, {3, 9}, {5, 11}, {8, 20}, {11, 15}}. We could schedule each meeting in a separate room, but we want to use the minimum amount of rooms. We observe that three meetings overlap: {2, 8}, {3, 4}, and {3, 9}. Therefore, at least these three will require separate rooms.

**TASK :** Task: Your goal is to create a functionality for scheduling meetings. You need to determine and block the minimum number of meeting rooms for these meetings.

## Two Pointers Technique
 Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

**Time Complexity**  
    * Naïve Approach using loops :  O(n2)  
    * Optimal approach using two pointer algorithm :O(n log n)   

**TASK :** we have to find a pair from a list  whose sum is equal to specific vale X and return the pair and X.

