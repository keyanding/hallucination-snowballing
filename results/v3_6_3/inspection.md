# Exact questions, prompts and outputs

No hidden first-hop repair: every generated-pipeline entry links to the actual U-GOLD raw/normalized state.

## v363-calibration-009 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_W58; supplied intermediate: None; expected: STATE_Z93.
Category: Bp; normalized: `STATE_Z93`; truncated=False.
Prompt SHA256: `12a269fae36b2d4ca1803e9d58c1432f7ccbd888ea37fa17d2165e335a62ccc1`; rendered SHA256: `6bab8ddb177bfc1d88715f866299ee57ef3f112d5be5836c256b366917df9b07`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_S32 -> STATE_B40
ENTITY_W58 -> STATE_Z93

Current entity:
ENTITY_W58

Return only the mapped state.
```

Raw output:
```json
"STATE_Z93"
```

## v363-calibration-013 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_E29; expected: OUTCOME_F38.
Category: C; normalized: `OUTCOME_F38`; truncated=False.
Prompt SHA256: `11015e54a4c3c32eb0f4887eed54e93800613175a912f3d20f88995b1e46f881`; rendered SHA256: `d371c11802d3b4679919d322808ebd7e7272b4a2a1848929305a9f4f11e1f2ff`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_E29

Downstream mappings:
STATE_E29 -> OUTCOME_F38
STATE_M55 -> OUTCOME_X26

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_F38"
```

## v363-calibration-003 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_F87; supplied intermediate: None; expected: STATE_U86.
Category: Bp; normalized: `STATE_U86`; truncated=False.
Prompt SHA256: `5a11ae2c131f4b1bc3d15e49cb9074342cfaeb95b3005be1eb62db67d9f733f2`; rendered SHA256: `38e079f0bfeabb3c32d4b6934414204d547abf88e46aeaa6690eb965d1397745`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_F87 -> STATE_U86
ENTITY_N19 -> STATE_L16

Current entity:
ENTITY_F87

Return only the mapped state.
```

Raw output:
```json
"STATE_U86"
```

## v363-calibration-018 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_L36; supplied intermediate: None; expected: STATE_X50.
Category: Bp; normalized: `STATE_X50`; truncated=False.
Prompt SHA256: `8131579aa4e39393b01cf35eaa0ee6ff193f35716919f328f6cf2147b9c9eb7f`; rendered SHA256: `0818d269a946e35e2303293672d7f899e870f67692ecddb4733ed282c52d8906`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_A24 -> STATE_D93
ENTITY_L36 -> STATE_X50

Current entity:
ENTITY_L36

Return only the mapped state.
```

Raw output:
```json
"STATE_X50"
```

## v363-calibration-007 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_D55; expected: OUTCOME_R77.
Category: C; normalized: `OUTCOME_R77`; truncated=False.
Prompt SHA256: `d7d88144432681e289dd07adbe1bd81590efd03a7fedcc00acd6882db01bdf2e`; rendered SHA256: `fdd5025ed4d517fe92c58166667a35dd504409ab2a7f6400c508b42a337a8e7f`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_D55

Downstream mappings:
STATE_J78 -> OUTCOME_C54
STATE_D55 -> OUTCOME_R77

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_R77"
```

## v363-calibration-011 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_P41; supplied intermediate: None; expected: STATE_H59.
Category: B; normalized: `STATE_H59`; truncated=False.
Prompt SHA256: `0e5fbc15f924eb800584b2594c75fd82564ab2a9be08b9ee52411120fe436752`; rendered SHA256: `b1056f6a27e99b78d72f99accba9e958968a44f6e211cbdac69d530aaa347899`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_P41 -> STATE_H59
ENTITY_T07 -> STATE_P42

Current entity:
ENTITY_P41

Return only the mapped state.
```

Raw output:
```json
"STATE_H59"
```

## v363-calibration-006 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_J10; supplied intermediate: None; expected: STATE_R23.
Category: B; normalized: `STATE_R23`; truncated=False.
Prompt SHA256: `15d6db05645254065e2e38ab03911269b4d72c020521fc8b3f44cea00c498e8a`; rendered SHA256: `fe6eed7e1992a21dfdc9e98cbc6cfdff21b43f8db973511248e697b9665236e4`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_J10 -> STATE_R23
ENTITY_D46 -> STATE_W72

Current entity:
ENTITY_J10

Return only the mapped state.
```

Raw output:
```json
"STATE_R23"
```

## v363-calibration-005 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_T23; supplied intermediate: None; expected: STATE_J73.
Category: B; normalized: `STATE_J73`; truncated=False.
Prompt SHA256: `ec6ed0c18ebafa3d922aaafe602c8dc03c836d9366578fb6996ef1a548378d2f`; rendered SHA256: `56a14eb440ab59f00b1f7e72b5470940a76f94d5a4546806dbfc210cf9625c60`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_B01 -> STATE_N15
ENTITY_T23 -> STATE_J73

Current entity:
ENTITY_T23

Return only the mapped state.
```

Raw output:
```json
"STATE_J73"
```

## v363-calibration-018 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_A24; supplied intermediate: None; expected: STATE_D93.
Category: B; normalized: `STATE_D93`; truncated=False.
Prompt SHA256: `875ba62a39951aade3396d1ea8558cbe0295127255071e8a205b8428a7c84e15`; rendered SHA256: `3cba2c1de4efecd23f615b8de302dce35008f325b24f3c86a9c607ba6e561218`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_A24 -> STATE_D93
ENTITY_L36 -> STATE_X50

Current entity:
ENTITY_A24

Return only the mapped state.
```

Raw output:
```json
"STATE_D93"
```

## v363-calibration-015 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_J01; expected: OUTCOME_C56.
Category: C; normalized: `OUTCOME_C56`; truncated=False.
Prompt SHA256: `0c9e80b36f9148b5d0a3c9fca6c8fee12d76bd4394b85bfe67c5fd22442215fb`; rendered SHA256: `dbe71c35c7e0607d9e0b417534077a2752780429b1c5303a09b6258066b1a12c`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_J01

Downstream mappings:
STATE_J01 -> OUTCOME_C56
STATE_W97 -> OUTCOME_U13

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_C56"
```

