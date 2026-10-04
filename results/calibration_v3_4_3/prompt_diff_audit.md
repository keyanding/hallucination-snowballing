# Prompt invariance and counterfactual diff audit

P1 is byte-identical to its original v3.4.2 prompt and rendered chat. Only the four numbered answer-option lines change. Original name-record order is retained as the canonical evidence order; the candidate list is not relocated to the preferred example layout because that would introduce another intervention.

## dev-04/EASY

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `201d1047dfe1485ac9c476af89282c8a69c826b6fc0a381da4cb19e87c732e2b`. Gold identity: Leopoldo Torre Nilsson. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Armando Robles Godoy
+2. Leopoldo Torre Nilsson
+3. Rahul Rawail
+4. Tinnu Anand
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Tinnu Anand
+4. Armando Robles Godoy
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Rahul Rawail
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
 
```

## dev-07/EASY

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `daeeb01b32bfdad0ef0c4230af702358c30471e95a1135903a31d241008d5da5`. Gold identity: Walter Hugo Khouri. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. Walter Hugo Khouri
+2. Marcello Fondato
+3. James Goldstone
+4. León Klimovsky
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. Marcello Fondato
+2. James Goldstone
+3. León Klimovsky
+4. Walter Hugo Khouri
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. James Goldstone
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Marcello Fondato
 
```

## dev-05/EASY

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `4fe0e43a928563fae34eeddd2d038e0a938c1646bae06f42f3e6d8c7db5fc750`. Gold identity: Helmut Käutner. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Feng Xiaoning
+2. Helmut Käutner
+3. Fridrikh Ermler
+4. Rolf Schübel
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Helmut Käutner
+2. Fridrikh Ermler
+3. Rolf Schübel
+4. Feng Xiaoning
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Helmut Käutner
 
```

## dev-01/EASY

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `bcb4ac448961d956c8155e6656a43f7727f48561689ff86279be94eb2f07f080`. Gold identity: Walter Hugo Khouri. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Marcello Fondato
+2. James Goldstone
+3. Vojtěch Jasný
+4. Walter Hugo Khouri
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. James Goldstone
+2. Vojtěch Jasný
+3. Walter Hugo Khouri
+4. Marcello Fondato
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Walter Hugo Khouri
+3. Marcello Fondato
+4. James Goldstone
 
```

## dev-06/EASY

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `88f76f5195b0446c48428fb0b8d122e62f4469be3800379e5b428ad997bdaf4c`. Gold identity: Gu Changwei. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Rodrigo Grande
+2. Anil Das
+3. Gu Changwei
+4. Rolf Schübel
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Anil Das
+2. Gu Changwei
+3. Rolf Schübel
+4. Rodrigo Grande
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Gu Changwei
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
 
```

## dev-08/EASY

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `bc4f590d5b391aaaab4534dfc3210536c224130b8e4982723b02a73eab9a40b2`. Gold identity: Yuen Woo-ping. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Tinnu Anand
+2. Ildikó Enyedi
+3. Rahul Rawail
+4. Yuen Woo-ping
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Ildikó Enyedi
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Tinnu Anand
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Ildikó Enyedi
 
```

## dev-04/MID

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `b1df1f3b2a0258c80a413aab397009a13460d5fd1bad7a9884b581d14623de2f`. Gold identity: Leopoldo Torre Nilsson. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Armando Robles Godoy
+2. Leopoldo Torre Nilsson
+3. Rahul Rawail
+4. Tinnu Anand
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Tinnu Anand
+4. Armando Robles Godoy
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Rahul Rawail
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
 
```

## dev-07/MID

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `a017f1b754f0d30c9c0122c04b9469daef7d5cac1cd1405a49faa59302633d54`. Gold identity: Walter Hugo Khouri. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. Walter Hugo Khouri
+2. Marcello Fondato
+3. James Goldstone
+4. León Klimovsky
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. Marcello Fondato
+2. James Goldstone
+3. León Klimovsky
+4. Walter Hugo Khouri
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. James Goldstone
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Marcello Fondato
 
```

## dev-05/MID

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `7a5e4c9d7f5a101d5faf5b58e3dc502a7106d4a0bdd2de8707615ad94116f849`. Gold identity: Helmut Käutner. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Feng Xiaoning
+2. Helmut Käutner
+3. Fridrikh Ermler
+4. Rolf Schübel
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Helmut Käutner
+2. Fridrikh Ermler
+3. Rolf Schübel
+4. Feng Xiaoning
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Helmut Käutner
 
