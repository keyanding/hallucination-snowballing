# Frozen prompt intervention audit

All planned cells, including unqueried confirmation difficulties, pass independent graph traversal, exact L prefix/suffix equality and R graph/query equality. N removes the separate list and changes only the two query/output phrases documented below. R1 and N are equal and are evaluated separately.

## development/v344-development-01/EASY

L1 sha256 `e860654432c6db213aaec6ae36d8d179be157ee7f245be62b5f1f616b3a898bd`; N sha256 `c2aa9d868b21b630d4911e77556df85bed2bd4fc05e3cda1ef8e3de13cf0ecef`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
@@ -18 +12 @@
-Which candidate is the credited director of Film T95882?
+Who is the credited director of Film T95882?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Tinnu Anand
+2. Jan Svěrák
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Jan Svěrák
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R78471 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R78471 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R19577 names Leopoldo Torre Nilsson.
+Record R30140 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R19577 names Leopoldo Torre Nilsson.
-Record R30140 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30140 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R30140 names Jan Svěrák.
```

## development/v344-development-01/MID

L1 sha256 `33056552a4b1a0bf6a3a6424413be25c2ed981829ad699e80cf2f47db3921366`; N sha256 `5ceca7e2c928522ce792e9eb103702e0c0e1e3d4ba4844d9b1750a3670ed1f2e`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
@@ -20 +14 @@
-Which candidate is the credited director of Film T95882?
+Who is the credited director of Film T95882?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Tinnu Anand
+2. Jan Svěrák
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Jan Svěrák
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R78471 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R78471 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R19577 names Leopoldo Torre Nilsson.
+Record R30140 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R19577 names Leopoldo Torre Nilsson.
-Record R30140 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30140 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R30140 names Jan Svěrák.
```

## development/v344-development-01/HARD

L1 sha256 `67cebc04ab7de0b156bd5d4f18e410647ca1062a5276d6d8ac223cd2baf3e991`; N sha256 `a102bf026904252166fc347729515faa5348e66d03440864efc7ec6a0455a49b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
@@ -29 +23 @@
-Which candidate is the credited director of Film T95882?
+Who is the credited director of Film T95882?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Tinnu Anand
+2. Jan Svěrák
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Jan Svěrák
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Tinnu Anand
-3. Jan Svěrák
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R78471 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R78471 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R19577 names Leopoldo Torre Nilsson.
+Record R30140 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R19577 names Leopoldo Torre Nilsson.
-Record R30140 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30140 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R30140 names Jan Svěrák.
```

## development/v344-development-02/EASY

L1 sha256 `0abd2f4b5157b68cc40eccbac6cab4bb084764c7c549456e966fd74e7a9c207d`; N sha256 `c9d8747ae0765ac3313831aebc9c38eabea2e72a76f1a0e3385dc7bc41c4baa0`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
@@ -18 +12 @@
-Which candidate is the credited director of Film T13533?
+Who is the credited director of Film T13533?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Leopoldo Torre Nilsson
+2. Tinnu Anand
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Tinnu Anand
+2. Yuen Woo-ping
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R24054 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R24054 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80408 names Yuen Woo-ping.
+Record R48293 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R80408 names Yuen Woo-ping.
-Record R48293 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R48293 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R48293 names Leopoldo Torre Nilsson.
```

## development/v344-development-02/MID

L1 sha256 `4cf1e12f5bcee069b226800d3458983b61738003a4ac3705747a3183c61f3889`; N sha256 `d42e1a0895792b8b99e0f8d5f6be9ca04a3a3b44f60eda0e82315b4c2740646e`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
@@ -20 +14 @@
-Which candidate is the credited director of Film T13533?
+Who is the credited director of Film T13533?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Leopoldo Torre Nilsson
+2. Tinnu Anand
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Tinnu Anand
+2. Yuen Woo-ping
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R24054 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R24054 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80408 names Yuen Woo-ping.
+Record R48293 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R80408 names Yuen Woo-ping.
-Record R48293 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R48293 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R48293 names Leopoldo Torre Nilsson.
```

## development/v344-development-02/HARD

L1 sha256 `5bd18147ce8f0d878ed52258914af81e6ca977b86b85aedab147c2cc3b1fce01`; N sha256 `5ffbb22aaef10504ffdb9d6b4e6a4010759dddc72d31201fbc28978d1b8a7848`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
@@ -29 +23 @@
-Which candidate is the credited director of Film T13533?
+Who is the credited director of Film T13533?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Leopoldo Torre Nilsson
+2. Tinnu Anand
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Leopoldo Torre Nilsson
-4. Tinnu Anand
+1. Tinnu Anand
+2. Yuen Woo-ping
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R24054 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R24054 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80408 names Yuen Woo-ping.
+Record R48293 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R80408 names Yuen Woo-ping.
-Record R48293 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R48293 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R48293 names Leopoldo Torre Nilsson.
```

## development/v344-development-03/EASY

L1 sha256 `accf336fb98cfbb838e1bbaead18fc87e4dc4df73ac34314c825d64794f65f3a`; N sha256 `8a594ae42af9fe2e180eb245bf48c89df4ace04d4fa9f3a67eb8e45dde3ce967`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
@@ -18 +12 @@
-Which candidate is the credited director of Film T30973?
+Who is the credited director of Film T30973?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Vojtěch Jasný
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. Walter Hugo Khouri
+2. Vojtěch Jasný
+3. Robert P. Kerr
+4. León Klimovsky
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Robert P. Kerr
+3. León Klimovsky
+4. Walter Hugo Khouri
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R92351 names León Klimovsky.
@@ -7,0 +7 @@
+Record R92351 names León Klimovsky.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R17613 names Vojtěch Jasný.
+Record R55562 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R17613 names Vojtěch Jasný.
-Record R55562 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R55562 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R55562 names Robert P. Kerr.
```

## development/v344-development-03/MID

L1 sha256 `73e7a65ad97ead7aa114dcb835fec85a0c34b4c6a247cfad78d7cff37840ad2d`; N sha256 `7d587b4d1f19cc4ec7742144ae6d1b675a0e7f328bdb6d7b70080d9a899661d2`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
@@ -20 +14 @@
-Which candidate is the credited director of Film T30973?
+Who is the credited director of Film T30973?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Vojtěch Jasný
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. Walter Hugo Khouri
+2. Vojtěch Jasný
+3. Robert P. Kerr
+4. León Klimovsky
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Robert P. Kerr
+3. León Klimovsky
+4. Walter Hugo Khouri
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R92351 names León Klimovsky.
@@ -7,0 +7 @@
+Record R92351 names León Klimovsky.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R17613 names Vojtěch Jasný.
+Record R55562 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R17613 names Vojtěch Jasný.
-Record R55562 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R55562 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R55562 names Robert P. Kerr.
```

## development/v344-development-03/HARD

L1 sha256 `82d4c8391524ea3a4d6827ffe953eed0410f30f425c6f2a05d1e23c66a62d71d`; N sha256 `3b630a9bf8728d07aa56989e941350896ee0eabc2ac9423cbdfd80dff281aa91`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
@@ -29 +23 @@
-Which candidate is the credited director of Film T30973?
+Who is the credited director of Film T30973?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Vojtěch Jasný
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. Walter Hugo Khouri
+2. Vojtěch Jasný
+3. Robert P. Kerr
+4. León Klimovsky
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. León Klimovsky
-3. Walter Hugo Khouri
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Robert P. Kerr
+3. León Klimovsky
+4. Walter Hugo Khouri
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R92351 names León Klimovsky.
@@ -7,0 +7 @@
+Record R92351 names León Klimovsky.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R17613 names Vojtěch Jasný.
+Record R55562 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R17613 names Vojtěch Jasný.
-Record R55562 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R55562 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R55562 names Robert P. Kerr.
```

## development/v344-development-04/EASY

L1 sha256 `9d3a928a39a94453efc58bb7a6c381cfbfa54ef555e6ed4c87a428802221a659`; N sha256 `0f9d2a1235676f221e11b620f38755d28b14badc60647bb73058251450351e05`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
@@ -18 +12 @@
-Which candidate is the credited director of Film T92782?
+Who is the credited director of Film T92782?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Leopoldo Torre Nilsson
+2. Yuen Woo-ping
+3. Armando Robles Godoy
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Yuen Woo-ping
+2. Armando Robles Godoy
+3. Jan Svěrák
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20859 names Jan Svěrák.
@@ -7,0 +7 @@
+Record R20859 names Jan Svěrák.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R21760 names Yuen Woo-ping.
+Record R37101 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R21760 names Yuen Woo-ping.
-Record R37101 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R37101 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R37101 names Leopoldo Torre Nilsson.
```

## development/v344-development-04/MID

L1 sha256 `4299ad38df9c671eeeb055f33448174b732b62a06da6f1333cd091db9f0b2ad3`; N sha256 `6e884477172f457d41ed5d9a6021434d4bb770d559063100af75df9031a11555`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
@@ -20 +14 @@
-Which candidate is the credited director of Film T92782?
+Who is the credited director of Film T92782?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Leopoldo Torre Nilsson
+2. Yuen Woo-ping
+3. Armando Robles Godoy
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Yuen Woo-ping
+2. Armando Robles Godoy
+3. Jan Svěrák
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20859 names Jan Svěrák.
@@ -7,0 +7 @@
+Record R20859 names Jan Svěrák.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R21760 names Yuen Woo-ping.
+Record R37101 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R21760 names Yuen Woo-ping.
-Record R37101 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R37101 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R37101 names Leopoldo Torre Nilsson.
```

## development/v344-development-04/HARD

L1 sha256 `622f72d8266594d60863768a0d054e2aafd97081ce2957b8dca5d354703ea4d0`; N sha256 `59aaa952a31afd6c61d1542a77ae300e1b96b3878f34245f0052dda4a6da9243`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
@@ -29 +23 @@
-Which candidate is the credited director of Film T92782?
+Who is the credited director of Film T92782?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Leopoldo Torre Nilsson
+2. Yuen Woo-ping
+3. Armando Robles Godoy
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Yuen Woo-ping
+2. Armando Robles Godoy
+3. Jan Svěrák
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Leopoldo Torre Nilsson
-3. Yuen Woo-ping
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20859 names Jan Svěrák.
@@ -7,0 +7 @@
+Record R20859 names Jan Svěrák.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R21760 names Yuen Woo-ping.
+Record R37101 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R21760 names Yuen Woo-ping.
-Record R37101 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R37101 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R37101 names Leopoldo Torre Nilsson.
```

## development/v344-development-05/EASY

L1 sha256 `67abc8d9dcc3bb9890460e65de46b9e390b92d49ce0703b363fe168561fcab5d`; N sha256 `605c2be8980375623a550503fbf65c2d6a01621896374e958890b456942308a2`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
@@ -18 +12 @@
-Which candidate is the credited director of Film T79932?
+Who is the credited director of Film T79932?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Fridrikh Ermler
+2. Feng Xiaoning
+3. Anil Das
+4. Rolf Schübel
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Feng Xiaoning
+2. Anil Das
+3. Rolf Schübel
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Anil Das
+2. Rolf Schübel
+3. Fridrikh Ermler
+4. Feng Xiaoning
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R89440 names Anil Das.
@@ -7,0 +7 @@
+Record R89440 names Anil Das.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R71906 names Fridrikh Ermler.
+Record R63155 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R71906 names Fridrikh Ermler.
-Record R63155 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R63155 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R63155 names Feng Xiaoning.
```

## development/v344-development-05/MID

L1 sha256 `10386247eb4f6b6195c66376d96ca376ff8919b6e39f11450b96c9bc603c7c02`; N sha256 `b9eba861260c2dec926b84e2508b4e6a5f5df8242a19d3b1233d25e2216f4cd3`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
@@ -20 +14 @@
-Which candidate is the credited director of Film T79932?
+Who is the credited director of Film T79932?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Fridrikh Ermler
+2. Feng Xiaoning
+3. Anil Das
+4. Rolf Schübel
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Feng Xiaoning
+2. Anil Das
+3. Rolf Schübel
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Anil Das
+2. Rolf Schübel
+3. Fridrikh Ermler
+4. Feng Xiaoning
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R89440 names Anil Das.
@@ -7,0 +7 @@
+Record R89440 names Anil Das.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R71906 names Fridrikh Ermler.
+Record R63155 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R71906 names Fridrikh Ermler.
-Record R63155 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R63155 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R63155 names Feng Xiaoning.
```

## development/v344-development-05/HARD

L1 sha256 `c004a71a497ad21d216779f94f8f1f2adf0129965bd97ebc87751f40beac9eda`; N sha256 `edb923c502129e8fd8832e5bae02ae0c584c1fad4f9466039bc4ed3218bde68f`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
@@ -29 +23 @@
-Which candidate is the credited director of Film T79932?
+Who is the credited director of Film T79932?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Fridrikh Ermler
+2. Feng Xiaoning
+3. Anil Das
+4. Rolf Schübel
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Feng Xiaoning
+2. Anil Das
+3. Rolf Schübel
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Anil Das
+2. Rolf Schübel
+3. Fridrikh Ermler
+4. Feng Xiaoning
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R89440 names Anil Das.
@@ -7,0 +7 @@
+Record R89440 names Anil Das.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R71906 names Fridrikh Ermler.
+Record R63155 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R71906 names Fridrikh Ermler.
-Record R63155 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R63155 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R63155 names Feng Xiaoning.
```

## development/v344-development-06/EASY

L1 sha256 `735648a02193f49b796d8a14c47c4ef2cad447a349c5395a49a8642cbcd3d1a1`; N sha256 `3822a1f5e79860aa9af28ccfa44b626846284f1898cce1ac4246097f28f2b675`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
@@ -18 +12 @@
-Which candidate is the credited director of Film T39322?
+Who is the credited director of Film T39322?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. James Goldstone
+2. Bhappi Sonie
+3. Marcello Fondato
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. Bhappi Sonie
+2. Marcello Fondato
+3. Robert P. Kerr
+4. James Goldstone
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. Marcello Fondato
+2. Robert P. Kerr
+3. James Goldstone
+4. Bhappi Sonie
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14460 names James Goldstone.
@@ -7,0 +7 @@
+Record R14460 names James Goldstone.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R54307 names Marcello Fondato.
+Record R66025 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R54307 names Marcello Fondato.
-Record R66025 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R66025 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R66025 names Robert P. Kerr.
```

## development/v344-development-06/MID

L1 sha256 `aee0b5291753f0844045424479a2361b15cc254cc57b357f2d5315f4ba850569`; N sha256 `36024dfcec36c9c7b77851a771778e53bb8c0d0c3515456bd15371b30071e53c`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
@@ -20 +14 @@
-Which candidate is the credited director of Film T39322?
+Who is the credited director of Film T39322?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. James Goldstone
+2. Bhappi Sonie
+3. Marcello Fondato
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. Bhappi Sonie
+2. Marcello Fondato
+3. Robert P. Kerr
+4. James Goldstone
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. Marcello Fondato
+2. Robert P. Kerr
+3. James Goldstone
+4. Bhappi Sonie
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14460 names James Goldstone.
@@ -7,0 +7 @@
+Record R14460 names James Goldstone.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R54307 names Marcello Fondato.
+Record R66025 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R54307 names Marcello Fondato.
-Record R66025 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R66025 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R66025 names Robert P. Kerr.
```

## development/v344-development-06/HARD

L1 sha256 `0ebbc8c02e4cf2d2ed83711841a327337efc867041d69874e83095ea3cc6a131`; N sha256 `a57e072f98dd23c63dcb8c7cef32d309579a46b5dbc6a87b98b580958bf75972`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
@@ -29 +23 @@
-Which candidate is the credited director of Film T39322?
+Who is the credited director of Film T39322?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. James Goldstone
+2. Bhappi Sonie
+3. Marcello Fondato
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. Bhappi Sonie
+2. Marcello Fondato
+3. Robert P. Kerr
+4. James Goldstone
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Bhappi Sonie
-4. Marcello Fondato
+1. Marcello Fondato
+2. Robert P. Kerr
+3. James Goldstone
+4. Bhappi Sonie
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14460 names James Goldstone.
@@ -7,0 +7 @@
+Record R14460 names James Goldstone.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R54307 names Marcello Fondato.
+Record R66025 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R54307 names Marcello Fondato.
-Record R66025 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R66025 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R66025 names Robert P. Kerr.
```

## development/v344-development-07/EASY

L1 sha256 `0f5a359b90efb0b678c317166625d50d7d6e6677f8f062653b04055ab85e9198`; N sha256 `6599023caa63db75daee7091e153ce754fc55a36268192913de1878630f1ab83`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
@@ -18 +12 @@
-Which candidate is the credited director of Film T51971?
+Who is the credited director of Film T51971?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. James Goldstone
+2. Marcello Fondato
+3. León Klimovsky
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Robert P. Kerr
+4. James Goldstone
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Robert P. Kerr
+3. James Goldstone
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R11159 names Robert P. Kerr.
@@ -7,0 +7 @@
+Record R11159 names Robert P. Kerr.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R91042 names León Klimovsky.
+Record R80061 names James Goldstone.
@@ -6,2 +7,0 @@
-Record R91042 names León Klimovsky.
-Record R80061 names James Goldstone.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R80061 names James Goldstone.
@@ -7 +7,0 @@
-Record R80061 names James Goldstone.
```

