# 📒 Mon carnet de bord

**Nom :** Aourak

**Prénom :** Yazid

**Adresse de mon site :** [https://______.pythonanywhere.com](https://yz78.pythonanywhere.com)

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Sur PythonAnywhere. GitHub stocke seulement le code, c'est le serveur de PythonAnywhere qui l'exécute et qui fabrique la page.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que le site est hébergé sur un serveur allumé en permanence et accessible depuis Internet. Mon voisin envoie une requête à ce serveur avec l'URL, et le serveur lui répond. Il n'a rien à installer, son navigateur suffit.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le nom de domaine est `www.google.com` (le serveur) et le chemin est `/maps` (la page demandée).

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Ça veut dire que le serveur n'a trouvé aucune route correspondant à l'adresse demandée (erreur 404). C'est le serveur qui l'envoie, pas mon navigateur.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Flask plante et le site affiche une erreur. L'Error log indique : `AssertionError: View function mapping is overwriting an existing endpoint function`.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie seulement du texte, avec des balises HTML. Le navigateur interprète ces balises et les transforme en une page mise en forme (titres, listes, images). 

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ `<h1>` sert à faire un titre principal, `<p>` un paragraphe, `<ul>` une liste à puces, et `<li>` un élément de cette liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ Parce que la balise `<img>` contient seulement l'adresse de l'image. Le navigateur va la télécharger lui-même depuis le serveur de Wikimedia, où elle est stockée, et l'affiche dans ma page.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Ça permet à chacun de travailler sur sa partie : le développeur s'occupe du code Python et le graphiste du HTML, sans se gêner ni casser le travail de l'autre. Le code est aussi plus lisible et plus facile à modifier.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Ils sont remplacés par le serveur, avant l'envoi. Je l'ai vérifié avec Ctrl + U : dans le code source reçu par le navigateur, on voit mon prénom et mon nom, plus aucun `{{ ... }}`.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML décrit la structure d'une page (titres, paragraphes, listes), tandis que le CSS décrit son apparence (couleurs, marges, polices, disposition).

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Au minimum deux fichiers : la page HTML et le fichier CSS. S'il y a d'autres ressources, le navigateur en télécharge aussi.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Parce que le navigateur garde parfois une ancienne version du CSS dans son cache. Le rechargement forcé oblige le navigateur à télécharger la nouvelle version.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. Le navigateur envoie la requête et le serveur envoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ Elle déclenche au moins la requête de la page HTML, puis celle du fichier CSS. Elle peut aussi demander un favicon si le navigateur le cherche.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ Le code `200` signifie que la requête a réussi. Le code `404` signifie que la ressource demandée n'a pas été trouvée, par exemple la petite icône de l'onglet.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Parce qu'elles ne modifient pas le fichier du serveur. Elles ne sont visibles que dans le navigateur local où on les a faites.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le nom du paramètre est `search_query` et sa valeur est `chat`.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Parce que le code essaie de convertir `bonjour` en entier avec `int(...)`, ce qui est impossible. Il faudrait vérifier que la valeur est bien un nombre avant de la convertir.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Parce qu'un utilisateur peut envoyer du HTML ou du JavaScript malveillant. Cela peut casser la page ou créer une faille de sécurité.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ En GET, les données apparaissent dans l'URL. En POST, les données sont envoyées dans le corps de la requête, donc elles ne sont pas visibles dans l'URL.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour une recherche, je choisirais GET car l'URL peut être partagée ou enregistrée. Pour une connexion avec mot de passe, je choisirais POST, car les données ne sont pas visibles dans l'URL.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Pas totalement. Elles ne sont pas visibles dans la barre d'adresse, mais elles peuvent apparaître dans les outils de développement, dans les logs ou si le site n'est pas bien sécurisé.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Les erreurs `4xx` viennent du client : il a demandé quelque chose de mauvais ou d'inexistant. Les erreurs `5xx` viennent du serveur : il y a un bug ou une panne.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur répond avec un code de redirection, puis le navigateur fait une nouvelle requête vers la nouvelle URL. C'est le navigateur qui fait la deuxième requête.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Un site peut rediriger une ancienne adresse vers une nouvelle page après une refonte, ou faire passer un utilisateur vers la page de connexion.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ L'adresse IP, le navigateur, et les langues préférées (Accept-Language).

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ Il permet de choisir la langue la plus adaptée à l'utilisateur, par exemple afficher la page en français si c'est sa langue préférée.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ On peut trouver une ligne qui demande une page introuvable, par exemple `/blabla`, avec le code `404` dans le journal d'accès.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ La navigation n'est pas vraiment anonyme. Même sans remplir un formulaire, le navigateur envoie des informations comme l'IP, le navigateur et les préférences.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Une page HTML est destinée aux humains et est affichée dans le navigateur. Une réponse JSON est destinée aux programmes et aux applications qui lisent des données structurées.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Sur le serveur, il y a le code Python qui fournit l'API `/api/heure`. Dans le navigateur, il y a le JavaScript qui récupère le JSON et met à jour l'heure sans recharger la page.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ Une application météo utilise une API pour échanger des données comme la ville, la température et la météo du jour.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Quand on tape une adresse, le navigateur envoie une requête au serveur. Le serveur recherche la bonne route, prépare une réponse (HTML, CSS, JSON, etc.) et l'envoie au navigateur. Le navigateur interprète cette réponse et affiche la page. C'est ainsi que le Web fonctionne.