## v363-calibration-008 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_J36; expected: OUTCOME_G83.
Category: Cp; normalized: `OUTCOME_G83`; truncated=False.
Prompt SHA256: `e194f1aa722a88ecf0ccac54e28380d1ca7f2f2c03e4e342712ab3526be1563a`; rendered SHA256: `9e6869f230df57119068be8d72a4e9e914f26178a520715af152ec02cc0107ef`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_J36

Downstream mappings:
STATE_Y45 -> OUTCOME_S51
STATE_J36 -> OUTCOME_G83

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_G83"
```

## v363-calibration-020 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_E82; expected: OUTCOME_T48.
Category: Cp; normalized: `OUTCOME_T48`; truncated=False.
Prompt SHA256: `3c8a1cd09c539a82ed7c166fb48de4552b7264cc78987f97b0662a7f69aaf39e`; rendered SHA256: `e39f074c7e74e29b4922f4e4ffe9f338f46ca5a3fd77bb030a9cc745f5369f15`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_E82

Downstream mappings:
STATE_H52 -> OUTCOME_J14
STATE_E82 -> OUTCOME_T48

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_T48"
```

## v363-calibration-019 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_U10; supplied intermediate: None; expected: STATE_E66.
Category: Bp; normalized: `STATE_E66`; truncated=False.
Prompt SHA256: `8c72616f5270fcd66eee6d502e9d2cd6b7dc0369efa8a9c78d663511ba12bc1d`; rendered SHA256: `2995ad254451fdaab192ab82412d84ae8495dd13e5afed73b6aaaf14a30b8705`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_U10 -> STATE_E66
ENTITY_E46 -> STATE_L28

Current entity:
ENTITY_U10

Return only the mapped state.
```

Raw output:
```json
"STATE_E66"
```

## v363-calibration-009 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_Z93; expected: OUTCOME_O29.
Category: Cp; normalized: `OUTCOME_O29`; truncated=False.
Prompt SHA256: `36d2ebb81b65f8967cac8e86f08d2c1e2e83bd8cd7537331aac427327b354456`; rendered SHA256: `cfe117f9758dd4c5ce6698d21fe2a6886ab3fc53548832c8577b034adb653ee5`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_Z93

Downstream mappings:
STATE_B40 -> OUTCOME_C25
STATE_Z93 -> OUTCOME_O29

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_O29"
```

## v363-calibration-003 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_N19; supplied intermediate: None; expected: STATE_L16.
Category: B; normalized: `STATE_L16`; truncated=False.
Prompt SHA256: `2a7507e81d4917404b4958c45dfc01d4f1f83ae5e7c074b106a0d80570e24a7d`; rendered SHA256: `3010f389a18b20c9de3c97597d0ee8e6fc8276eb7718aa2a27c0885d665a2f30`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_F87 -> STATE_U86
ENTITY_N19 -> STATE_L16

Current entity:
ENTITY_N19

Return only the mapped state.
```

Raw output:
```json
"STATE_L16"
```

## v363-calibration-004 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_R97; expected: OUTCOME_M14.
Category: C; normalized: `OUTCOME_M14`; truncated=False.
Prompt SHA256: `f5f1ad6aa6c1746fd929168fba19e82c986a746f4852726ce6aba239d5689895`; rendered SHA256: `17a3865152cf4d46371a923deaf2971e0ae6cc016c72f156efb096a47078e1a8`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_R97

Downstream mappings:
STATE_U27 -> OUTCOME_M40
STATE_R97 -> OUTCOME_M14

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_M14"
```

## v363-calibration-008 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_T95; supplied intermediate: None; expected: STATE_J36.
Category: Bp; normalized: `STATE_J36`; truncated=False.
Prompt SHA256: `2310de8f08292f9763089864e0d4364b1472194170d378f4afd06bbefd3c9b4e`; rendered SHA256: `cbe811cea5d9b550659ae953c959f9973a59716b31b93b5c7db90bc7e70950bd`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_T95 -> STATE_J36
ENTITY_B76 -> STATE_Y45

Current entity:
ENTITY_T95

Return only the mapped state.
```

Raw output:
```json
"STATE_J36"
```

## v363-calibration-010 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_W07; expected: OUTCOME_E02.
Category: C; normalized: `OUTCOME_E02`; truncated=False.
Prompt SHA256: `67f10f2fea9893ea00b2fc053f24684474e0ee450aa5b7a6506819e877d5949d`; rendered SHA256: `2b3e46250d845525d767bb1cf02c7651951add4c29fc59a5e2f48486e34f4cfb`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_W07

Downstream mappings:
STATE_K31 -> OUTCOME_B47
STATE_W07 -> OUTCOME_E02

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_E02"
```

## v363-calibration-020 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_E52; supplied intermediate: None; expected: STATE_H52.
Category: B; normalized: `STATE_H52`; truncated=False.
Prompt SHA256: `9505e8b078bdad94e7db788822454e2753faff4b8abad8a312c9b47ce02cf00e`; rendered SHA256: `d125a625e38d8ccc613ff0e3f00b979691b045f5434c1665b9e7c425c7aaa19b`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_E52 -> STATE_H52
ENTITY_L76 -> STATE_E82

Current entity:
ENTITY_E52

Return only the mapped state.
```

Raw output:
```json
"STATE_H52"
```

## v363-calibration-012 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_U07; supplied intermediate: None; expected: STATE_Q97.
Category: Bp; normalized: `STATE_Q97`; truncated=False.
Prompt SHA256: `085f89384a5062a447190c414bc0db2343c29f1b3049ebe7feef97c3b2a267b8`; rendered SHA256: `b9e6148237deb2cdb96d0e23b48813fa8634526f976b3ba2c2bc2f002d7c446b`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_S17 -> STATE_G20
ENTITY_U07 -> STATE_Q97

Current entity:
ENTITY_U07

Return only the mapped state.
```