## development/v344-development-07/MID

L1 sha256 `7b83171cbb1ccdc689c1d1115af1b6be9067f2cbd3a0b57f38b1d24d046c26c3`; N sha256 `accef4e4573568d24e42616bdf66abe9ce5534c01f2a2401899dfb9b19d0bcae`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
@@ -20 +14 @@
-Which candidate is the credited director of Film T51971?
+Who is the credited director of Film T51971?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. James Goldstone
+2. Marcello Fondato
+3. León Klimovsky
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Robert P. Kerr
+4. James Goldstone
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Robert P. Kerr
+3. James Goldstone
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R11159 names Robert P. Kerr.
@@ -7,0 +7 @@
+Record R11159 names Robert P. Kerr.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R91042 names León Klimovsky.
+Record R80061 names James Goldstone.
@@ -6,2 +7,0 @@
-Record R91042 names León Klimovsky.
-Record R80061 names James Goldstone.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R80061 names James Goldstone.
@@ -7 +7,0 @@
-Record R80061 names James Goldstone.
```

## development/v344-development-07/HARD

L1 sha256 `ae42d4c9cf1655013eaa1458e9f5a1bfa8d8b86d6c30ab0628256dac65f30f45`; N sha256 `48049a0844084c155d4660753e1428a33dd4b74e298fac5e79aad8e3c8c6c35d`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
@@ -29 +23 @@
-Which candidate is the credited director of Film T51971?
+Who is the credited director of Film T51971?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. James Goldstone
+2. Marcello Fondato
+3. León Klimovsky
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Robert P. Kerr
+4. James Goldstone
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. James Goldstone
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Robert P. Kerr
+3. James Goldstone
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R11159 names Robert P. Kerr.
@@ -7,0 +7 @@
+Record R11159 names Robert P. Kerr.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R91042 names León Klimovsky.
+Record R80061 names James Goldstone.
@@ -6,2 +7,0 @@
-Record R91042 names León Klimovsky.
-Record R80061 names James Goldstone.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R80061 names James Goldstone.
@@ -7 +7,0 @@
-Record R80061 names James Goldstone.
```

## development/v344-development-08/EASY

L1 sha256 `86a07d18c78e12e842cebd0effb4f5bf93b19ea9ef340f04dcc3a884e35bc3c0`; N sha256 `31fe86407c1c97fa32320134413bc7101b4ffffbdeba2fedf691545426d38eaf`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
@@ -18 +12 @@
-Which candidate is the credited director of Film T52893?
+Who is the credited director of Film T52893?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Helmut Käutner
+2. Anil Das
+3. Fridrikh Ermler
+4. Gu Changwei
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Anil Das
+2. Fridrikh Ermler
+3. Gu Changwei
+4. Helmut Käutner
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Gu Changwei
+3. Helmut Käutner
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R84465 names Fridrikh Ermler.
@@ -7,0 +7 @@
+Record R84465 names Fridrikh Ermler.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80092 names Gu Changwei.
+Record R32193 names Anil Das.
@@ -6,2 +7,0 @@
-Record R80092 names Gu Changwei.
-Record R32193 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R32193 names Anil Das.
@@ -7 +7,0 @@
-Record R32193 names Anil Das.
```

## development/v344-development-08/MID

L1 sha256 `f55756d14d92faed1a8656313011a6582bcc32ecb9e219fc02030a7f2651423a`; N sha256 `58b2d4f8527423c2fb9ac06d2bdd177617745dd480d40826c25c771d462fa3ef`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
@@ -20 +14 @@
-Which candidate is the credited director of Film T52893?
+Who is the credited director of Film T52893?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Helmut Käutner
+2. Anil Das
+3. Fridrikh Ermler
+4. Gu Changwei
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Anil Das
+2. Fridrikh Ermler
+3. Gu Changwei
+4. Helmut Käutner
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Gu Changwei
+3. Helmut Käutner
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R84465 names Fridrikh Ermler.
@@ -7,0 +7 @@
+Record R84465 names Fridrikh Ermler.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80092 names Gu Changwei.
+Record R32193 names Anil Das.
@@ -6,2 +7,0 @@
-Record R80092 names Gu Changwei.
-Record R32193 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R32193 names Anil Das.
@@ -7 +7,0 @@
-Record R32193 names Anil Das.
```

## development/v344-development-08/HARD

L1 sha256 `fa0d30174ce3e0aa33b29518e86ecbcf3370619647fcb542beaa29d5219b2281`; N sha256 `052d1a7fe848b2aeb1b079970dee96041dbd0d7a20ceea5f7440a235dba4f463`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
@@ -29 +23 @@
-Which candidate is the credited director of Film T52893?
+Who is the credited director of Film T52893?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Helmut Käutner
+2. Anil Das
+3. Fridrikh Ermler
+4. Gu Changwei
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Anil Das
+2. Fridrikh Ermler
+3. Gu Changwei
+4. Helmut Käutner
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Gu Changwei
-2. Helmut Käutner
-3. Anil Das
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Gu Changwei
+3. Helmut Käutner
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R84465 names Fridrikh Ermler.
@@ -7,0 +7 @@
+Record R84465 names Fridrikh Ermler.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80092 names Gu Changwei.
+Record R32193 names Anil Das.
@@ -6,2 +7,0 @@
-Record R80092 names Gu Changwei.
-Record R32193 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R32193 names Anil Das.
@@ -7 +7,0 @@
-Record R32193 names Anil Das.
```

## development/v344-development-09/EASY

L1 sha256 `d581fb3be7597a3276aa68ec0a761ad4aac8055234a5fa7ef1a9a15309bfc5f7`; N sha256 `9f1a03e29c2e2aa2bbddadeb30ef8e6237f4c0ed5728bb1f56ba463d57be0702`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
@@ -18 +12 @@
-Which candidate is the credited director of Film T83397?
+Who is the credited director of Film T83397?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Vojtěch Jasný
+2. Marcello Fondato
+3. León Klimovsky
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Bhappi Sonie
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Bhappi Sonie
+3. Vojtěch Jasný
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R89158 names León Klimovsky.
@@ -7,0 +7 @@
+Record R89158 names León Klimovsky.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R16904 names Vojtěch Jasný.
+Record R95593 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R16904 names Vojtěch Jasný.
-Record R95593 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R95593 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R95593 names Marcello Fondato.
```

## development/v344-development-09/MID

L1 sha256 `59c4c35a4795005102f5347e724339aa5ab786636b1d6c83c708d7c7a385e49e`; N sha256 `321addade5345d75e37161d0fd881f2266dce2172c20c7296046b795643a9651`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
@@ -20 +14 @@
-Which candidate is the credited director of Film T83397?
+Who is the credited director of Film T83397?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Vojtěch Jasný
+2. Marcello Fondato
+3. León Klimovsky
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Bhappi Sonie
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Bhappi Sonie
+3. Vojtěch Jasný
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R89158 names León Klimovsky.
@@ -7,0 +7 @@
+Record R89158 names León Klimovsky.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R16904 names Vojtěch Jasný.
+Record R95593 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R16904 names Vojtěch Jasný.
-Record R95593 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R95593 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R95593 names Marcello Fondato.
```

## development/v344-development-09/HARD

L1 sha256 `8d664d6ecc910a7651ccc829ceac984d1b256741f066aa1f4fdc7f7668c3ae59`; N sha256 `d673b541e59bac1624b29717a860ee2fe8c934bae49f8970750e817d9b1be242`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
@@ -29 +23 @@
-Which candidate is the credited director of Film T83397?
+Who is the credited director of Film T83397?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Vojtěch Jasný
+2. Marcello Fondato
+3. León Klimovsky
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Bhappi Sonie
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Bhappi Sonie
+3. Vojtěch Jasný
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R89158 names León Klimovsky.
@@ -7,0 +7 @@
+Record R89158 names León Klimovsky.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R16904 names Vojtěch Jasný.
+Record R95593 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R16904 names Vojtěch Jasný.
-Record R95593 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R95593 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R95593 names Marcello Fondato.
```

## development/v344-development-10/EASY

L1 sha256 `f1324354c35a3261041612d089f0ffb10774c3ea32d89d7e81958c8ab23d20b5`; N sha256 `fb55878783877b1fc438b17fc3a695fc3ac9d0de5f71653d84427f4715fc1aec`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
@@ -18 +12 @@
-Which candidate is the credited director of Film T76581?
+Who is the credited director of Film T76581?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Rolf Schübel
+2. Rodrigo Grande
+3. Anil Das
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Rodrigo Grande
+2. Anil Das
+3. Fridrikh Ermler
+4. Rolf Schübel
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R15047 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R15047 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R45727 names Fridrikh Ermler.
+Record R52105 names Anil Das.
@@ -6,2 +7,0 @@
-Record R45727 names Fridrikh Ermler.
-Record R52105 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R52105 names Anil Das.
@@ -7 +7,0 @@
-Record R52105 names Anil Das.
```

## development/v344-development-10/MID

L1 sha256 `c72f07f78e80ef239f6386ba178f1bb8fb26f9ecdee6a45d053319694f741b92`; N sha256 `84aba04500a77da2ebb8a330ecdb278caac8723e83027eab11cf38cd418cc790`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
@@ -20 +14 @@
-Which candidate is the credited director of Film T76581?
+Who is the credited director of Film T76581?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Rolf Schübel
+2. Rodrigo Grande
+3. Anil Das
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Rodrigo Grande
+2. Anil Das
+3. Fridrikh Ermler
+4. Rolf Schübel
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R15047 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R15047 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R45727 names Fridrikh Ermler.
+Record R52105 names Anil Das.
@@ -6,2 +7,0 @@
-Record R45727 names Fridrikh Ermler.
-Record R52105 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R52105 names Anil Das.
@@ -7 +7,0 @@
-Record R52105 names Anil Das.
```

## development/v344-development-10/HARD

L1 sha256 `900d89ad288dee0cc7728fa56a33c99feeeda81c9dd949d4fccdcbda092aa391`; N sha256 `b760734f4342c30e2cb2a3c22a0ec6cd19bb8213a467bdf837cb357e8228dfb8`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
@@ -29 +23 @@
-Which candidate is the credited director of Film T76581?
+Who is the credited director of Film T76581?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Rolf Schübel
+2. Rodrigo Grande
+3. Anil Das
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Fridrikh Ermler
-3. Rolf Schübel
-4. Rodrigo Grande
+1. Rodrigo Grande
+2. Anil Das
+3. Fridrikh Ermler
+4. Rolf Schübel
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R15047 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R15047 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R45727 names Fridrikh Ermler.
+Record R52105 names Anil Das.
@@ -6,2 +7,0 @@
-Record R45727 names Fridrikh Ermler.
-Record R52105 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R52105 names Anil Das.
@@ -7 +7,0 @@
-Record R52105 names Anil Das.
```

## development/v344-development-11/EASY

L1 sha256 `5fbfb8938b3b77b19dc256fbecc84e45de5d2c8da6db16b22e64c5c2a5f0792f`; N sha256 `8fa4c505df8547b5a1709cab8ae33b4cd7bf36c88f751acd83bcccac20b6ee2a`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
@@ -18 +12 @@
-Which candidate is the credited director of Film T43844?
+Who is the credited director of Film T43844?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. Bhappi Sonie
+2. James Goldstone
+3. Robert P. Kerr
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. James Goldstone
+2. Robert P. Kerr
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. Robert P. Kerr
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R70597 names Vojtěch Jasný.
@@ -7,0 +7 @@
+Record R70597 names Vojtěch Jasný.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R81632 names Bhappi Sonie.
+Record R16007 names James Goldstone.
@@ -6,2 +7,0 @@
-Record R81632 names Bhappi Sonie.
-Record R16007 names James Goldstone.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R16007 names James Goldstone.
@@ -7 +7,0 @@
-Record R16007 names James Goldstone.
```

## development/v344-development-11/MID

L1 sha256 `512393756208e6cf3f918554cf6a5d1e4e02444b738196592c98f4183e80eb2d`; N sha256 `3dc2c8d8f9bd4411bb3e52550e265d642477e7481b990476c40c63826015b592`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
@@ -20 +14 @@
-Which candidate is the credited director of Film T43844?
+Who is the credited director of Film T43844?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. Bhappi Sonie
+2. James Goldstone
+3. Robert P. Kerr
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. James Goldstone
+2. Robert P. Kerr
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. Robert P. Kerr
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R70597 names Vojtěch Jasný.
@@ -7,0 +7 @@
+Record R70597 names Vojtěch Jasný.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R81632 names Bhappi Sonie.
+Record R16007 names James Goldstone.
@@ -6,2 +7,0 @@
-Record R81632 names Bhappi Sonie.
-Record R16007 names James Goldstone.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R16007 names James Goldstone.
@@ -7 +7,0 @@
-Record R16007 names James Goldstone.
```

## development/v344-development-11/HARD

L1 sha256 `8cf12b2e8d7c8d962764bda5f100cd82e7ed29da93f41c81c0fcab4817a48142`; N sha256 `163bc3f8f25544708ef7de6f169b86fe09aee1f932d3ddc71d39c7074df24295`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
@@ -29 +23 @@
-Which candidate is the credited director of Film T43844?
+Who is the credited director of Film T43844?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. Bhappi Sonie
+2. James Goldstone
+3. Robert P. Kerr
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. James Goldstone
+2. Robert P. Kerr
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. Robert P. Kerr
+1. Robert P. Kerr
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R70597 names Vojtěch Jasný.
@@ -7,0 +7 @@
+Record R70597 names Vojtěch Jasný.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R81632 names Bhappi Sonie.
+Record R16007 names James Goldstone.
@@ -6,2 +7,0 @@
-Record R81632 names Bhappi Sonie.
-Record R16007 names James Goldstone.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R16007 names James Goldstone.
@@ -7 +7,0 @@
-Record R16007 names James Goldstone.
```

## development/v344-development-12/EASY

L1 sha256 `ae62a6a73c268e7e6dc84d5e1177ce0e62cca657be3859b9a85a0d34a7291aec`; N sha256 `6a9077462ca1ba7408ada1c20692651d44faec4cbe8e892340c395370a82b8de`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
@@ -18 +12 @@
-Which candidate is the credited director of Film T59052?
+Who is the credited director of Film T59052?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Yuen Woo-ping
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Tinnu Anand
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Tinnu Anand
+3. Yuen Woo-ping
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R67704 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R67704 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R68982 names Ildikó Enyedi.
+Record R30834 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R68982 names Ildikó Enyedi.
-Record R30834 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30834 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R30834 names Armando Robles Godoy.
```

## development/v344-development-12/MID

L1 sha256 `45ea1c1ebfcf86ca271843499d84b7e83625260a67d6ec844f2b95536305c2de`; N sha256 `f762b65d2125cb1d1aa583a4f3f2e325b32f51604df21e94d70734f39509d2f2`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
@@ -20 +14 @@
-Which candidate is the credited director of Film T59052?
+Who is the credited director of Film T59052?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Yuen Woo-ping
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Tinnu Anand
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Tinnu Anand
+3. Yuen Woo-ping
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R67704 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R67704 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R68982 names Ildikó Enyedi.
+Record R30834 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R68982 names Ildikó Enyedi.
-Record R30834 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30834 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R30834 names Armando Robles Godoy.
```

## development/v344-development-12/HARD

