# Case studies

Oracle replacements are supplied gold facts; semantic validity must be reviewed.


## Who is Malcolm Iv Of Scotland's father?

Gold chain: The mother of Malcolm IV of Scotland is Ada de Warenne. The spouse of Ada de Warenne is Henry of Scotland.

| Baseline | Injected error | Oracle correction |

|---|---|---|

| Step 1: Malcolm Iv of Scotland's father is Sir Malcolm Iv of Scotland.<br>Step 1: Malcolm Iv of Scotland's father is Sir Malcolm Iv of Scotland.  <br>Step 2: Malcolm Iv of Scotland was born in 1531.  <br>Final answer: Sir Malcolm Iv of Scotland is the father of Malcolm Iv of Scotland. | Step 1: The mother of Malcolm IV of Scotland is Ermesinda of Bigorre.<br>Step 2: The father of Malcolm IV of Scotland is King Malcolm of Scotland.  <br>Final answer: King Malcolm of Scotland. | Step 1: The mother of Malcolm IV of Scotland is Ada de Warenne.<br>Step 2: The father of Malcolm IV of Scotland is King John of England.  <br>Final answer: King John of England. |


## Where did Prince David Of Kakheti's father die?

Gold chain: The father of Prince David of Kakheti is Teimuraz I of Kakheti. The place of death of Teimuraz I of Kakheti is Astarabad.

| Baseline | Injected error | Oracle correction |

|---|---|---|

| Step 1: Prince David Of Kakheti's father was born in 1961.<br>Step 1: Prince David Of Kakheti's father was born in 1961.  <br>Step 2: He died in 2004.  <br><br>Final answer: Prince David Of Kakheti's father died in 2004. | Step 1: The father of Prince David of Kakheti is Frederick III of Nuremberg.<br>Step 2: Frederick III of Nuremberg died in 1547.  <br>Final answer: Frederick III of Nuremberg died in 1547. | Step 1: The father of Prince David of Kakheti is Teimuraz I of Kakheti.<br>Step 2: Teimuraz I of Kakheti died in 1991.  <br>Final answer: Teimuraz I of Kakheti died in 1991. |


## Who is the paternal grandfather of Walter Butler Of Polestown?

Gold chain: The father of Walter Butler of Polestown is Edmund MacRichard Butler. The father of Edmund MacRichard Butler is Sir Richard Butler of Polestown.

| Baseline | Injected error | Oracle correction |

|---|---|---|

| Step 1: <first fact> Walter Butler Of Polestown was born in 1858, and his paternal grandfather is a prominent figure in the community.<br>Step 1: <first fact> Walter Butler Of Polestown was born in 1858, and his paternal grandfather is a prominent figure in the community.  <br>Step 2: <dependent fact> Walter Butler Of Polestown’s paternal grandfather was John D. Rockefeller, a leading industrialist and philanthropist.  <br>Final answer: <short answer> John D. Rockefeller is the paternal grandfather of Walter Butler Of Polestown. | Step 1: The father of Walter Butler of Polestown is Robert Deane.<br>Step 2: Walter Butler of Polestown's paternal grandfather is Robert Deane.  <br>Final answer: Robert Deane. | Step 1: The father of Walter Butler of Polestown is Edmund MacRichard Butler.<br>Step 2: The paternal grandfather of Walter Butler of Polestown is Edmund MacRichard Butler.  <br>Final answer: Edmund MacRichard Butler |