Raw output:
```json
"STATE_Q97"
```

## v363-calibration-019 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_L28; expected: OUTCOME_L59.
Category: INVALID; normalized (JSON): `"The recorded intermediate result is STATE_L28.  \nThe downstream mapping is STATE"`; truncated=True.
Prompt SHA256: `6e265ba25649f6d5e1445874664f19f4b7271fda2199907f5b06cfdf94dbcb0c`; rendered SHA256: `69577bb74d2bd49f907db3d46d3536c21f7c7679c87ce8ca0835d756365a496e`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_L28

Downstream mappings:
STATE_L28 -> OUTCOME_L59
STATE_E66 -> OUTCOME_V49

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"The recorded intermediate result is STATE_L28.  \nThe downstream mapping is STATE"
```

## v363-calibration-004 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_Z70; supplied intermediate: None; expected: STATE_R97.
Category: B; normalized: `STATE_R97`; truncated=False.
Prompt SHA256: `3f0cb472e350d594f6cefcd4e3f450d36e9ad2ecd682ed422e516a5c7a6ce45d`; rendered SHA256: `21120bafdd8ef7adee2a8f63fce6be8f64360b2f74f27b17d6fcd1c1494eae77`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_Z70 -> STATE_R97
ENTITY_P94 -> STATE_U27

Current entity:
ENTITY_Z70

Return only the mapped state.
```

Raw output:
```json
"STATE_R97"
```

## v363-calibration-007 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_J78; expected: OUTCOME_C54.
Category: Cp; normalized: `OUTCOME_C54`; truncated=False.
Prompt SHA256: `b7280ab5124d27a5f704ce519d3e34a4c9b0b02b5636c509ec2a5c651a46ecac`; rendered SHA256: `9edb8682b09d0078e95a914cea723f93503efb15255d9f05fadb620812b27402`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_J78

Downstream mappings:
STATE_J78 -> OUTCOME_C54
STATE_D55 -> OUTCOME_R77

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_C54"
```

## v363-calibration-006 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_R23; expected: OUTCOME_G57.
Category: C; normalized: `OUTCOME_G57`; truncated=False.
Prompt SHA256: `7d1a9279ed423960ec61c2eade2b3a0d2c9b772043bd618cb9a067668a3abd9e`; rendered SHA256: `c0d18b578811efb0cd25144ff529a218efea8135418d7983a9ff733b82b71ed5`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_R23

Downstream mappings:
STATE_R23 -> OUTCOME_G57
STATE_W72 -> OUTCOME_W24

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_G57"
```

## v363-calibration-010 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_Y93; supplied intermediate: None; expected: STATE_W07.
Category: B; normalized: `STATE_W07`; truncated=False.
Prompt SHA256: `3db445a71c73ef742834c616049db1473bebce5c4942b7470047c5837c06ec1c`; rendered SHA256: `40cf3855cc642938f7933df2696c195e3314237f5898a9889ce713793391595e`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_M84 -> STATE_K31
ENTITY_Y93 -> STATE_W07

Current entity:
ENTITY_Y93

Return only the mapped state.
```

Raw output:
```json
"STATE_W07"
```

## v363-calibration-016 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_X41; supplied intermediate: None; expected: STATE_J09.
Category: Bp; normalized: `STATE_J09`; truncated=False.
Prompt SHA256: `04676d65eeb1956fe30114a75e5949e537e7dbe77ffda6e4ea6c3178ffff418e`; rendered SHA256: `dd851b6265c321fba3c09d16901d565ccdfff7e2ec92bc8ffa1cd26b85cc7db7`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_E48 -> STATE_P11
ENTITY_X41 -> STATE_J09

Current entity:
ENTITY_X41

Return only the mapped state.
```

Raw output:
```json
"STATE_J09"
```

## v363-calibration-003 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_U86; expected: OUTCOME_D63.
Category: Cp; normalized: `OUTCOME_D63`; truncated=False.
Prompt SHA256: `6700fcca7724dc00249486fdcdec0e00725e39453a6b605f3173b6d33c65dc1b`; rendered SHA256: `af97c2043e095371ebfb02c12087b12f714f125981fd4bca7481f5d5ac4b8d97`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_U86

Downstream mappings:
STATE_U86 -> OUTCOME_D63
STATE_L16 -> OUTCOME_J87

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_D63"
```

## v363-calibration-007 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_O55; supplied intermediate: None; expected: STATE_D55.
Category: B; normalized: `STATE_D55`; truncated=False.
Prompt SHA256: `3794b354b022baa0d2f03ce4dc2ea13b077ba65d78f665c51e80759eb095c31e`; rendered SHA256: `644796abdd37ac35c2301ed148e8262583e5d1cde7a93a0a84127106c1a8ed3b`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_M30 -> STATE_J78
ENTITY_O55 -> STATE_D55

Current entity:
ENTITY_O55

Return only the mapped state.
```

Raw output:
```json
"STATE_D55"
```

## v363-calibration-016 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_J09; expected: OUTCOME_W04.
Category: Cp; normalized: `OUTCOME_W04`; truncated=False.
Prompt SHA256: `48d05b738d6b3f3e667478c8ebc595edb68daf9267b254ad110c1500542989a1`; rendered SHA256: `4f734ece9f399c11507706b349f43620c35787bc84ea920e74a9c057aa81d2d7`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_J09

Downstream mappings:
STATE_J09 -> OUTCOME_W04
STATE_P11 -> OUTCOME_F26

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_W04"
```

## v363-calibration-015 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_S12; supplied intermediate: None; expected: STATE_W97.
Category: Bp; normalized: `STATE_W97`; truncated=False.
Prompt SHA256: `89efa74e8b495f9d5c872fe7d11b6b97040ea0b0c4feed0c4119b6499d747b20`; rendered SHA256: `9a01e83d69a18eb97567475f0b9f2d0a9a6a7e5aecbb2bcd85d4f4a124a3cc5c`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_S12 -> STATE_W97
ENTITY_N98 -> STATE_J01

Current entity:
ENTITY_S12

Return only the mapped state.
```

