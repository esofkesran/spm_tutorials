# Partie A — Le DFS naïf : explorer « toutes les possibilités »

### Étape 1.
Implémentation faite.

### Étape 2.
C'est surtout des `a` qui s'affichent avec un nombre de plus en plus grand. Le
message d'erreur est : `RecursionError: maximum recursion depth exceeded`. La
dernière séquence a une longueur de 998 éléments.

### Étape 3.
La séquence `b` ne s'est pas du tout affiché. La raison est que le programme
essaye de brancher sur les `a` d'abord et il ne finit jamais de le faire jusqu'à
l'arrêt forcé causé par l'exception `RecursionError`.

### Étape 4.
Implémentation faite. Exécution faite avec `d_max = 2` et `d_max = 3`.

### Étape 5.
Fait.
