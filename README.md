# 🃏 Blackjack Game

A simple command-line Blackjack game written in Python. The game follows standard Blackjack rules where you play against the computer dealer.

## 🎮 How to Play
1. Run the script to start the game.
2. You and the computer are dealt two cards each.
3. The goal is to get as close to 21 as possible without going over.
4. Aces can be 1 or 11, and face cards are worth 10 points.
5. You can choose to draw another card (`y`) or stop (`n`).
6. The dealer (computer) must draw until reaching a score of 17 or higher.
7. The game announces the winner based on Blackjack rules.

## 🏆 Winning Conditions
- If you get **Blackjack (Ace + 10)**, you win instantly unless the dealer also has Blackjack.
- If your score is higher than the dealer's without exceeding 21, you win.
- If the dealer busts (goes over 21), you win.
- If your score exceeds 21, you lose.

## ⚙️ Installation & Running
1. Clone the repository:
   ```bash
   git clone https://github.com/BekaluEshete/blackjack-game.git
   cd blackjack