L1 sha256 `f6990c8875396a83c2b7b70b0f9f369ed2413293da360e947e416e36ae846e02`; N sha256 `2f3504aba84769308d88cb742e1519c8cf2fb87337f5dcaf5602678278313123`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
@@ -29 +23 @@
-Which candidate is the credited director of Film T59052?
+Who is the credited director of Film T59052?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Yuen Woo-ping
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Tinnu Anand
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Yuen Woo-ping
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Tinnu Anand
+3. Yuen Woo-ping
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R67704 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R67704 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R68982 names Ildikó Enyedi.
+Record R30834 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R68982 names Ildikó Enyedi.
-Record R30834 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30834 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R30834 names Armando Robles Godoy.
```

## development/v344-development-13/EASY

L1 sha256 `0c1c8b38cdeb1d53624384515b2ebf51b489c40ffe190a2347384cf79ef076ca`; N sha256 `5e93f3894ba02e2ca56ad2040c9b417d60f0f9d0a6e7aa15bc3b1e89a3131e64`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
@@ -18 +12 @@
-Which candidate is the credited director of Film T86343?
+Who is the credited director of Film T86343?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Marcello Fondato
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Bhappi Sonie
+4. Marcello Fondato
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Bhappi Sonie
+3. Marcello Fondato
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R87911 names Marcello Fondato.
@@ -7,0 +7 @@
+Record R87911 names Marcello Fondato.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R45088 names Walter Hugo Khouri.
+Record R34507 names Bhappi Sonie.
@@ -6,2 +7,0 @@
-Record R45088 names Walter Hugo Khouri.
-Record R34507 names Bhappi Sonie.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R34507 names Bhappi Sonie.
@@ -7 +7,0 @@
-Record R34507 names Bhappi Sonie.
```

## development/v344-development-13/MID

L1 sha256 `0497552716650a17db457d893e52dabfd85bc7e86e7176ce2ed1d72434cf8787`; N sha256 `83577d4cbfa86ef50516bb71eeaaed351e4f1863d2dbe7f1b77ae6d89d644a1b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
@@ -20 +14 @@
-Which candidate is the credited director of Film T86343?
+Who is the credited director of Film T86343?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Marcello Fondato
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Bhappi Sonie
+4. Marcello Fondato
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Bhappi Sonie
+3. Marcello Fondato
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R87911 names Marcello Fondato.
@@ -7,0 +7 @@
+Record R87911 names Marcello Fondato.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R45088 names Walter Hugo Khouri.
+Record R34507 names Bhappi Sonie.
@@ -6,2 +7,0 @@
-Record R45088 names Walter Hugo Khouri.
-Record R34507 names Bhappi Sonie.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R34507 names Bhappi Sonie.
@@ -7 +7,0 @@
-Record R34507 names Bhappi Sonie.
```

## development/v344-development-13/HARD

L1 sha256 `23d99cb358ebac017c28ec34cf1e83b403d20438be85d6000a6024cb7c7194c3`; N sha256 `5d325727e898f7cd9666d5b77057a02eff005d840b9cb0afd986fca9c266122b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
@@ -29 +23 @@
-Which candidate is the credited director of Film T86343?
+Who is the credited director of Film T86343?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Marcello Fondato
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Bhappi Sonie
+4. Marcello Fondato
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Marcello Fondato
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Bhappi Sonie
+3. Marcello Fondato
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R87911 names Marcello Fondato.
@@ -7,0 +7 @@
+Record R87911 names Marcello Fondato.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R45088 names Walter Hugo Khouri.
+Record R34507 names Bhappi Sonie.
@@ -6,2 +7,0 @@
-Record R45088 names Walter Hugo Khouri.
-Record R34507 names Bhappi Sonie.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R34507 names Bhappi Sonie.
@@ -7 +7,0 @@
-Record R34507 names Bhappi Sonie.
```

## development/v344-development-14/EASY

L1 sha256 `3a1bf0ea8f4319ffa9bce596065fcd760405b9ca201d7a189688cf964284a1a5`; N sha256 `d25dcdd8eb3da8bdcbf0aa5bd163d189fae33edfff080951985bcea5c27228ac`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
@@ -18 +12 @@
-Which candidate is the credited director of Film T30907?
+Who is the credited director of Film T30907?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Robert P. Kerr
+2. Marcello Fondato
+3. Walter Hugo Khouri
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Marcello Fondato
+2. Walter Hugo Khouri
+3. Bhappi Sonie
+4. Robert P. Kerr
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Bhappi Sonie
+3. Robert P. Kerr
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R57955 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R57955 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53231 names Marcello Fondato.
+Record R95322 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R53231 names Marcello Fondato.
-Record R95322 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R95322 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R95322 names Robert P. Kerr.
```

## development/v344-development-14/MID

L1 sha256 `27feb5f8e82db4931f858f92183fbb7b3414435a5b77e170153a6c0a0c141a5f`; N sha256 `f966b6c68fe4ed492e28578c851d9a5a6af8c810325c6f9ead2bf43f8560932b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
@@ -20 +14 @@
-Which candidate is the credited director of Film T30907?
+Who is the credited director of Film T30907?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Robert P. Kerr
+2. Marcello Fondato
+3. Walter Hugo Khouri
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Marcello Fondato
+2. Walter Hugo Khouri
+3. Bhappi Sonie
+4. Robert P. Kerr
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Bhappi Sonie
+3. Robert P. Kerr
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R57955 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R57955 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53231 names Marcello Fondato.
+Record R95322 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R53231 names Marcello Fondato.
-Record R95322 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R95322 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R95322 names Robert P. Kerr.
```

## development/v344-development-14/HARD

L1 sha256 `4c3755901f408b04fd2808afe171ba07410f9b6b8d3d2ce8546326600a13ecaa`; N sha256 `9c52c922cd0d3fb85965ac910730026a6339ad59c20db3219e83a06fbe02ba4c`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
@@ -29 +23 @@
-Which candidate is the credited director of Film T30907?
+Who is the credited director of Film T30907?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Robert P. Kerr
+2. Marcello Fondato
+3. Walter Hugo Khouri
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Marcello Fondato
+2. Walter Hugo Khouri
+3. Bhappi Sonie
+4. Robert P. Kerr
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. Marcello Fondato
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Bhappi Sonie
+3. Robert P. Kerr
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R57955 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R57955 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53231 names Marcello Fondato.
+Record R95322 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R53231 names Marcello Fondato.
-Record R95322 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R95322 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R95322 names Robert P. Kerr.
```

## development/v344-development-15/EASY

L1 sha256 `d6758c7d9e5a1aedf9032e77db2a1d8079456559818644259c118c7e24bf3156`; N sha256 `55aca92155a249353d0ad3d69f040c58bb2f404992083eb2b4867d241a75610b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
@@ -18 +12 @@
-Which candidate is the credited director of Film T14409?
+Who is the credited director of Film T14409?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Ildikó Enyedi
+2. Armando Robles Godoy
+3. Yuen Woo-ping
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Armando Robles Godoy
+2. Yuen Woo-ping
+3. Jan Svěrák
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Yuen Woo-ping
+2. Jan Svěrák
+3. Ildikó Enyedi
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20106 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R20106 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R43735 names Yuen Woo-ping.
+Record R62865 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R43735 names Yuen Woo-ping.
-Record R62865 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R62865 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R62865 names Jan Svěrák.
```

## development/v344-development-15/MID

L1 sha256 `33ffc8e6f3876b760fbb9706f097361fc3b16156201beeb482287dd983705a4f`; N sha256 `7f6e907908e8feba8783d4e406cbb5def886f273e0b4bed948760a4120d90ec6`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
@@ -20 +14 @@
-Which candidate is the credited director of Film T14409?
+Who is the credited director of Film T14409?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Ildikó Enyedi
+2. Armando Robles Godoy
+3. Yuen Woo-ping
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Armando Robles Godoy
+2. Yuen Woo-ping
+3. Jan Svěrák
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Yuen Woo-ping
+2. Jan Svěrák
+3. Ildikó Enyedi
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20106 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R20106 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R43735 names Yuen Woo-ping.
+Record R62865 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R43735 names Yuen Woo-ping.
-Record R62865 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R62865 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R62865 names Jan Svěrák.
```

## development/v344-development-15/HARD

L1 sha256 `2c1d6ab30804b764bc96d5d02f15ee535621ce7bd927712dd2e263c3be28d2c1`; N sha256 `bf99c632188b2b74d6755f24af4e420684de967b19327b054cfe749e5e7c204f`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
@@ -29 +23 @@
-Which candidate is the credited director of Film T14409?
+Who is the credited director of Film T14409?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Ildikó Enyedi
+2. Armando Robles Godoy
+3. Yuen Woo-ping
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Armando Robles Godoy
+2. Yuen Woo-ping
+3. Jan Svěrák
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Yuen Woo-ping
+1. Yuen Woo-ping
+2. Jan Svěrák
+3. Ildikó Enyedi
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20106 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R20106 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R43735 names Yuen Woo-ping.
+Record R62865 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R43735 names Yuen Woo-ping.
-Record R62865 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R62865 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R62865 names Jan Svěrák.
```

## development/v344-development-16/EASY

L1 sha256 `c8707515d840c171f252919d915ccd98fe70d8c98a6f5d092a41dd044663f8cc`; N sha256 `70f1edd26f7b3e92cb524ae471da9fc9b524013f91f564c53aea0323d1aff5e8`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
@@ -18 +12 @@
-Which candidate is the credited director of Film T64663?
+Who is the credited director of Film T64663?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Rahul Rawail
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Jan Svěrák
+2. Leopoldo Torre Nilsson
+3. Armando Robles Godoy
+4. Rahul Rawail
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Rahul Rawail
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R68061 names Leopoldo Torre Nilsson.
@@ -7,0 +7 @@
+Record R68061 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R78450 names Armando Robles Godoy.
+Record R84496 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R78450 names Armando Robles Godoy.
-Record R84496 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R84496 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R84496 names Jan Svěrák.
```

## development/v344-development-16/MID

L1 sha256 `39d72130c11cc5a2cb5e0b4efc2a50c75c88fa5a30e0256dd58d7edebf75ca43`; N sha256 `f19aedfa76466f341bf1e1d399a01036c768949bc5016498986cbf8616aa463d`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
@@ -20 +14 @@
-Which candidate is the credited director of Film T64663?
+Who is the credited director of Film T64663?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Rahul Rawail
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Jan Svěrák
+2. Leopoldo Torre Nilsson
+3. Armando Robles Godoy
+4. Rahul Rawail
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Rahul Rawail
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R68061 names Leopoldo Torre Nilsson.
@@ -7,0 +7 @@
+Record R68061 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R78450 names Armando Robles Godoy.
+Record R84496 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R78450 names Armando Robles Godoy.
-Record R84496 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R84496 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R84496 names Jan Svěrák.
```

## development/v344-development-16/HARD

L1 sha256 `3c02787da2503e9570f312ba8e9861a8fc24f57eee818646f5113e75449f0474`; N sha256 `64c1a50ae1bf5c009eb5ca67146cc688302dbea95ecba9eabf71530902ef9568`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
@@ -29 +23 @@
-Which candidate is the credited director of Film T64663?
+Who is the credited director of Film T64663?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Rahul Rawail
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Jan Svěrák
+2. Leopoldo Torre Nilsson
+3. Armando Robles Godoy
+4. Rahul Rawail
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Rahul Rawail
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Rahul Rawail
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R68061 names Leopoldo Torre Nilsson.
@@ -7,0 +7 @@
+Record R68061 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R78450 names Armando Robles Godoy.
+Record R84496 names Jan Svěrák.
@@ -6,2 +7,0 @@
-Record R78450 names Armando Robles Godoy.
-Record R84496 names Jan Svěrák.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R84496 names Jan Svěrák.
@@ -7 +7,0 @@
-Record R84496 names Jan Svěrák.
```

## development/v344-development-17/EASY

L1 sha256 `52d7350480714a2bb7bbb6fcc3b0aca588d1e136b459abe9e0795bd92e047f01`; N sha256 `6f29c6595e67d4d66032a300a99ba37f5dcc3a15938f757364ba8728e6a97b9b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
@@ -18 +12 @@
-Which candidate is the credited director of Film T31878?
+Who is the credited director of Film T31878?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Bhappi Sonie
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Robert P. Kerr
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Robert P. Kerr
+3. Bhappi Sonie
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R90426 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R90426 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14814 names Bhappi Sonie.
+Record R47577 names León Klimovsky.
@@ -6,2 +7,0 @@
-Record R14814 names Bhappi Sonie.
-Record R47577 names León Klimovsky.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R47577 names León Klimovsky.
@@ -7 +7,0 @@
-Record R47577 names León Klimovsky.
```

## development/v344-development-17/MID

L1 sha256 `5c5ff25a32090ac6058f6efc2f2ba5c38ca0f219c96a53a4e91551702a4dae27`; N sha256 `a26fa635b30b4e060a0369ab7c016874b6444b0ecc673d147deb82493e22abf9`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
@@ -20 +14 @@
-Which candidate is the credited director of Film T31878?
+Who is the credited director of Film T31878?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Bhappi Sonie
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Robert P. Kerr
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Robert P. Kerr
+3. Bhappi Sonie
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R90426 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R90426 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14814 names Bhappi Sonie.
+Record R47577 names León Klimovsky.
@@ -6,2 +7,0 @@
-Record R14814 names Bhappi Sonie.
-Record R47577 names León Klimovsky.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R47577 names León Klimovsky.
@@ -7 +7,0 @@
-Record R47577 names León Klimovsky.
```

## development/v344-development-17/HARD

L1 sha256 `ce87139ec8d0e1ee50073e668db0d534224d54500b67331dc55c48551eb1702d`; N sha256 `1b2822bd229a391893b553f8d3604247f0b5f1e4900d7130ed65e73e4317fbae`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
@@ -29 +23 @@
-Which candidate is the credited director of Film T31878?
+Who is the credited director of Film T31878?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Bhappi Sonie
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. León Klimovsky
+2. Walter Hugo Khouri
+3. Robert P. Kerr
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. León Klimovsky
-4. Walter Hugo Khouri
+1. Walter Hugo Khouri
+2. Robert P. Kerr
+3. Bhappi Sonie
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R90426 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R90426 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14814 names Bhappi Sonie.
+Record R47577 names León Klimovsky.
@@ -6,2 +7,0 @@
-Record R14814 names Bhappi Sonie.
-Record R47577 names León Klimovsky.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R47577 names León Klimovsky.
@@ -7 +7,0 @@
-Record R47577 names León Klimovsky.
```

## development/v344-development-18/EASY

L1 sha256 `823c453b1e0e611ab824c78e1f307f5845d76749c9449ba337e03e6e1d9f1d4d`; N sha256 `e387ecd5d90b5ebd9c5cdb75f9801dc71bf60841f1e51923217b9bef64200b20`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
@@ -18 +12 @@
-Which candidate is the credited director of Film T20146?
+Who is the credited director of Film T20146?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Tinnu Anand
+2. Yuen Woo-ping
+3. Leopoldo Torre Nilsson
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Yuen Woo-ping
+2. Leopoldo Torre Nilsson
+3. Jan Svěrák
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Jan Svěrák
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R25995 names Leopoldo Torre Nilsson.
@@ -7,0 +7 @@
+Record R25995 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R11032 names Tinnu Anand.
+Record R81645 names Yuen Woo-ping.
@@ -6,2 +7,0 @@
-Record R11032 names Tinnu Anand.
-Record R81645 names Yuen Woo-ping.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R81645 names Yuen Woo-ping.
@@ -7 +7,0 @@
-Record R81645 names Yuen Woo-ping.
```

## development/v344-development-18/MID

L1 sha256 `0bc2e2bc4f9f589b2ff6c7a4b43ea988387f475cee6a5d03e9d42a0e9ccd12f0`; N sha256 `96ad65911d2bcce9f1f4b3fd2dd20a055e1ee4f8ae8ea2ae4baf4b1f9d17a08b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
@@ -20 +14 @@
-Which candidate is the credited director of Film T20146?
+Who is the credited director of Film T20146?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Tinnu Anand
+2. Yuen Woo-ping
+3. Leopoldo Torre Nilsson
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Yuen Woo-ping
+2. Leopoldo Torre Nilsson
+3. Jan Svěrák
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Jan Svěrák
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R25995 names Leopoldo Torre Nilsson.
@@ -7,0 +7 @@
+Record R25995 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R11032 names Tinnu Anand.
+Record R81645 names Yuen Woo-ping.
@@ -6,2 +7,0 @@
-Record R11032 names Tinnu Anand.
-Record R81645 names Yuen Woo-ping.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R81645 names Yuen Woo-ping.
@@ -7 +7,0 @@
-Record R81645 names Yuen Woo-ping.
```

## development/v344-development-18/HARD

