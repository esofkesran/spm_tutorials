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


# Partie C — Sous-séquences, plongements, support, préfixes et suffixes

### Étape 1.
- `ac` oui, `ca` oui, `cb` non, `aa` oui, `abc` oui.
- Avec une sous-chaîne, il aurait été nécessaire de suivre l'ordre des éléments
de manière contigue.

### Étape 2.
- Les plongements de `ac` dans `s` : (0, 2), (0, 4), (3, 4).
- Les plongements de `abc` dans `s` : (0, 1, 2), (0, 1, 4).
- ??

### Étape 3.
Implémentation faite.

### Étape 4.
Le plongement glouton choisit toujours la première occurrence possible de
chaque élément. Par conséquent, son dernier indice est également le plus petit
possible parmi tous les plongements.

### Étape 5.
Implémentation faite. Calcul fait. Vérification faite.

```
support( ['a'] ) = 5
support( ['d'] ) = 1
support( ['a', 'b'] ) = 4
support( ['b', 'a'] ) = 3
support( ['c', 'a'] ) = 2
support( ['a', 'b', 'c'] ) = 3
support( ['a', 'a'] ) = 1
```

### Étape 6.
- `support(ab) = 4` et `support(abc) = 3`. Alors `support(ab) > support(abc)`.
- `support(b) = 5` et `support(ba) = 3`. Donc `support(b) > support(ba)`.
- De manière générale, pour `t ⊑ t′`, on a : `support(t) >= support(t′)`. C'est
  la propriété d'anti-monotonie.
- Si une séquence ne possède pas un support suffisant, aucune de ses extensions
  ne pourra avoir un support suffisant non plus. On peut donc arrêter
  l'exploration de cette branche du DFS (en quelque sorte la couper) sans
  examiner toutes ses extensions.

### Étape 7.
`s = abcac`

- **Préfixes** : Un préfixe contient les k premiers éléments de la séquence.
  1. []
  2. [a]
  3. [a, b]
  4. [a, b, c]
  5. [a, b, c, a]
  6. [a, b, c, a, c]
- **Suffixes** : Un suffixe contient les éléments restants à partir d'une position donnée.
  1. [a, b, c, a, c]
  2. [b, c, a, c]
  3. [c, a, c]
  4. [a, c]
  5. [c]
  6. []
- **Projections** : `s|a = bcac`, `s|ab = cac`, `s|ac = ac`, `s|ca = c`.
