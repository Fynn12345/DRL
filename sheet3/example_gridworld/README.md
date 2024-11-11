# RL Gridworld

Beispiel für eine GridWorld (5 x 5 grid), wie in Sutton and Barto (2021) eingeführt. Ein Agent kann sich in dem Grid bewegen (in vier Richtungen). Bewegungen in die Begrenzungen hinein ergeben einen negativen Reward von -1, belassen den Agenten aber auf der Stelle. Dazu gibt es zwei Positionen am oberen Rand, von denen der Agent teleportiert wird und jeweils einen hohen positiven Reward erhält.

Die Gridworld-Umgebung ist angelehnt an die Implementierung in https://github.com/aurora1007/Reinforcement_Learning_Gridworld, aber vereinfacht.