L1 sha256 `a7e52a0817d1252e38c9b5ca7fe9981117be2d3b86b05f20b2d18b88802438b3`; N sha256 `4b4a8dd96af7be14f8f33f2f533497c7a044141e18d84ba10c021a77b0e6c1d2`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
@@ -29 +23 @@
-Which candidate is the credited director of Film T20146?
+Who is the credited director of Film T20146?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Tinnu Anand
+2. Yuen Woo-ping
+3. Leopoldo Torre Nilsson
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Yuen Woo-ping
+2. Leopoldo Torre Nilsson
+3. Jan Svěrák
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Tinnu Anand
-3. Yuen Woo-ping
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Jan Svěrák
+3. Tinnu Anand
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R25995 names Leopoldo Torre Nilsson.
@@ -7,0 +7 @@
+Record R25995 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R11032 names Tinnu Anand.
+Record R81645 names Yuen Woo-ping.
@@ -6,2 +7,0 @@
-Record R11032 names Tinnu Anand.
-Record R81645 names Yuen Woo-ping.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R81645 names Yuen Woo-ping.
@@ -7 +7,0 @@
-Record R81645 names Yuen Woo-ping.
```

## development/v344-development-19/EASY

L1 sha256 `09ac209fd14c65d9790d422259ecca9225c1de2550aeed2f9177101d70d5835c`; N sha256 `1a33f5adb52ee416313cf31f02f919f653f59854bb2c154e632aebf074389865`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
@@ -18 +12 @@
-Which candidate is the credited director of Film T45562?
+Who is the credited director of Film T45562?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Fridrikh Ermler
+2. Feng Xiaoning
+3. Anil Das
+4. Helmut Käutner
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Feng Xiaoning
+2. Anil Das
+3. Helmut Käutner
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Anil Das
+2. Helmut Käutner
+3. Fridrikh Ermler
+4. Feng Xiaoning
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R84440 names Feng Xiaoning.
@@ -7,0 +7 @@
+Record R84440 names Feng Xiaoning.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R72971 names Fridrikh Ermler.
+Record R43372 names Anil Das.
@@ -6,2 +7,0 @@
-Record R72971 names Fridrikh Ermler.
-Record R43372 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R43372 names Anil Das.
@@ -7 +7,0 @@
-Record R43372 names Anil Das.
```

## development/v344-development-19/MID

L1 sha256 `4698d86df3b1dca828e6f4f85b698b297a532dea016495ab0b0551e2a9f72085`; N sha256 `e4baef0547c7c3b97672bb6dbe725b4d053816dd41ceab8c0aa48b2c1b4c7c6a`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
@@ -20 +14 @@
-Which candidate is the credited director of Film T45562?
+Who is the credited director of Film T45562?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Fridrikh Ermler
+2. Feng Xiaoning
+3. Anil Das
+4. Helmut Käutner
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Feng Xiaoning
+2. Anil Das
+3. Helmut Käutner
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Anil Das
+2. Helmut Käutner
+3. Fridrikh Ermler
+4. Feng Xiaoning
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R84440 names Feng Xiaoning.
@@ -7,0 +7 @@
+Record R84440 names Feng Xiaoning.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R72971 names Fridrikh Ermler.
+Record R43372 names Anil Das.
@@ -6,2 +7,0 @@
-Record R72971 names Fridrikh Ermler.
-Record R43372 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R43372 names Anil Das.
@@ -7 +7,0 @@
-Record R43372 names Anil Das.
```

## development/v344-development-19/HARD

L1 sha256 `56a5fad1f43fbe63232f47cfafbdcb893385e2612e4333d0e08c083186058187`; N sha256 `706edc0c7ed66acf548ed90ae72b0ed2bfd66366df5f43e361ecea35434deaf5`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
@@ -29 +23 @@
-Which candidate is the credited director of Film T45562?
+Who is the credited director of Film T45562?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Fridrikh Ermler
+2. Feng Xiaoning
+3. Anil Das
+4. Helmut Käutner
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Feng Xiaoning
+2. Anil Das
+3. Helmut Käutner
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Fridrikh Ermler
-3. Feng Xiaoning
-4. Anil Das
+1. Anil Das
+2. Helmut Käutner
+3. Fridrikh Ermler
+4. Feng Xiaoning
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R84440 names Feng Xiaoning.
@@ -7,0 +7 @@
+Record R84440 names Feng Xiaoning.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R72971 names Fridrikh Ermler.
+Record R43372 names Anil Das.
@@ -6,2 +7,0 @@
-Record R72971 names Fridrikh Ermler.
-Record R43372 names Anil Das.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R43372 names Anil Das.
@@ -7 +7,0 @@
-Record R43372 names Anil Das.
```

## development/v344-development-20/EASY

L1 sha256 `5000d233d13dc6e7a85b27288f4723c29824d352e00a227bb0a4043fddf84ea1`; N sha256 `13ac322b9e4d049f6039500dc4d8690b8bd58bff045cbf5e698b95ae8c7de3bc`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
@@ -18 +12 @@
-Which candidate is the credited director of Film T71705?
+Who is the credited director of Film T71705?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Armando Robles Godoy
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Yuen Woo-ping
+2. Tinnu Anand
+3. Jan Svěrák
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Tinnu Anand
+2. Jan Svěrák
+3. Armando Robles Godoy
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R46666 names Jan Svěrák.
@@ -7,0 +7 @@
+Record R46666 names Jan Svěrák.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R96295 names Yuen Woo-ping.
+Record R23965 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R96295 names Yuen Woo-ping.
-Record R23965 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R23965 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R23965 names Armando Robles Godoy.
```

## development/v344-development-20/MID

L1 sha256 `914ae6de33b165aae7f4a0a0bc6cccdb5c463a27a2aa3aea90d169972d39f416`; N sha256 `a52c0402559b23c20f53671422a2eb943cecf4014c52259b081197962bc89bb1`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
@@ -20 +14 @@
-Which candidate is the credited director of Film T71705?
+Who is the credited director of Film T71705?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Armando Robles Godoy
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Yuen Woo-ping
+2. Tinnu Anand
+3. Jan Svěrák
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Tinnu Anand
+2. Jan Svěrák
+3. Armando Robles Godoy
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R46666 names Jan Svěrák.
@@ -7,0 +7 @@
+Record R46666 names Jan Svěrák.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R96295 names Yuen Woo-ping.
+Record R23965 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R96295 names Yuen Woo-ping.
-Record R23965 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R23965 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R23965 names Armando Robles Godoy.
```

## development/v344-development-20/HARD

L1 sha256 `81511cc60e250e206b1f2534add933191a0eebad4a3d302cfb03834719b49213`; N sha256 `5677aadbe7df0208219675ff453389c23a5f6d8ef37845d433b87ef9bda08f45`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
@@ -29 +23 @@
-Which candidate is the credited director of Film T71705?
+Who is the credited director of Film T71705?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Armando Robles Godoy
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Yuen Woo-ping
+2. Tinnu Anand
+3. Jan Svěrák
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Armando Robles Godoy
-3. Yuen Woo-ping
-4. Tinnu Anand
+1. Tinnu Anand
+2. Jan Svěrák
+3. Armando Robles Godoy
+4. Yuen Woo-ping
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R46666 names Jan Svěrák.
@@ -7,0 +7 @@
+Record R46666 names Jan Svěrák.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R96295 names Yuen Woo-ping.
+Record R23965 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R96295 names Yuen Woo-ping.
-Record R23965 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R23965 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R23965 names Armando Robles Godoy.
```

## development/v344-development-21/EASY

L1 sha256 `5573df005fd4556ff73c3431903ad537026cc6a74c859e51514c51e04e384e4c`; N sha256 `f1054d47201cbf97ea12e723898859d9b3de8abd767d4f8ebcd4ff02d6e8b9b3`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
@@ -18 +12 @@
-Which candidate is the credited director of Film T17571?
+Who is the credited director of Film T17571?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Rodrigo Grande
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Rolf Schübel
+2. Feng Xiaoning
+3. Fridrikh Ermler
+4. Rodrigo Grande
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Feng Xiaoning
+2. Fridrikh Ermler
+3. Rodrigo Grande
+4. Rolf Schübel
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R52185 names Rolf Schübel.
@@ -7,0 +7 @@
+Record R52185 names Rolf Schübel.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R49538 names Rodrigo Grande.
+Record R18610 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R49538 names Rodrigo Grande.
-Record R18610 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R18610 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R18610 names Feng Xiaoning.
```

## development/v344-development-21/MID

L1 sha256 `78744035d8527e2d1bbb1942ea680a7d5b83c4962d27b9ce0603dde62e7b6cc3`; N sha256 `6013b4d7682f6cebad51b773a31e6503311835a90e989bf5caf30e9bb326fda5`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
@@ -20 +14 @@
-Which candidate is the credited director of Film T17571?
+Who is the credited director of Film T17571?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Rodrigo Grande
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Rolf Schübel
+2. Feng Xiaoning
+3. Fridrikh Ermler
+4. Rodrigo Grande
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Feng Xiaoning
+2. Fridrikh Ermler
+3. Rodrigo Grande
+4. Rolf Schübel
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R52185 names Rolf Schübel.
@@ -7,0 +7 @@
+Record R52185 names Rolf Schübel.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R49538 names Rodrigo Grande.
+Record R18610 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R49538 names Rodrigo Grande.
-Record R18610 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R18610 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R18610 names Feng Xiaoning.
```

## development/v344-development-21/HARD

L1 sha256 `aa3b7eb902c438fdb2947be36ca7dca75026c438cab3250c4c2c4d7686ad477e`; N sha256 `182b0fe0b67dd97d4d5a82d8b3d6e28c6831bdb91e404353383d74a2f17885bb`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
@@ -29 +23 @@
-Which candidate is the credited director of Film T17571?
+Who is the credited director of Film T17571?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Rodrigo Grande
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Fridrikh Ermler
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Rolf Schübel
+2. Feng Xiaoning
+3. Fridrikh Ermler
+4. Rodrigo Grande
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Fridrikh Ermler
-2. Rodrigo Grande
-3. Rolf Schübel
-4. Feng Xiaoning
+1. Feng Xiaoning
+2. Fridrikh Ermler
+3. Rodrigo Grande
+4. Rolf Schübel
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R52185 names Rolf Schübel.
@@ -7,0 +7 @@
+Record R52185 names Rolf Schübel.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R49538 names Rodrigo Grande.
+Record R18610 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R49538 names Rodrigo Grande.
-Record R18610 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R18610 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R18610 names Feng Xiaoning.
```

## development/v344-development-22/EASY

L1 sha256 `0d3e6010dcba9560b1f9d90ecf51353831d8e85a38c492a7cb069a40f08e4433`; N sha256 `3afb714368214274d3e0da62f36bf84963567d4d1e873d08cfe11a99115a134b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
@@ -18 +12 @@
-Which candidate is the credited director of Film T72677?
+Who is the credited director of Film T72677?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Yuen Woo-ping
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Tinnu Anand
+2. Armando Robles Godoy
+3. Leopoldo Torre Nilsson
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Leopoldo Torre Nilsson
+3. Yuen Woo-ping
+4. Tinnu Anand
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R39216 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R39216 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53402 names Leopoldo Torre Nilsson.
+Record R99233 names Yuen Woo-ping.
@@ -6,2 +7,0 @@
-Record R53402 names Leopoldo Torre Nilsson.
-Record R99233 names Yuen Woo-ping.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R99233 names Yuen Woo-ping.
@@ -7 +7,0 @@
-Record R99233 names Yuen Woo-ping.
```

## development/v344-development-22/MID

L1 sha256 `e5745f40c1032e98af485e41cd462f436a4b0d063b5162e9975719a4b4ca5741`; N sha256 `576e33a52301ab206946287fa97d5473e46b2ddb3bb4601d8a304bbdc6a9f05c`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
@@ -20 +14 @@
-Which candidate is the credited director of Film T72677?
+Who is the credited director of Film T72677?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Yuen Woo-ping
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Tinnu Anand
+2. Armando Robles Godoy
+3. Leopoldo Torre Nilsson
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Leopoldo Torre Nilsson
+3. Yuen Woo-ping
+4. Tinnu Anand
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R39216 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R39216 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53402 names Leopoldo Torre Nilsson.
+Record R99233 names Yuen Woo-ping.
@@ -6,2 +7,0 @@
-Record R53402 names Leopoldo Torre Nilsson.
-Record R99233 names Yuen Woo-ping.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R99233 names Yuen Woo-ping.
@@ -7 +7,0 @@
-Record R99233 names Yuen Woo-ping.
```

## development/v344-development-22/HARD

L1 sha256 `6b4dfdf1e6566bbe4ea6eab7b200bae4f0e213371e54800920cca3ec9781ddd8`; N sha256 `9e73c01189e608c087f8e7d4fbac9092731a114f8808f9d146d376fc7fb9bdef`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
@@ -29 +23 @@
-Which candidate is the credited director of Film T72677?
+Who is the credited director of Film T72677?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Yuen Woo-ping
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Tinnu Anand
+2. Armando Robles Godoy
+3. Leopoldo Torre Nilsson
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Yuen Woo-ping
-3. Tinnu Anand
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Leopoldo Torre Nilsson
+3. Yuen Woo-ping
+4. Tinnu Anand
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R39216 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R39216 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53402 names Leopoldo Torre Nilsson.
+Record R99233 names Yuen Woo-ping.
@@ -6,2 +7,0 @@
-Record R53402 names Leopoldo Torre Nilsson.
-Record R99233 names Yuen Woo-ping.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R99233 names Yuen Woo-ping.
@@ -7 +7,0 @@
-Record R99233 names Yuen Woo-ping.
```

## development/v344-development-23/EASY

L1 sha256 `c9fdcd02818057187355ad4c30187494856033f0d2adb3cc49832e6acde9d155`; N sha256 `444b3011f2ec50ba335ea7305e682eba9639338594e2f544d02913eb95a4b4d9`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
@@ -18 +12 @@
-Which candidate is the credited director of Film T98590?
+Who is the credited director of Film T98590?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Rodrigo Grande
+2. Gu Changwei
+3. Fridrikh Ermler
+4. Anil Das
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Gu Changwei
+2. Fridrikh Ermler
+3. Anil Das
+4. Rodrigo Grande
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Anil Das
+3. Rodrigo Grande
+4. Gu Changwei
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R47546 names Gu Changwei.
@@ -7,0 +7 @@
+Record R47546 names Gu Changwei.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R77647 names Anil Das.
+Record R31727 names Rodrigo Grande.
@@ -6,2 +7,0 @@
-Record R77647 names Anil Das.
-Record R31727 names Rodrigo Grande.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R31727 names Rodrigo Grande.
@@ -7 +7,0 @@
-Record R31727 names Rodrigo Grande.
```

## development/v344-development-23/MID

L1 sha256 `b3d02e268e8a3eebfdefe58266fc1ca5ba845875f86348c7721d303af0424dda`; N sha256 `9763c5413360c0c06cf1bb907e15055fa75fedcdfd5c062ac44c7a648b9d32b0`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
@@ -20 +14 @@
-Which candidate is the credited director of Film T98590?
+Who is the credited director of Film T98590?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Rodrigo Grande
+2. Gu Changwei
+3. Fridrikh Ermler
+4. Anil Das
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Gu Changwei
+2. Fridrikh Ermler
+3. Anil Das
+4. Rodrigo Grande
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Anil Das
+3. Rodrigo Grande
+4. Gu Changwei
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R47546 names Gu Changwei.
@@ -7,0 +7 @@
+Record R47546 names Gu Changwei.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R77647 names Anil Das.
+Record R31727 names Rodrigo Grande.
@@ -6,2 +7,0 @@
-Record R77647 names Anil Das.
-Record R31727 names Rodrigo Grande.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R31727 names Rodrigo Grande.
@@ -7 +7,0 @@
-Record R31727 names Rodrigo Grande.
```

## development/v344-development-23/HARD

