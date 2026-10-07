# Full prompt and output inspection

Each entry shows the exact subquestion, supplied state, mappings, full prompt, raw output and strict parse. No first-hop question is run; the intermediate state is externally supplied.

## v360-calibration-001 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?
Supplied intermediate: `State_D49`
Expected: `Outcome_F93`; parsed: C; normalized: `Outcome_F93`; truncated: False
Prompt SHA256: `ded06a44a6aa92f8e292eaac794d188d0556076bbd6c58a2edae87ac0ee58044`; rendered SHA256: `636cd7450b31d0541859894dfa74acb3e822ec84187bca89b776b1641e14cde6`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J94 maps to Outcome_I48.
State_D49 maps to Outcome_F93.

Current entity:
Entity_J44

Working intermediate state:
State_D49

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_F93"
```

## v360-calibration-006 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?
Supplied intermediate: `State_Y82`
Expected: `Outcome_M73`; parsed: C; normalized: `Outcome_M73`; truncated: False
Prompt SHA256: `67ede38e7734f511b22bd857bb8f670d7c1e68cb929f05243b24fd896a1bc4c5`; rendered SHA256: `b9ab9ac230be735cae95d581e46e6b838fff5b0dcfbe06fc5ca23ad67d92acbb`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y82 maps to Outcome_M73.
State_W27 maps to Outcome_A15.

Current entity:
Entity_V79

Working intermediate state:
State_Y82

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M73"
```

## v360-calibration-005 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_R00 map to?
Supplied intermediate: `State_R00`
Expected: `Outcome_Z51`; parsed: Cp; normalized: `Outcome_Z51`; truncated: False
Prompt SHA256: `85fab0eeffe6f32a778ead5a954fae1b432377288e57024dc90a6f371d48eacf`; rendered SHA256: `4a6a81652e62823664a171cd2b84f42e7bd3295701def3874485a9d00dc14f96`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R00 maps to Outcome_Z51.
State_R64 maps to Outcome_M36.

Question:
According to the supplied mapping, what does State_R00 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_Z51"
```

## v360-calibration-009 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_Q05?
Supplied intermediate: `State_J02`
Expected: `Outcome_S45`; parsed: C; normalized: `Outcome_S45`; truncated: False
Prompt SHA256: `e9ec48d3d0f7c77453c04404e30dfc5a0469f6776204010c97c9f6aebc77995e`; rendered SHA256: `4673efc09ee7100ee8fab19be6c709bf61b89cd62590ae6e42b86bac72abab3e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J02 maps to Outcome_S45.
State_H06 maps to Outcome_D81.

Current entity:
Entity_Q05

Working intermediate state:
State_J02

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_Q05?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_S45"
```

## v360-calibration-012 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?
Supplied intermediate: `State_M41`
Expected: `Outcome_W11`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `1c1c0bdb58196ea92ee91a3c5b68f15ca7f600a5231a0d28da7e5ee93006ea95`; rendered SHA256: `c48a4c25ac928a9138e87cfa27307d0677a0ef0a6f17e4ba06114c20468fb65f`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E16 maps to Outcome_A20.
State_M41 maps to Outcome_W11.

Current entity:
Entity_R10

Working intermediate state:
State_M41

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-009 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_J02 map to?
Supplied intermediate: `State_J02`
Expected: `Outcome_S45`; parsed: C; normalized: `Outcome_S45`; truncated: False
Prompt SHA256: `d5352c58b80fa4b97f4e95863f901284efa11292aae269692425b22d4acc5fd7`; rendered SHA256: `430ea1e660c80f5d6cdb784d04de0e31458df569e9009b403d341249ac2f95b1`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J02 maps to Outcome_S45.
State_H06 maps to Outcome_D81.

Question:
According to the supplied mapping, what does State_J02 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_S45"
```

## v360-calibration-003 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_W16?
Supplied intermediate: `State_Z38`
Expected: `Outcome_L24`; parsed: C; normalized: `Outcome_L24`; truncated: False
Prompt SHA256: `1b14e6a719ec0be5e8ba737af2b447fc7cc1fd3eb88b33f88e2f0e67d5358e6d`; rendered SHA256: `e774ff471834e9c1d8384665a0336779508d6ac2e7f964748e78663018230af6`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z43 maps to Outcome_P70.
State_Z38 maps to Outcome_L24.

Current entity:
Entity_W16

Working intermediate state:
State_Z38

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_W16?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_L24"
```

## v360-calibration-001 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_J94 map to?
Supplied intermediate: `State_J94`
Expected: `Outcome_I48`; parsed: Cp; normalized: `Outcome_I48`; truncated: False
Prompt SHA256: `ca02b91c270bf48eb26feaadf0e184b6bccef9347c9845677230029f28d9a7c7`; rendered SHA256: `760d6a07dac937d715eeb3a1a582e24603d5d5acf3662138ba8d6f3265349ec4`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D49 maps to Outcome_F93.
State_J94 maps to Outcome_I48.

Question:
According to the supplied mapping, what does State_J94 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_I48"
```

## v360-calibration-006 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?
Supplied intermediate: `State_Y82`
Expected: `Outcome_A15`; parsed: Cp; normalized: `Outcome_A15`; truncated: False
Prompt SHA256: `2b4dc0f717d80a829408a3f726b0395d005c1903db984296adefa720e0907a99`; rendered SHA256: `625cb92eda464fbc7a46ed057b9d5fc92817bedcf1676ded80207e266d1a7d37`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y82 maps to Outcome_A15.
State_W27 maps to Outcome_M73.

Current entity:
Entity_V79

Working intermediate state:
State_Y82

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A15"
```

## v360-calibration-008 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?
Supplied intermediate: `State_N96`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `2685ee50f270ebb314582dad2a73be833897abeb26f08beee681379314a633d6`; rendered SHA256: `aa26eb07fe7d5eba2519ade9e417c9f1c0919f7a73e8b257191cdd1c5a7a1173`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_H25 maps to Outcome_C61.
State_P32 maps to Outcome_H92.

Current entity:
Entity_E79

Working intermediate state:
State_N96

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-004 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?
Supplied intermediate: `State_S38`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `31d9522e2efe9f6fd957a53c54bf0fd5e5d32d32b0e81a2c5fe749f59f54e8d6`; rendered SHA256: `24e1709fc6cf569e2c3b00c4096d585f4083bed20099a6c1caf2e2c8bb22b61d`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_O94 maps to Outcome_N09.
State_M06 maps to Outcome_I15.

Current entity:
Entity_G19

Working intermediate state:
State_S38

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-010 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?
Supplied intermediate: `State_U30`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `9a5f47442a4ea547c657e0b8f86cd9f1a5b96c9930dddf3c9ee8c97a71c4d880`; rendered SHA256: `291237874bc41783b0ea5acaa16d2668fed62212224181ce8e70efec2fe0d9e0`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y20 maps to Outcome_V88.
State_A36 maps to Outcome_X40.

Current entity:
Entity_E59

Working intermediate state:
State_U30

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-004 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_O94 map to?
Supplied intermediate: `State_O94`
Expected: `Outcome_N09`; parsed: C; normalized: `Outcome_N09`; truncated: False
Prompt SHA256: `53a5a996e0ff52f85170bdcb57b26a9c2ff89fa520ee5726261daefe5d5a7f2a`; rendered SHA256: `48ef58422cf5553541c972b1f1527445ef1817e074ead1727a978f58e37343cc`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_O94 maps to Outcome_N09.
State_M06 maps to Outcome_I15.

Question:
According to the supplied mapping, what does State_O94 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_N09"
```

## v360-calibration-006 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?
Supplied intermediate: `State_W27`
Expected: `Outcome_A15`; parsed: Cp; normalized: `Outcome_A15`; truncated: False
Prompt SHA256: `68635636f643826df006cbfddd9035184e82122cba543d313340463dc9ad5fec`; rendered SHA256: `e0dc203c77197f257d756fa6a75c18f137292aae69213180a3d7d41f62831497`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y82 maps to Outcome_M73.
State_W27 maps to Outcome_A15.

Current entity:
Entity_V79

Working intermediate state:
State_W27

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A15"
```

## v360-calibration-003 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?
Supplied intermediate: `State_T72`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `4c64686951251cab3f014d37a1f4b13864af88c2ccccf5ea7e942573b24efe85`; rendered SHA256: `a0fddbf851e9faffcb95874fec7fed4a9c87743317a1294944363a26e6b5ea89`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z43 maps to Outcome_P70.
State_Z38 maps to Outcome_L24.

Current entity:
Entity_F60

Working intermediate state:
State_T72

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-017 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_I11 map to?
Supplied intermediate: `State_I11`
Expected: `Outcome_H41`; parsed: Cp; normalized: `Outcome_H41`; truncated: False
Prompt SHA256: `12ffa8a63b4acf74bbca8fdd8283b3149f72679bea89c7486854e21014837135`; rendered SHA256: `cf822ec50b25eb2f922828fb77accc0683542b47def4df0e434f88dda5d58749`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_I11 maps to Outcome_H41.
State_J32 maps to Outcome_E53.

Question:
According to the supplied mapping, what does State_I11 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_H41"
```

## v360-calibration-001 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_M55?
Supplied intermediate: `State_D49`
Expected: `Outcome_F93`; parsed: C; normalized: `Outcome_F93`; truncated: False
Prompt SHA256: `639200909226ee8d28cc8e275b8b223dae75bfe22934c405e7e7f58ded7adae9`; rendered SHA256: `0e65e5a8209bc4da1f0b7730bd194c45aabe801401036c2e40876f6cc86ccb04`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D49 maps to Outcome_F93.
State_J94 maps to Outcome_I48.

Current entity:
Entity_M55

Working intermediate state:
State_D49

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_M55?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_F93"
```

## v360-calibration-016 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?
Supplied intermediate: `State_D05`
Expected: `Outcome_Q30`; parsed: Cp; normalized: `Outcome_Q30`; truncated: False
Prompt SHA256: `214d76dcd05df0f79e00da8408739075e753e6bb4f57aa914b22d37d2ee6f6d7`; rendered SHA256: `9ac1fa730aeb0094d15f99bf61c2923623cae82b6389cff17bd6967b4ede2348`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D05 maps to Outcome_Q30.
State_B20 maps to Outcome_X89.

Current entity:
Entity_R01

Working intermediate state:
State_D05

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_Q30"
```

## v360-calibration-007 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?
Supplied intermediate: `State_X38`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `26cb28936cb44efa907858b4f408a6fce665d02801b079ff813cb653e3df4bcf`; rendered SHA256: `efb3b5b434d3aa3e3d90b0b7559244a9781de57f1960733589cc6e842a08c181`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E40 maps to Outcome_A64.
State_T18 maps to Outcome_R32.

Current entity:
Entity_N53

Working intermediate state:
State_X38

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-001 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_D49 map to?
Supplied intermediate: `State_D49`
Expected: `Outcome_F93`; parsed: C; normalized: `Outcome_F93`; truncated: False
Prompt SHA256: `d46d91c533c3dba948c233e4c685e841c85e21ee509b6bbeed95361ed95c2a17`; rendered SHA256: `21b102e4a547cf07240b16b2a514489f26a113ef72dd45d712450a1a7af2d82b`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D49 maps to Outcome_F93.
State_J94 maps to Outcome_I48.

Question:
According to the supplied mapping, what does State_D49 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_F93"
```

## v360-calibration-002 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?
Supplied intermediate: `State_C68`
Expected: `Outcome_E87`; parsed: C; normalized: `Outcome_E87`; truncated: False
Prompt SHA256: `19a6257fe1f529811b8c2410ea43eff14d86401bf03f8e13966959ebfc3b4d16`; rendered SHA256: `d20bc78f739fc18c560abe412f6ed4149305965086b37f73e22ed10cdd28410d`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_C68 maps to Outcome_E87.
State_K13 maps to Outcome_N34.

Current entity:
Entity_H61

Working intermediate state:
State_C68

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_E87"
```