Raw output:
```json
"STATE_W97"
```

## v363-calibration-014 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_I05; expected: OUTCOME_M55.
Category: INVALID; normalized: `M55`; truncated=False.
Prompt SHA256: `2c3cae299b5332fa6a84d18b18360d7f63e8d25855b2febe18058403f7f50581`; rendered SHA256: `ab66bf6e16f1902b09dff2099ce27864a21343b1ef1dc4d30b36424a5b419fd3`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_I05

Downstream mappings:
STATE_I55 -> OUTCOME_O51
STATE_I05 -> OUTCOME_M55

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"M55"
```

## v363-calibration-016 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_P11; expected: OUTCOME_F26.
Category: C; normalized: `OUTCOME_F26`; truncated=False.
Prompt SHA256: `7de1bfb0803591d764b8647b40786c74ae024814a81cf620023fbed1e3a7c086`; rendered SHA256: `7aad4806fa6fe33758ca09f500439fbb811f153532f238e8c6ea4581500dc7c0`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_P11

Downstream mappings:
STATE_J09 -> OUTCOME_W04
STATE_P11 -> OUTCOME_F26

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_F26"
```

## v363-calibration-011 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_T07; supplied intermediate: None; expected: STATE_P42.
Category: Bp; normalized: `STATE_P42`; truncated=False.
Prompt SHA256: `b5b4175a4a31194f5fcc17999aa6a931b4eeccd89db59795c2ef8bd0bb5765c6`; rendered SHA256: `77e18dd6463a117bba78eca20a5a970d7867da90310cfdf7a605cbae6da7e004`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_P41 -> STATE_H59
ENTITY_T07 -> STATE_P42

Current entity:
ENTITY_T07

Return only the mapped state.
```

Raw output:
```json
"STATE_P42"
```

## v363-calibration-009 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_B40; expected: OUTCOME_C25.
Category: C; normalized: `OUTCOME_C25`; truncated=False.
Prompt SHA256: `d785b0a1e518b198c53eae6a5e2a2b3e493fd36b65f0e0cbdb78872d4ab48421`; rendered SHA256: `842ac46417f27ddcc0114afaddc98d52a56dcdacfa060121e31bb0f668113f6f`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_B40

Downstream mappings:
STATE_B40 -> OUTCOME_C25
STATE_Z93 -> OUTCOME_O29

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_C25"
```

## v363-calibration-002 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_K70; expected: OUTCOME_B75.
Category: C; normalized: `OUTCOME_B75`; truncated=False.
Prompt SHA256: `0ea6a31a8b4f863eff2d5c33aeb48256b1295e250012bb165011c7a8de0e9daa`; rendered SHA256: `934e2b85529e68bc65544aca0b269168cfead848bff1b16c2df77466a058e9ea`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_K70

Downstream mappings:
STATE_K70 -> OUTCOME_B75
STATE_E72 -> OUTCOME_N02

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_B75"
```

## v363-calibration-010 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_K31; expected: OUTCOME_B47.
Category: Cp; normalized: `OUTCOME_B47`; truncated=False.
Prompt SHA256: `3179d1fe943e2471a7548b4ee317eece9520b0aa9a99918c4733e506baeab147`; rendered SHA256: `5aa84d4835f5651dfdc0dcb02b7bf29076e6bb99af9657959fe69e431bc36a40`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_K31

Downstream mappings:
STATE_K31 -> OUTCOME_B47
STATE_W07 -> OUTCOME_E02

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_B47"
```

## v363-calibration-002 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_A05; supplied intermediate: None; expected: STATE_E72.
Category: Bp; normalized: `STATE_E72`; truncated=False.
Prompt SHA256: `197276d74f347f5b02cf1e23f2a716d089dcbfeec3d81ed7232d2135b411d2f2`; rendered SHA256: `409560664674710d93f11c878c8363c86ae44750b98669931822049534494949`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_A05 -> STATE_E72
ENTITY_L54 -> STATE_K70

Current entity:
ENTITY_A05

Return only the mapped state.
```

Raw output:
```json
"STATE_E72"
```

## v363-calibration-014 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_Q03; supplied intermediate: None; expected: STATE_I55.
Category: Bp; normalized: `STATE_I55`; truncated=False.
Prompt SHA256: `8787c7c14a5e48a0f06eced38521587d1c8709446cc91288ae6a67cc517f3736`; rendered SHA256: `79062218607c664b444974b04ea3f1a4769a1c0c04d9a4a8154b69e1fdabbbca`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_Q03 -> STATE_I55
ENTITY_M07 -> STATE_I05

Current entity:
ENTITY_Q03

Return only the mapped state.
```

Raw output:
```json
"STATE_I55"
```

## v363-calibration-019 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_E46; supplied intermediate: None; expected: STATE_L28.
Category: B; normalized: `STATE_L28`; truncated=False.
Prompt SHA256: `7c3f363fb8b52c160b056dda7c1eb9abedc2a67eaa6110bfc2d8e2037c864640`; rendered SHA256: `0ae8aab2f484233c9dc7ab62d33877010ffc60869e6996f56a85f4c6a8365b60`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_U10 -> STATE_E66
ENTITY_E46 -> STATE_L28

Current entity:
ENTITY_E46

Return only the mapped state.
```

Raw output:
```json
"STATE_L28"
```

## v363-calibration-014 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_M07; supplied intermediate: None; expected: STATE_I05.
Category: B; normalized: `STATE_I05`; truncated=False.
Prompt SHA256: `d5460c1bc45753d88c078e9d5f55e5854fd1106ac0252de63e35c2fe27d7fbbd`; rendered SHA256: `fb7fdb3b2ad5efd01ce8a62d781bd95b5e9e93367d03753116c74196457064ff`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_Q03 -> STATE_I55
ENTITY_M07 -> STATE_I05

Current entity:
ENTITY_M07

Return only the mapped state.
```

Raw output:
```json
"STATE_I05"
```

