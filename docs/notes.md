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


# Partie B — Combien de possibilités ? Théorie et pratique

### Étape 1.
- Il y a `m^k` séquences de longueur `k`. Cela est dû au fait que à chaque fois
qu'on veut passer des séquences de longueur `l` à des séquences de longueur
`l + 1`, on combine chacune des séquences avec chacun des éléments de
l'alphabet. Par conséquent le nombre de séquences avec une longueur `l + 1` est
`m` fois le nombre de séquences avec une longueur `l`.
- `N(m, d) = somme de l=1 à l=d de m^l`
- `N(3, 2) = 12`, `N(3, 3) = 39`, `N(3, 10) = 88572`.
- Quand `d` devient grand, le rapport `N(m, d+1) / N(m, d)` tend vers la valeur
de `m`. Cela implique que, lorsque l’on augmente la profondeur de `1`, le temps est multiplié par `m` environ.

### Étape 2.
Implémentation faite. Vérification faite.

### Étape 3.
Fait.

### Étape 4.
Les courbes sont presque linéaires.

### Étape 5.
- Le temps est presque proportionnelle au nombre de séquence, surtout quand le 
nombre de séquence devient élevé.
- De manière générale, le temps d'exécution de la fonction `generer` est
légèrement supérieur à celui de la fonction `compter`.