## v360-calibration-005 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?
Supplied intermediate: `State_R00`
Expected: `Outcome_Z51`; parsed: Cp; normalized: `Outcome_Z51`; truncated: False
Prompt SHA256: `471616ea20261fd2a2878af4e0f0c1c6dce4f1a414655ff383520a853305e749`; rendered SHA256: `6acf486596f98a0431c38a1aee5c936dd32f4d4bad1e270d979ced9f9808fb6e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R00 maps to Outcome_Z51.
State_R64 maps to Outcome_M36.

Current entity:
Entity_D18

Working intermediate state:
State_R00

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_Z51"
```

## v360-calibration-020 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_D25 map to?
Supplied intermediate: `State_D25`
Expected: `Outcome_K93`; parsed: C; normalized: `Outcome_K93`; truncated: False
Prompt SHA256: `46d43f196081a1b5ba620451662933e455c4348cbcc347b1b78501c7e740507d`; rendered SHA256: `a1a47edb8637769d921274c1aa5a24caf99bd0b2fa2e2e2f496e92994fdb06aa`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M13 maps to Outcome_G48.
State_D25 maps to Outcome_K93.

Question:
According to the supplied mapping, what does State_D25 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_K93"
```

## v360-calibration-011 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?
Supplied intermediate: `State_J91`
Expected: `Outcome_B21`; parsed: C; normalized: `Outcome_B21`; truncated: False
Prompt SHA256: `6cf221c9ad5f9d58a7e3edfb4367af3b57849aabab29b67d7e14a1c7c5b3862c`; rendered SHA256: `ced5f03359ea31ba34216a44b0b329aaecce20af7efa90ca5475b259115f1e12`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_I31 maps to Outcome_C69.
State_J91 maps to Outcome_B21.

Current entity:
Entity_L33

Working intermediate state:
State_J91

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_B21"
```

## v360-calibration-005 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_R64 map to?
Supplied intermediate: `State_R64`
Expected: `Outcome_M36`; parsed: C; normalized: `Outcome_M36`; truncated: False
Prompt SHA256: `53541615d9879c55dbd9a723a80abf4ce867d2176a888e7df312e725c030acc7`; rendered SHA256: `b45f15be22619c5c6d8407e63a0eacdde89e176b9aa2d951266d9a1e5227a15c`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R00 maps to Outcome_Z51.
State_R64 maps to Outcome_M36.

Question:
According to the supplied mapping, what does State_R64 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M36"
```

## v360-calibration-015 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?
Supplied intermediate: `State_X78`
Expected: `Outcome_K40`; parsed: Cp; normalized: `Outcome_K40`; truncated: False
Prompt SHA256: `ae61769486813ad95ad570f257a3c7f10904b0065928d91b77ad897933d90d12`; rendered SHA256: `19de0b4e5b24a42f96ba49b760d656c0ed1ad183849fa883fb1d8644adc98c56`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R43 maps to Outcome_T88.
State_X78 maps to Outcome_K40.

Current entity:
Entity_I23

Working intermediate state:
State_X78

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_K40"
```

## v360-calibration-002 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_C68 map to?
Supplied intermediate: `State_C68`
Expected: `Outcome_E87`; parsed: C; normalized: `Outcome_E87`; truncated: False
Prompt SHA256: `c31d560f22051f835be29dfb13eb6d8def693402be61dde5b2a0d0a56d98855c`; rendered SHA256: `11d42ea7a697af4521b6540d64b113d0a3976a08aa497f2458cc5291e8a7cd71`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_C68 maps to Outcome_E87.
State_K13 maps to Outcome_N34.

Question:
According to the supplied mapping, what does State_C68 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_E87"
```

## v360-calibration-017 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?
Supplied intermediate: `State_V08`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `14ddcfe4746e50168e4892e85b92027f77396574b3c8bc3c6935be096ef7347f`; rendered SHA256: `18bf0376cd92879f815a50f03fb29817d94a39b6caf4baf816fa0d7789a2fd41`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_I11 maps to Outcome_H41.
State_J32 maps to Outcome_E53.

Current entity:
Entity_K46

Working intermediate state:
State_V08

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-013 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?
Supplied intermediate: `State_Z41`
Expected: `Outcome_D95`; parsed: C; normalized: `Outcome_D95`; truncated: False
Prompt SHA256: `fc1bb0549d65f2ea0fd8e40207c20c4744a603f97b5c8934d0af44e8e4593f69`; rendered SHA256: `d19a99c0bcf5b2b9111fb46ad3756efdd91a3043477c7b44a5ec250739b56a1d`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z41 maps to Outcome_D95.
State_V34 maps to Outcome_L31.

Current entity:
Entity_A61

Working intermediate state:
State_Z41

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_D95"
```

## v360-calibration-014 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?
Supplied intermediate: `State_F19`
Expected: `Outcome_B00`; parsed: C; normalized: `Outcome_B00`; truncated: False
Prompt SHA256: `492ef0242172b3a1999fa3268c9d8f7ffc7f79995584d363bf4369a6a0f7b4e5`; rendered SHA256: `bb9a7a6377a4e0377f3710fb737b976d2a013cb22396f2673d6a97b8d44266f6`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_L73 maps to Outcome_A74.
State_F19 maps to Outcome_B00.

Current entity:
Entity_U55

Working intermediate state:
State_F19

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_B00"
```

## v360-calibration-005 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?
Supplied intermediate: `State_R64`
Expected: `Outcome_Z51`; parsed: Cp; normalized: `Outcome_Z51`; truncated: False
Prompt SHA256: `3fdfd6a32124473551e5f2f17f302ca47b1ecd17438f203f6e33aab774049b78`; rendered SHA256: `72095142e01dfd9addef70e026a165d22f1299ffc15b6acee7b16cf78917a598`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R00 maps to Outcome_M36.
State_R64 maps to Outcome_Z51.

Current entity:
Entity_D18

Working intermediate state:
State_R64

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_Z51"
```

## v360-calibration-002 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?
Supplied intermediate: `State_S67`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `37aa816b84541c2d5d40736e454579056e9fa6c05f5ea2886894079a06854c0f`; rendered SHA256: `4d021776344f49673020c39109a99472bd3085c20f2f640d0f77bc76bdc1bcf8`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_C68 maps to Outcome_E87.
State_K13 maps to Outcome_N34.

Current entity:
Entity_H61

Working intermediate state:
State_S67

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-003 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?
Supplied intermediate: `State_Z43`
Expected: `Outcome_P70`; parsed: Cp; normalized: `Outcome_P70`; truncated: False
Prompt SHA256: `5b65677aac44d42734bad38edd5b5ed27cd39015dea5b8fddc106567bf210682`; rendered SHA256: `84b7405519e3748f5744f33e593ce61ec254eb52fd431b630370b2395a430c9e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z43 maps to Outcome_P70.
State_Z38 maps to Outcome_L24.

Current entity:
Entity_F60

Working intermediate state:
State_Z43

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_P70"
```

## v360-calibration-020 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?
Supplied intermediate: `State_D25`
Expected: `Outcome_K93`; parsed: C; normalized: `Outcome_K93`; truncated: False
Prompt SHA256: `623b001d90cb85b6fcfb7cabf8c07a2d0dc276fbeb25f230af2dc32937be7509`; rendered SHA256: `e0b0dae5025e97408e57c0ff75092389296c2884cc840480e1c7fb85e1205e4b`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D25 maps to Outcome_K93.
State_M13 maps to Outcome_G48.

Current entity:
Entity_P81

Working intermediate state:
State_D25

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_K93"
```

## v360-calibration-004 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_M06 map to?
Supplied intermediate: `State_M06`
Expected: `Outcome_I15`; parsed: Cp; normalized: `Outcome_I15`; truncated: False
Prompt SHA256: `48b28a230529470490f0600f826a7588ba91c6f56bbf6ae85cc29636d71d6f75`; rendered SHA256: `afb41b59c145a122b03467bbf4aa230fb7ed88a316ddd35c938796add817fdba`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_O94 maps to Outcome_N09.
State_M06 maps to Outcome_I15.

Question:
According to the supplied mapping, what does State_M06 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_I15"
```

## v360-calibration-008 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_Z91?
Supplied intermediate: `State_H25`
Expected: `Outcome_C61`; parsed: C; normalized: `Outcome_C61`; truncated: False
Prompt SHA256: `aec0da90a7b30c6db94e0c2a98e5de048c6923a12098fd89d29ec651dc1210b4`; rendered SHA256: `7c6d6906cbb4dfec44c5bc8ad0f6f80df25638e1d237d210d4910091dc10597e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_H25 maps to Outcome_C61.
State_P32 maps to Outcome_H92.

Current entity:
Entity_Z91

Working intermediate state:
State_H25

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_Z91?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_C61"
```

## v360-calibration-020 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U89?
Supplied intermediate: `State_D25`
Expected: `Outcome_K93`; parsed: C; normalized: `Outcome_K93`; truncated: False
Prompt SHA256: `ed13445d4b5e66be42dba1f711cd7f7b91619f7f8ff0c417a301b3761eac53e5`; rendered SHA256: `887d1b559a2c60f570d3f733f3209bb95cf136b00c4b24dd8f751262c99b5cf5`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M13 maps to Outcome_G48.
State_D25 maps to Outcome_K93.

Current entity:
Entity_U89

Working intermediate state:
State_D25

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U89?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_K93"
```

## v360-calibration-012 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?
Supplied intermediate: `State_E16`
Expected: `Outcome_A20`; parsed: Cp; normalized: `Outcome_A20`; truncated: False
Prompt SHA256: `d5e6fc583789b317f4f99741f6c5a864682b78322455aa1b2112fa4e8cb09c0a`; rendered SHA256: `3bdfa3bce6ca20a18afb684050f5de32675c90473659177bc21e0892db67ec27`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E16 maps to Outcome_A20.
State_M41 maps to Outcome_W11.

Current entity:
Entity_R10

Working intermediate state:
State_E16

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A20"
```

## v360-calibration-019 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?
Supplied intermediate: `State_D75`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `f60f545f7737fb636da422d9a378271513d336aac06b3e7d0b8e253b5eca8d27`; rendered SHA256: `e9a91487b81eb4f8d04c3828a749dcbf286032a225cc8829644f575561a13c14`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_T91 maps to Outcome_W79.
State_M70 maps to Outcome_V51.

Current entity:
Entity_A34

Working intermediate state:
State_D75

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-014 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?
Supplied intermediate: `State_F19`
Expected: `Outcome_A74`; parsed: Cp; normalized: `Outcome_A74`; truncated: False
Prompt SHA256: `2f38e0947d2a520fe8536bf8f1fec469187883726bc4a8084d76a62023db8726`; rendered SHA256: `29227ebca2cfc6672ddf11187705565f0bb94d39c9563c575dc9675767ad748a`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_F19 maps to Outcome_A74.
State_L73 maps to Outcome_B00.

Current entity:
Entity_U55

Working intermediate state:
State_F19

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A74"
```

## v360-calibration-020 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?
Supplied intermediate: `State_M13`
Expected: `Outcome_G48`; parsed: Cp; normalized: `Outcome_G48`; truncated: False
Prompt SHA256: `97a413fe9bce0f358aabae17c95eb8f64118e34d6b7718379f52bd5f64a0ba91`; rendered SHA256: `b2b078341a6ccc927305a37fb96f3f5be05e41e56d938d4b533e2aa7ff573d49`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M13 maps to Outcome_G48.
State_D25 maps to Outcome_K93.

Current entity:
Entity_P81

Working intermediate state:
State_M13

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_G48"
```