## v363-calibration-013 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_F03; supplied intermediate: None; expected: STATE_M55.
Category: Bp; normalized: `STATE_M55`; truncated=False.
Prompt SHA256: `e0a43d1756d596d86cf9166394636899c26d462fa654cc56fdb0b0a9d92db77b`; rendered SHA256: `1c13425834e18298a3a6117fa9561be72ccb8cd6def4a28a3011c8defa63eca5`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_F03 -> STATE_M55
ENTITY_I91 -> STATE_E29

Current entity:
ENTITY_F03

Return only the mapped state.
```

Raw output:
```json
"STATE_M55"
```

## v363-calibration-006 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_W72; expected: OUTCOME_W24.
Category: Cp; normalized: `OUTCOME_W24`; truncated=False.
Prompt SHA256: `330b40f96182e782d41eff25da16e2f6f2c803f39972ead2b5ba584fcf5acb81`; rendered SHA256: `52097c060a1b0b870dcea8bf83f46e0fc150aa8dfaf084e09e4a90a69e948d31`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_W72

Downstream mappings:
STATE_R23 -> OUTCOME_G57
STATE_W72 -> OUTCOME_W24

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_W24"
```

## v363-calibration-005 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_N15; expected: OUTCOME_G85.
Category: Cp; normalized: `OUTCOME_G85`; truncated=False.
Prompt SHA256: `52250f842b87c9e517447ddcf11e7367f8a9322f11808e3f83a23593e2c51c10`; rendered SHA256: `bcfa1b63438e8b866fac34443c61fb1dcd37166821d5d3cff878ec7045b01243`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_N15

Downstream mappings:
STATE_N15 -> OUTCOME_G85
STATE_J73 -> OUTCOME_N73

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_G85"
```

## v363-calibration-004 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_U27; expected: OUTCOME_M40.
Category: Cp; normalized: `OUTCOME_M40`; truncated=False.
Prompt SHA256: `1d78739153f089b0958251cb7c8d3622841131fec77d12fcd0f51a6975a2a197`; rendered SHA256: `0f077ac6027466fd0c741502923bfaf519c84db4781908fd6c2595769f4349ba`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_U27

Downstream mappings:
STATE_U27 -> OUTCOME_M40
STATE_R97 -> OUTCOME_M14

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_M40"
```

## v363-calibration-007 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_M30; supplied intermediate: None; expected: STATE_J78.
Category: Bp; normalized: `STATE_J78`; truncated=False.
Prompt SHA256: `29b15417b0aba54ba0a1136d87c3a906fba11c516aea9c55b2bb84ac23342497`; rendered SHA256: `4790c02f8150c1c5fcb97247ec68c12bce322e53287f132af9164b11de9f2290`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_M30 -> STATE_J78
ENTITY_O55 -> STATE_D55

Current entity:
ENTITY_M30

Return only the mapped state.
```

Raw output:
```json
"STATE_J78"
```

## v363-calibration-011 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_H59; expected: OUTCOME_Z50.
Category: C; normalized: `OUTCOME_Z50`; truncated=False.
Prompt SHA256: `2aa1982eef77ad2c00c2703527146ec7ae731b65e43657a0eb397edf501f436f`; rendered SHA256: `c1839a46cb86e9aee4d64b92c8178fffef5a019e7097076d5a17ae06c91c68b2`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_H59

Downstream mappings:
STATE_P42 -> OUTCOME_K85
STATE_H59 -> OUTCOME_Z50

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_Z50"
```

## v363-calibration-018 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_D93; expected: OUTCOME_J01.
Category: C; normalized: `OUTCOME_J01`; truncated=False.
Prompt SHA256: `5f19a1db6ce6889b73c2eef765d11fbd252ea72fc51a16286f51e4c0e6693d08`; rendered SHA256: `adc301c9b4e1aedd2d31954c4b9951b3b4a2c699ca49ecf2494dba177b27014b`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_D93

Downstream mappings:
STATE_D93 -> OUTCOME_J01
STATE_X50 -> OUTCOME_Q85

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_J01"
```

## v363-calibration-002 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_E72; expected: OUTCOME_N02.
Category: Cp; normalized: `OUTCOME_N02`; truncated=False.
Prompt SHA256: `a1acfce5198dc07452622dba9a16bcc9cff3d8394826dc285b88fbc3dd37e93f`; rendered SHA256: `657ee8fcef5a0afb3c3020ee9c57127c59b1cfe13a5bc9dad81bfffa71d3f2a0`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_E72

Downstream mappings:
STATE_K70 -> OUTCOME_B75
STATE_E72 -> OUTCOME_N02

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_N02"
```

## v363-calibration-012 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_G20; expected: OUTCOME_M84.
Category: C; normalized: `OUTCOME_M84`; truncated=False.
Prompt SHA256: `5e81dca79ced3eacbad89c8f9ab8cdf7917defdbdc03eac4c752601e43b31e2c`; rendered SHA256: `220737c8859f0a16febd971074a9907e3feadacacf47f8cff6b4d94b85660a22`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_G20

Downstream mappings:
STATE_Q97 -> OUTCOME_E90
STATE_G20 -> OUTCOME_M84

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_M84"
```

## v363-calibration-015 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_N98; supplied intermediate: None; expected: STATE_J01.
Category: B; normalized: `STATE_J01`; truncated=False.
Prompt SHA256: `4ea6ab33fe7344a414ee20e72cff9c2d6b288288f796b3aaaf00e56f0ba6a519`; rendered SHA256: `6e4554d6286affac076d7ababc607c2842d56e4cb00fd73eecaf3ec646936975`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_S12 -> STATE_W97
ENTITY_N98 -> STATE_J01

Current entity:
ENTITY_N98

Return only the mapped state.
```

Raw output:
```json
"STATE_J01"
```

## v363-calibration-017 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_M80; expected: OUTCOME_A88.
Category: C; normalized: `OUTCOME_A88`; truncated=False.
Prompt SHA256: `0e110cfd9496d1e7b374252148c22ed355231a52590ad7c97acd7406cde9b3bf`; rendered SHA256: `dca16cd27460c33470b7bfb6e17a9cc8ff181d31eff38fe2fa8a23718945a43e`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_M80