```

## dev-01/MID

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `2fdd8dc056e6feacb9d4727d5ae4a6cc820bc0033b380711a3709d327cce7b40`. Gold identity: Walter Hugo Khouri. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Marcello Fondato
+2. James Goldstone
+3. Vojtěch Jasný
+4. Walter Hugo Khouri
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. James Goldstone
+2. Vojtěch Jasný
+3. Walter Hugo Khouri
+4. Marcello Fondato
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Walter Hugo Khouri
+3. Marcello Fondato
+4. James Goldstone
 
```

## dev-06/MID

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `ec532e0cad83db165f20ea90d55dcdeb40a16ccaf76fa29ff8eec0e961ea7978`. Gold identity: Gu Changwei. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Rodrigo Grande
+2. Anil Das
+3. Gu Changwei
+4. Rolf Schübel
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Anil Das
+2. Gu Changwei
+3. Rolf Schübel
+4. Rodrigo Grande
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Gu Changwei
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
 
```

## dev-08/MID

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `489b64b4dce0a13f045ba3313e79ba4c9200971b4ed0a3492c1227924eb35fdc`. Gold identity: Yuen Woo-ping. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Tinnu Anand
+2. Ildikó Enyedi
+3. Rahul Rawail
+4. Yuen Woo-ping
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Ildikó Enyedi
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Tinnu Anand
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Ildikó Enyedi
 
```

## dev-04/HARD

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `815a8910734d8b85b7520075a0cd5cac008b01f61b6d112aac122cc471fe39ed`. Gold identity: Leopoldo Torre Nilsson. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Armando Robles Godoy
+2. Leopoldo Torre Nilsson
+3. Rahul Rawail
+4. Tinnu Anand
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Tinnu Anand
+4. Armando Robles Godoy
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Rahul Rawail
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
 
```

## dev-07/HARD

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `dd8477a2ac1fec0166fe80ab8782d73fa7d48f8502d8b977f1bf6eebdf625a80`. Gold identity: Walter Hugo Khouri. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. Walter Hugo Khouri
+2. Marcello Fondato
+3. James Goldstone
+4. León Klimovsky
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. Marcello Fondato
+2. James Goldstone
+3. León Klimovsky
+4. Walter Hugo Khouri
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. James Goldstone
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Marcello Fondato
 
```

## dev-05/HARD

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `16afd69e4ffb6b80cf1a9530b1ccc8a35dd1d9ab3aecf0ed5a99ef4ee2036a09`. Gold identity: Helmut Käutner. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Feng Xiaoning
+2. Helmut Käutner
+3. Fridrikh Ermler
+4. Rolf Schübel
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Helmut Käutner
+2. Fridrikh Ermler
+3. Rolf Schübel
+4. Feng Xiaoning
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Helmut Käutner
 
```

## dev-01/HARD

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `8b63ec3e72fdc609fd96d838c04a16d57d3e50dbec8b15759ea4fc1620490eac`. Gold identity: Walter Hugo Khouri. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Marcello Fondato
+2. James Goldstone
+3. Vojtěch Jasný
+4. Walter Hugo Khouri
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. James Goldstone
+2. Vojtěch Jasný
+3. Walter Hugo Khouri
+4. Marcello Fondato
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Walter Hugo Khouri
+3. Marcello Fondato
+4. James Goldstone
 
```

## dev-06/HARD

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `58b47ad1b3ea6e24975242fb168e659f51009e16148782dc7def57d964e55292`. Gold identity: Gu Changwei. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Rodrigo Grande
+2. Anil Das
+3. Gu Changwei
+4. Rolf Schübel
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Anil Das
+2. Gu Changwei
+3. Rolf Schübel
+4. Rodrigo Grande
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Gu Changwei
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
 
```

## dev-08/HARD

Fixed prefix SHA256: `d86d694c219da7ab683fbb5aa454aa12bc02d85508b807b77e979c09c28747ee`. Fixed suffix (name records, graph, query, output instruction) SHA256: `d074cf9a962ef19786883664357d6c8ad1543014cff9b2c91b7d97fdc287b4af`. Gold identity: Yuen Woo-ping. Every identity occupies each position once.

```diff
--- P1
+++ P2
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Tinnu Anand
+2. Ildikó Enyedi
+3. Rahul Rawail
+4. Yuen Woo-ping
 
```

```diff
--- P1
+++ P3
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Ildikó Enyedi
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Tinnu Anand
 
```

```diff
--- P1
+++ P4
@@ -3,6 +3,6 @@
 Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Ildikó Enyedi
 
```