## v360-calibration-010 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_A36 map to?
Supplied intermediate: `State_A36`
Expected: `Outcome_X40`; parsed: Cp; normalized: `Outcome_X40`; truncated: False
Prompt SHA256: `680b2c6dd52436236694ad2d9337a09da01a24f8044ba8893f51cbc8460980d4`; rendered SHA256: `fd64b5ed079f0aca843f9f8335732cdb39ff9179917b8094e27228ed290ecf89`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y20 maps to Outcome_V88.
State_A36 maps to Outcome_X40.

Question:
According to the supplied mapping, what does State_A36 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_X40"
```

## v360-calibration-017 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?
Supplied intermediate: `State_J32`
Expected: `Outcome_E53`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `97cd1198bb72ff978a5252c24c5f78eee5984b7c72670645a7826f0347296b17`; rendered SHA256: `6769cb57edbec3fc137904c44420a5cbea82522af1071838e6547a45edc08856`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_I11 maps to Outcome_H41.
State_J32 maps to Outcome_E53.

Current entity:
Entity_K46

Working intermediate state:
State_J32

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-020 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_M13 map to?
Supplied intermediate: `State_M13`
Expected: `Outcome_G48`; parsed: Cp; normalized: `Outcome_G48`; truncated: False
Prompt SHA256: `fd6a19522bb13706248f6c716c6ceeecea1ca121261966045703c3f430a8828d`; rendered SHA256: `b2717fd1c506e0f280b38430b9f96ebed7d932fba4a9b894fa76a015d36f24cb`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M13 maps to Outcome_G48.
State_D25 maps to Outcome_K93.

Question:
According to the supplied mapping, what does State_M13 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_G48"
```

## v360-calibration-009 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?
Supplied intermediate: `State_J02`
Expected: `Outcome_D81`; parsed: Cp; normalized: `Outcome_D81`; truncated: False
Prompt SHA256: `84463229e3ead77c1b84872a0ccfcf472e6055011217698c419b7f59e49f0618`; rendered SHA256: `39d10455e984367949f3eebf65f126eb1a01a664432b3f4732dcf8e814eb6447`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J02 maps to Outcome_D81.
State_H06 maps to Outcome_S45.

Current entity:
Entity_E83

Working intermediate state:
State_J02

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_D81"
```

## v360-calibration-019 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_O18?
Supplied intermediate: `State_M70`
Expected: `Outcome_V51`; parsed: C; normalized: `Outcome_V51`; truncated: False
Prompt SHA256: `bb2941c47623786a5597b6df76d5f2fd7ac50042f08bd041f39bf634ec4b939e`; rendered SHA256: `132147f63d319de1a05f6b40b3f86a3620162b2c64d9cb83aef3b1f992538478`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_T91 maps to Outcome_W79.
State_M70 maps to Outcome_V51.

Current entity:
Entity_O18

Working intermediate state:
State_M70

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_O18?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_V51"
```

## v360-calibration-004 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?
Supplied intermediate: `State_O94`
Expected: `Outcome_I15`; parsed: Cp; normalized: `Outcome_I15`; truncated: False
Prompt SHA256: `b208f06c3d683a986e1e781befba9050f41d283ac33a1e8d266ba19c5549cb94`; rendered SHA256: `2bc4e1adbd81bba1f3921dc129d54a1a91eacfc12e84334658c00b3b8a49014e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_O94 maps to Outcome_I15.
State_M06 maps to Outcome_N09.

Current entity:
Entity_G19

Working intermediate state:
State_O94

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_I15"
```

## v360-calibration-002 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_K13 map to?
Supplied intermediate: `State_K13`
Expected: `Outcome_N34`; parsed: Cp; normalized: `Outcome_N34`; truncated: False
Prompt SHA256: `2a9c475bc0f69f5541437d65e1aa9621f83a13eb53aeaf46e22b00f8fd02ecc8`; rendered SHA256: `48b01d7ea508bcd9883df12e37162d50c7a646c4c1cb5df7b6f79099e855db03`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_C68 maps to Outcome_E87.
State_K13 maps to Outcome_N34.

Question:
According to the supplied mapping, what does State_K13 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_N34"
```

## v360-calibration-003 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?
Supplied intermediate: `State_Z38`
Expected: `Outcome_L24`; parsed: C; normalized: `Outcome_L24`; truncated: False
Prompt SHA256: `302dd38de16e0144893fd847e0533fc58a07e1850685b5a25d9e45efeb901bb1`; rendered SHA256: `d198b3a4e11f5ee2435394c0adb882656e04189a567766b8bed114a37b50bd15`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z38 maps to Outcome_L24.
State_Z43 maps to Outcome_P70.

Current entity:
Entity_F60

Working intermediate state:
State_Z38

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_L24"
```

## v360-calibration-013 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?
Supplied intermediate: `State_V34`
Expected: `Outcome_L31`; parsed: Cp; normalized: `Outcome_L31`; truncated: False
Prompt SHA256: `3e34dea778820e101132cacfd7052ed82f231bbe98b3aa292762569e72fb23c1`; rendered SHA256: `9825d7a25847b4459335950c43223895b3868c2f1d288abf671fdf3cc8e4dcc2`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_V34 maps to Outcome_L31.
State_Z41 maps to Outcome_D95.

Current entity:
Entity_A61

Working intermediate state:
State_V34

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_L31"
```

## v360-calibration-008 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?
Supplied intermediate: `State_P32`
Expected: `Outcome_H92`; parsed: Cp; normalized: `Outcome_H92`; truncated: False
Prompt SHA256: `babd633b55097514d09517796f0d9bd1ab4a21febc88c6fc3c943fdf21943487`; rendered SHA256: `cafc5c15887de741d269259def37c17f0d5f1304e75740afe2493047370c32fe`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_H25 maps to Outcome_C61.
State_P32 maps to Outcome_H92.

Current entity:
Entity_E79

Working intermediate state:
State_P32

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_H92"
```

## v360-calibration-004 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?
Supplied intermediate: `State_O94`
Expected: `Outcome_N09`; parsed: C; normalized: `Outcome_N09`; truncated: False
Prompt SHA256: `25c61b0908f80e13bdbb7afc7132acf91344338d5e94ed64f4a903ae8bb0ee8c`; rendered SHA256: `ec5e661230d122243a0af865512b90cd934168541f3c3c8b8f4690b4e307b133`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_O94 maps to Outcome_N09.
State_M06 maps to Outcome_I15.

Current entity:
Entity_G19

Working intermediate state:
State_O94

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_N09"
```

## v360-calibration-013 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?
Supplied intermediate: `State_F29`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `6afe1b1c97be2ed460a3e9729cfcb93f01dc9ba6ba177ca9c232afd24b7fec31`; rendered SHA256: `77608904e68baeb3705cd7316e183ebb8d0198c633774a37b43ab85d161c7882`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_V34 maps to Outcome_L31.
State_Z41 maps to Outcome_D95.

Current entity:
Entity_A61

Working intermediate state:
State_F29

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-014 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_L73 map to?
Supplied intermediate: `State_L73`
Expected: `Outcome_A74`; parsed: Cp; normalized: `Outcome_A74`; truncated: False
Prompt SHA256: `76577b22ff84abcfc5888a149b551a29ddaeb8ce6f376285c68aba3e12fa8f3b`; rendered SHA256: `59740f89c04b2e8287c9a76b19b26a989554da9d53d758393c3f8be91d63666b`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_F19 maps to Outcome_B00.
State_L73 maps to Outcome_A74.

Question:
According to the supplied mapping, what does State_L73 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A74"
```

## v360-calibration-020 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?
Supplied intermediate: `State_D25`
Expected: `Outcome_K93`; parsed: C; normalized: `Outcome_K93`; truncated: False
Prompt SHA256: `8d7cfa5aff1600f497a76386f81e4bdcbd16f5d731bdc184f4f8f88bfe6d5901`; rendered SHA256: `2d7afb7a258fd608ecc7989f64c820d88a4d7e5f8f618afaee0dd26eb5551a49`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M13 maps to Outcome_G48.
State_D25 maps to Outcome_K93.

Current entity:
Entity_P81

Working intermediate state:
State_D25

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_K93"
```

## v360-calibration-017 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?
Supplied intermediate: `State_I11`
Expected: `Outcome_H41`; parsed: Cp; normalized: `Outcome_H41`; truncated: False
Prompt SHA256: `b304b1ffcfd57e28894393df1206d70e7060dfa116ec9ba27ecce9bb631a36af`; rendered SHA256: `0a6d0b6597e0c349ee81b77e0f7b6ebb2e706a8692b78bbfba003314824ac4c3`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_I11 maps to Outcome_H41.
State_J32 maps to Outcome_E53.

Current entity:
Entity_K46

Working intermediate state:
State_I11

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_H41"
```

## v360-calibration-012 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_M41 map to?
Supplied intermediate: `State_M41`
Expected: `Outcome_W11`; parsed: C; normalized: `Outcome_W11`; truncated: False
Prompt SHA256: `a2a142c452ff1f3563f554b9a8625cfa9a58b99a8e6a92f02cfae7b0aa46a1fa`; rendered SHA256: `cf4595122c015327d7b4bd843c79ba1aaef84e7bb027537082263f2d49ea2a2f`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E16 maps to Outcome_A20.
State_M41 maps to Outcome_W11.

Question:
According to the supplied mapping, what does State_M41 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_W11"
```

## v360-calibration-008 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_H25 map to?
Supplied intermediate: `State_H25`
Expected: `Outcome_C61`; parsed: C; normalized: `Outcome_C61`; truncated: False
Prompt SHA256: `9e0c8aab95186e9f7de9ce208bff35098f70b7a8a890b99ef48d929692a31b71`; rendered SHA256: `2761dff11a9a2bb98221bf40e4330a3d664ed83aaf9859333ef1cdc1bcba363a`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_H25 maps to Outcome_C61.
State_P32 maps to Outcome_H92.

Question:
According to the supplied mapping, what does State_H25 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_C61"
```

## v360-calibration-019 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_M70 map to?
Supplied intermediate: `State_M70`
Expected: `Outcome_V51`; parsed: C; normalized: `Outcome_V51`; truncated: False
Prompt SHA256: `672725591ba898b508ac4a7618ec352d0ad1a635d27b1a0befe2f70214b65bbb`; rendered SHA256: `8e540f8c2c6a4d17044d2214772f578e06e2fe9db587d2220f270ba4938ef813`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_T91 maps to Outcome_W79.
State_M70 maps to Outcome_V51.

Question:
According to the supplied mapping, what does State_M70 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_V51"
```

## v360-calibration-018 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_W35?
Supplied intermediate: `State_D36`
Expected: `Outcome_M04`; parsed: C; normalized: `Outcome_M04`; truncated: False
Prompt SHA256: `cd6d1a6bf9caa36b05abcf039ba15155fe157928f7f51781c49e39c5ca041ba5`; rendered SHA256: `1e83015a63e6bb72bf503dc5a9eb179fa9167507de700be8f964a950b7acf99a`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Q80 maps to Outcome_J28.
State_D36 maps to Outcome_M04.

Current entity:
Entity_W35

Working intermediate state:
State_D36

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_W35?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M04"
```

## v360-calibration-010 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?
Supplied intermediate: `State_Y20`
Expected: `Outcome_X40`; parsed: Cp; normalized: `Outcome_X40`; truncated: False
Prompt SHA256: `f79def02509124e5557ed88337744c30e024a730b7d645250e391ef630e0fb6a`; rendered SHA256: `f1c3d4b29338779f56530cac080a94b81b3fded5aaa8b775a85fb92539e2c21e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y20 maps to Outcome_X40.
State_A36 maps to Outcome_V88.

Current entity:
Entity_E59

Working intermediate state:
State_Y20

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_X40"
```