Downstream mappings:
STATE_M80 -> OUTCOME_A88
STATE_H28 -> OUTCOME_H00

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_A88"
```

## v363-calibration-015 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_W97; expected: OUTCOME_U13.
Category: Cp; normalized: `OUTCOME_U13`; truncated=False.
Prompt SHA256: `a7cb33235040f55ce7cc94f70060afd87e95d30da4fe3e9cce061c6beb9073bc`; rendered SHA256: `5793145de0fc9098871ab06cf196414997472418315005394884b2f1f8ee4416`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_W97

Downstream mappings:
STATE_J01 -> OUTCOME_C56
STATE_W97 -> OUTCOME_U13

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_U13"
```

## v363-calibration-001 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_A40; supplied intermediate: None; expected: STATE_F88.
Category: B; normalized: `STATE_F88`; truncated=False.
Prompt SHA256: `91630782efacb80a9395ad444fd3ed3a7097c2b6072db63c1f65726fc52d364f`; rendered SHA256: `d2932558c2bc186e52f90988b8fb0ef1eb31df9f7e150e4bd1024a88d83cee13`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_A40 -> STATE_F88
ENTITY_J46 -> STATE_Y10

Current entity:
ENTITY_A40

Return only the mapped state.
```

Raw output:
```json
"STATE_F88"
```

## v363-calibration-010 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_M84; supplied intermediate: None; expected: STATE_K31.
Category: Bp; normalized: `STATE_K31`; truncated=False.
Prompt SHA256: `d6e5c31c00590fca8c614d854e4834cf79ce3d77a8d2e9bdcab788b0a73a66f3`; rendered SHA256: `a8d6bb4887898a6a0c0e45b695bed55aad7f33bd9f704911056fa6ee51b49568`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_M84 -> STATE_K31
ENTITY_Y93 -> STATE_W07

Current entity:
ENTITY_M84

Return only the mapped state.
```

Raw output:
```json
"STATE_K31"
```

## v363-calibration-001 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_Y10; expected: OUTCOME_L16.
Category: INVALID; normalized: `STATE_Y10 implies OUTCOME_L16`; truncated=False.
Prompt SHA256: `030c6c61c3edcac2bad269c6d98b0a831b8ce9845520209c53a07d57956bc764`; rendered SHA256: `3edafe07f16e6ba02afe6773a90efaf1153928f34f5cc0f3eea84b5c8421d343`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_Y10

Downstream mappings:
STATE_Y10 -> OUTCOME_L16
STATE_F88 -> OUTCOME_X13

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"STATE_Y10 implies OUTCOME_L16."
```

## v363-calibration-017 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_H28; expected: OUTCOME_H00.
Category: Cp; normalized: `OUTCOME_H00`; truncated=False.
Prompt SHA256: `abcc6bea85ae8b5bc0f977abe4c86a2906ed046ea21cd09aa0364e5125c33b6e`; rendered SHA256: `7442be2c588ed7b328fa86d3914349a67ae8a7268c0c42abe2e0b5605fc3b80a`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_H28

Downstream mappings:
STATE_M80 -> OUTCOME_A88
STATE_H28 -> OUTCOME_H00

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_H00"
```

## v363-calibration-008 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_Y45; expected: OUTCOME_S51.
Category: C; normalized: `OUTCOME_S51`; truncated=False.
Prompt SHA256: `8611023d3ba0eacf7a5d832c293b357a15cad87d12a5756df51c4fe02ff33f0c`; rendered SHA256: `cd5234d8492e3a1907216b9d34b42d9fea9e19c4852227babfa89b2e4067d623`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_Y45

Downstream mappings:
STATE_Y45 -> OUTCOME_S51
STATE_J36 -> OUTCOME_G83

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_S51"
```

## v363-calibration-013 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_I91; supplied intermediate: None; expected: STATE_E29.
Category: B; normalized: `STATE_E29`; truncated=False.
Prompt SHA256: `8cfb576187f9d4a00ae44244b2e8de4e8adf9e3baa3b4d6984a242308583c25c`; rendered SHA256: `49e2c5269b49c2caf2c342516314225312c38b15520ee22411c40718ba97c77e`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_F03 -> STATE_M55
ENTITY_I91 -> STATE_E29

Current entity:
ENTITY_I91

Return only the mapped state.
```

Raw output:
```json
"STATE_E29"
```

## v363-calibration-003 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_L16; expected: OUTCOME_J87.
Category: C; normalized: `OUTCOME_J87`; truncated=False.
Prompt SHA256: `0000a7a97e22af3e4dc1f558e2013ab712ede0fb3a2fffe936a1c0d1c9b7bf1b`; rendered SHA256: `7a5a179526e9e4bd1089b73eef5a440ca3fa1ff05cb1692dee971dfc31d2af4f`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_L16

Downstream mappings:
STATE_U86 -> OUTCOME_D63
STATE_L16 -> OUTCOME_J87

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_J87"
```

## v363-calibration-018 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_X50; expected: OUTCOME_Q85.
Category: Cp; normalized: `OUTCOME_Q85`; truncated=False.
Prompt SHA256: `7ab013a381ea7555bc7e25345dbecb014166221fa91adba866dea852b5536a14`; rendered SHA256: `49ae7e795f91f0daf9af1cf98763996dbb828c3fc5b543058309e77714351cf0`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_X50

Downstream mappings:
STATE_D93 -> OUTCOME_J01
STATE_X50 -> OUTCOME_Q85

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_Q85"
```

## v363-calibration-004 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_P94; supplied intermediate: None; expected: STATE_U27.
Category: Bp; normalized: `STATE_U27`; truncated=False.
Prompt SHA256: `4d56636d8f8d921fdf83aa5813904ee255b6852df01647cbf6c43c47e5c23e9c`; rendered SHA256: `af0bbb3a9e55f5f1569a12784e518c54866034c214710d519d3f4037dab648a6`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_Z70 -> STATE_R97
ENTITY_P94 -> STATE_U27