L1 sha256 `cc1d98b3689a66dc2bbf2059eb9ff39018123fe988f430cb318aa87e8a17f76d`; N sha256 `5e217bbee253670dc89790654a5d790df7407934a5ed4819503fac87b372023a`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
@@ -29 +23 @@
-Which candidate is the credited director of Film T98590?
+Who is the credited director of Film T98590?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Rodrigo Grande
+2. Gu Changwei
+3. Fridrikh Ermler
+4. Anil Das
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Gu Changwei
+2. Fridrikh Ermler
+3. Anil Das
+4. Rodrigo Grande
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Anil Das
-2. Rodrigo Grande
-3. Gu Changwei
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Anil Das
+3. Rodrigo Grande
+4. Gu Changwei
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R47546 names Gu Changwei.
@@ -7,0 +7 @@
+Record R47546 names Gu Changwei.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R77647 names Anil Das.
+Record R31727 names Rodrigo Grande.
@@ -6,2 +7,0 @@
-Record R77647 names Anil Das.
-Record R31727 names Rodrigo Grande.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R31727 names Rodrigo Grande.
@@ -7 +7,0 @@
-Record R31727 names Rodrigo Grande.
```

## development/v344-development-24/EASY

L1 sha256 `bd7abaa60c7efd48768a328c0a83115fe92bcda551dbd0c819a7397ba45af8af`; N sha256 `06807dfccc1a3b687fc71c767b47cf5acedc05beaf05a987ec1ad19ef293f389`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
@@ -18 +12 @@
-Which candidate is the credited director of Film T74644?
+Who is the credited director of Film T74644?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Yuen Woo-ping
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Rahul Rawail
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Rahul Rawail
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R31436 names Yuen Woo-ping.
@@ -7,0 +7 @@
+Record R31436 names Yuen Woo-ping.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14519 names Ildikó Enyedi.
+Record R47408 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R14519 names Ildikó Enyedi.
-Record R47408 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R47408 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R47408 names Leopoldo Torre Nilsson.
```

## development/v344-development-24/MID

L1 sha256 `d5fbe138ae4b8aaa02c04c800aa502edc096847ebf70147132bff8103b16e5c4`; N sha256 `f68ca8795d532602084b7c0d9ea1628c39de39fe51a7729d177c9a5d51048adb`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
@@ -20 +14 @@
-Which candidate is the credited director of Film T74644?
+Who is the credited director of Film T74644?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Yuen Woo-ping
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Rahul Rawail
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Rahul Rawail
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R31436 names Yuen Woo-ping.
@@ -7,0 +7 @@
+Record R31436 names Yuen Woo-ping.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14519 names Ildikó Enyedi.
+Record R47408 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R14519 names Ildikó Enyedi.
-Record R47408 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R47408 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R47408 names Leopoldo Torre Nilsson.
```

## development/v344-development-24/HARD

L1 sha256 `ca1647c9a6b9522186582853b5e3659155074f64ad190c884fb42edb9578f1cd`; N sha256 `358628494c2c506b422d5b908d94f81e578e9d8f4e5bd5700c386395471a0e34`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
@@ -29 +23 @@
-Which candidate is the credited director of Film T74644?
+Who is the credited director of Film T74644?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Yuen Woo-ping
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Rahul Rawail
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Ildikó Enyedi
+2. Leopoldo Torre Nilsson
+3. Rahul Rawail
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rahul Rawail
-2. Yuen Woo-ping
-3. Ildikó Enyedi
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R31436 names Yuen Woo-ping.
@@ -7,0 +7 @@
+Record R31436 names Yuen Woo-ping.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14519 names Ildikó Enyedi.
+Record R47408 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R14519 names Ildikó Enyedi.
-Record R47408 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R47408 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R47408 names Leopoldo Torre Nilsson.
```

## old/dev-04/EASY

L1 sha256 `ce9af672c4a254f75e817bddc43bb314e48f2b9dd37abd3fea0e80b7fa92cc7d`; N sha256 `522e5b496d60915918fdbb64a3e80ea3001e3c1fc22b700d5a6cd5d28fa42199`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
@@ -18 +12 @@
-Which candidate is the credited director of Film T34217?
+Who is the credited director of Film T34217?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Rahul Rawail
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48842 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R48842 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R34060 names Leopoldo Torre Nilsson.
+Record R31383 names Tinnu Anand.
@@ -6,2 +7,0 @@
-Record R34060 names Leopoldo Torre Nilsson.
-Record R31383 names Tinnu Anand.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R31383 names Tinnu Anand.
@@ -7 +7,0 @@
-Record R31383 names Tinnu Anand.
```

## old/dev-04/MID

L1 sha256 `4de0a4b58e6fec2f901c3b7a7f4a8ab284e3fcc17c00ae58a71ea80753959162`; N sha256 `c76485ab8e749e04ae1778690c3e07d0b536b2f0a8610df1a680b0ce531c44cb`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
@@ -20 +14 @@
-Which candidate is the credited director of Film T34217?
+Who is the credited director of Film T34217?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Rahul Rawail
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48842 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R48842 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R34060 names Leopoldo Torre Nilsson.
+Record R31383 names Tinnu Anand.
@@ -6,2 +7,0 @@
-Record R34060 names Leopoldo Torre Nilsson.
-Record R31383 names Tinnu Anand.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R31383 names Tinnu Anand.
@@ -7 +7,0 @@
-Record R31383 names Tinnu Anand.
```

## old/dev-04/HARD

L1 sha256 `3c965819d518989d981f66c8458cc26c4262751718f0a32806fa5bd5abcb7934`; N sha256 `b13e8cd8febdab58ba8d9a5a8f4bdfb55aeb01ea9b1310500f57a8a27d79fcf4`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
@@ -29 +23 @@
-Which candidate is the credited director of Film T34217?
+Who is the credited director of Film T34217?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Tinnu Anand
-2. Armando Robles Godoy
-3. Leopoldo Torre Nilsson
-4. Rahul Rawail
+1. Rahul Rawail
+2. Tinnu Anand
+3. Armando Robles Godoy
+4. Leopoldo Torre Nilsson
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48842 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R48842 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R34060 names Leopoldo Torre Nilsson.
+Record R31383 names Tinnu Anand.
@@ -6,2 +7,0 @@
-Record R34060 names Leopoldo Torre Nilsson.
-Record R31383 names Tinnu Anand.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R31383 names Tinnu Anand.
@@ -7 +7,0 @@
-Record R31383 names Tinnu Anand.
```

## old/dev-07/EASY

L1 sha256 `31c8cd8dc0f475435482bde034b4a85e31a542d451a8025cb4fd4ae877d16207`; N sha256 `1d4ff4bcb4d7fbfb40e8f21bc0116c5d2c3e1f7d1f0306623609e6507bad323c`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
@@ -18 +12 @@
-Which candidate is the credited director of Film T66029?
+Who is the credited director of Film T66029?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. James Goldstone
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R35006 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R35006 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R58951 names León Klimovsky.
+Record R91884 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R58951 names León Klimovsky.
-Record R91884 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R91884 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R91884 names Marcello Fondato.
```

## old/dev-07/MID

L1 sha256 `fd6c5ab0877fdb866f437fe1934555f7342f5b5e7eb915195d6a7677ee1d5974`; N sha256 `b6ebd21e5dab21882a9eae31e46d5eedccd4906b22ea5e220799206a0aa88e5e`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
@@ -20 +14 @@
-Which candidate is the credited director of Film T66029?
+Who is the credited director of Film T66029?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. James Goldstone
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R35006 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R35006 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R58951 names León Klimovsky.
+Record R91884 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R58951 names León Klimovsky.
-Record R91884 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R91884 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R91884 names Marcello Fondato.
```

## old/dev-07/HARD

L1 sha256 `c23158e34b18dba536e142809f10af4f1863c80354aa2af9be07832ac85f9860`; N sha256 `efef152e1f62f708ae2638bb06e608ada744b9a5c5f9d0c867ce7af58349b6fa`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
@@ -29 +23 @@
-Which candidate is the credited director of Film T66029?
+Who is the credited director of Film T66029?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. León Klimovsky
-2. Walter Hugo Khouri
-3. Marcello Fondato
-4. James Goldstone
+1. James Goldstone
+2. León Klimovsky
+3. Walter Hugo Khouri
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R35006 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R35006 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R58951 names León Klimovsky.
+Record R91884 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R58951 names León Klimovsky.
-Record R91884 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R91884 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R91884 names Marcello Fondato.
```

## old/dev-05/EASY

L1 sha256 `0c78cdb91f3023c882b52ce903dfe98a1495803ff411e5c53cd3f6d5cc4d6abe`; N sha256 `fbbce21347e05f1f99b792b3563e99749b3954c8f773a37083417f1fbbf41099`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
@@ -18 +12 @@
-Which candidate is the credited director of Film T89245?
+Who is the credited director of Film T89245?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Helmut Käutner
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R18891 names Feng Xiaoning.
@@ -7,0 +7 @@
+Record R18891 names Feng Xiaoning.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41884 names Fridrikh Ermler.
+Record R14678 names Rolf Schübel.
@@ -6,2 +7,0 @@
-Record R41884 names Fridrikh Ermler.
-Record R14678 names Rolf Schübel.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R14678 names Rolf Schübel.
@@ -7 +7,0 @@
-Record R14678 names Rolf Schübel.
```

## old/dev-05/MID

L1 sha256 `7d22e284e3c3396ac521e0355d2bf9c260b2a9b7bc8adf64145419bda922a1e6`; N sha256 `79b1a2d96044814bc63eae9b165328219b365b1e2fd13c8b159813f50b6fbecc`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
@@ -20 +14 @@
-Which candidate is the credited director of Film T89245?
+Who is the credited director of Film T89245?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Helmut Käutner
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R18891 names Feng Xiaoning.
@@ -7,0 +7 @@
+Record R18891 names Feng Xiaoning.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41884 names Fridrikh Ermler.
+Record R14678 names Rolf Schübel.
@@ -6,2 +7,0 @@
-Record R41884 names Fridrikh Ermler.
-Record R14678 names Rolf Schübel.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R14678 names Rolf Schübel.
@@ -7 +7,0 @@
-Record R14678 names Rolf Schübel.
```

## old/dev-05/HARD

L1 sha256 `6e789251d6ed49530546344c7e302a93aa18231b69a3d91e11a26129f504d47f`; N sha256 `040858c8c65ff14a075486804a607509c60a92d9fb66e79168461087bc90b492`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
@@ -29 +23 @@
-Which candidate is the credited director of Film T89245?
+Who is the credited director of Film T89245?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Feng Xiaoning
-3. Helmut Käutner
-4. Fridrikh Ermler
+1. Fridrikh Ermler
+2. Rolf Schübel
+3. Feng Xiaoning
+4. Helmut Käutner
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R18891 names Feng Xiaoning.
@@ -7,0 +7 @@
+Record R18891 names Feng Xiaoning.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41884 names Fridrikh Ermler.
+Record R14678 names Rolf Schübel.
@@ -6,2 +7,0 @@
-Record R41884 names Fridrikh Ermler.
-Record R14678 names Rolf Schübel.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R14678 names Rolf Schübel.
@@ -7 +7,0 @@
-Record R14678 names Rolf Schübel.
```

## old/dev-01/EASY

L1 sha256 `40207f6fb7cf96b1fd42d64974972b6820156a8446a4f7af7a22146e5f7a8d38`; N sha256 `380b45a5abb33bf8eeaaf5413081fff742f9bb708a5f60c307007ade8c43964e`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
@@ -18 +12 @@
-Which candidate is the credited director of Film T27036?
+Who is the credited director of Film T27036?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Walter Hugo Khouri
+3. Marcello Fondato
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R25049 names Vojtěch Jasný.
@@ -7,0 +7 @@
+Record R25049 names Vojtěch Jasný.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R44296 names James Goldstone.
+Record R28362 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R44296 names James Goldstone.
-Record R28362 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R28362 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R28362 names Marcello Fondato.
```

## old/dev-01/MID

L1 sha256 `6f6b523dd3c36c2a45bfb2a7195c32d2e26020fab66e97a1722c93d302598c3b`; N sha256 `3c92ef0e9310c0f33e2bfab84cc6e4b601def4b385712cc77c45b0ccad568883`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
@@ -20 +14 @@
-Which candidate is the credited director of Film T27036?
+Who is the credited director of Film T27036?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Walter Hugo Khouri
+3. Marcello Fondato
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R25049 names Vojtěch Jasný.
@@ -7,0 +7 @@
+Record R25049 names Vojtěch Jasný.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R44296 names James Goldstone.
+Record R28362 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R44296 names James Goldstone.
-Record R28362 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R28362 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R28362 names Marcello Fondato.
```

## old/dev-01/HARD

L1 sha256 `39de8155ba974e72a667b8002486731a57abe1e65c6a68d6802982a22a0f7627`; N sha256 `067d4dd8d920836d54c67c8257f7b878215a99c5043d333bf23a94e14dee8659`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
@@ -29 +23 @@
-Which candidate is the credited director of Film T27036?
+Who is the credited director of Film T27036?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Walter Hugo Khouri
-2. Marcello Fondato
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Walter Hugo Khouri
+3. Marcello Fondato
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R25049 names Vojtěch Jasný.
@@ -7,0 +7 @@
+Record R25049 names Vojtěch Jasný.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R44296 names James Goldstone.
+Record R28362 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R44296 names James Goldstone.
-Record R28362 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R28362 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R28362 names Marcello Fondato.
```

## old/dev-06/EASY

L1 sha256 `e518f38fa6914bef512205bf5dd6c84f690b7842d0060c9a224435a8d49f690e`; N sha256 `a22632b81564c7868812694d541b7e8fbd4910657df60d0c88370633df94c23f`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
@@ -18 +12 @@
-Which candidate is the credited director of Film T12112?
+Who is the credited director of Film T12112?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Gu Changwei
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48845 names Rolf Schübel.
@@ -7,0 +7 @@
+Record R48845 names Rolf Schübel.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R27156 names Anil Das.
+Record R62230 names Gu Changwei.
@@ -6,2 +7,0 @@
-Record R27156 names Anil Das.
-Record R62230 names Gu Changwei.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R62230 names Gu Changwei.
@@ -7 +7,0 @@
-Record R62230 names Gu Changwei.
```

## old/dev-06/MID

L1 sha256 `b517a385a03c86ba63c773fd6b50b2786dd7787fc0f54ac301b066da7a2cce39`; N sha256 `7963ee81c6fd4e75d00b2b6122b39b0a79843d0edd01f128bffcf40cb731200f`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
@@ -20 +14 @@
-Which candidate is the credited director of Film T12112?
+Who is the credited director of Film T12112?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Gu Changwei
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48845 names Rolf Schübel.
@@ -7,0 +7 @@
+Record R48845 names Rolf Schübel.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R27156 names Anil Das.
+Record R62230 names Gu Changwei.
@@ -6,2 +7,0 @@
-Record R27156 names Anil Das.
-Record R62230 names Gu Changwei.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R62230 names Gu Changwei.
@@ -7 +7,0 @@
-Record R62230 names Gu Changwei.
```

## old/dev-06/HARD

L1 sha256 `d8de18a4c1f466cee1ee530c3d43148318fb87df545a2b8da5d62de25428d91f`; N sha256 `57949021fc6c6719af2e5a1134016d0510c3934860f39ed93401a574a65f7943`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
@@ -29 +23 @@
-Which candidate is the credited director of Film T12112?
+Who is the credited director of Film T12112?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rolf Schübel
-2. Rodrigo Grande
-3. Anil Das
-4. Gu Changwei
+1. Gu Changwei
+2. Rolf Schübel
+3. Rodrigo Grande
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48845 names Rolf Schübel.
@@ -7,0 +7 @@
+Record R48845 names Rolf Schübel.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R27156 names Anil Das.
+Record R62230 names Gu Changwei.
@@ -6,2 +7,0 @@
-Record R27156 names Anil Das.
-Record R62230 names Gu Changwei.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R62230 names Gu Changwei.
@@ -7 +7,0 @@
-Record R62230 names Gu Changwei.
```

## old/dev-08/EASY

L1 sha256 `e65f7b134745a871cefda18d3a110b9a9dee10b1107135ebc02b84644ee79ee1`; N sha256 `002686d8b047352a049f944944f99ecf96d2a7420acff0c6845625d473d698ec`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
@@ -18 +12 @@
-Which candidate is the credited director of Film T49524?
+Who is the credited director of Film T49524?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Ildikó Enyedi
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R80186 names Yuen Woo-ping.
@@ -7,0 +7 @@
+Record R80186 names Yuen Woo-ping.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41387 names Tinnu Anand.
+Record R30932 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R41387 names Tinnu Anand.
-Record R30932 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30932 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R30932 names Rahul Rawail.
```

## old/dev-08/MID