## v360-calibration-016 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?
Supplied intermediate: `State_B20`
Expected: `Outcome_X89`; parsed: C; normalized: `Outcome_X89`; truncated: False
Prompt SHA256: `56f6104c734e0f16a6da071dabe6c3ee25f07426f85b8524e9e207e1556442ca`; rendered SHA256: `773f9078ab83a2c33ff5fd8e7eef0380b377e219688c0d78245ad7dffb3dbbf7`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_B20 maps to Outcome_X89.
State_D05 maps to Outcome_Q30.

Current entity:
Entity_R01

Working intermediate state:
State_B20

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_X89"
```

## v360-calibration-014 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_F19 map to?
Supplied intermediate: `State_F19`
Expected: `Outcome_B00`; parsed: C; normalized: `Outcome_B00`; truncated: False
Prompt SHA256: `d8c2cf0fdb15654e612dd6e1355b77cee52b5dc09eb93543327528c055ad7878`; rendered SHA256: `81ea362a52dbca7f275c1d4c1bf9a7ffe26356806f2f574ea788e40dde9f1628`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_F19 maps to Outcome_B00.
State_L73 maps to Outcome_A74.

Question:
According to the supplied mapping, what does State_F19 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_B00"
```

## v360-calibration-017 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_B59?
Supplied intermediate: `State_J32`
Expected: `Outcome_E53`; parsed: C; normalized: `Outcome_E53`; truncated: False
Prompt SHA256: `26b4c84ab898a5e6f05eb4a2e16cb266a485a67cfe055d4d1995091f95e87bf2`; rendered SHA256: `7042dbfc9cff6d6c41854cc301e4094131b4a678096852a41e8e3cb1172030df`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_I11 maps to Outcome_H41.
State_J32 maps to Outcome_E53.

Current entity:
Entity_B59

Working intermediate state:
State_J32

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_B59?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_E53"
```

## v360-calibration-002 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?
Supplied intermediate: `State_K13`
Expected: `Outcome_N34`; parsed: Cp; normalized: `Outcome_N34`; truncated: False
Prompt SHA256: `99b2cd83362d7c8bbe5fab2b2993c91ab079ad557cc4db17565e09c574168e72`; rendered SHA256: `1e5f5fd7d2a00ff00bcb92f13dd88dbe3a1a06ebde32535aad47e03b38cc43d8`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_C68 maps to Outcome_E87.
State_K13 maps to Outcome_N34.

Current entity:
Entity_H61

Working intermediate state:
State_K13

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_N34"
```

## v360-calibration-004 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L30?
Supplied intermediate: `State_O94`
Expected: `Outcome_N09`; parsed: C; normalized: `Outcome_N09`; truncated: False
Prompt SHA256: `688ea0741854b1cfb82d9f56e1642fc73e9329fdfef6559ae6425f8ff145f121`; rendered SHA256: `dcf5b20711ebe1499776f9ba9564966b7a426a37a8d63faf507fb96f2113d135`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_O94 maps to Outcome_N09.
State_M06 maps to Outcome_I15.

Current entity:
Entity_L30

Working intermediate state:
State_O94

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L30?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_N09"
```

## v360-calibration-019 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?
Supplied intermediate: `State_M70`
Expected: `Outcome_V51`; parsed: C; normalized: `Outcome_V51`; truncated: False
Prompt SHA256: `9e4e73802202ce558ee68745d0525dc260ba22b9b5582433ee7d3fea4a069077`; rendered SHA256: `16de0375a3eae107fe7b676fdc37d095db2862cf0580cb2d05ca2ea54b8f0d6e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_T91 maps to Outcome_W79.
State_M70 maps to Outcome_V51.

Current entity:
Entity_A34

Working intermediate state:
State_M70

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_V51"
```

## v360-calibration-008 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?
Supplied intermediate: `State_H25`
Expected: `Outcome_H92`; parsed: Cp; normalized: `Outcome_H92`; truncated: False
Prompt SHA256: `de6b71ebc77107b9b4281739fae95d8ee8415ce49f841222ce1adacfbbccdc0b`; rendered SHA256: `f1ed6b998138bb6fa608ddbe169d2d63bdcfcfc2b4f0c304c977ca9559412106`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_H25 maps to Outcome_H92.
State_P32 maps to Outcome_C61.

Current entity:
Entity_E79

Working intermediate state:
State_H25

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_H92"
```

## v360-calibration-004 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?
Supplied intermediate: `State_M06`
Expected: `Outcome_I15`; parsed: Cp; normalized: `Outcome_I15`; truncated: False
Prompt SHA256: `39189775661a18aa29b9b947f73e2b81f86ab4ae97be038f1fcc2c60cee081d4`; rendered SHA256: `b252883a27fd5fa89eebe10a70cb2c81ec5df10f8642cbec14217e3295f13aa6`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_O94 maps to Outcome_N09.
State_M06 maps to Outcome_I15.

Current entity:
Entity_G19

Working intermediate state:
State_M06

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_I15"
```

## v360-calibration-016 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?
Supplied intermediate: `State_D90`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `4d47f234a19fde39b7b6bc554063a3bb1e96ba7b2ee3bb9fead25472018c4981`; rendered SHA256: `d6f0c96d3afe0ef1777d3cc59117fdbcd6ab1d863ad2912093d18e9b8b629994`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D05 maps to Outcome_Q30.
State_B20 maps to Outcome_X89.

Current entity:
Entity_R01

Working intermediate state:
State_D90

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-007 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_T18 map to?
Supplied intermediate: `State_T18`
Expected: `Outcome_R32`; parsed: C; normalized: `Outcome_R32`; truncated: False
Prompt SHA256: `01b519289d797e0388bb7427d2e77c5d40b9b0f7ad3ca3df658713a6deb9d066`; rendered SHA256: `35414316d9533321aef309f883b002282bd199633487d15fb38a4b1d4654045b`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E40 maps to Outcome_A64.
State_T18 maps to Outcome_R32.

Question:
According to the supplied mapping, what does State_T18 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_R32"
```

## v360-calibration-001 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?
Supplied intermediate: `State_D49`
Expected: `Outcome_F93`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `37415ff01812d0dddb6fae3b383247eb525e6e22dac5f6b065c2995a0b252e14`; rendered SHA256: `fd21e1786ee211b56b4233ad9cc3b1f988229c7daac8b1f992cf2154d2f8cc68`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D49 maps to Outcome_F93.
State_J94 maps to Outcome_I48.

Current entity:
Entity_J44

Working intermediate state:
State_D49

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-015 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?
Supplied intermediate: `State_R43`
Expected: `Outcome_T88`; parsed: C; normalized: `Outcome_T88`; truncated: False
Prompt SHA256: `e80a8ba61e2b0fa566523704751b9768f7588684462ea1f280ebcbaea7d733d0`; rendered SHA256: `9973b12a6e87c5b5997647df01b408ab6ac844ce1242434e730a3093baeb8fb6`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R43 maps to Outcome_T88.
State_X78 maps to Outcome_K40.

Current entity:
Entity_I23

Working intermediate state:
State_R43

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_T88"
```

## v360-calibration-008 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?
Supplied intermediate: `State_H25`
Expected: `Outcome_C61`; parsed: C; normalized: `Outcome_C61`; truncated: False
Prompt SHA256: `ac1e35dd0ed9f597546c4b8da71e9df822cccae4759cd9035cbde0a52cbde7a1`; rendered SHA256: `ff461553fe03c5ccd9922d411138e4fd3d2805af515b02fa53366c5b97e79197`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_H25 maps to Outcome_C61.
State_P32 maps to Outcome_H92.

Current entity:
Entity_E79

Working intermediate state:
State_H25

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_C61"
```

## v360-calibration-020 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?
Supplied intermediate: `State_G69`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `2843a280c70722552c6b60b404bc6a0b899e3315a6c7f233f77bdebe2d5891a0`; rendered SHA256: `83b9efd6989eaf73e63b6fbfcd19a52056fc07d812a98e86e92c69e90e1a3aed`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M13 maps to Outcome_G48.
State_D25 maps to Outcome_K93.

Current entity:
Entity_P81

Working intermediate state:
State_G69

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-019 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?
Supplied intermediate: `State_M70`
Expected: `Outcome_V51`; parsed: C; normalized: `Outcome_V51`; truncated: False
Prompt SHA256: `b707756178b682af79368924ed308ddb0026c90b298e4bde68cb459e416822d1`; rendered SHA256: `4932911ff2564014f142a98a96f87120f9f50ac351f876aeb57f7be8b78d7d0c`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M70 maps to Outcome_V51.
State_T91 maps to Outcome_W79.

Current entity:
Entity_A34

Working intermediate state:
State_M70

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_V51"
```

## v360-calibration-006 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_W27 map to?
Supplied intermediate: `State_W27`
Expected: `Outcome_A15`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `8f6acdb5e996f7501525f32ad6a967d1e4a4159bfc19402f2f781c05a2346725`; rendered SHA256: `b91e3776be8ed783a51667be27ddae50c0a2a0bb71ef12c2a5d017201359cc32`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y82 maps to Outcome_M73.
State_W27 maps to Outcome_A15.

Question:
According to the supplied mapping, what does State_W27 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-001 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?
Supplied intermediate: `State_D49`
Expected: `Outcome_I48`; parsed: Cp; normalized: `Outcome_I48`; truncated: False
Prompt SHA256: `0c52de96491e801f75ce4b97e60de14a289a3f13c8807e5e0e8c1af7ccf5f873`; rendered SHA256: `25f8a777ed031f34c5f055624735e1b7304c93b16ea4416534cb901ac6ceb029`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D49 maps to Outcome_I48.
State_J94 maps to Outcome_F93.

Current entity:
Entity_J44

Working intermediate state:
State_D49

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_I48"
```

## v360-calibration-016 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P78?
Supplied intermediate: `State_B20`
Expected: `Outcome_X89`; parsed: C; normalized: `Outcome_X89`; truncated: False
Prompt SHA256: `bb59bdaa72e8e80a323ce1eb7b3a222c9229ae047b53e115f5ea81eb47ee768a`; rendered SHA256: `577fda65f3f10aa756fa206693bae509af0e3ffc5508290d86582fc9cf23664e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D05 maps to Outcome_Q30.
State_B20 maps to Outcome_X89.

Current entity:
Entity_P78

Working intermediate state:
State_B20

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P78?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_X89"
```

## v360-calibration-019 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?
Supplied intermediate: `State_M70`
Expected: `Outcome_W79`; parsed: Cp; normalized: `Outcome_W79`; truncated: False
Prompt SHA256: `0f7f02c66e0a329b06958f83c7d34ae69790e0f113e9d86fcc4df6574ab530fd`; rendered SHA256: `74e2f675a2da3fb9dfc084585bf8760c6b703354891ceea6262eb4b8ed9703d0`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_T91 maps to Outcome_V51.
State_M70 maps to Outcome_W79.

Current entity:
Entity_A34

Working intermediate state:
State_M70

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_W79"
```

## v360-calibration-009 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_H06 map to?
Supplied intermediate: `State_H06`
Expected: `Outcome_D81`; parsed: Cp; normalized: `Outcome_D81`; truncated: False
Prompt SHA256: `507a90dfbbd24722557417e83b4f95284fd2ee069ac9db5e4c7aecbb4699d2c6`; rendered SHA256: `bec2d779e6c8b10f6a56304e36aea3791ae4a48e3648ed26a7055fa0b3865c34`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J02 maps to Outcome_S45.
State_H06 maps to Outcome_D81.

Question:
According to the supplied mapping, what does State_H06 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_D81"
```