Current entity:
ENTITY_P94

Return only the mapped state.
```

Raw output:
```json
"STATE_U27"
```

## v363-calibration-008 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_B76; supplied intermediate: None; expected: STATE_Y45.
Category: B; normalized: `STATE_Y45`; truncated=False.
Prompt SHA256: `89cc1b6f1ecc281d50ab34a174c081b825679ff171cc33addb903c7015ec7459`; rendered SHA256: `26631b5fb86442b0039047793b455164d7357e88e71e65365d158671d62a43cf`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_T95 -> STATE_J36
ENTITY_B76 -> STATE_Y45

Current entity:
ENTITY_B76

Return only the mapped state.
```

Raw output:
```json
"STATE_Y45"
```

## v363-calibration-012 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_S17; supplied intermediate: None; expected: STATE_G20.
Category: B; normalized: `STATE_G20`; truncated=False.
Prompt SHA256: `041f9dc35d5a5b0cb9ed36b55783c2fab0e2a2b95c0ed70e328a20f44de19214`; rendered SHA256: `25cd382adbb4ffe9cb6eb3dda302ea51b27954e746b4914b1b150c9413ed2878`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_S17 -> STATE_G20
ENTITY_U07 -> STATE_Q97

Current entity:
ENTITY_S17

Return only the mapped state.
```

Raw output:
```json
"STATE_G20"
```

## v363-calibration-017 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_P10; supplied intermediate: None; expected: STATE_H28.
Category: Bp; normalized: `STATE_H28`; truncated=False.
Prompt SHA256: `51a03bcc93f7e21976755d116f8c780cb6a89c75d1be27c0c889b0ab4fc85d33`; rendered SHA256: `99f05fc7f3bea162acba5ff26c7649101a4099e85217368431067ee31580b69f`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_V68 -> STATE_M80
ENTITY_P10 -> STATE_H28

Current entity:
ENTITY_P10

Return only the mapped state.
```

Raw output:
```json
"STATE_H28"
```

## v363-calibration-011 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_P42; expected: OUTCOME_K85.
Category: Cp; normalized: `OUTCOME_K85`; truncated=False.
Prompt SHA256: `57d97a73ab179ef0f9cbe4d959c1f5346681081c1e513a978ef709e61fc32bef`; rendered SHA256: `c9d58806ca3612a5b7c03c21e191ff52dc760502cdccb3be6ff29a1d52ecdbbb`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_P42

Downstream mappings:
STATE_P42 -> OUTCOME_K85
STATE_H59 -> OUTCOME_Z50

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_K85"
```

## v363-calibration-017 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_V68; supplied intermediate: None; expected: STATE_M80.
Category: B; normalized: `STATE_M80`; truncated=False.
Prompt SHA256: `3d32442ab28ac93bcb24c990f5a558a71608fabfd9fdb1d76368c623fd4a3abb`; rendered SHA256: `6cb07e3947f667a1bbd9e7d17af1c721dbf6b0f4f4b5f148f860efe474b2ef45`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_V68 -> STATE_M80
ENTITY_P10 -> STATE_H28

Current entity:
ENTITY_V68

Return only the mapped state.
```

Raw output:
```json
"STATE_M80"
```

## v363-calibration-001 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_F88; expected: OUTCOME_X13.
Category: C; normalized: `OUTCOME_X13`; truncated=False.
Prompt SHA256: `dcd12fa1560d6671de80a7f342f31ea9ba70f9afe480fba67974113506613c4a`; rendered SHA256: `6ea280fd870583ea04ba20f782dda0986f76e633c946a236aa91459b21a3a676`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_F88

Downstream mappings:
STATE_Y10 -> OUTCOME_L16
STATE_F88 -> OUTCOME_X13

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_X13"
```

## v363-calibration-006 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_D46; supplied intermediate: None; expected: STATE_W72.
Category: Bp; normalized: `STATE_W72`; truncated=False.
Prompt SHA256: `1faf9eaea442e531a259c6e549f6756ec83489b50a602b809cb943f986c1a35d`; rendered SHA256: `f7d02218cf7dee7cbd837f39b7856a2d3bc575cc2cf1e9dd4d27ea60e9995e5c`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_J10 -> STATE_R23
ENTITY_D46 -> STATE_W72

Current entity:
ENTITY_D46

Return only the mapped state.
```

Raw output:
```json
"STATE_W72"
```

## v363-calibration-013 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_M55; expected: OUTCOME_X26.
Category: Cp; normalized: `OUTCOME_X26`; truncated=False.
Prompt SHA256: `57b08a088ab8935fa7b3347c067cd99a3727ed9dfe689772b85c095e23901e8c`; rendered SHA256: `37bf913ed79b894957ebcabca9b234b7c51b74c20aeece91a1bce86e5f2b2fff`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_M55

Downstream mappings:
STATE_E29 -> OUTCOME_F38
STATE_M55 -> OUTCOME_X26

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_X26"
```

## v363-calibration-002 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_L54; supplied intermediate: None; expected: STATE_K70.
Category: B; normalized: `STATE_K70`; truncated=False.
Prompt SHA256: `e5b924ebb6ea5355dc32e20547411f3a66a4bea3247265c1af191634a280cd3b`; rendered SHA256: `eda8a5a4ada38841a6b571115bd168a34ca5f21a7e842f4d38ba5325acb67b8c`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_A05 -> STATE_E72
ENTITY_L54 -> STATE_K70

Current entity:
ENTITY_L54

Return only the mapped state.
```

Raw output:
```json
"STATE_K70"
```

## v363-calibration-019 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_E66; expected: OUTCOME_V49.
Category: Cp; normalized: `OUTCOME_V49`; truncated=False.
Prompt SHA256: `a37fdf33a165bffdba8ecf5adf2796942abd49deaea674c2823aa1360ebf69b0`; rendered SHA256: `8d28d64b850492ca2565fd730d2d046b70397daf4ed72571bf684dafb4ac77b9`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_E66

