# Analyse des résultats de la régression logistique :

## TOUR 1 : 

Meilleur score CV: 0.9887
Accuracy sur test: 0.9910

```
  model__C: 10
  model__class_weight: None
  model__penalty: l1
  model__solver: saga
```


### TOUR 2 : 

Meilleur score CV: 0.9900
Accuracy sur test: 0.9930

Les meilleurs paramètres au premier tour étaient : 
   ```
    model__C: 100
    model__class_weight: None
    model__penalty: l1
    model__solver: saga
   ```

### TOUR 3 : 

Meilleur score CV: 0.9900
Accuracy sur test: 0.9930

```
  model__C: 80
  model__class_weight: None
  model__penalty: l1
  model__solver: saga
```

### TOUR 4 : 

Meilleur score CV: 0.9900
Accuracy sur test: 0.9930

```
  model__C: 70
  model__class_weight: None
  model__penalty: l1
  model__solver: saga
```


### Avec SCORING = 'accuracy'



### Avec SCORING = 'recall_macro'

Comparaison finale :
- Régression logistique: 0.9745
- Arbre de décision: 1.0000
- SVM: 0.9915

### Avec SCORING = 'f1_macro'
Comparaison finale :
- Régression logistique: 0.9894
- Arbre de décision: 1.0000
- SVM: 0.9915