## v360-calibration-012 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?
Supplied intermediate: `State_M41`
Expected: `Outcome_W11`; parsed: C; normalized: `Outcome_W11`; truncated: False
Prompt SHA256: `a0d85c197583ed6e514280f66900e84681ae6d377b7a5a33c862be8e9eacaae3`; rendered SHA256: `69b15399e907a9201bc82b9696c94f9fd668330e2f11bbc39ee356bb77f6baa3`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M41 maps to Outcome_W11.
State_E16 maps to Outcome_A20.

Current entity:
Entity_R10

Working intermediate state:
State_M41

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_W11"
```

## v360-calibration-013 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?
Supplied intermediate: `State_Z41`
Expected: `Outcome_L31`; parsed: Cp; normalized: `Outcome_L31`; truncated: False
Prompt SHA256: `e94a64e0a022c074a1c32e3911ecd5cc5c9c2f872c53f3bf13084d381c9c3803`; rendered SHA256: `ee2054b3fa0e669450533c8a36024c6758a98ae8cb9bb9090d2c78ed593695f0`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_V34 maps to Outcome_D95.
State_Z41 maps to Outcome_L31.

Current entity:
Entity_A61

Working intermediate state:
State_Z41

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_L31"
```

## v360-calibration-018 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_D36 map to?
Supplied intermediate: `State_D36`
Expected: `Outcome_M04`; parsed: C; normalized: `Outcome_M04`; truncated: False
Prompt SHA256: `832f65a808f3e7da27966c66d799c56b856a6e289cf86d64acb94901db13309f`; rendered SHA256: `09b864116f590f6582c9e7daa3fcb76cadd688d302886459807f9a11b03b4a8f`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Q80 maps to Outcome_J28.
State_D36 maps to Outcome_M04.

Question:
According to the supplied mapping, what does State_D36 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M04"
```

## v360-calibration-005 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I24?
Supplied intermediate: `State_R64`
Expected: `Outcome_M36`; parsed: C; normalized: `Outcome_M36`; truncated: False
Prompt SHA256: `73eb405105b5a1d4eba16f3190c8b9a799257042d35fe1a63ede9c03171c1468`; rendered SHA256: `e8d64a7c1fa24d0895032f12779dac03429868db3aca7968aaa3b411e9150b18`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R00 maps to Outcome_Z51.
State_R64 maps to Outcome_M36.

Current entity:
Entity_I24

Working intermediate state:
State_R64

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I24?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M36"
```

## v360-calibration-006 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?
Supplied intermediate: `State_Y82`
Expected: `Outcome_M73`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `1d75027a4133f1bb1e53af2d0c8503be54b972c17a3d2fb940f446e7fc3a0b5e`; rendered SHA256: `c2c03bc3d0958dc89f2fbb346eaa050a45039fd5ba08e87849346062e8d7b222`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_W27 maps to Outcome_A15.
State_Y82 maps to Outcome_M73.

Current entity:
Entity_V79

Working intermediate state:
State_Y82

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-015 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_R43 map to?
Supplied intermediate: `State_R43`
Expected: `Outcome_T88`; parsed: C; normalized: `Outcome_T88`; truncated: False
Prompt SHA256: `f8cddce983e22431204f24326f993b3516f3a96869a7ac675cd5b62780d32e23`; rendered SHA256: `9866ff3244e6584e8ef463f5c1f17a760b2cbaf62277105bb27869ad72c86dd6`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R43 maps to Outcome_T88.
State_X78 maps to Outcome_K40.

Question:
According to the supplied mapping, what does State_R43 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_T88"
```

## v360-calibration-007 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?
Supplied intermediate: `State_T18`
Expected: `Outcome_R32`; parsed: C; normalized: `Outcome_R32`; truncated: False
Prompt SHA256: `63783f7f92daf1e967364f3a5885bb3b3340e5b0046581fadea31ed0ca5f7a26`; rendered SHA256: `e60f207b2fa210c7db673f3848f4f242de573bb9f22ae1af17b6634873db98dd`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_T18 maps to Outcome_R32.
State_E40 maps to Outcome_A64.

Current entity:
Entity_N53

Working intermediate state:
State_T18

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_R32"
```

## v360-calibration-010 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_Y20 map to?
Supplied intermediate: `State_Y20`
Expected: `Outcome_V88`; parsed: C; normalized: `Outcome_V88`; truncated: False
Prompt SHA256: `4d0fd472fde01a884f5500161f0bda8cc61bb073b51504944321d14e840129bf`; rendered SHA256: `e3ac36fced26e69a7a1076dd5709e1c0d156f876852331b3e80ad8c5d0f615af`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y20 maps to Outcome_V88.
State_A36 maps to Outcome_X40.

Question:
According to the supplied mapping, what does State_Y20 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_V88"
```

## v360-calibration-005 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?
Supplied intermediate: `State_E86`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `f72e70b35e44cef0ceb7bbb33090a4a2f8cebf3cf7f64428f34095b4661e3897`; rendered SHA256: `e9dd080cbdc9c01cf8f834afcad4510a75333cc52b80797196c739692a679066`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R00 maps to Outcome_Z51.
State_R64 maps to Outcome_M36.

Current entity:
Entity_D18

Working intermediate state:
State_E86

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-015 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?
Supplied intermediate: `State_L96`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `6835b8e0f7d2ac89bdeeaafa135b502fae26e103b913e3475ffe2fc256687f9b`; rendered SHA256: `b6b1b31069745a74d49d7db2581833da131fd166fe8d589d583b27d579408293`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R43 maps to Outcome_T88.
State_X78 maps to Outcome_K40.

Current entity:
Entity_I23

Working intermediate state:
State_L96

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-016 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?
Supplied intermediate: `State_B20`
Expected: `Outcome_Q30`; parsed: Cp; normalized: `Outcome_Q30`; truncated: False
Prompt SHA256: `e38844b8b3ad563dbffec1ea025c65068c62a6421eadc2a05738662b7d072d0f`; rendered SHA256: `d552b3ebf5333524cdb24ac0f48ab2acb1a3d4a914f95bfe9a5c008724a90a6b`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D05 maps to Outcome_X89.
State_B20 maps to Outcome_Q30.

Current entity:
Entity_R01

Working intermediate state:
State_B20

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_Q30"
```

## v360-calibration-012 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_E16 map to?
Supplied intermediate: `State_E16`
Expected: `Outcome_A20`; parsed: Cp; normalized: `Outcome_A20`; truncated: False
Prompt SHA256: `dabb88d33932be53f089f3b6654c65ae8517ef822e53f22ab2b35c91938fa8d4`; rendered SHA256: `6e31ed53870d7e30fa62147ecdf0c4a8af69839d90bc967cf33d0ab58fc46ee5`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E16 maps to Outcome_A20.
State_M41 maps to Outcome_W11.

Question:
According to the supplied mapping, what does State_E16 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A20"
```

## v360-calibration-002 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?
Supplied intermediate: `State_C68`
Expected: `Outcome_N34`; parsed: Cp; normalized: `Outcome_N34`; truncated: False
Prompt SHA256: `c92fb48e8f5afa0520ed0393761bcd36c5bd0276e10de2e88927957e3ce648c5`; rendered SHA256: `109191db3b8197d3c5e237c35b1e102483f27f4ec6e5da1ed95c4582296a53a1`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_C68 maps to Outcome_N34.
State_K13 maps to Outcome_E87.

Current entity:
Entity_H61

Working intermediate state:
State_C68

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_N34"
```

## v360-calibration-009 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?
Supplied intermediate: `State_U03`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `e40f2e5ea589cba9fbd531a489c07bc834f2607eeb4b90ca51537ef2f490e374`; rendered SHA256: `de91f72bce3f85184f632109a5d3371591c7b76f36e4dd41fb50c5717955f005`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J02 maps to Outcome_S45.
State_H06 maps to Outcome_D81.

Current entity:
Entity_E83

Working intermediate state:
State_U03

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-013 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_Z41 map to?
Supplied intermediate: `State_Z41`
Expected: `Outcome_D95`; parsed: C; normalized: `Outcome_D95`; truncated: False
Prompt SHA256: `2696adf7ba0478920b8202f93eb570ca60c8dabc7a292a366fa21d050efdfa78`; rendered SHA256: `5c78297abc1103ac24d6007d51609d74eabfb07907b1a079b664e25989db3053`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_V34 maps to Outcome_L31.
State_Z41 maps to Outcome_D95.

Question:
According to the supplied mapping, what does State_Z41 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_D95"
```

## v360-calibration-015 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?
Supplied intermediate: `State_R43`
Expected: `Outcome_T88`; parsed: C; normalized: `Outcome_T88`; truncated: False
Prompt SHA256: `bfb671d7ea8e68187656d5087a0a04e495148c073d45fd0567e31987e0a16d9c`; rendered SHA256: `d63a8524649274ccc220e98bd9ec35f501cdabc188e804323264d05b76ddddc7`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_X78 maps to Outcome_K40.
State_R43 maps to Outcome_T88.

Current entity:
Entity_I23

Working intermediate state:
State_R43

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_T88"
```

## v360-calibration-011 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_S16?
Supplied intermediate: `State_J91`
Expected: `Outcome_B21`; parsed: C; normalized: `Outcome_B21`; truncated: False
Prompt SHA256: `1974f22191835a800a40ede51e1af6f4d2bfc71a483ed264f801bdfce05c96db`; rendered SHA256: `14fff4fcec98d90d9c245820b8c96eff1db16a34d09753c0636767276110ec25`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J91 maps to Outcome_B21.
State_I31 maps to Outcome_C69.

Current entity:
Entity_S16

Working intermediate state:
State_J91

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_S16?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_B21"
```

## v360-calibration-014 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_T09?
Supplied intermediate: `State_F19`
Expected: `Outcome_B00`; parsed: C; normalized: `Outcome_B00`; truncated: False
Prompt SHA256: `34e0b315fde00c55edb6be0a379aa436834e0229c8faf8c7285a7abdd5efd1b8`; rendered SHA256: `78e5cf036e4769915278919aa921786edcc73338dbea63d4aa60576cb48dfccd`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_F19 maps to Outcome_B00.
State_L73 maps to Outcome_A74.

Current entity:
Entity_T09

Working intermediate state:
State_F19

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_T09?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_B00"
```

## v360-calibration-011 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_J91 map to?
Supplied intermediate: `State_J91`
Expected: `Outcome_B21`; parsed: C; normalized: `Outcome_B21`; truncated: False
Prompt SHA256: `7a3ad00f00be0ca44fa3751c655e6024262a904906ec570cf7655218ee882e3b`; rendered SHA256: `04851945b5aaacbfddd70f4c3dcd9e14da6aef9cea8086fec98cff6963262e20`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J91 maps to Outcome_B21.
State_I31 maps to Outcome_C69.

Question:
According to the supplied mapping, what does State_J91 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_B21"
```

## v360-calibration-019 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_T91 map to?
Supplied intermediate: `State_T91`
Expected: `Outcome_W79`; parsed: Cp; normalized: `Outcome_W79`; truncated: False
Prompt SHA256: `6d6a614fdaa5d7961bdbd62e4f3ab22465e312cb6e01a313a5292846adb5fd81`; rendered SHA256: `f16487852c428740422e5ee12cf7ca90cb633f9985446a7892213c72ebb5fdc0`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_T91 maps to Outcome_W79.
State_M70 maps to Outcome_V51.

Question:
According to the supplied mapping, what does State_T91 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_W79"
```