Downstream mappings:
STATE_L28 -> OUTCOME_L59
STATE_E66 -> OUTCOME_V49

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_V49"
```

## v363-calibration-005 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_B01; supplied intermediate: None; expected: STATE_N15.
Category: Bp; normalized: `STATE_N15`; truncated=False.
Prompt SHA256: `e17aec813701144ae04c9251caa5416f7ddbf114635c65ee206d9101c25fbb38`; rendered SHA256: `6dac974de17b721b02785efc1002859684bd3e239883fd35bb868b2b0df9a647`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_B01 -> STATE_N15
ENTITY_T23 -> STATE_J73

Current entity:
ENTITY_B01

Return only the mapped state.
```

Raw output:
```json
"STATE_N15"
```

## v363-calibration-012 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_Q97; expected: OUTCOME_E90.
Category: Cp; normalized: `OUTCOME_E90`; truncated=False.
Prompt SHA256: `ca37818db9d9c69f0364a6cf8d1c587d879c7ac60a89e45c79fc97e408ceb805`; rendered SHA256: `95b6384d9b20b7da176fb4f56265bc2ca01bcb594475fbbf2770762d8c339819`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_Q97

Downstream mappings:
STATE_Q97 -> OUTCOME_E90
STATE_G20 -> OUTCOME_M84

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_E90"
```

## v363-calibration-001 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_J46; supplied intermediate: None; expected: STATE_Y10.
Category: Bp; normalized: `STATE_Y10`; truncated=False.
Prompt SHA256: `e456bd8cebf20acc27a5c4f2289fde78ed3d849920e8582a2c04d04e4877be4a`; rendered SHA256: `bde8ea7f23c2ca68e96a9d2daadf58332fa7184c90ad6b57af6576ad5861894e`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_A40 -> STATE_F88
ENTITY_J46 -> STATE_Y10

Current entity:
ENTITY_J46

Return only the mapped state.
```

Raw output:
```json
"STATE_Y10"
```

## v363-calibration-016 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_E48; supplied intermediate: None; expected: STATE_P11.
Category: B; normalized: `STATE_P11`; truncated=False.
Prompt SHA256: `366e92e59b98b84937e567962c26553464a617b2b7947be50465f3dfbb4910cd`; rendered SHA256: `f7a597145fadf170a6f1de89d2b63fa4c370052248da28169a12ed72e4d7131c`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_E48 -> STATE_P11
ENTITY_X41 -> STATE_J09

Current entity:
ENTITY_E48

Return only the mapped state.
```

Raw output:
```json
"STATE_P11"
```

## v363-calibration-009 / U-GOLD / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_S32; supplied intermediate: None; expected: STATE_B40.
Category: B; normalized: `STATE_B40`; truncated=False.
Prompt SHA256: `faeef8c5b0cc71dd0f8e360487b840a2c8f613eec18dfb56a65f2a7acc2fe0ed`; rendered SHA256: `79fea575a265fe6fe8d11dba8f64de6020dbf2b44350ccda39bfc76eabab9bec`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_S32 -> STATE_B40
ENTITY_W58 -> STATE_Z93

Current entity:
ENTITY_S32

Return only the mapped state.
```

Raw output:
```json
"STATE_B40"
```

## v363-calibration-005 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_J73; expected: OUTCOME_N73.
Category: C; normalized: `OUTCOME_N73`; truncated=False.
Prompt SHA256: `5eb78ceb877f9c29761648900486d2077f69c3f4eea60cbdaddaf076a652fdf1`; rendered SHA256: `6e7f3920a9ea3916ddccd5359484cc98ecea8fbd75d41fcb9090d8c2849ac5cf`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_J73

Downstream mappings:
STATE_N15 -> OUTCOME_G85
STATE_J73 -> OUTCOME_N73

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_N73"
```

## v363-calibration-020 / P-GOLD / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_H52; expected: OUTCOME_J14.
Category: C; normalized: `OUTCOME_J14`; truncated=False.
Prompt SHA256: `015f97f01ca9eba74e6304bc8b1681117a8f8ccb8d6107063682a1a03b051725`; rendered SHA256: `a0864c39b9c80ec672b77db2adf13baa7dc9ca0670229daa69b5a63e41005b7a`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_H52

Downstream mappings:
STATE_H52 -> OUTCOME_J14
STATE_E82 -> OUTCOME_T48

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_J14"
```

## v363-calibration-014 / P-ALT / reverse=False

Question/instruction: Return only the outcome implied by the recorded intermediate result.
Current entity: None; supplied intermediate: STATE_I55; expected: OUTCOME_O51.
Category: Cp; normalized: `OUTCOME_O51`; truncated=False.
Prompt SHA256: `b7bfeb112358227aa7c33b5985522d661bacf11c46260c3979ab298600e13b90`; rendered SHA256: `a928b1850e5a6e1e52f14fd7c66e3c930f133eb66000d5e3b05bbbce451726e9`.

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_I55

Downstream mappings:
STATE_I55 -> OUTCOME_O51
STATE_I05 -> OUTCOME_M55

Return only the outcome implied by the recorded intermediate result.
```

Raw output:
```json
"OUTCOME_O51"
```

## v363-calibration-020 / U-ALT / reverse=False

Question/instruction: Return only the mapped state.
Current entity: ENTITY_L76; supplied intermediate: None; expected: STATE_E82.
Category: Bp; normalized: `STATE_E82`; truncated=False.
Prompt SHA256: `ec92abf1dc0ad2adb07b652faaedd2aebdaa1cd196a8bd08a08b6823073f1aa1`; rendered SHA256: `8fb0f498e7332fd5a68049ff8c3f8a4d6aceb69a6a1d85f478d491c32c838a80`.

```text
Synthetic transition task.

Upstream mappings:
ENTITY_E52 -> STATE_H52
ENTITY_L76 -> STATE_E82

Current entity:
ENTITY_L76

Return only the mapped state.
```

Raw output:
```json
"STATE_E82"
```