L1 sha256 `482384596e88044480d760c5b82d7b2821d6938e0bf23f0535a6f716eafacdc8`; N sha256 `c2921f16ab37bb45cff45754711da15555fa5188258c072995a6d0819c05bdb8`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
@@ -20 +14 @@
-Which candidate is the credited director of Film T49524?
+Who is the credited director of Film T49524?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Ildikó Enyedi
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R80186 names Yuen Woo-ping.
@@ -7,0 +7 @@
+Record R80186 names Yuen Woo-ping.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41387 names Tinnu Anand.
+Record R30932 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R41387 names Tinnu Anand.
-Record R30932 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30932 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R30932 names Rahul Rawail.
```

## old/dev-08/HARD

L1 sha256 `ac3e5c8bc347bf33499f39629634fda07c576a4bd53ea917706c570a27b66552`; N sha256 `2947eb6d8c4589e24e3c890a3c3a6cf20e74e55c3942003b42e19f22c6d0b1b7`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
@@ -29 +23 @@
-Which candidate is the credited director of Film T49524?
+Who is the credited director of Film T49524?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
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
--- L1
+++ L3
@@ -4,4 +4,4 @@
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
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Tinnu Anand
-3. Ildikó Enyedi
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Tinnu Anand
+4. Ildikó Enyedi
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R80186 names Yuen Woo-ping.
@@ -7,0 +7 @@
+Record R80186 names Yuen Woo-ping.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41387 names Tinnu Anand.
+Record R30932 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R41387 names Tinnu Anand.
-Record R30932 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R30932 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R30932 names Rahul Rawail.
```

## confirmation/v344-confirmation-01/EASY

L1 sha256 `ab0191ddfe0466eb1f1f7f263c0cc33dd3b679b9f360fb02684acf157f8cf6d7`; N sha256 `b4e2175bea73eab854f53b54308144c40384680ab92e8ea579d90ade85a97b9a`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
@@ -18 +12 @@
-Which candidate is the credited director of Film T16005?
+Who is the credited director of Film T16005?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Vojtěch Jasný
+2. Marcello Fondato
+3. León Klimovsky
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Robert P. Kerr
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Robert P. Kerr
+3. Vojtěch Jasný
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R43572 names Robert P. Kerr.
@@ -7,0 +7 @@
+Record R43572 names Robert P. Kerr.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42080 names León Klimovsky.
+Record R18305 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R42080 names León Klimovsky.
-Record R18305 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R18305 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R18305 names Marcello Fondato.
```

## confirmation/v344-confirmation-01/MID

L1 sha256 `346e4ad5531e6afd7d535a12825a34935e067c0a75274ed69a2b84fb4d85d440`; N sha256 `c5764c86580c3c258f55196682e265d06d2e0b56f9aeefabe0d68da31bcb037e`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
@@ -20 +14 @@
-Which candidate is the credited director of Film T16005?
+Who is the credited director of Film T16005?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Vojtěch Jasný
+2. Marcello Fondato
+3. León Klimovsky
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Robert P. Kerr
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Robert P. Kerr
+3. Vojtěch Jasný
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R43572 names Robert P. Kerr.
@@ -7,0 +7 @@
+Record R43572 names Robert P. Kerr.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42080 names León Klimovsky.
+Record R18305 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R42080 names León Klimovsky.
-Record R18305 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R18305 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R18305 names Marcello Fondato.
```

## confirmation/v344-confirmation-01/HARD

L1 sha256 `b6e0b61cf4fff28c81c8bcceb83893c3e57b29f5b8951ef7a84b45c4729295b1`; N sha256 `a4854075d0684da464e6c52584781de2ed5b518e947eef735fdf05a372656dc3`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
@@ -29 +23 @@
-Which candidate is the credited director of Film T16005?
+Who is the credited director of Film T16005?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Vojtěch Jasný
+2. Marcello Fondato
+3. León Klimovsky
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. Marcello Fondato
+2. León Klimovsky
+3. Robert P. Kerr
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Vojtěch Jasný
-3. Marcello Fondato
-4. León Klimovsky
+1. León Klimovsky
+2. Robert P. Kerr
+3. Vojtěch Jasný
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R43572 names Robert P. Kerr.
@@ -7,0 +7 @@
+Record R43572 names Robert P. Kerr.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42080 names León Klimovsky.
+Record R18305 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R42080 names León Klimovsky.
-Record R18305 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R18305 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R18305 names Marcello Fondato.
```

## confirmation/v344-confirmation-02/EASY

L1 sha256 `98f0c8ec38a9c5db78682bd0479bd428c74e8a5e61b204401136b83ad760267f`; N sha256 `9e69d923974dd3cfd3ca8cce9190d72a6106a0e2018505b58c211d95cfeff53c`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
@@ -18 +12 @@
-Which candidate is the credited director of Film T34219?
+Who is the credited director of Film T34219?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Ildikó Enyedi
+2. Armando Robles Godoy
+3. Rahul Rawail
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Armando Robles Godoy
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Ildikó Enyedi
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20615 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R20615 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42272 names Armando Robles Godoy.
+Record R82446 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R42272 names Armando Robles Godoy.
-Record R82446 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R82446 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R82446 names Rahul Rawail.
```

## confirmation/v344-confirmation-02/MID

L1 sha256 `2fbfe4413287305e5d76b1374b6251586596398d0b94af125e13e7b32cebb3eb`; N sha256 `231296e393c536f52a9f272dc8e95caec3cc95d11a1830bb22fb80a133901de5`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
@@ -20 +14 @@
-Which candidate is the credited director of Film T34219?
+Who is the credited director of Film T34219?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Ildikó Enyedi
+2. Armando Robles Godoy
+3. Rahul Rawail
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Armando Robles Godoy
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Ildikó Enyedi
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20615 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R20615 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42272 names Armando Robles Godoy.
+Record R82446 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R42272 names Armando Robles Godoy.
-Record R82446 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R82446 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R82446 names Rahul Rawail.
```

## confirmation/v344-confirmation-02/HARD

L1 sha256 `e30a4d9bef490cfaefd44f3ee61040362c66a5e6e6faac02757526561f3add28`; N sha256 `0d2b0dad30afb1c9c9ee8b756e930178e679a7a294a98bf3cd7e0d8e67e23d40`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
@@ -29 +23 @@
-Which candidate is the credited director of Film T34219?
+Who is the credited director of Film T34219?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Ildikó Enyedi
+2. Armando Robles Godoy
+3. Rahul Rawail
+4. Yuen Woo-ping
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Armando Robles Godoy
+2. Rahul Rawail
+3. Yuen Woo-ping
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Yuen Woo-ping
-2. Ildikó Enyedi
-3. Armando Robles Godoy
-4. Rahul Rawail
+1. Rahul Rawail
+2. Yuen Woo-ping
+3. Ildikó Enyedi
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R20615 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R20615 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42272 names Armando Robles Godoy.
+Record R82446 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R42272 names Armando Robles Godoy.
-Record R82446 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R82446 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R82446 names Rahul Rawail.
```

## confirmation/v344-confirmation-03/EASY

L1 sha256 `0fc0e3c9eacde2639184996d4665bfca00b121caea4c2e80e5b6f27eb772e117`; N sha256 `ff3c0ea0f82370f76f32ca3c54fe29b05dbd0b173da53da1f866aaf78671de0d`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
@@ -18 +12 @@
-Which candidate is the credited director of Film T68568?
+Who is the credited director of Film T68568?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Rahul Rawail
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Jan Svěrák
+4. Rahul Rawail
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Jan Svěrák
+3. Rahul Rawail
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R50583 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R50583 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R10646 names Ildikó Enyedi.
+Record R70409 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R10646 names Ildikó Enyedi.
-Record R70409 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R70409 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R70409 names Rahul Rawail.
```

## confirmation/v344-confirmation-03/MID

L1 sha256 `9dc87eb3436ec3dd8acb61687fed6702ae2de0a53eca638da684cd95081e1371`; N sha256 `c11a77ad87b5bf725e49a82cf7a471f67d20c3d5617d795604015261a55dd1a7`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
@@ -20 +14 @@
-Which candidate is the credited director of Film T68568?
+Who is the credited director of Film T68568?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Rahul Rawail
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Jan Svěrák
+4. Rahul Rawail
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Jan Svěrák
+3. Rahul Rawail
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R50583 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R50583 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R10646 names Ildikó Enyedi.
+Record R70409 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R10646 names Ildikó Enyedi.
-Record R70409 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R70409 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R70409 names Rahul Rawail.
```

## confirmation/v344-confirmation-03/HARD

L1 sha256 `3cd7abbedfef2bc9f52bfd69fd92560c91339bda0df2d5fc7cb56b96d89f2b86`; N sha256 `a9edd825e0e0a9c84164589ddada082741adf5943659d526f986df49c0b33c5f`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
@@ -29 +23 @@
-Which candidate is the credited director of Film T68568?
+Who is the credited director of Film T68568?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Rahul Rawail
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Jan Svěrák
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Jan Svěrák
+4. Rahul Rawail
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Jan Svěrák
-2. Rahul Rawail
-3. Armando Robles Godoy
-4. Ildikó Enyedi
+1. Ildikó Enyedi
+2. Jan Svěrák
+3. Rahul Rawail
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R50583 names Armando Robles Godoy.
@@ -7,0 +7 @@
+Record R50583 names Armando Robles Godoy.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R10646 names Ildikó Enyedi.
+Record R70409 names Rahul Rawail.
@@ -6,2 +7,0 @@
-Record R10646 names Ildikó Enyedi.
-Record R70409 names Rahul Rawail.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R70409 names Rahul Rawail.
@@ -7 +7,0 @@
-Record R70409 names Rahul Rawail.
```

## confirmation/v344-confirmation-04/EASY

L1 sha256 `15e449e2fe5501ab02d85fef91fc2d638192563f758ef92a04544de21265bb2b`; N sha256 `7e3a3506a2156aeedb1f1dd13a2634970dc9a496a542bacffa3f52551be36306`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
@@ -18 +12 @@
-Which candidate is the credited director of Film T13991?
+Who is the credited director of Film T13991?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. Walter Hugo Khouri
+2. Robert P. Kerr
+3. León Klimovsky
+4. Marcello Fondato
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. Robert P. Kerr
+2. León Klimovsky
+3. Marcello Fondato
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. León Klimovsky
+2. Marcello Fondato
+3. Walter Hugo Khouri
+4. Robert P. Kerr
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48117 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R48117 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53667 names León Klimovsky.
+Record R17834 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R53667 names León Klimovsky.
-Record R17834 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R17834 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R17834 names Robert P. Kerr.
```

## confirmation/v344-confirmation-04/MID

L1 sha256 `6a70818733418327f672205868743a2c49e208b83e009309f7b641672236fa14`; N sha256 `64b07cb4437de4101561ac323718040e628378d922c23f681720380818195fef`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
@@ -20 +14 @@
-Which candidate is the credited director of Film T13991?
+Who is the credited director of Film T13991?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. Walter Hugo Khouri
+2. Robert P. Kerr
+3. León Klimovsky
+4. Marcello Fondato
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. Robert P. Kerr
+2. León Klimovsky
+3. Marcello Fondato
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. León Klimovsky
+2. Marcello Fondato
+3. Walter Hugo Khouri
+4. Robert P. Kerr
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48117 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R48117 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53667 names León Klimovsky.
+Record R17834 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R53667 names León Klimovsky.
-Record R17834 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R17834 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R17834 names Robert P. Kerr.
```

## confirmation/v344-confirmation-04/HARD

L1 sha256 `c2321657edf0e0577eaa552f7069c8ef5c2d8154530e8f16c03fb0a6b72077fe`; N sha256 `55405fd01073e70c8240e3ca55d343a5fe2d4b7c7d2ae7506821dd665e39dd5a`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
@@ -29 +23 @@
-Which candidate is the credited director of Film T13991?
+Who is the credited director of Film T13991?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. Walter Hugo Khouri
+2. Robert P. Kerr
+3. León Klimovsky
+4. Marcello Fondato
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. Robert P. Kerr
+2. León Klimovsky
+3. Marcello Fondato
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Marcello Fondato
-2. Walter Hugo Khouri
-3. Robert P. Kerr
-4. León Klimovsky
+1. León Klimovsky
+2. Marcello Fondato
+3. Walter Hugo Khouri
+4. Robert P. Kerr
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48117 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R48117 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R53667 names León Klimovsky.
+Record R17834 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R53667 names León Klimovsky.
-Record R17834 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R17834 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R17834 names Robert P. Kerr.
```

## confirmation/v344-confirmation-05/EASY

L1 sha256 `57e7dacccbb92a356738d46719ea58f8e895d5de34b14dc3ae6afeb034d69983`; N sha256 `34d462f56ba346d5ac60f8ecf39218cbace4a47ffef02b89e0d3fd6361c2c4a7`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
@@ -18 +12 @@
-Which candidate is the credited director of Film T83771?
+Who is the credited director of Film T83771?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Gu Changwei
+2. Anil Das
+3. Helmut Käutner
+4. Rodrigo Grande
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Anil Das
+2. Helmut Käutner
+3. Rodrigo Grande
+4. Gu Changwei
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Helmut Käutner
+2. Rodrigo Grande
+3. Gu Changwei
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R44365 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R44365 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14297 names Gu Changwei.
+Record R49071 names Helmut Käutner.
@@ -6,2 +7,0 @@
-Record R14297 names Gu Changwei.
-Record R49071 names Helmut Käutner.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R49071 names Helmut Käutner.
@@ -7 +7,0 @@
-Record R49071 names Helmut Käutner.
```

## confirmation/v344-confirmation-05/MID

L1 sha256 `b2e3ddcacedf5a00275d3b2c36f98ce940907704c18bf88f21363886eef9d031`; N sha256 `394fb6cc4dc05d6b78d881c69047c1c4f0c7e760bb9044ee8d75774f3ae6b06e`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
@@ -20 +14 @@
-Which candidate is the credited director of Film T83771?
+Who is the credited director of Film T83771?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Gu Changwei
+2. Anil Das
+3. Helmut Käutner
+4. Rodrigo Grande
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Anil Das
+2. Helmut Käutner
+3. Rodrigo Grande
+4. Gu Changwei
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Helmut Käutner
+2. Rodrigo Grande
+3. Gu Changwei
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R44365 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R44365 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14297 names Gu Changwei.
+Record R49071 names Helmut Käutner.
@@ -6,2 +7,0 @@
-Record R14297 names Gu Changwei.
-Record R49071 names Helmut Käutner.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R49071 names Helmut Käutner.
@@ -7 +7,0 @@
-Record R49071 names Helmut Käutner.
```

## confirmation/v344-confirmation-05/HARD

L1 sha256 `f056ed78aa1fed7eaad394b3e54491b6fc4e29bc9a5f676ad566149ccc82bd3b`; N sha256 `eec795163394a94e33b8fc9f950224999fb02e4fdab0f6c6166e6ebbeba4cc31`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
@@ -29 +23 @@
-Which candidate is the credited director of Film T83771?
+Who is the credited director of Film T83771?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Gu Changwei
+2. Anil Das
+3. Helmut Käutner
+4. Rodrigo Grande
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Anil Das
+2. Helmut Käutner
+3. Rodrigo Grande
+4. Gu Changwei
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Gu Changwei
-3. Anil Das
-4. Helmut Käutner
+1. Helmut Käutner
+2. Rodrigo Grande
+3. Gu Changwei
+4. Anil Das
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R44365 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R44365 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R14297 names Gu Changwei.
+Record R49071 names Helmut Käutner.
@@ -6,2 +7,0 @@
-Record R14297 names Gu Changwei.
-Record R49071 names Helmut Käutner.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R49071 names Helmut Käutner.
@@ -7 +7,0 @@
-Record R49071 names Helmut Käutner.
```

## confirmation/v344-confirmation-06/EASY

L1 sha256 `1d17a039f873b13dadfff0fec00ff0f11a4cc6ab787415ef482f042860964dbb`; N sha256 `4aa14a276449ac74b5270d153d2f73b220fb5f741e81cebb9fd73afbaa515160`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
@@ -18 +12 @@
-Which candidate is the credited director of Film T21269?
+Who is the credited director of Film T21269?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. Walter Hugo Khouri
+2. León Klimovsky
+3. Marcello Fondato
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. León Klimovsky
+2. Marcello Fondato
+3. Vojtěch Jasný
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. Marcello Fondato
+2. Vojtěch Jasný
+3. Walter Hugo Khouri
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14908 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R14908 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R76025 names León Klimovsky.
+Record R46110 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R76025 names León Klimovsky.
-Record R46110 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R46110 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R46110 names Marcello Fondato.
```