## v360-calibration-007 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?
Supplied intermediate: `State_T18`
Expected: `Outcome_A64`; parsed: Cp; normalized: `Outcome_A64`; truncated: False
Prompt SHA256: `46e19bbef6c37ccdf31e5b3ff48e87793022f4d878832193639d6624ce51485c`; rendered SHA256: `e9d8f797b6e1bc698553e7b9727e3b8fea252a864055b1e219ab4cb7d37feb53`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E40 maps to Outcome_R32.
State_T18 maps to Outcome_A64.

Current entity:
Entity_N53

Working intermediate state:
State_T18

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A64"
```

## v360-calibration-006 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G37?
Supplied intermediate: `State_Y82`
Expected: `Outcome_M73`; parsed: C; normalized: `Outcome_M73`; truncated: False
Prompt SHA256: `2ea8c6ef950fff8ed12488ba68a2aadec0dabbe1b9c66bc471c7cadab1086c58`; rendered SHA256: `b246a2cd932dbd639dac10dbe0b58f28973aa6295536091dbfe4da27ed720fbc`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y82 maps to Outcome_M73.
State_W27 maps to Outcome_A15.

Current entity:
Entity_G37

Working intermediate state:
State_Y82

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G37?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M73"
```

## v360-calibration-010 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?
Supplied intermediate: `State_Y20`
Expected: `Outcome_V88`; parsed: C; normalized: `Outcome_V88`; truncated: False
Prompt SHA256: `e27cef14eff8b88d5ac535e4c793f3ec9253dfe0944d07b3d454db4a81644b9c`; rendered SHA256: `d94236cb9696b0e24f39105fe37a7ecfc000ad5c39784d97c908e8d1a788918f`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y20 maps to Outcome_V88.
State_A36 maps to Outcome_X40.

Current entity:
Entity_E59

Working intermediate state:
State_Y20

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_V88"
```

## v360-calibration-015 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F24?
Supplied intermediate: `State_R43`
Expected: `Outcome_T88`; parsed: C; normalized: `Outcome_T88`; truncated: False
Prompt SHA256: `3558e9e2ed220b3198d19e18a830e54e4aa325e28d4b46737e662ba6fba31a9b`; rendered SHA256: `2d3cd1067dda1087e056c2b6feea02225686249fbf1759baea0db533987ed3db`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R43 maps to Outcome_T88.
State_X78 maps to Outcome_K40.

Current entity:
Entity_F24

Working intermediate state:
State_R43

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F24?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_T88"
```

## v360-calibration-006 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_Y82 map to?
Supplied intermediate: `State_Y82`
Expected: `Outcome_M73`; parsed: C; normalized: `Outcome_M73`; truncated: False
Prompt SHA256: `64748d5ac6395a18ae70bb1bab7270ec7934309cf4261cdf9b89f9e4e84427c3`; rendered SHA256: `94119f3fff4c797ff967411fdce2e81d6760eb369ad8f92f1f5c40f4861d9220`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y82 maps to Outcome_M73.
State_W27 maps to Outcome_A15.

Question:
According to the supplied mapping, what does State_Y82 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M73"
```

## v360-calibration-011 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?
Supplied intermediate: `State_F89`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `ff8055a75cda62c0671be2981df222772c2a4a578ed98054bcc8d0bc217c73c5`; rendered SHA256: `23edb413f61b8304e6d8c81bb29fbaa38a5e9bfe229f750ba586a1061d9caa9e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J91 maps to Outcome_B21.
State_I31 maps to Outcome_C69.

Current entity:
Entity_L33

Working intermediate state:
State_F89

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-008 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_P32 map to?
Supplied intermediate: `State_P32`
Expected: `Outcome_H92`; parsed: Cp; normalized: `Outcome_H92`; truncated: False
Prompt SHA256: `e79b7ea75357042d1a772fc303e55367bad23936834c22477b819aa49ffcf17b`; rendered SHA256: `525566429afbd7db7a9facfbe787dabf32e9c51699cc21aa1ca4527069571f69`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_H25 maps to Outcome_C61.
State_P32 maps to Outcome_H92.

Question:
According to the supplied mapping, what does State_P32 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_H92"
```

## v360-calibration-002 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D22?
Supplied intermediate: `State_C68`
Expected: `Outcome_E87`; parsed: C; normalized: `Outcome_E87`; truncated: False
Prompt SHA256: `5bc9fd469e1bc644e0e6a7f441156327b95bc7d2d8a9394d39e1ab2b087891d3`; rendered SHA256: `cee18372d8da91cd3313cba31e39f9bdd635f7357978cc0ca24806a902f5ade2`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_C68 maps to Outcome_E87.
State_K13 maps to Outcome_N34.

Current entity:
Entity_D22

Working intermediate state:
State_C68

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D22?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_E87"
```

## v360-calibration-009 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?
Supplied intermediate: `State_H06`
Expected: `Outcome_D81`; parsed: Cp; normalized: `Outcome_D81`; truncated: False
Prompt SHA256: `13d3cf63d8b0106d0c40bfa9b3977563c90df63f02abfae82623454c2305291c`; rendered SHA256: `2d3927f26206c144270597b03934583afdcc1e7f19a13a13abb957d130cffc21`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J02 maps to Outcome_S45.
State_H06 maps to Outcome_D81.

Current entity:
Entity_E83

Working intermediate state:
State_H06

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_D81"
```

## v360-calibration-014 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?
Supplied intermediate: `State_L73`
Expected: `Outcome_A74`; parsed: Cp; normalized: `Outcome_A74`; truncated: False
Prompt SHA256: `6aec40cc5962e4b97e136d3d91b3645077cb699f99d58cf6308d151cd8587494`; rendered SHA256: `79cd247059213251b6f8b4039fbd72b887008c0d938397ab178613abc48203f5`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_F19 maps to Outcome_B00.
State_L73 maps to Outcome_A74.

Current entity:
Entity_U55

Working intermediate state:
State_L73

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A74"
```

## v360-calibration-011 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?
Supplied intermediate: `State_J91`
Expected: `Outcome_B21`; parsed: C; normalized: `Outcome_B21`; truncated: False
Prompt SHA256: `8a5ce6727c8133eca075b46e81a537695bdd1fec2ca034ee80e5168eda4e14d3`; rendered SHA256: `9259d78483d49dc243eb46f607aae9ce6239e83cc5e08ae2cc04ef36bbbc7b1a`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J91 maps to Outcome_B21.
State_I31 maps to Outcome_C69.

Current entity:
Entity_L33

Working intermediate state:
State_J91

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_B21"
```

## v360-calibration-005 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?
Supplied intermediate: `State_R64`
Expected: `Outcome_M36`; parsed: C; normalized: `Outcome_M36`; truncated: False
Prompt SHA256: `ff37b456a43cbbbb7027830f1567abbe3a463fb16c22236ffe7515caaa8189c6`; rendered SHA256: `c85e16bdb037b990a4c8ddd381a96dfa34b363707c8362b3116a895ceceaeba7`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R00 maps to Outcome_Z51.
State_R64 maps to Outcome_M36.

Current entity:
Entity_D18

Working intermediate state:
State_R64

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M36"
```

## v360-calibration-017 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?
Supplied intermediate: `State_J32`
Expected: `Outcome_H41`; parsed: Cp; normalized: `Outcome_H41`; truncated: False
Prompt SHA256: `2087aa4c407db668a49bab9250251f0e3894598ebbd5f77413a309da86fa1a23`; rendered SHA256: `8decef786ca638241388c165864f18685fa159ec93c91999e95c0123b0893381`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_I11 maps to Outcome_E53.
State_J32 maps to Outcome_H41.

Current entity:
Entity_K46

Working intermediate state:
State_J32

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_H41"
```

## v360-calibration-018 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?
Supplied intermediate: `State_L86`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `81f76980ddeb6f5cdc2853220f0613e93dfa14e52a0ecc59e075520d8dd7085a`; rendered SHA256: `84ad7d386e8396accd7c4cebcc3a77e2d9ec236f056759d2b2a42e44d0a7e092`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Q80 maps to Outcome_J28.
State_D36 maps to Outcome_M04.

Current entity:
Entity_P02

Working intermediate state:
State_L86

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-001 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?
Supplied intermediate: `State_W42`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `71aa2eb0bd655b3693a12c049304d5f15c06b16081153b809377786273ac19f8`; rendered SHA256: `5ab4c8195f937734f2d9cc5215cdb1ee3c23804cf3a80d076bd8ca2194038ea6`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D49 maps to Outcome_F93.
State_J94 maps to Outcome_I48.

Current entity:
Entity_J44

Working intermediate state:
State_W42

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-012 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?
Supplied intermediate: `State_O89`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `c38c04bf357bae632c3f78d12203dc91f663ccee3fbdcb88678d87bbead342a4`; rendered SHA256: `dfca1b4bf0b97ac04c09930b966071e9f9e76ab1c608c4e7b52bee92987e688d`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E16 maps to Outcome_A20.
State_M41 maps to Outcome_W11.

Current entity:
Entity_R10

Working intermediate state:
State_O89

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-011 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?
Supplied intermediate: `State_I31`
Expected: `Outcome_C69`; parsed: Cp; normalized: `Outcome_C69`; truncated: False
Prompt SHA256: `e9e3f0224ae5ce5e7d62201171d5c39aedd1ddad929870e7c1c67c5b9d0d81cf`; rendered SHA256: `58230d85965dfd4651bc7ad187fcc8e3e91c2eceeecf4a0b4cb8d4f77684b3fa`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J91 maps to Outcome_B21.
State_I31 maps to Outcome_C69.

Current entity:
Entity_L33

Working intermediate state:
State_I31

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_C69"
```

## v360-calibration-009 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?
Supplied intermediate: `State_J02`
Expected: `Outcome_S45`; parsed: C; normalized: `Outcome_S45`; truncated: False
Prompt SHA256: `f1f19162d82a4678761de7cc84efac0a210e8e42159c1817e2ea3881c7eb2078`; rendered SHA256: `d96f03a536180d1a48fda71cf44d64243a91b5c4eb504b59d8e3180daf11cc77`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J02 maps to Outcome_S45.
State_H06 maps to Outcome_D81.

Current entity:
Entity_E83

Working intermediate state:
State_J02

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_S45"
```

## v360-calibration-014 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?
Supplied intermediate: `State_F19`
Expected: `Outcome_B00`; parsed: C; normalized: `Outcome_B00`; truncated: False
Prompt SHA256: `9df1c9f6f7020d35a5aa615cbd8c6cd5d838fa806e030c2e0cd9b84e07938e0a`; rendered SHA256: `d911cf6f14a240c4971877dca90def5bd42fdbf9c8441848f8b97343e25e25d4`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_F19 maps to Outcome_B00.
State_L73 maps to Outcome_A74.

Current entity:
Entity_U55

Working intermediate state:
State_F19

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_B00"
```

## v360-calibration-003 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?
Supplied intermediate: `State_Z38`
Expected: `Outcome_P70`; parsed: Cp; normalized: `Outcome_P70`; truncated: False
Prompt SHA256: `7076d8c9c288cc643e03208c322cc50279f9bfba8b1dd16666e09a0a212100be`; rendered SHA256: `92e858601821f284d77315d29a94ecfc9cde8711ed598034a6ae2a2e53ca0591`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z43 maps to Outcome_L24.
State_Z38 maps to Outcome_P70.

Current entity:
Entity_F60

Working intermediate state:
State_Z38

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_P70"
```

## v360-calibration-018 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?
Supplied intermediate: `State_D36`
Expected: `Outcome_M04`; parsed: C; normalized: `Outcome_M04`; truncated: False
Prompt SHA256: `df7707596b95a458ff9aff03ce27a305a19c2428c35fa59db47ed18b30fc290a`; rendered SHA256: `918a5f85987ea2f9fdecf6fcd73618b0e097b422e8cae248144ddc7ee22776d9`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Q80 maps to Outcome_J28.
State_D36 maps to Outcome_M04.

Current entity:
Entity_P02

Working intermediate state:
State_D36

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M04"
```

