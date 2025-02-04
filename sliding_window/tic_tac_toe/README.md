[Problem Statement](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)

# Constraints


# Intuition/Problem Info
 - moves[i] = [row, col]
 - A Always plays first
 - Return will be "A", "B", "draw", or "pending"
 - How do I know if a player's won? 
   - Winning combo could be diagonal, horizontal, or vertical 
   - If it's horizontal, the row stays the same, while the col increases by 1 
   - If it's vertical, it's the reverse 
   - If it's diagonal, either the row and col incr by 1 together or the row and col decr by 1 together 
 - How often do I check for a win? 
 - A player has to move three times to win, so after player A moves 3 times, I can start checking for a winner 
 - Need an object for the players that tracks player 1 and player 2 
 - The object should count the number of moves? Or can there just be a tmp counter for the initial set 
 - if the index is an even number, then it's player A's move and vice versa 
 - There should be a board with spots that get filled with x's and o's???