## confirmation/v344-confirmation-06/MID

L1 sha256 `498d51b45b9f37f29ee083672b788c451c0123d5008960d13470f212eb80d954`; N sha256 `f5b4d4dabe84f71f140f29e9517435b05cc980cc1b25fbac9e516a8d8d4e5e89`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
@@ -20 +14 @@
-Which candidate is the credited director of Film T21269?
+Who is the credited director of Film T21269?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. Walter Hugo Khouri
+2. León Klimovsky
+3. Marcello Fondato
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. León Klimovsky
+2. Marcello Fondato
+3. Vojtěch Jasný
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. Marcello Fondato
+2. Vojtěch Jasný
+3. Walter Hugo Khouri
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14908 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R14908 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R76025 names León Klimovsky.
+Record R46110 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R76025 names León Klimovsky.
-Record R46110 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R46110 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R46110 names Marcello Fondato.
```

## confirmation/v344-confirmation-06/HARD

L1 sha256 `bd8a774424e6a905f7124a95fd6711132ed590a50d54305129c64b0f45b4116e`; N sha256 `6d206d0d4855b3c71b3a0d361b100ad8abd16684dfc40bac2f832126a2e60bf4`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
@@ -29 +23 @@
-Which candidate is the credited director of Film T21269?
+Who is the credited director of Film T21269?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. Walter Hugo Khouri
+2. León Klimovsky
+3. Marcello Fondato
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. León Klimovsky
+2. Marcello Fondato
+3. Vojtěch Jasný
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Walter Hugo Khouri
-3. León Klimovsky
-4. Marcello Fondato
+1. Marcello Fondato
+2. Vojtěch Jasný
+3. Walter Hugo Khouri
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14908 names Walter Hugo Khouri.
@@ -7,0 +7 @@
+Record R14908 names Walter Hugo Khouri.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R76025 names León Klimovsky.
+Record R46110 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R76025 names León Klimovsky.
-Record R46110 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R46110 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R46110 names Marcello Fondato.
```

## confirmation/v344-confirmation-07/EASY

L1 sha256 `f5e8199bb93d4a7d97602e40ddb4e49f1962e637ce346fcb87674f02838acf04`; N sha256 `6adef916505874139e7399bd4cae102e0baf6ad7a304520cd35f737f1f6727a8`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
@@ -18 +12 @@
-Which candidate is the credited director of Film T98395?
+Who is the credited director of Film T98395?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Bhappi Sonie
+2. Marcello Fondato
+3. Vojtěch Jasný
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Marcello Fondato
+2. Vojtěch Jasný
+3. Robert P. Kerr
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Robert P. Kerr
+3. Bhappi Sonie
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R69174 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R69174 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R30000 names Vojtěch Jasný.
+Record R74849 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R30000 names Vojtěch Jasný.
-Record R74849 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R74849 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R74849 names Marcello Fondato.
```

## confirmation/v344-confirmation-07/MID

L1 sha256 `c5385bf7917aa100cd5b794f25ac3d058f9f036904300ae165590dcf0b272449`; N sha256 `e28c7c8a6e35c96668c334eec0678b875bb94ae1d548bfd7d914f9221adae5f5`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
@@ -20 +14 @@
-Which candidate is the credited director of Film T98395?
+Who is the credited director of Film T98395?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Bhappi Sonie
+2. Marcello Fondato
+3. Vojtěch Jasný
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Marcello Fondato
+2. Vojtěch Jasný
+3. Robert P. Kerr
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Robert P. Kerr
+3. Bhappi Sonie
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R69174 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R69174 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R30000 names Vojtěch Jasný.
+Record R74849 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R30000 names Vojtěch Jasný.
-Record R74849 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R74849 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R74849 names Marcello Fondato.
```

## confirmation/v344-confirmation-07/HARD

L1 sha256 `784dc3c949314f81281ff8168d8ecc2dd47a44c611fd6114bf24d33546031b3d`; N sha256 `7f906af870b665eec69f57e51e1ce3ba199ad1b42cb54b1480bf2599f321599b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
@@ -29 +23 @@
-Which candidate is the credited director of Film T98395?
+Who is the credited director of Film T98395?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Bhappi Sonie
+2. Marcello Fondato
+3. Vojtěch Jasný
+4. Robert P. Kerr
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Marcello Fondato
+2. Vojtěch Jasný
+3. Robert P. Kerr
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Robert P. Kerr
-2. Bhappi Sonie
-3. Marcello Fondato
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Robert P. Kerr
+3. Bhappi Sonie
+4. Marcello Fondato
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R69174 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R69174 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R30000 names Vojtěch Jasný.
+Record R74849 names Marcello Fondato.
@@ -6,2 +7,0 @@
-Record R30000 names Vojtěch Jasný.
-Record R74849 names Marcello Fondato.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R74849 names Marcello Fondato.
@@ -7 +7,0 @@
-Record R74849 names Marcello Fondato.
```

## confirmation/v344-confirmation-08/EASY

L1 sha256 `128bc5cb0d4c52623922c92c96f09c89dd4c88d14ab9865a4e06dcdf5e885a02`; N sha256 `d522d74110ee8bdf6bfe60f4c04717302311895d0b0fb14018ba828e742e5d36`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
@@ -18 +12 @@
-Which candidate is the credited director of Film T13391?
+Who is the credited director of Film T13391?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Feng Xiaoning
+2. Fridrikh Ermler
+3. Rodrigo Grande
+4. Helmut Käutner
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Fridrikh Ermler
+2. Rodrigo Grande
+3. Helmut Käutner
+4. Feng Xiaoning
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Rodrigo Grande
+2. Helmut Käutner
+3. Feng Xiaoning
+4. Fridrikh Ermler
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R83464 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R83464 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R57402 names Fridrikh Ermler.
+Record R27097 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R57402 names Fridrikh Ermler.
-Record R27097 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R27097 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R27097 names Feng Xiaoning.
```

## confirmation/v344-confirmation-08/MID

L1 sha256 `f79327f05104b40923e38c3d846fc0a0b1453b3e137161644c0d35f6533afbda`; N sha256 `6654fe8a0a6b6c444d6e2a6e91816f1ac6cb67a5f9213256e37b59120fa534c9`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
@@ -20 +14 @@
-Which candidate is the credited director of Film T13391?
+Who is the credited director of Film T13391?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Feng Xiaoning
+2. Fridrikh Ermler
+3. Rodrigo Grande
+4. Helmut Käutner
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Fridrikh Ermler
+2. Rodrigo Grande
+3. Helmut Käutner
+4. Feng Xiaoning
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Rodrigo Grande
+2. Helmut Käutner
+3. Feng Xiaoning
+4. Fridrikh Ermler
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R83464 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R83464 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R57402 names Fridrikh Ermler.
+Record R27097 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R57402 names Fridrikh Ermler.
-Record R27097 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R27097 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R27097 names Feng Xiaoning.
```

## confirmation/v344-confirmation-08/HARD

L1 sha256 `cf764ee8c2625f3945507f213be3c77565ff8d3fc2dbc57f0f04fcffa66235c5`; N sha256 `b26626f6fe78c9caef74e1c72cad04d3cd4b7323d922163d4e993de125176cd6`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
@@ -29 +23 @@
-Which candidate is the credited director of Film T13391?
+Who is the credited director of Film T13391?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Feng Xiaoning
+2. Fridrikh Ermler
+3. Rodrigo Grande
+4. Helmut Käutner
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Fridrikh Ermler
+2. Rodrigo Grande
+3. Helmut Käutner
+4. Feng Xiaoning
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Helmut Käutner
-2. Feng Xiaoning
-3. Fridrikh Ermler
-4. Rodrigo Grande
+1. Rodrigo Grande
+2. Helmut Käutner
+3. Feng Xiaoning
+4. Fridrikh Ermler
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R83464 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R83464 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R57402 names Fridrikh Ermler.
+Record R27097 names Feng Xiaoning.
@@ -6,2 +7,0 @@
-Record R57402 names Fridrikh Ermler.
-Record R27097 names Feng Xiaoning.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R27097 names Feng Xiaoning.
@@ -7 +7,0 @@
-Record R27097 names Feng Xiaoning.
```

## confirmation/v344-confirmation-09/EASY

L1 sha256 `85921903218dc20de4682b3c9283568ca2335208a7250b03f402ad313defa258`; N sha256 `449302c0c4bc98b0a7604197b9f2568d62deb8ebcb48a174c01c8cb964eab98d`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
@@ -18 +12 @@
-Which candidate is the credited director of Film T78497?
+Who is the credited director of Film T78497?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Tinnu Anand
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Jan Svěrák
+2. Leopoldo Torre Nilsson
+3. Armando Robles Godoy
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48171 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R48171 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R95790 names Leopoldo Torre Nilsson.
+Record R77980 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R95790 names Leopoldo Torre Nilsson.
-Record R77980 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R77980 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R77980 names Armando Robles Godoy.
```

## confirmation/v344-confirmation-09/MID

L1 sha256 `6a3ba2fa57f75c266fea07fdcbe03eac18d1f222255d51980da659a2dd8c481c`; N sha256 `de640f20bd453abe4953df0e293eafab1e11686ca3745f92023717b77bcef2c2`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
@@ -20 +14 @@
-Which candidate is the credited director of Film T78497?
+Who is the credited director of Film T78497?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Tinnu Anand
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Jan Svěrák
+2. Leopoldo Torre Nilsson
+3. Armando Robles Godoy
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48171 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R48171 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R95790 names Leopoldo Torre Nilsson.
+Record R77980 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R95790 names Leopoldo Torre Nilsson.
-Record R77980 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R77980 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R77980 names Armando Robles Godoy.
```

## confirmation/v344-confirmation-09/HARD

L1 sha256 `ac50078c887fa8cb199162ad354e3032795a70201e1c2dca417f65dc66a72742`; N sha256 `4a48dab7ca913f1ce067ea7742b075d8f6260efd5c50f757169df0e4469c3921`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
@@ -29 +23 @@
-Which candidate is the credited director of Film T78497?
+Who is the credited director of Film T78497?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Tinnu Anand
+2. Jan Svěrák
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Jan Svěrák
+2. Leopoldo Torre Nilsson
+3. Armando Robles Godoy
+4. Tinnu Anand
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Armando Robles Godoy
-2. Tinnu Anand
-3. Jan Svěrák
-4. Leopoldo Torre Nilsson
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Tinnu Anand
+4. Jan Svěrák
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R48171 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R48171 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R95790 names Leopoldo Torre Nilsson.
+Record R77980 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R95790 names Leopoldo Torre Nilsson.
-Record R77980 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R77980 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R77980 names Armando Robles Godoy.
```

## confirmation/v344-confirmation-10/EASY

L1 sha256 `33d5926b82f0b7264682a2a0c5416a89d4828230225bb287598d54702e4a01b7`; N sha256 `5b02200656da8042e7f7414556b5a246bdecc5c776040930d4dbb150331268ae`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
@@ -18 +12 @@
-Which candidate is the credited director of Film T85889?
+Who is the credited director of Film T85889?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. Walter Hugo Khouri
+2. James Goldstone
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. James Goldstone
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Bhappi Sonie
+3. Walter Hugo Khouri
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14406 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R14406 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41508 names James Goldstone.
+Record R42726 names Vojtěch Jasný.
@@ -6,2 +7,0 @@
-Record R41508 names James Goldstone.
-Record R42726 names Vojtěch Jasný.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R42726 names Vojtěch Jasný.
@@ -7 +7,0 @@
-Record R42726 names Vojtěch Jasný.
```

## confirmation/v344-confirmation-10/MID

L1 sha256 `b5614ba648734840029d65360b9215e4c1ce6ad7acc2e9d43231c97f75793362`; N sha256 `6f672b9979a009b2dc57d21762e2fb1f0ffc1434b73fde8f2ba95d844b0a1108`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
@@ -20 +14 @@
-Which candidate is the credited director of Film T85889?
+Who is the credited director of Film T85889?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. Walter Hugo Khouri
+2. James Goldstone
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. James Goldstone
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Bhappi Sonie
+3. Walter Hugo Khouri
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14406 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R14406 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41508 names James Goldstone.
+Record R42726 names Vojtěch Jasný.
@@ -6,2 +7,0 @@
-Record R41508 names James Goldstone.
-Record R42726 names Vojtěch Jasný.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R42726 names Vojtěch Jasný.
@@ -7 +7,0 @@
-Record R42726 names Vojtěch Jasný.
```

## confirmation/v344-confirmation-10/HARD

L1 sha256 `00b1cf65f926ffda29e85470cc3ff7f57631b943319744e56da3092fc82806ef`; N sha256 `61e38dc8f91019b483de897c423f2c672ff4d8fc4053cd22622ceca4c02d9f6d`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
@@ -29 +23 @@
-Which candidate is the credited director of Film T85889?
+Who is the credited director of Film T85889?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. Walter Hugo Khouri
+2. James Goldstone
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. James Goldstone
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. Walter Hugo Khouri
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Walter Hugo Khouri
-3. James Goldstone
-4. Vojtěch Jasný
+1. Vojtěch Jasný
+2. Bhappi Sonie
+3. Walter Hugo Khouri
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R14406 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R14406 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R41508 names James Goldstone.
+Record R42726 names Vojtěch Jasný.
@@ -6,2 +7,0 @@
-Record R41508 names James Goldstone.
-Record R42726 names Vojtěch Jasný.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R42726 names Vojtěch Jasný.
@@ -7 +7,0 @@
-Record R42726 names Vojtěch Jasný.
```

## confirmation/v344-confirmation-11/EASY

L1 sha256 `494d2b4f35dfad4dc66eb2688829d839400c61fc7c96c71242dbf4a6f9d039a1`; N sha256 `6f6c55769dd3d3e5924b1143980a27b901c5395d892aa67ec2937e7aa010e345`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
@@ -18 +12 @@
-Which candidate is the credited director of Film T80908?
+Who is the credited director of Film T80908?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. Bhappi Sonie
+2. James Goldstone
+3. León Klimovsky
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. James Goldstone
+2. León Klimovsky
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. León Klimovsky
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R91620 names James Goldstone.
@@ -7,0 +7 @@
+Record R91620 names James Goldstone.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R23453 names Vojtěch Jasný.
+Record R85787 names León Klimovsky.
@@ -6,2 +7,0 @@
-Record R23453 names Vojtěch Jasný.
-Record R85787 names León Klimovsky.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R85787 names León Klimovsky.
@@ -7 +7,0 @@
-Record R85787 names León Klimovsky.
```

## confirmation/v344-confirmation-11/MID

L1 sha256 `a48c03d86a6b7284fa873c8676387429a099b852a64500a2e409bd18df6a3eef`; N sha256 `ff72a4833461d867ee865758b949daba60319cdcd62d3078b9c34f466dedfa8a`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
@@ -20 +14 @@
-Which candidate is the credited director of Film T80908?
+Who is the credited director of Film T80908?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. Bhappi Sonie
+2. James Goldstone
+3. León Klimovsky
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. James Goldstone
+2. León Klimovsky
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. León Klimovsky
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R91620 names James Goldstone.
@@ -7,0 +7 @@
+Record R91620 names James Goldstone.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R23453 names Vojtěch Jasný.
+Record R85787 names León Klimovsky.
@@ -6,2 +7,0 @@
-Record R23453 names Vojtěch Jasný.
-Record R85787 names León Klimovsky.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R85787 names León Klimovsky.
@@ -7 +7,0 @@
-Record R85787 names León Klimovsky.
```

## confirmation/v344-confirmation-11/HARD

L1 sha256 `4790229a9f4f5f2bcde1106465721bfaabd5a02275f158a61de4306980de44be`; N sha256 `2372e5032b1f23de7e5e7357b0e90fec1b02e17fb90aa9bcd4ebea9c1a9d38b2`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
@@ -29 +23 @@
-Which candidate is the credited director of Film T80908?
+Who is the credited director of Film T80908?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. Bhappi Sonie
+2. James Goldstone
+3. León Klimovsky
+4. Vojtěch Jasný
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. James Goldstone
+2. León Klimovsky
+3. Vojtěch Jasný
+4. Bhappi Sonie
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Vojtěch Jasný
-2. Bhappi Sonie
-3. James Goldstone
-4. León Klimovsky
+1. León Klimovsky
+2. Vojtěch Jasný
+3. Bhappi Sonie
+4. James Goldstone
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R91620 names James Goldstone.
@@ -7,0 +7 @@
+Record R91620 names James Goldstone.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R23453 names Vojtěch Jasný.
+Record R85787 names León Klimovsky.
@@ -6,2 +7,0 @@
-Record R23453 names Vojtěch Jasný.
-Record R85787 names León Klimovsky.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R85787 names León Klimovsky.
@@ -7 +7,0 @@
-Record R85787 names León Klimovsky.
```