## v360-calibration-010 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L13?
Supplied intermediate: `State_Y20`
Expected: `Outcome_V88`; parsed: C; normalized: `Outcome_V88`; truncated: False
Prompt SHA256: `b15244c19d9fdd035ef37ff4c7de20a56c4835a3cc1e8e06a2da4a1bbf6fc651`; rendered SHA256: `a7f76d36d1ff8aee08475a9bfb2972b05c1cd56ed5d8d411209f0dfeea5886d3`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y20 maps to Outcome_V88.
State_A36 maps to Outcome_X40.

Current entity:
Entity_L13

Working intermediate state:
State_Y20

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L13?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_V88"
```

## v360-calibration-018 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?
Supplied intermediate: `State_Q80`
Expected: `Outcome_J28`; parsed: Cp; normalized: `Outcome_J28`; truncated: False
Prompt SHA256: `aa82fa9fa643b5acf34c32502b444ab19251e94bf630b8086dfb9bb3ee84b463`; rendered SHA256: `c1af196112a4d55e200ce6bda7453c21a5909a75f5c52df9c2959223da7e59b7`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Q80 maps to Outcome_J28.
State_D36 maps to Outcome_M04.

Current entity:
Entity_P02

Working intermediate state:
State_Q80

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_J28"
```

## v360-calibration-003 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?
Supplied intermediate: `State_Z38`
Expected: `Outcome_L24`; parsed: C; normalized: `Outcome_L24`; truncated: False
Prompt SHA256: `a1829c61cc1398314351504b8a91ec1d49ad87d7b28c79b0e9176b30461eef64`; rendered SHA256: `e14a899a671fecdf5de26b87a59e3485becdd4abe29ffed2f76b0222bb5c8462`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z43 maps to Outcome_P70.
State_Z38 maps to Outcome_L24.

Current entity:
Entity_F60

Working intermediate state:
State_Z38

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_F60?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_L24"
```

## v360-calibration-016 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?
Supplied intermediate: `State_B20`
Expected: `Outcome_X89`; parsed: C; normalized: `Outcome_X89`; truncated: False
Prompt SHA256: `1f7cf7c9efcf95dadc6ad8a40a9fa2aaa8eec016be6010d09a210ad248d57211`; rendered SHA256: `cfc2bd0fc60793492939c6248f48e0563ab0ce22faaf7410d77ebace9d39ef5d`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D05 maps to Outcome_Q30.
State_B20 maps to Outcome_X89.

Current entity:
Entity_R01

Working intermediate state:
State_B20

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R01?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_X89"
```

## v360-calibration-017 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?
Supplied intermediate: `State_J32`
Expected: `Outcome_E53`; parsed: C; normalized: `Outcome_E53`; truncated: False
Prompt SHA256: `b32f12b376ec69110aa7d1c82adb1ea7e911498e1025ce9895b9a42206f99325`; rendered SHA256: `9a1f2d85ec5ffeff7b90c1c408a68c9f771a9046de461c86ec2341ad5148ed55`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J32 maps to Outcome_E53.
State_I11 maps to Outcome_H41.

Current entity:
Entity_K46

Working intermediate state:
State_J32

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_K46?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_E53"
```

## v360-calibration-018 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?
Supplied intermediate: `State_D36`
Expected: `Outcome_J28`; parsed: Cp; normalized: `Outcome_J28`; truncated: False
Prompt SHA256: `ef050698b2fe628d2210264790c61e0ba95e0cfe2c694cabc0f62f8f6721d81b`; rendered SHA256: `d3b9b1c470eaf4e2ba6e5ed0f2f646eeaf7be64e92ffeb735364086aceb45aaa`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Q80 maps to Outcome_M04.
State_D36 maps to Outcome_J28.

Current entity:
Entity_P02

Working intermediate state:
State_D36

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_J28"
```

## v360-calibration-007 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_E40 map to?
Supplied intermediate: `State_E40`
Expected: `Outcome_A64`; parsed: Cp; normalized: `Outcome_A64`; truncated: False
Prompt SHA256: `e592552553f1227efdaccaaa9d319ae17a475419ebec459e14e5c1a075c99184`; rendered SHA256: `d2335caec1f980e009ed81e2307fc37cc568054082a2c972e18c1fb295e44472`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E40 maps to Outcome_A64.
State_T18 maps to Outcome_R32.

Question:
According to the supplied mapping, what does State_E40 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A64"
```

## v360-calibration-011 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_I31 map to?
Supplied intermediate: `State_I31`
Expected: `Outcome_C69`; parsed: Cp; normalized: `Outcome_C69`; truncated: False
Prompt SHA256: `3c08c31547c8aab9c0b0189198ddd54ecf5eecac5a93605a4bea89d36387545b`; rendered SHA256: `799bc3f2081860d28536795766d8cae53ec7149dbdf1928d54bcb8b088ca5686`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J91 maps to Outcome_B21.
State_I31 maps to Outcome_C69.

Question:
According to the supplied mapping, what does State_I31 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_C69"
```

## v360-calibration-013 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_X07?
Supplied intermediate: `State_Z41`
Expected: `Outcome_D95`; parsed: C; normalized: `Outcome_D95`; truncated: False
Prompt SHA256: `4b21b2705b5a63345da71e398600233d0b43165423ae1af8cb46a0de0ea6c06e`; rendered SHA256: `59b2a2eb71d7e5db9760c96bdbe5ab381b2d5c69e5295b1d4e03f192a6f0018f`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_V34 maps to Outcome_L31.
State_Z41 maps to Outcome_D95.

Current entity:
Entity_X07

Working intermediate state:
State_Z41

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_X07?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_D95"
```

## v360-calibration-020 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?
Supplied intermediate: `State_D25`
Expected: `Outcome_G48`; parsed: Cp; normalized: `Outcome_G48`; truncated: False
Prompt SHA256: `6589af8fc09e0d0e24ad0d7fcba196e23abe47d254619b940125530949e5fa69`; rendered SHA256: `689077a4640970a3b68a1eab348102461e78e8b950bb478cf00e33e8663c22e4`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M13 maps to Outcome_K93.
State_D25 maps to Outcome_G48.

Current entity:
Entity_P81

Working intermediate state:
State_D25

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P81?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_G48"
```

## v360-calibration-015 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_X78 map to?
Supplied intermediate: `State_X78`
Expected: `Outcome_K40`; parsed: Cp; normalized: `Outcome_K40`; truncated: False
Prompt SHA256: `34e891321d22af809e4b881dec782feb4dcec0a1e755c31e8fe7f329da410f72`; rendered SHA256: `be9817996f0913b9978f56f05a514e8e229bc5889638f3611e8348295ecb886e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R43 maps to Outcome_T88.
State_X78 maps to Outcome_K40.

Question:
According to the supplied mapping, what does State_X78 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_K40"
```

## v360-calibration-013 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?
Supplied intermediate: `State_Z41`
Expected: `Outcome_D95`; parsed: C; normalized: `Outcome_D95`; truncated: False
Prompt SHA256: `1a0f19adc28c3a2413712a125cb802f6808f1858f60e46d178f9fb91c1cd03d7`; rendered SHA256: `650a6e1d8eb43cbaa4dc36737372d49101f837a1db0cb6fdbe3eabc3ee770efa`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_V34 maps to Outcome_L31.
State_Z41 maps to Outcome_D95.

Current entity:
Entity_A61

Working intermediate state:
State_Z41

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_D95"
```

## v360-calibration-006 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?
Supplied intermediate: `State_N95`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `65577fd8432c5c3cb3cc04fc6d45f74f317a999e40c3b976b044e82e2949a73b`; rendered SHA256: `93ea3d4524c173224159f1172c356947d250db36146bc0f0d9657285ed362dec`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y82 maps to Outcome_M73.
State_W27 maps to Outcome_A15.

Current entity:
Entity_V79

Working intermediate state:
State_N95

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_V79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-016 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_D05 map to?
Supplied intermediate: `State_D05`
Expected: `Outcome_Q30`; parsed: Cp; normalized: `Outcome_Q30`; truncated: False
Prompt SHA256: `8ec0029450ee7dc28f667f22940c352ae0fff1c21b78c6b3a102d9cb88edd2ba`; rendered SHA256: `8d984cf3fc9ecd20318da37ccdce9f29e9a10a5e6d1eebd285c2838bb001c6da`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D05 maps to Outcome_Q30.
State_B20 maps to Outcome_X89.

Question:
According to the supplied mapping, what does State_D05 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_Q30"
```

## v360-calibration-002 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?
Supplied intermediate: `State_C68`
Expected: `Outcome_E87`; parsed: C; normalized: `Outcome_E87`; truncated: False
Prompt SHA256: `acf8685e2a62dc132cb994a9b184c176605b7288131840253e658a576c47d9ac`; rendered SHA256: `a9a3360f80ed4beca0a7107ab479e9e71affbd7cf29c5047e8335308dc2ddc4e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_K13 maps to Outcome_N34.
State_C68 maps to Outcome_E87.

Current entity:
Entity_H61

Working intermediate state:
State_C68

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_H61?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_E87"
```

## v360-calibration-010 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?
Supplied intermediate: `State_Y20`
Expected: `Outcome_V88`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `4476c19e3aa99f1b9c97b1d0753e07e59de45cafc7b6ba282303e55379631ef5`; rendered SHA256: `6bdd6a1f745b241edd50f7bd8d23f34727284d018e4b40ddbd09f4ba78094834`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_A36 maps to Outcome_X40.
State_Y20 maps to Outcome_V88.

Current entity:
Entity_E59

Working intermediate state:
State_Y20

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-007 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?
Supplied intermediate: `State_E40`
Expected: `Outcome_A64`; parsed: Cp; normalized: `Outcome_A64`; truncated: False
Prompt SHA256: `15dea87ed4d55f1bdb6b22647f4cd3c5f62496c8d2a25fa43e1a89e9280a8b5f`; rendered SHA256: `8e9c280ec15b481feb2ffae2dc6c336af7cfef005d3f604df33515e736cc4a88`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E40 maps to Outcome_A64.
State_T18 maps to Outcome_R32.

Current entity:
Entity_N53

Working intermediate state:
State_E40

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_A64"
```

## v360-calibration-004 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?
Supplied intermediate: `State_O94`
Expected: `Outcome_N09`; parsed: C; normalized: `Outcome_N09`; truncated: False
Prompt SHA256: `c7e7ac0571595ba9ed1bf291974ebdac5ff41ddcb6f65d4c99e2cd63dd7bf1a1`; rendered SHA256: `f3014ef5da52e16266910201441cc241f66b935953586326d6a94e8c76c196dd`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_M06 maps to Outcome_I15.
State_O94 maps to Outcome_N09.

Current entity:
Entity_G19

Working intermediate state:
State_O94

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G19?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_N09"
```

## v360-calibration-018 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?
Supplied intermediate: `State_D36`
Expected: `Outcome_M04`; parsed: C; normalized: `Outcome_M04`; truncated: False
Prompt SHA256: `8107773160271e5ee63a426fb8fa12ed09b51d6f139077254b3e5f330306c090`; rendered SHA256: `04c372a98508635e82f648be1fac803a11d9bc55005a9e6ce0d4fbc854a87fd7`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D36 maps to Outcome_M04.
State_Q80 maps to Outcome_J28.

Current entity:
Entity_P02

