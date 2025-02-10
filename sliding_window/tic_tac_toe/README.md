[Problem Statement](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)

# Constraints

 - 1 <= moves.length <= 9
 - moves[i].length == 2
 - 0 <= rowi, coli <= 2
 - There are no repeated elements on moves.
 - moves follow the rules of tic-tac-toe

# Intuition/Problem Info
- A Always plays first - even number indices
- moves[i] = [row, col]
- The len of the input moves is the number of spots that are taken on the board
- if len(moves) < 4:
     - return "pending"
 - Return will be "A", "B", "draw", or "pending"
   - Draw means all 9 spots are taken? Or all possible wins are blocked
   - Pending means there's still spots to move on the board
 - How do I know if a player's won? 
   - Winning combo could be diagonal, horizontal, or vertical 
   - If it's horizontal, the row stays the same, while the col increases by 1 
   - If it's vertical, it's the reverse 
   - If it's diagonal, either the row and col incr by 1 together or the row and col decr by 1 together 
 - How often do I check for a win? 
   - A player has to move three times to win, so after player A moves 3 times, I can start checking for a winner 
 - Need an object for the players that tracks player 1 and player 2 ?
 - The object should count the number of moves? Or can there just be a tmp counter for the initial set 
 - if the index is an even number, then it's player A's move and vice versa 
 - There should be a board with spots that get filled with x's and o's???

 - I could potentially split the problem in 2 by searching for a winner for player 1 and then for a winner for player 2
   - if len(moves) < 4: return "pending"
   - This way, there would be a two sliding window problem, the first window starts at 4 and goes to the length of the moves array, it would increase by 2
     - Check for a winner by checking the previous indexes for player A which is the current window to 0
   - if len(moves) < 5: return "pending"
   - The second window starts at 5 and goes to the length of the list, and increases by 2
     - Check for a winner by checking the previous indexes for player B which is the current window to 1, decr by 2
   - return winner if it exists or return draw
 - If I use the sliding window technique:
   - The window size is variable to check for a winner, because if a player doesn't win in 3 moves, their fourth move may win based on their last 3 or two moves
   - What if I sorted the data differently, by like ascending order? w/row preference? that sounds like too much tho