## confirmation/v344-confirmation-12/EASY

L1 sha256 `2d20c61a525395083ba30b2f3f84795fc1a2c353fd11bdf8dbbbbd9deccb1b2c`; N sha256 `52e4eaa58e88f5e9b021ed6aed6fe07db26d4ff8a995608dedea540584fedd47`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
@@ -18 +12 @@
-Which candidate is the credited director of Film T83379?
+Who is the credited director of Film T83379?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Jan Svěrák
+2. Tinnu Anand
+3. Rahul Rawail
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Tinnu Anand
+2. Rahul Rawail
+3. Leopoldo Torre Nilsson
+4. Jan Svěrák
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Rahul Rawail
+2. Leopoldo Torre Nilsson
+3. Jan Svěrák
+4. Tinnu Anand
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R57310 names Rahul Rawail.
@@ -7,0 +7 @@
+Record R57310 names Rahul Rawail.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80282 names Tinnu Anand.
+Record R99737 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R80282 names Tinnu Anand.
-Record R99737 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R99737 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R99737 names Leopoldo Torre Nilsson.
```

## confirmation/v344-confirmation-12/MID

L1 sha256 `13833d91667617eaadaaa79cc51a49d9b4187dc20436e0658cfa52430e64a1be`; N sha256 `61b5b71999784114b6faf2793b50d1c414f6498deda0e6ebf32f82e53bb89ada`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
@@ -20 +14 @@
-Which candidate is the credited director of Film T83379?
+Who is the credited director of Film T83379?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Jan Svěrák
+2. Tinnu Anand
+3. Rahul Rawail
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Tinnu Anand
+2. Rahul Rawail
+3. Leopoldo Torre Nilsson
+4. Jan Svěrák
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Rahul Rawail
+2. Leopoldo Torre Nilsson
+3. Jan Svěrák
+4. Tinnu Anand
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R57310 names Rahul Rawail.
@@ -7,0 +7 @@
+Record R57310 names Rahul Rawail.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80282 names Tinnu Anand.
+Record R99737 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R80282 names Tinnu Anand.
-Record R99737 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R99737 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R99737 names Leopoldo Torre Nilsson.
```

## confirmation/v344-confirmation-12/HARD

L1 sha256 `aa67f3f4085fc6aa1a97fefd115eb66d37ffb06260188cd862adbf098d9ab64e`; N sha256 `3a78819a328f78a13be1262ac9f28f80e01100293865b8ebef1a4a715047ffbf`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
@@ -29 +23 @@
-Which candidate is the credited director of Film T83379?
+Who is the credited director of Film T83379?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Jan Svěrák
+2. Tinnu Anand
+3. Rahul Rawail
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Tinnu Anand
+2. Rahul Rawail
+3. Leopoldo Torre Nilsson
+4. Jan Svěrák
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Leopoldo Torre Nilsson
-2. Jan Svěrák
-3. Tinnu Anand
-4. Rahul Rawail
+1. Rahul Rawail
+2. Leopoldo Torre Nilsson
+3. Jan Svěrák
+4. Tinnu Anand
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R57310 names Rahul Rawail.
@@ -7,0 +7 @@
+Record R57310 names Rahul Rawail.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R80282 names Tinnu Anand.
+Record R99737 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R80282 names Tinnu Anand.
-Record R99737 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R99737 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R99737 names Leopoldo Torre Nilsson.
```

## confirmation/v344-confirmation-13/EASY

L1 sha256 `8273059526fcfaf0fa531b32ae7b82eb5db80ac9f882860710500bfe85ba1fa4`; N sha256 `ef6eb25fb28bdc8810bd2b94875fdc4a92165c04ca4a57db31ca5202c77505b6`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
@@ -18 +12 @@
-Which candidate is the credited director of Film T51919?
+Who is the credited director of Film T51919?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Rolf Schübel
+2. Gu Changwei
+3. Helmut Käutner
+4. Rodrigo Grande
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Gu Changwei
+2. Helmut Käutner
+3. Rodrigo Grande
+4. Rolf Schübel
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Helmut Käutner
+2. Rodrigo Grande
+3. Rolf Schübel
+4. Gu Changwei
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R78808 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R78808 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R76481 names Rolf Schübel.
+Record R54642 names Helmut Käutner.
@@ -6,2 +7,0 @@
-Record R76481 names Rolf Schübel.
-Record R54642 names Helmut Käutner.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R54642 names Helmut Käutner.
@@ -7 +7,0 @@
-Record R54642 names Helmut Käutner.
```

## confirmation/v344-confirmation-13/MID

L1 sha256 `e062176fd07ea83917025eb788c66ee5b9aba01b67607a4a71d90d10837522b7`; N sha256 `7951037f21a30bb5bdca3d86dd858fcad1e7b594f78fd497a89295dae8d884ee`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
@@ -20 +14 @@
-Which candidate is the credited director of Film T51919?
+Who is the credited director of Film T51919?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Rolf Schübel
+2. Gu Changwei
+3. Helmut Käutner
+4. Rodrigo Grande
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Gu Changwei
+2. Helmut Käutner
+3. Rodrigo Grande
+4. Rolf Schübel
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Helmut Käutner
+2. Rodrigo Grande
+3. Rolf Schübel
+4. Gu Changwei
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R78808 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R78808 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R76481 names Rolf Schübel.
+Record R54642 names Helmut Käutner.
@@ -6,2 +7,0 @@
-Record R76481 names Rolf Schübel.
-Record R54642 names Helmut Käutner.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R54642 names Helmut Käutner.
@@ -7 +7,0 @@
-Record R54642 names Helmut Käutner.
```

## confirmation/v344-confirmation-13/HARD

L1 sha256 `a43485d02ae51e77767a3c42623f95d2f507ad9c0142276d3e52a7e3d43d6339`; N sha256 `2dc23bcc5225617e8c663bbac3624a3db739e4826ef222e42532893b14a322a6`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
@@ -29 +23 @@
-Which candidate is the credited director of Film T51919?
+Who is the credited director of Film T51919?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Rolf Schübel
+2. Gu Changwei
+3. Helmut Käutner
+4. Rodrigo Grande
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Gu Changwei
+2. Helmut Käutner
+3. Rodrigo Grande
+4. Rolf Schübel
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Rodrigo Grande
-2. Rolf Schübel
-3. Gu Changwei
-4. Helmut Käutner
+1. Helmut Käutner
+2. Rodrigo Grande
+3. Rolf Schübel
+4. Gu Changwei
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R78808 names Rodrigo Grande.
@@ -7,0 +7 @@
+Record R78808 names Rodrigo Grande.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R76481 names Rolf Schübel.
+Record R54642 names Helmut Käutner.
@@ -6,2 +7,0 @@
-Record R76481 names Rolf Schübel.
-Record R54642 names Helmut Käutner.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R54642 names Helmut Käutner.
@@ -7 +7,0 @@
-Record R54642 names Helmut Käutner.
```

## confirmation/v344-confirmation-14/EASY

L1 sha256 `0382f20fe58974b85571f0ba991d998bb2afa489b434d2d386645f5c117b5e9d`; N sha256 `d445037fab9c0aeb729918afa69ebb12a05028f49b79ce9cab2d35329225987f`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
@@ -18 +12 @@
-Which candidate is the credited director of Film T26132?
+Who is the credited director of Film T26132?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Armando Robles Godoy
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Rahul Rawail
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Rahul Rawail
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R24368 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R24368 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42794 names Rahul Rawail.
+Record R91965 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R42794 names Rahul Rawail.
-Record R91965 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R91965 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R91965 names Leopoldo Torre Nilsson.
```

## confirmation/v344-confirmation-14/MID

L1 sha256 `82237b4d4c93b803d2b72aa92d8492113ae0a1beb5182b5023491c6ec84f9639`; N sha256 `58225da86995d1d4bb33d0eeac89790fe9af16406121ab8ae77c35daa9f93bef`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
@@ -20 +14 @@
-Which candidate is the credited director of Film T26132?
+Who is the credited director of Film T26132?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Armando Robles Godoy
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Rahul Rawail
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Rahul Rawail
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R24368 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R24368 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42794 names Rahul Rawail.
+Record R91965 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R42794 names Rahul Rawail.
-Record R91965 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R91965 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R91965 names Leopoldo Torre Nilsson.
```

## confirmation/v344-confirmation-14/HARD

L1 sha256 `61e0ffa520a12cbea3f17f86e76159c5ca39494824116d0f5ed713a140909426`; N sha256 `d5c737205111a9036fc52f9566dd356d60d05951df674e7df9b04ddf821e604b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
@@ -29 +23 @@
-Which candidate is the credited director of Film T26132?
+Who is the credited director of Film T26132?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Leopoldo Torre Nilsson
+2. Rahul Rawail
+3. Armando Robles Godoy
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Rahul Rawail
+2. Armando Robles Godoy
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Rahul Rawail
-4. Armando Robles Godoy
+1. Armando Robles Godoy
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Rahul Rawail
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R24368 names Ildikó Enyedi.
@@ -7,0 +7 @@
+Record R24368 names Ildikó Enyedi.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R42794 names Rahul Rawail.
+Record R91965 names Leopoldo Torre Nilsson.
@@ -6,2 +7,0 @@
-Record R42794 names Rahul Rawail.
-Record R91965 names Leopoldo Torre Nilsson.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R91965 names Leopoldo Torre Nilsson.
@@ -7 +7,0 @@
-Record R91965 names Leopoldo Torre Nilsson.
```

## confirmation/v344-confirmation-15/EASY

L1 sha256 `7f0eb29235f8153e62bd4791ef5627acd9665533ae1ead89d7140821ce60b387`; N sha256 `3c06c5420d4172fb502d9539743553bbdcb3e5d8adedcc55e1b13661a5b782e1`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
@@ -18 +12 @@
-Which candidate is the credited director of Film T72869?
+Who is the credited director of Film T72869?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Tinnu Anand
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Armando Robles Godoy
+2. Tinnu Anand
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Tinnu Anand
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R12838 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R12838 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R71011 names Leopoldo Torre Nilsson.
+Record R13581 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R71011 names Leopoldo Torre Nilsson.
-Record R13581 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R13581 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R13581 names Armando Robles Godoy.
```

## confirmation/v344-confirmation-15/MID

L1 sha256 `87e0f986a4352b5e11b24e0c4aa8b44c36162e02bdfe323ac9b0d4307cbcacca`; N sha256 `7426db9a84fb8009bac3aba4152a0068a116b223d81694e128012f945c8c4fd1`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
@@ -20 +14 @@
-Which candidate is the credited director of Film T72869?
+Who is the credited director of Film T72869?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Tinnu Anand
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Armando Robles Godoy
+2. Tinnu Anand
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Tinnu Anand
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R12838 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R12838 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R71011 names Leopoldo Torre Nilsson.
+Record R13581 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R71011 names Leopoldo Torre Nilsson.
-Record R13581 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R13581 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R13581 names Armando Robles Godoy.
```

## confirmation/v344-confirmation-15/HARD

L1 sha256 `4f58e352d8149f9fff05284b39f4b0cd738090a706487fd9bc372e91d7f08d88`; N sha256 `4426fd7aa183881190baa365e9a178fe9dfc2de6a12fba1e9df2211b4f057cdc`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
@@ -29 +23 @@
-Which candidate is the credited director of Film T72869?
+Who is the credited director of Film T72869?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Leopoldo Torre Nilsson
+2. Armando Robles Godoy
+3. Tinnu Anand
+4. Ildikó Enyedi
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Armando Robles Godoy
+2. Tinnu Anand
+3. Ildikó Enyedi
+4. Leopoldo Torre Nilsson
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Ildikó Enyedi
-2. Leopoldo Torre Nilsson
-3. Armando Robles Godoy
-4. Tinnu Anand
+1. Tinnu Anand
+2. Ildikó Enyedi
+3. Leopoldo Torre Nilsson
+4. Armando Robles Godoy
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R12838 names Tinnu Anand.
@@ -7,0 +7 @@
+Record R12838 names Tinnu Anand.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R71011 names Leopoldo Torre Nilsson.
+Record R13581 names Armando Robles Godoy.
@@ -6,2 +7,0 @@
-Record R71011 names Leopoldo Torre Nilsson.
-Record R13581 names Armando Robles Godoy.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R13581 names Armando Robles Godoy.
@@ -7 +7,0 @@
-Record R13581 names Armando Robles Godoy.
```

## confirmation/v344-confirmation-16/EASY

L1 sha256 `a45b48b9a25000642a3ec062a1ae3dff71dac44570c8087b201b301298eaa397`; N sha256 `f1c4466a0fa262fd94c5eab8b230ad09b35ff31a2caac6aa9a67c080361e27dc`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
@@ -18 +12 @@
-Which candidate is the credited director of Film T77924?
+Who is the credited director of Film T77924?
@@ -20 +14 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. Robert P. Kerr
+2. León Klimovsky
+3. Marcello Fondato
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. León Klimovsky
+2. Marcello Fondato
+3. Bhappi Sonie
+4. Robert P. Kerr
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. Marcello Fondato
+2. Bhappi Sonie
+3. Robert P. Kerr
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R38080 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R38080 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R93401 names Marcello Fondato.
+Record R12040 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R93401 names Marcello Fondato.
-Record R12040 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R12040 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R12040 names Robert P. Kerr.
```

## confirmation/v344-confirmation-16/MID

L1 sha256 `43202332cafa144ee3cc845600e95cf7683d8c9e592158a424a57f241f5a16eb`; N sha256 `d2cb2627e0d7427a4ba6f501df535386af3fb15662b05bc68f9469b2b7d1f36b`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
@@ -20 +14 @@
-Which candidate is the credited director of Film T77924?
+Who is the credited director of Film T77924?
@@ -22 +16 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. Robert P. Kerr
+2. León Klimovsky
+3. Marcello Fondato
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. León Klimovsky
+2. Marcello Fondato
+3. Bhappi Sonie
+4. Robert P. Kerr
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. Marcello Fondato
+2. Bhappi Sonie
+3. Robert P. Kerr
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R38080 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R38080 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R93401 names Marcello Fondato.
+Record R12040 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R93401 names Marcello Fondato.
-Record R12040 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R12040 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R12040 names Robert P. Kerr.
```

## confirmation/v344-confirmation-16/HARD

L1 sha256 `c415683e5ea8b305d91857d1c803e1dcf83a75afb70166cbce1c5ab65c4a19a4`; N sha256 `dd229398d7fa284ab88d59d0eea5b37b6c8dac694d6feec1150f6eb103b49d71`.

```diff
--- L1
+++ N
@@ -2,6 +1,0 @@
-
-Candidate names:
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
@@ -29 +23 @@
-Which candidate is the credited director of Film T77924?
+Who is the credited director of Film T77924?
@@ -31 +25 @@
-Answer with only one candidate name.
+Output only the person's name.
```

```diff
--- L1
+++ L2
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. Robert P. Kerr
+2. León Klimovsky
+3. Marcello Fondato
+4. Bhappi Sonie
```

```diff
--- L1
+++ L3
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. León Klimovsky
+2. Marcello Fondato
+3. Bhappi Sonie
+4. Robert P. Kerr
```

```diff
--- L1
+++ L4
@@ -4,4 +4,4 @@
-1. Bhappi Sonie
-2. Robert P. Kerr
-3. León Klimovsky
-4. Marcello Fondato
+1. Marcello Fondato
+2. Bhappi Sonie
+3. Robert P. Kerr
+4. León Klimovsky
```

```diff
--- N
+++ R2
@@ -4 +3,0 @@
-Record R38080 names Bhappi Sonie.
@@ -7,0 +7 @@
+Record R38080 names Bhappi Sonie.
```

```diff
--- N
+++ R3
@@ -3,0 +4,2 @@
+Record R93401 names Marcello Fondato.
+Record R12040 names Robert P. Kerr.
@@ -6,2 +7,0 @@
-Record R93401 names Marcello Fondato.
-Record R12040 names Robert P. Kerr.
```

```diff
--- N
+++ R4
@@ -3,0 +4 @@
+Record R12040 names Robert P. Kerr.
@@ -7 +7,0 @@
-Record R12040 names Robert P. Kerr.
```