Working intermediate state:
State_D36

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_P02?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M04"
```

## v360-calibration-019 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?
Supplied intermediate: `State_T91`
Expected: `Outcome_W79`; parsed: Cp; normalized: `Outcome_W79`; truncated: False
Prompt SHA256: `1231c9d76cba613f1843189d3bd1634e2584a2ffa2ffd7151113cbf09ae9b8df`; rendered SHA256: `45688de725108100b3c08f8236508ec580360b7de84e0942b1cd1c878d0c3995`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_T91 maps to Outcome_W79.
State_M70 maps to Outcome_V51.

Current entity:
Entity_A34

Working intermediate state:
State_T91

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A34?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_W79"
```

## v360-calibration-010 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?
Supplied intermediate: `State_A36`
Expected: `Outcome_X40`; parsed: Cp; normalized: `Outcome_X40`; truncated: False
Prompt SHA256: `dffd5b798eff73aee412a674b720d7f1f7c3228f4ce81575f4a9540f97b4c04e`; rendered SHA256: `1fdcbb43fa74cad4bafc466f95135a086b00f14eefa1127ea48963e3856357c9`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Y20 maps to Outcome_V88.
State_A36 maps to Outcome_X40.

Current entity:
Entity_E59

Working intermediate state:
State_A36

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E59?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_X40"
```

## v360-calibration-013 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_V34 map to?
Supplied intermediate: `State_V34`
Expected: `Outcome_L31`; parsed: Cp; normalized: `Outcome_L31`; truncated: False
Prompt SHA256: `fc96fec03ef82a024d9b7ca8718aeaff571a3345776397386c7b7c0275eee9f1`; rendered SHA256: `c23d56dc095e2078ebaf799cd021d54a0b9bb6d1c3a519f718ab3cb2652c6fe6`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_V34 maps to Outcome_L31.
State_Z41 maps to Outcome_D95.

Question:
According to the supplied mapping, what does State_V34 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_L31"
```

## v360-calibration-012 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?
Supplied intermediate: `State_M41`
Expected: `Outcome_A20`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `af0ffcce12c4495280229d1593290a173efcebebbc4ea2f8ac8094762fc45b5d`; rendered SHA256: `0f7e0a2afe4b3390aa302b9cb3c082e38baf979c1e3cca3266bb4ccf173b29ee`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E16 maps to Outcome_W11.
State_M41 maps to Outcome_A20.

Current entity:
Entity_R10

Working intermediate state:
State_M41

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_R10?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-008 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?
Supplied intermediate: `State_H25`
Expected: `Outcome_C61`; parsed: C; normalized: `Outcome_C61`; truncated: False
Prompt SHA256: `ef4e12aae315abad32d91022fbad4f7316e2bb284a238fe541d2dbff760f8e65`; rendered SHA256: `b0262ba393979717d0f612144ed31d8b2c984cd42c45c9c910f548a351916a63`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_P32 maps to Outcome_H92.
State_H25 maps to Outcome_C61.

Current entity:
Entity_E79

Working intermediate state:
State_H25

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E79?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_C61"
```

## v360-calibration-007 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G54?
Supplied intermediate: `State_T18`
Expected: `Outcome_R32`; parsed: C; normalized: `Outcome_R32`; truncated: False
Prompt SHA256: `6d21cc17e916cf20576effce45ea75aaa5a428058fb834c14e87a3cbc870b804`; rendered SHA256: `ffcdb6774789ca1f0510dabcc2d4cb026c2932695bc52ad82948bbf382071ec7`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E40 maps to Outcome_A64.
State_T18 maps to Outcome_R32.

Current entity:
Entity_G54

Working intermediate state:
State_T18

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_G54?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_R32"
```

## v360-calibration-016 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_B20 map to?
Supplied intermediate: `State_B20`
Expected: `Outcome_X89`; parsed: C; normalized: `Outcome_X89`; truncated: False
Prompt SHA256: `70c9a35c0fc21851b32f17c4956a3dd3c9d42c6bb53acce930a6e8e2593f08a7`; rendered SHA256: `afe1a7e479f5555cb102ff9c6778813744375480c4c57be6bf0bcb9888b2964d`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D05 maps to Outcome_Q30.
State_B20 maps to Outcome_X89.

Question:
According to the supplied mapping, what does State_B20 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_X89"
```

## v360-calibration-014 / UNMAPPED

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?
Supplied intermediate: `State_N21`
Expected: `UNKNOWN`; parsed: UNKNOWN; normalized: `UNKNOWN`; truncated: False
Prompt SHA256: `0c45fdad0641e1d17a7ccd36504f466b8c2b5926862d6ebdd35335e805a5feab`; rendered SHA256: `3da31d9bfb7ba2740a0b87a7761b54514b78fd389b57469c4dc20ec92c392e30`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_F19 maps to Outcome_B00.
State_L73 maps to Outcome_A74.

Current entity:
Entity_U55

Working intermediate state:
State_N21

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_U55?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"UNKNOWN"
```

## v360-calibration-018 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_Q80 map to?
Supplied intermediate: `State_Q80`
Expected: `Outcome_J28`; parsed: Cp; normalized: `Outcome_J28`; truncated: False
Prompt SHA256: `bc17700e411f8fd82b1180b88bd65f984bee12e4cf5cb056b3e1214af8e9a0fd`; rendered SHA256: `892a79a612a4f22dd8b042d7877723b91121f066a82c3eb37b576630106d3919`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Q80 maps to Outcome_J28.
State_D36 maps to Outcome_M04.

Question:
According to the supplied mapping, what does State_Q80 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_J28"
```

## v360-calibration-003 / LOOKUP_WRONG

Subquestion: According to the supplied mapping, what does State_Z43 map to?
Supplied intermediate: `State_Z43`
Expected: `Outcome_P70`; parsed: Cp; normalized: `Outcome_P70`; truncated: False
Prompt SHA256: `d9f56ead2cb53c62786d3339013bf5353626242f8eebe069f35dad4de20337d3`; rendered SHA256: `83eb2dedbf6c1fc93541affcd2fb5b4f77306bf4fd47e082fceea6db7e5970a0`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z43 maps to Outcome_P70.
State_Z38 maps to Outcome_L24.

Question:
According to the supplied mapping, what does State_Z43 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_P70"
```

## v360-calibration-011 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?
Supplied intermediate: `State_J91`
Expected: `Outcome_C69`; parsed: Cp; normalized: `Outcome_C69`; truncated: False
Prompt SHA256: `85909a039b4a267ffec0b8f6c8334b0ba9c7f6bf9f33cd0250e9d04cf00e3863`; rendered SHA256: `24a27f5a416b376e7cfd2ce9c006c811e171426c5ef140d59abdc0dac4928089`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_J91 maps to Outcome_C69.
State_I31 maps to Outcome_B21.

Current entity:
Entity_L33

Working intermediate state:
State_J91

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_L33?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_C69"
```

## v360-calibration-015 / SWAP

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?
Supplied intermediate: `State_R43`
Expected: `Outcome_K40`; parsed: Cp; normalized: `Outcome_K40`; truncated: False
Prompt SHA256: `a8a7bc1c2800f7811b8dccf10dcca2d3b577a80f84df96a46646a179ef9aac92`; rendered SHA256: `e20ec66ef611519e2a074a9c9db31b40edb1208dc949c6f9da72f83ceafc26ca`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R43 maps to Outcome_K40.
State_X78 maps to Outcome_T88.

Current entity:
Entity_I23

Working intermediate state:
State_R43

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_I23?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_K40"
```

## v360-calibration-009 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?
Supplied intermediate: `State_J02`
Expected: `Outcome_S45`; parsed: C; normalized: `Outcome_S45`; truncated: False
Prompt SHA256: `63d0a5d4779283b77d9e3364b06f9dbef0cf2ced853bffd70d9e5ee90ccb7512`; rendered SHA256: `d2e99ae766728bc710e53a6520b0b54542440d599b0ac62729f74fbd901b53c9`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_H06 maps to Outcome_D81.
State_J02 maps to Outcome_S45.

Current entity:
Entity_E83

Working intermediate state:
State_J02

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_E83?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_S45"
```

## v360-calibration-001 / W0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?
Supplied intermediate: `State_J94`
Expected: `Outcome_I48`; parsed: Cp; normalized: `Outcome_I48`; truncated: False
Prompt SHA256: `b1c7b310fddb155c7ef8455a297f8d8dc3e21efdd2f832b7ce9926176da7f564`; rendered SHA256: `8bdb66de290057d26ca69dc572e31e19202d06f18aca51ad8fee617c2f085641`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_D49 maps to Outcome_F93.
State_J94 maps to Outcome_I48.

Current entity:
Entity_J44

Working intermediate state:
State_J94

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_J44?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_I48"
```

## v360-calibration-012 / ENTITY_LABEL

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_X55?
Supplied intermediate: `State_M41`
Expected: `Outcome_W11`; parsed: C; normalized: `Outcome_W11`; truncated: False
Prompt SHA256: `d88294246321621df29604d714a9c76d32a86e3de5c73ef502405b25a257a140`; rendered SHA256: `7cab24452a6f253551746aa1cd15c2b22fc8b9ab611c3b89a3be6822c2d5f6b8`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E16 maps to Outcome_A20.
State_M41 maps to Outcome_W11.

Current entity:
Entity_X55

Working intermediate state:
State_M41

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_X55?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_W11"
```

## v360-calibration-005 / REVERSE

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?
Supplied intermediate: `State_R64`
Expected: `Outcome_M36`; parsed: C; normalized: `Outcome_M36`; truncated: False
Prompt SHA256: `03ad27e6dc50ccfb1f06dad3600a853419d972af86e037efb59573ee7e2c3173`; rendered SHA256: `a38cd9d5346dbf7aefeed1f7976d696982a26576cea6455f57771d8fcd43b73e`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_R64 maps to Outcome_M36.
State_R00 maps to Outcome_Z51.

Current entity:
Entity_D18

Working intermediate state:
State_R64

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_D18?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_M36"
```

## v360-calibration-017 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_J32 map to?
Supplied intermediate: `State_J32`
Expected: `Outcome_E53`; parsed: C; normalized: `Outcome_E53`; truncated: False
Prompt SHA256: `c6615f8744478e58c7719093e039683bd1d2fac6004b10e3ac8719c0447e1643`; rendered SHA256: `6c285c92f4872e199113cba06bfd1f39958274280c9ca7f44f0399524bd2588d`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_I11 maps to Outcome_H41.
State_J32 maps to Outcome_E53.

Question:
According to the supplied mapping, what does State_J32 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_E53"
```

## v360-calibration-003 / LOOKUP_GOLD

Subquestion: According to the supplied mapping, what does State_Z38 map to?
Supplied intermediate: `State_Z38`
Expected: `Outcome_L24`; parsed: C; normalized: `Outcome_L24`; truncated: False
Prompt SHA256: `7ae76f1fb7578d913551425b5999d8f1fed81d880ac7338fa1b418c6f399c8b9`; rendered SHA256: `e7f0e0ff16d2e080ffbdea7b01c001c039139f35e9895aaeca12937ee8c5be67`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_Z43 maps to Outcome_P70.
State_Z38 maps to Outcome_L24.

Question:
According to the supplied mapping, what does State_Z38 map to?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_L24"
```

## v360-calibration-007 / C0

Subquestion: Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?
Supplied intermediate: `State_T18`
Expected: `Outcome_R32`; parsed: C; normalized: `Outcome_R32`; truncated: False
Prompt SHA256: `32706f7d4404bbf2cdafc1f7b56b5d03b8618d8b55f1e17972c358449de386d3`; rendered SHA256: `79ef63868dbc360517e2f64a24400793a7f074dd820723a83203ea27ebeb6c6c`

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_E40 maps to Outcome_A64.
State_T18 maps to Outcome_R32.

Current entity:
Entity_N53

Working intermediate state:
State_T18

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_N53?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Raw output (JSON string):
```json
"Outcome_R32"
```

## Main

Not run: calibration validity gate failed.
