# module: Margin

Various margin properties:

* margin top, right, bottom and left
* margin (shorthand for all margins)
* margin horizontal and vertical (x & y)








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.m` |`margin`|
| `.mt` |`margin-top`|
| `.mr` |`margin-right`|
| `.mb` |`margin-bottom`|
| `.ml` |`margin-left`|
| `.mx` |`margin-left`, |`margin-right`|
| `.my` |`margin-top`, |`margin-bottom`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`0` | `0`
`1` | `0.0625rem`
`2` | `0.125rem`
`3` | `0.25rem`
`4` | `0.5rem`
`5` | `1rem`
`6` | `2rem`
`7` | `4rem`
`8` | `8rem`
`9` | `999rem`
`-1` | `0.0625rem`
`-2` | `-0.125rem`
`-3` | `-0.25rem`
`-4` | `-0.5rem`
`-5` | `-1rem`
`-6` | `-2rem`
`-7` | `-4rem`
`-8` | `-8rem`
`-9` | `-999rem`
`a` | `auto`




## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|






## CSS rules
```css

.m0 { margin: 0; }
.m1 { margin: 0.0625rem; }
.m2 { margin: 0.125rem; }
.m3 { margin: 0.25rem; }
.m4 { margin: 0.5rem; }
.m5 { margin: 1rem; }
.m6 { margin: 2rem; }
.m7 { margin: 4rem; }
.m8 { margin: 8rem; }
.m9 { margin: 999rem; }
.m-1 { margin: 0.0625rem; }
.m-2 { margin: -0.125rem; }
.m-3 { margin: -0.25rem; }
.m-4 { margin: -0.5rem; }
.m-5 { margin: -1rem; }
.m-6 { margin: -2rem; }
.m-7 { margin: -4rem; }
.m-8 { margin: -8rem; }
.m-9 { margin: -999rem; }
.m-a { margin: auto; }
.mt0 { margin-top: 0; }
.mt1 { margin-top: 0.0625rem; }
.mt2 { margin-top: 0.125rem; }
.mt3 { margin-top: 0.25rem; }
.mt4 { margin-top: 0.5rem; }
.mt5 { margin-top: 1rem; }
.mt6 { margin-top: 2rem; }
.mt7 { margin-top: 4rem; }
.mt8 { margin-top: 8rem; }
.mt9 { margin-top: 999rem; }
.mt-1 { margin-top: 0.0625rem; }
.mt-2 { margin-top: -0.125rem; }
.mt-3 { margin-top: -0.25rem; }
.mt-4 { margin-top: -0.5rem; }
.mt-5 { margin-top: -1rem; }
.mt-6 { margin-top: -2rem; }
.mt-7 { margin-top: -4rem; }
.mt-8 { margin-top: -8rem; }
.mt-9 { margin-top: -999rem; }
.mt-a { margin-top: auto; }
.mr0 { margin-right: 0; }
.mr1 { margin-right: 0.0625rem; }
.mr2 { margin-right: 0.125rem; }
.mr3 { margin-right: 0.25rem; }
.mr4 { margin-right: 0.5rem; }
.mr5 { margin-right: 1rem; }
.mr6 { margin-right: 2rem; }
.mr7 { margin-right: 4rem; }
.mr8 { margin-right: 8rem; }
.mr9 { margin-right: 999rem; }
.mr-1 { margin-right: 0.0625rem; }
.mr-2 { margin-right: -0.125rem; }
.mr-3 { margin-right: -0.25rem; }
.mr-4 { margin-right: -0.5rem; }
.mr-5 { margin-right: -1rem; }
.mr-6 { margin-right: -2rem; }
.mr-7 { margin-right: -4rem; }
.mr-8 { margin-right: -8rem; }
.mr-9 { margin-right: -999rem; }
.mr-a { margin-right: auto; }
.mb0 { margin-bottom: 0; }
.mb1 { margin-bottom: 0.0625rem; }
.mb2 { margin-bottom: 0.125rem; }
.mb3 { margin-bottom: 0.25rem; }
.mb4 { margin-bottom: 0.5rem; }
.mb5 { margin-bottom: 1rem; }
.mb6 { margin-bottom: 2rem; }
.mb7 { margin-bottom: 4rem; }
.mb8 { margin-bottom: 8rem; }
.mb9 { margin-bottom: 999rem; }
.mb-1 { margin-bottom: 0.0625rem; }
.mb-2 { margin-bottom: -0.125rem; }
.mb-3 { margin-bottom: -0.25rem; }
.mb-4 { margin-bottom: -0.5rem; }
.mb-5 { margin-bottom: -1rem; }
.mb-6 { margin-bottom: -2rem; }
.mb-7 { margin-bottom: -4rem; }
.mb-8 { margin-bottom: -8rem; }
.mb-9 { margin-bottom: -999rem; }
.mb-a { margin-bottom: auto; }
.ml0 { margin-left: 0; }
.ml1 { margin-left: 0.0625rem; }
.ml2 { margin-left: 0.125rem; }
.ml3 { margin-left: 0.25rem; }
.ml4 { margin-left: 0.5rem; }
.ml5 { margin-left: 1rem; }
.ml6 { margin-left: 2rem; }
.ml7 { margin-left: 4rem; }
.ml8 { margin-left: 8rem; }
.ml9 { margin-left: 999rem; }
.ml-1 { margin-left: 0.0625rem; }
.ml-2 { margin-left: -0.125rem; }
.ml-3 { margin-left: -0.25rem; }
.ml-4 { margin-left: -0.5rem; }
.ml-5 { margin-left: -1rem; }
.ml-6 { margin-left: -2rem; }
.ml-7 { margin-left: -4rem; }
.ml-8 { margin-left: -8rem; }
.ml-9 { margin-left: -999rem; }
.ml-a { margin-left: auto; }
.mx0 { margin-left: 0; margin-right: 0; }
.mx1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.mx2 { margin-left: 0.125rem; margin-right: 0.125rem; }
.mx3 { margin-left: 0.25rem; margin-right: 0.25rem; }
.mx4 { margin-left: 0.5rem; margin-right: 0.5rem; }
.mx5 { margin-left: 1rem; margin-right: 1rem; }
.mx6 { margin-left: 2rem; margin-right: 2rem; }
.mx7 { margin-left: 4rem; margin-right: 4rem; }
.mx8 { margin-left: 8rem; margin-right: 8rem; }
.mx9 { margin-left: 999rem; margin-right: 999rem; }
.mx-1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.mx-2 { margin-left: -0.125rem; margin-right: -0.125rem; }
.mx-3 { margin-left: -0.25rem; margin-right: -0.25rem; }
.mx-4 { margin-left: -0.5rem; margin-right: -0.5rem; }
.mx-5 { margin-left: -1rem; margin-right: -1rem; }
.mx-6 { margin-left: -2rem; margin-right: -2rem; }
.mx-7 { margin-left: -4rem; margin-right: -4rem; }
.mx-8 { margin-left: -8rem; margin-right: -8rem; }
.mx-9 { margin-left: -999rem; margin-right: -999rem; }
.mx-a { margin-left: auto; margin-right: auto; }
.my0 { margin-top: 0; margin-bottom: 0; }
.my1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.my2 { margin-top: 0.125rem; margin-bottom: 0.125rem; }
.my3 { margin-top: 0.25rem; margin-bottom: 0.25rem; }
.my4 { margin-top: 0.5rem; margin-bottom: 0.5rem; }
.my5 { margin-top: 1rem; margin-bottom: 1rem; }
.my6 { margin-top: 2rem; margin-bottom: 2rem; }
.my7 { margin-top: 4rem; margin-bottom: 4rem; }
.my8 { margin-top: 8rem; margin-bottom: 8rem; }
.my9 { margin-top: 999rem; margin-bottom: 999rem; }
.my-1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.my-2 { margin-top: -0.125rem; margin-bottom: -0.125rem; }
.my-3 { margin-top: -0.25rem; margin-bottom: -0.25rem; }
.my-4 { margin-top: -0.5rem; margin-bottom: -0.5rem; }
.my-5 { margin-top: -1rem; margin-bottom: -1rem; }
.my-6 { margin-top: -2rem; margin-bottom: -2rem; }
.my-7 { margin-top: -4rem; margin-bottom: -4rem; }
.my-8 { margin-top: -8rem; margin-bottom: -8rem; }
.my-9 { margin-top: -999rem; margin-bottom: -999rem; }
.my-a { margin-top: auto; margin-bottom: auto; }


@media (min-width: 36em) {
.s_m0 { margin: 0; }
.s_m1 { margin: 0.0625rem; }
.s_m2 { margin: 0.125rem; }
.s_m3 { margin: 0.25rem; }
.s_m4 { margin: 0.5rem; }
.s_m5 { margin: 1rem; }
.s_m6 { margin: 2rem; }
.s_m7 { margin: 4rem; }
.s_m8 { margin: 8rem; }
.s_m9 { margin: 999rem; }
.s_m-1 { margin: 0.0625rem; }
.s_m-2 { margin: -0.125rem; }
.s_m-3 { margin: -0.25rem; }
.s_m-4 { margin: -0.5rem; }
.s_m-5 { margin: -1rem; }
.s_m-6 { margin: -2rem; }
.s_m-7 { margin: -4rem; }
.s_m-8 { margin: -8rem; }
.s_m-9 { margin: -999rem; }
.s_m-a { margin: auto; }
.s_mt0 { margin-top: 0; }
.s_mt1 { margin-top: 0.0625rem; }
.s_mt2 { margin-top: 0.125rem; }
.s_mt3 { margin-top: 0.25rem; }
.s_mt4 { margin-top: 0.5rem; }
.s_mt5 { margin-top: 1rem; }
.s_mt6 { margin-top: 2rem; }
.s_mt7 { margin-top: 4rem; }
.s_mt8 { margin-top: 8rem; }
.s_mt9 { margin-top: 999rem; }
.s_mt-1 { margin-top: 0.0625rem; }
.s_mt-2 { margin-top: -0.125rem; }
.s_mt-3 { margin-top: -0.25rem; }
.s_mt-4 { margin-top: -0.5rem; }
.s_mt-5 { margin-top: -1rem; }
.s_mt-6 { margin-top: -2rem; }
.s_mt-7 { margin-top: -4rem; }
.s_mt-8 { margin-top: -8rem; }
.s_mt-9 { margin-top: -999rem; }
.s_mt-a { margin-top: auto; }
.s_mr0 { margin-right: 0; }
.s_mr1 { margin-right: 0.0625rem; }
.s_mr2 { margin-right: 0.125rem; }
.s_mr3 { margin-right: 0.25rem; }
.s_mr4 { margin-right: 0.5rem; }
.s_mr5 { margin-right: 1rem; }
.s_mr6 { margin-right: 2rem; }
.s_mr7 { margin-right: 4rem; }
.s_mr8 { margin-right: 8rem; }
.s_mr9 { margin-right: 999rem; }
.s_mr-1 { margin-right: 0.0625rem; }
.s_mr-2 { margin-right: -0.125rem; }
.s_mr-3 { margin-right: -0.25rem; }
.s_mr-4 { margin-right: -0.5rem; }
.s_mr-5 { margin-right: -1rem; }
.s_mr-6 { margin-right: -2rem; }
.s_mr-7 { margin-right: -4rem; }
.s_mr-8 { margin-right: -8rem; }
.s_mr-9 { margin-right: -999rem; }
.s_mr-a { margin-right: auto; }
.s_mb0 { margin-bottom: 0; }
.s_mb1 { margin-bottom: 0.0625rem; }
.s_mb2 { margin-bottom: 0.125rem; }
.s_mb3 { margin-bottom: 0.25rem; }
.s_mb4 { margin-bottom: 0.5rem; }
.s_mb5 { margin-bottom: 1rem; }
.s_mb6 { margin-bottom: 2rem; }
.s_mb7 { margin-bottom: 4rem; }
.s_mb8 { margin-bottom: 8rem; }
.s_mb9 { margin-bottom: 999rem; }
.s_mb-1 { margin-bottom: 0.0625rem; }
.s_mb-2 { margin-bottom: -0.125rem; }
.s_mb-3 { margin-bottom: -0.25rem; }
.s_mb-4 { margin-bottom: -0.5rem; }
.s_mb-5 { margin-bottom: -1rem; }
.s_mb-6 { margin-bottom: -2rem; }
.s_mb-7 { margin-bottom: -4rem; }
.s_mb-8 { margin-bottom: -8rem; }
.s_mb-9 { margin-bottom: -999rem; }
.s_mb-a { margin-bottom: auto; }
.s_ml0 { margin-left: 0; }
.s_ml1 { margin-left: 0.0625rem; }
.s_ml2 { margin-left: 0.125rem; }
.s_ml3 { margin-left: 0.25rem; }
.s_ml4 { margin-left: 0.5rem; }
.s_ml5 { margin-left: 1rem; }
.s_ml6 { margin-left: 2rem; }
.s_ml7 { margin-left: 4rem; }
.s_ml8 { margin-left: 8rem; }
.s_ml9 { margin-left: 999rem; }
.s_ml-1 { margin-left: 0.0625rem; }
.s_ml-2 { margin-left: -0.125rem; }
.s_ml-3 { margin-left: -0.25rem; }
.s_ml-4 { margin-left: -0.5rem; }
.s_ml-5 { margin-left: -1rem; }
.s_ml-6 { margin-left: -2rem; }
.s_ml-7 { margin-left: -4rem; }
.s_ml-8 { margin-left: -8rem; }
.s_ml-9 { margin-left: -999rem; }
.s_ml-a { margin-left: auto; }
.s_mx0 { margin-left: 0; margin-right: 0; }
.s_mx1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.s_mx2 { margin-left: 0.125rem; margin-right: 0.125rem; }
.s_mx3 { margin-left: 0.25rem; margin-right: 0.25rem; }
.s_mx4 { margin-left: 0.5rem; margin-right: 0.5rem; }
.s_mx5 { margin-left: 1rem; margin-right: 1rem; }
.s_mx6 { margin-left: 2rem; margin-right: 2rem; }
.s_mx7 { margin-left: 4rem; margin-right: 4rem; }
.s_mx8 { margin-left: 8rem; margin-right: 8rem; }
.s_mx9 { margin-left: 999rem; margin-right: 999rem; }
.s_mx-1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.s_mx-2 { margin-left: -0.125rem; margin-right: -0.125rem; }
.s_mx-3 { margin-left: -0.25rem; margin-right: -0.25rem; }
.s_mx-4 { margin-left: -0.5rem; margin-right: -0.5rem; }
.s_mx-5 { margin-left: -1rem; margin-right: -1rem; }
.s_mx-6 { margin-left: -2rem; margin-right: -2rem; }
.s_mx-7 { margin-left: -4rem; margin-right: -4rem; }
.s_mx-8 { margin-left: -8rem; margin-right: -8rem; }
.s_mx-9 { margin-left: -999rem; margin-right: -999rem; }
.s_mx-a { margin-left: auto; margin-right: auto; }
.s_my0 { margin-top: 0; margin-bottom: 0; }
.s_my1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.s_my2 { margin-top: 0.125rem; margin-bottom: 0.125rem; }
.s_my3 { margin-top: 0.25rem; margin-bottom: 0.25rem; }
.s_my4 { margin-top: 0.5rem; margin-bottom: 0.5rem; }
.s_my5 { margin-top: 1rem; margin-bottom: 1rem; }
.s_my6 { margin-top: 2rem; margin-bottom: 2rem; }
.s_my7 { margin-top: 4rem; margin-bottom: 4rem; }
.s_my8 { margin-top: 8rem; margin-bottom: 8rem; }
.s_my9 { margin-top: 999rem; margin-bottom: 999rem; }
.s_my-1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.s_my-2 { margin-top: -0.125rem; margin-bottom: -0.125rem; }
.s_my-3 { margin-top: -0.25rem; margin-bottom: -0.25rem; }
.s_my-4 { margin-top: -0.5rem; margin-bottom: -0.5rem; }
.s_my-5 { margin-top: -1rem; margin-bottom: -1rem; }
.s_my-6 { margin-top: -2rem; margin-bottom: -2rem; }
.s_my-7 { margin-top: -4rem; margin-bottom: -4rem; }
.s_my-8 { margin-top: -8rem; margin-bottom: -8rem; }
.s_my-9 { margin-top: -999rem; margin-bottom: -999rem; }
.s_my-a { margin-top: auto; margin-bottom: auto; }
}


@media (min-width: 48em) {
.m_m0 { margin: 0; }
.m_m1 { margin: 0.0625rem; }
.m_m2 { margin: 0.125rem; }
.m_m3 { margin: 0.25rem; }
.m_m4 { margin: 0.5rem; }
.m_m5 { margin: 1rem; }
.m_m6 { margin: 2rem; }
.m_m7 { margin: 4rem; }
.m_m8 { margin: 8rem; }
.m_m9 { margin: 999rem; }
.m_m-1 { margin: 0.0625rem; }
.m_m-2 { margin: -0.125rem; }
.m_m-3 { margin: -0.25rem; }
.m_m-4 { margin: -0.5rem; }
.m_m-5 { margin: -1rem; }
.m_m-6 { margin: -2rem; }
.m_m-7 { margin: -4rem; }
.m_m-8 { margin: -8rem; }
.m_m-9 { margin: -999rem; }
.m_m-a { margin: auto; }
.m_mt0 { margin-top: 0; }
.m_mt1 { margin-top: 0.0625rem; }
.m_mt2 { margin-top: 0.125rem; }
.m_mt3 { margin-top: 0.25rem; }
.m_mt4 { margin-top: 0.5rem; }
.m_mt5 { margin-top: 1rem; }
.m_mt6 { margin-top: 2rem; }
.m_mt7 { margin-top: 4rem; }
.m_mt8 { margin-top: 8rem; }
.m_mt9 { margin-top: 999rem; }
.m_mt-1 { margin-top: 0.0625rem; }
.m_mt-2 { margin-top: -0.125rem; }
.m_mt-3 { margin-top: -0.25rem; }
.m_mt-4 { margin-top: -0.5rem; }
.m_mt-5 { margin-top: -1rem; }
.m_mt-6 { margin-top: -2rem; }
.m_mt-7 { margin-top: -4rem; }
.m_mt-8 { margin-top: -8rem; }
.m_mt-9 { margin-top: -999rem; }
.m_mt-a { margin-top: auto; }
.m_mr0 { margin-right: 0; }
.m_mr1 { margin-right: 0.0625rem; }
.m_mr2 { margin-right: 0.125rem; }
.m_mr3 { margin-right: 0.25rem; }
.m_mr4 { margin-right: 0.5rem; }
.m_mr5 { margin-right: 1rem; }
.m_mr6 { margin-right: 2rem; }
.m_mr7 { margin-right: 4rem; }
.m_mr8 { margin-right: 8rem; }
.m_mr9 { margin-right: 999rem; }
.m_mr-1 { margin-right: 0.0625rem; }
.m_mr-2 { margin-right: -0.125rem; }
.m_mr-3 { margin-right: -0.25rem; }
.m_mr-4 { margin-right: -0.5rem; }
.m_mr-5 { margin-right: -1rem; }
.m_mr-6 { margin-right: -2rem; }
.m_mr-7 { margin-right: -4rem; }
.m_mr-8 { margin-right: -8rem; }
.m_mr-9 { margin-right: -999rem; }
.m_mr-a { margin-right: auto; }
.m_mb0 { margin-bottom: 0; }
.m_mb1 { margin-bottom: 0.0625rem; }
.m_mb2 { margin-bottom: 0.125rem; }
.m_mb3 { margin-bottom: 0.25rem; }
.m_mb4 { margin-bottom: 0.5rem; }
.m_mb5 { margin-bottom: 1rem; }
.m_mb6 { margin-bottom: 2rem; }
.m_mb7 { margin-bottom: 4rem; }
.m_mb8 { margin-bottom: 8rem; }
.m_mb9 { margin-bottom: 999rem; }
.m_mb-1 { margin-bottom: 0.0625rem; }
.m_mb-2 { margin-bottom: -0.125rem; }
.m_mb-3 { margin-bottom: -0.25rem; }
.m_mb-4 { margin-bottom: -0.5rem; }
.m_mb-5 { margin-bottom: -1rem; }
.m_mb-6 { margin-bottom: -2rem; }
.m_mb-7 { margin-bottom: -4rem; }
.m_mb-8 { margin-bottom: -8rem; }
.m_mb-9 { margin-bottom: -999rem; }
.m_mb-a { margin-bottom: auto; }
.m_ml0 { margin-left: 0; }
.m_ml1 { margin-left: 0.0625rem; }
.m_ml2 { margin-left: 0.125rem; }
.m_ml3 { margin-left: 0.25rem; }
.m_ml4 { margin-left: 0.5rem; }
.m_ml5 { margin-left: 1rem; }
.m_ml6 { margin-left: 2rem; }
.m_ml7 { margin-left: 4rem; }
.m_ml8 { margin-left: 8rem; }
.m_ml9 { margin-left: 999rem; }
.m_ml-1 { margin-left: 0.0625rem; }
.m_ml-2 { margin-left: -0.125rem; }
.m_ml-3 { margin-left: -0.25rem; }
.m_ml-4 { margin-left: -0.5rem; }
.m_ml-5 { margin-left: -1rem; }
.m_ml-6 { margin-left: -2rem; }
.m_ml-7 { margin-left: -4rem; }
.m_ml-8 { margin-left: -8rem; }
.m_ml-9 { margin-left: -999rem; }
.m_ml-a { margin-left: auto; }
.m_mx0 { margin-left: 0; margin-right: 0; }
.m_mx1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.m_mx2 { margin-left: 0.125rem; margin-right: 0.125rem; }
.m_mx3 { margin-left: 0.25rem; margin-right: 0.25rem; }
.m_mx4 { margin-left: 0.5rem; margin-right: 0.5rem; }
.m_mx5 { margin-left: 1rem; margin-right: 1rem; }
.m_mx6 { margin-left: 2rem; margin-right: 2rem; }
.m_mx7 { margin-left: 4rem; margin-right: 4rem; }
.m_mx8 { margin-left: 8rem; margin-right: 8rem; }
.m_mx9 { margin-left: 999rem; margin-right: 999rem; }
.m_mx-1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.m_mx-2 { margin-left: -0.125rem; margin-right: -0.125rem; }
.m_mx-3 { margin-left: -0.25rem; margin-right: -0.25rem; }
.m_mx-4 { margin-left: -0.5rem; margin-right: -0.5rem; }
.m_mx-5 { margin-left: -1rem; margin-right: -1rem; }
.m_mx-6 { margin-left: -2rem; margin-right: -2rem; }
.m_mx-7 { margin-left: -4rem; margin-right: -4rem; }
.m_mx-8 { margin-left: -8rem; margin-right: -8rem; }
.m_mx-9 { margin-left: -999rem; margin-right: -999rem; }
.m_mx-a { margin-left: auto; margin-right: auto; }
.m_my0 { margin-top: 0; margin-bottom: 0; }
.m_my1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.m_my2 { margin-top: 0.125rem; margin-bottom: 0.125rem; }
.m_my3 { margin-top: 0.25rem; margin-bottom: 0.25rem; }
.m_my4 { margin-top: 0.5rem; margin-bottom: 0.5rem; }
.m_my5 { margin-top: 1rem; margin-bottom: 1rem; }
.m_my6 { margin-top: 2rem; margin-bottom: 2rem; }
.m_my7 { margin-top: 4rem; margin-bottom: 4rem; }
.m_my8 { margin-top: 8rem; margin-bottom: 8rem; }
.m_my9 { margin-top: 999rem; margin-bottom: 999rem; }
.m_my-1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.m_my-2 { margin-top: -0.125rem; margin-bottom: -0.125rem; }
.m_my-3 { margin-top: -0.25rem; margin-bottom: -0.25rem; }
.m_my-4 { margin-top: -0.5rem; margin-bottom: -0.5rem; }
.m_my-5 { margin-top: -1rem; margin-bottom: -1rem; }
.m_my-6 { margin-top: -2rem; margin-bottom: -2rem; }
.m_my-7 { margin-top: -4rem; margin-bottom: -4rem; }
.m_my-8 { margin-top: -8rem; margin-bottom: -8rem; }
.m_my-9 { margin-top: -999rem; margin-bottom: -999rem; }
.m_my-a { margin-top: auto; margin-bottom: auto; }
}


@media (min-width: 62em) {
.l_m0 { margin: 0; }
.l_m1 { margin: 0.0625rem; }
.l_m2 { margin: 0.125rem; }
.l_m3 { margin: 0.25rem; }
.l_m4 { margin: 0.5rem; }
.l_m5 { margin: 1rem; }
.l_m6 { margin: 2rem; }
.l_m7 { margin: 4rem; }
.l_m8 { margin: 8rem; }
.l_m9 { margin: 999rem; }
.l_m-1 { margin: 0.0625rem; }
.l_m-2 { margin: -0.125rem; }
.l_m-3 { margin: -0.25rem; }
.l_m-4 { margin: -0.5rem; }
.l_m-5 { margin: -1rem; }
.l_m-6 { margin: -2rem; }
.l_m-7 { margin: -4rem; }
.l_m-8 { margin: -8rem; }
.l_m-9 { margin: -999rem; }
.l_m-a { margin: auto; }
.l_mt0 { margin-top: 0; }
.l_mt1 { margin-top: 0.0625rem; }
.l_mt2 { margin-top: 0.125rem; }
.l_mt3 { margin-top: 0.25rem; }
.l_mt4 { margin-top: 0.5rem; }
.l_mt5 { margin-top: 1rem; }
.l_mt6 { margin-top: 2rem; }
.l_mt7 { margin-top: 4rem; }
.l_mt8 { margin-top: 8rem; }
.l_mt9 { margin-top: 999rem; }
.l_mt-1 { margin-top: 0.0625rem; }
.l_mt-2 { margin-top: -0.125rem; }
.l_mt-3 { margin-top: -0.25rem; }
.l_mt-4 { margin-top: -0.5rem; }
.l_mt-5 { margin-top: -1rem; }
.l_mt-6 { margin-top: -2rem; }
.l_mt-7 { margin-top: -4rem; }
.l_mt-8 { margin-top: -8rem; }
.l_mt-9 { margin-top: -999rem; }
.l_mt-a { margin-top: auto; }
.l_mr0 { margin-right: 0; }
.l_mr1 { margin-right: 0.0625rem; }
.l_mr2 { margin-right: 0.125rem; }
.l_mr3 { margin-right: 0.25rem; }
.l_mr4 { margin-right: 0.5rem; }
.l_mr5 { margin-right: 1rem; }
.l_mr6 { margin-right: 2rem; }
.l_mr7 { margin-right: 4rem; }
.l_mr8 { margin-right: 8rem; }
.l_mr9 { margin-right: 999rem; }
.l_mr-1 { margin-right: 0.0625rem; }
.l_mr-2 { margin-right: -0.125rem; }
.l_mr-3 { margin-right: -0.25rem; }
.l_mr-4 { margin-right: -0.5rem; }
.l_mr-5 { margin-right: -1rem; }
.l_mr-6 { margin-right: -2rem; }
.l_mr-7 { margin-right: -4rem; }
.l_mr-8 { margin-right: -8rem; }
.l_mr-9 { margin-right: -999rem; }
.l_mr-a { margin-right: auto; }
.l_mb0 { margin-bottom: 0; }
.l_mb1 { margin-bottom: 0.0625rem; }
.l_mb2 { margin-bottom: 0.125rem; }
.l_mb3 { margin-bottom: 0.25rem; }
.l_mb4 { margin-bottom: 0.5rem; }
.l_mb5 { margin-bottom: 1rem; }
.l_mb6 { margin-bottom: 2rem; }
.l_mb7 { margin-bottom: 4rem; }
.l_mb8 { margin-bottom: 8rem; }
.l_mb9 { margin-bottom: 999rem; }
.l_mb-1 { margin-bottom: 0.0625rem; }
.l_mb-2 { margin-bottom: -0.125rem; }
.l_mb-3 { margin-bottom: -0.25rem; }
.l_mb-4 { margin-bottom: -0.5rem; }
.l_mb-5 { margin-bottom: -1rem; }
.l_mb-6 { margin-bottom: -2rem; }
.l_mb-7 { margin-bottom: -4rem; }
.l_mb-8 { margin-bottom: -8rem; }
.l_mb-9 { margin-bottom: -999rem; }
.l_mb-a { margin-bottom: auto; }
.l_ml0 { margin-left: 0; }
.l_ml1 { margin-left: 0.0625rem; }
.l_ml2 { margin-left: 0.125rem; }
.l_ml3 { margin-left: 0.25rem; }
.l_ml4 { margin-left: 0.5rem; }
.l_ml5 { margin-left: 1rem; }
.l_ml6 { margin-left: 2rem; }
.l_ml7 { margin-left: 4rem; }
.l_ml8 { margin-left: 8rem; }
.l_ml9 { margin-left: 999rem; }
.l_ml-1 { margin-left: 0.0625rem; }
.l_ml-2 { margin-left: -0.125rem; }
.l_ml-3 { margin-left: -0.25rem; }
.l_ml-4 { margin-left: -0.5rem; }
.l_ml-5 { margin-left: -1rem; }
.l_ml-6 { margin-left: -2rem; }
.l_ml-7 { margin-left: -4rem; }
.l_ml-8 { margin-left: -8rem; }
.l_ml-9 { margin-left: -999rem; }
.l_ml-a { margin-left: auto; }
.l_mx0 { margin-left: 0; margin-right: 0; }
.l_mx1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.l_mx2 { margin-left: 0.125rem; margin-right: 0.125rem; }
.l_mx3 { margin-left: 0.25rem; margin-right: 0.25rem; }
.l_mx4 { margin-left: 0.5rem; margin-right: 0.5rem; }
.l_mx5 { margin-left: 1rem; margin-right: 1rem; }
.l_mx6 { margin-left: 2rem; margin-right: 2rem; }
.l_mx7 { margin-left: 4rem; margin-right: 4rem; }
.l_mx8 { margin-left: 8rem; margin-right: 8rem; }
.l_mx9 { margin-left: 999rem; margin-right: 999rem; }
.l_mx-1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.l_mx-2 { margin-left: -0.125rem; margin-right: -0.125rem; }
.l_mx-3 { margin-left: -0.25rem; margin-right: -0.25rem; }
.l_mx-4 { margin-left: -0.5rem; margin-right: -0.5rem; }
.l_mx-5 { margin-left: -1rem; margin-right: -1rem; }
.l_mx-6 { margin-left: -2rem; margin-right: -2rem; }
.l_mx-7 { margin-left: -4rem; margin-right: -4rem; }
.l_mx-8 { margin-left: -8rem; margin-right: -8rem; }
.l_mx-9 { margin-left: -999rem; margin-right: -999rem; }
.l_mx-a { margin-left: auto; margin-right: auto; }
.l_my0 { margin-top: 0; margin-bottom: 0; }
.l_my1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.l_my2 { margin-top: 0.125rem; margin-bottom: 0.125rem; }
.l_my3 { margin-top: 0.25rem; margin-bottom: 0.25rem; }
.l_my4 { margin-top: 0.5rem; margin-bottom: 0.5rem; }
.l_my5 { margin-top: 1rem; margin-bottom: 1rem; }
.l_my6 { margin-top: 2rem; margin-bottom: 2rem; }
.l_my7 { margin-top: 4rem; margin-bottom: 4rem; }
.l_my8 { margin-top: 8rem; margin-bottom: 8rem; }
.l_my9 { margin-top: 999rem; margin-bottom: 999rem; }
.l_my-1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.l_my-2 { margin-top: -0.125rem; margin-bottom: -0.125rem; }
.l_my-3 { margin-top: -0.25rem; margin-bottom: -0.25rem; }
.l_my-4 { margin-top: -0.5rem; margin-bottom: -0.5rem; }
.l_my-5 { margin-top: -1rem; margin-bottom: -1rem; }
.l_my-6 { margin-top: -2rem; margin-bottom: -2rem; }
.l_my-7 { margin-top: -4rem; margin-bottom: -4rem; }
.l_my-8 { margin-top: -8rem; margin-bottom: -8rem; }
.l_my-9 { margin-top: -999rem; margin-bottom: -999rem; }
.l_my-a { margin-top: auto; margin-bottom: auto; }
}


@media (min-width: 75em) {
.x_m0 { margin: 0; }
.x_m1 { margin: 0.0625rem; }
.x_m2 { margin: 0.125rem; }
.x_m3 { margin: 0.25rem; }
.x_m4 { margin: 0.5rem; }
.x_m5 { margin: 1rem; }
.x_m6 { margin: 2rem; }
.x_m7 { margin: 4rem; }
.x_m8 { margin: 8rem; }
.x_m9 { margin: 999rem; }
.x_m-1 { margin: 0.0625rem; }
.x_m-2 { margin: -0.125rem; }
.x_m-3 { margin: -0.25rem; }
.x_m-4 { margin: -0.5rem; }
.x_m-5 { margin: -1rem; }
.x_m-6 { margin: -2rem; }
.x_m-7 { margin: -4rem; }
.x_m-8 { margin: -8rem; }
.x_m-9 { margin: -999rem; }
.x_m-a { margin: auto; }
.x_mt0 { margin-top: 0; }
.x_mt1 { margin-top: 0.0625rem; }
.x_mt2 { margin-top: 0.125rem; }
.x_mt3 { margin-top: 0.25rem; }
.x_mt4 { margin-top: 0.5rem; }
.x_mt5 { margin-top: 1rem; }
.x_mt6 { margin-top: 2rem; }
.x_mt7 { margin-top: 4rem; }
.x_mt8 { margin-top: 8rem; }
.x_mt9 { margin-top: 999rem; }
.x_mt-1 { margin-top: 0.0625rem; }
.x_mt-2 { margin-top: -0.125rem; }
.x_mt-3 { margin-top: -0.25rem; }
.x_mt-4 { margin-top: -0.5rem; }
.x_mt-5 { margin-top: -1rem; }
.x_mt-6 { margin-top: -2rem; }
.x_mt-7 { margin-top: -4rem; }
.x_mt-8 { margin-top: -8rem; }
.x_mt-9 { margin-top: -999rem; }
.x_mt-a { margin-top: auto; }
.x_mr0 { margin-right: 0; }
.x_mr1 { margin-right: 0.0625rem; }
.x_mr2 { margin-right: 0.125rem; }
.x_mr3 { margin-right: 0.25rem; }
.x_mr4 { margin-right: 0.5rem; }
.x_mr5 { margin-right: 1rem; }
.x_mr6 { margin-right: 2rem; }
.x_mr7 { margin-right: 4rem; }
.x_mr8 { margin-right: 8rem; }
.x_mr9 { margin-right: 999rem; }
.x_mr-1 { margin-right: 0.0625rem; }
.x_mr-2 { margin-right: -0.125rem; }
.x_mr-3 { margin-right: -0.25rem; }
.x_mr-4 { margin-right: -0.5rem; }
.x_mr-5 { margin-right: -1rem; }
.x_mr-6 { margin-right: -2rem; }
.x_mr-7 { margin-right: -4rem; }
.x_mr-8 { margin-right: -8rem; }
.x_mr-9 { margin-right: -999rem; }
.x_mr-a { margin-right: auto; }
.x_mb0 { margin-bottom: 0; }
.x_mb1 { margin-bottom: 0.0625rem; }
.x_mb2 { margin-bottom: 0.125rem; }
.x_mb3 { margin-bottom: 0.25rem; }
.x_mb4 { margin-bottom: 0.5rem; }
.x_mb5 { margin-bottom: 1rem; }
.x_mb6 { margin-bottom: 2rem; }
.x_mb7 { margin-bottom: 4rem; }
.x_mb8 { margin-bottom: 8rem; }
.x_mb9 { margin-bottom: 999rem; }
.x_mb-1 { margin-bottom: 0.0625rem; }
.x_mb-2 { margin-bottom: -0.125rem; }
.x_mb-3 { margin-bottom: -0.25rem; }
.x_mb-4 { margin-bottom: -0.5rem; }
.x_mb-5 { margin-bottom: -1rem; }
.x_mb-6 { margin-bottom: -2rem; }
.x_mb-7 { margin-bottom: -4rem; }
.x_mb-8 { margin-bottom: -8rem; }
.x_mb-9 { margin-bottom: -999rem; }
.x_mb-a { margin-bottom: auto; }
.x_ml0 { margin-left: 0; }
.x_ml1 { margin-left: 0.0625rem; }
.x_ml2 { margin-left: 0.125rem; }
.x_ml3 { margin-left: 0.25rem; }
.x_ml4 { margin-left: 0.5rem; }
.x_ml5 { margin-left: 1rem; }
.x_ml6 { margin-left: 2rem; }
.x_ml7 { margin-left: 4rem; }
.x_ml8 { margin-left: 8rem; }
.x_ml9 { margin-left: 999rem; }
.x_ml-1 { margin-left: 0.0625rem; }
.x_ml-2 { margin-left: -0.125rem; }
.x_ml-3 { margin-left: -0.25rem; }
.x_ml-4 { margin-left: -0.5rem; }
.x_ml-5 { margin-left: -1rem; }
.x_ml-6 { margin-left: -2rem; }
.x_ml-7 { margin-left: -4rem; }
.x_ml-8 { margin-left: -8rem; }
.x_ml-9 { margin-left: -999rem; }
.x_ml-a { margin-left: auto; }
.x_mx0 { margin-left: 0; margin-right: 0; }
.x_mx1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.x_mx2 { margin-left: 0.125rem; margin-right: 0.125rem; }
.x_mx3 { margin-left: 0.25rem; margin-right: 0.25rem; }
.x_mx4 { margin-left: 0.5rem; margin-right: 0.5rem; }
.x_mx5 { margin-left: 1rem; margin-right: 1rem; }
.x_mx6 { margin-left: 2rem; margin-right: 2rem; }
.x_mx7 { margin-left: 4rem; margin-right: 4rem; }
.x_mx8 { margin-left: 8rem; margin-right: 8rem; }
.x_mx9 { margin-left: 999rem; margin-right: 999rem; }
.x_mx-1 { margin-left: 0.0625rem; margin-right: 0.0625rem; }
.x_mx-2 { margin-left: -0.125rem; margin-right: -0.125rem; }
.x_mx-3 { margin-left: -0.25rem; margin-right: -0.25rem; }
.x_mx-4 { margin-left: -0.5rem; margin-right: -0.5rem; }
.x_mx-5 { margin-left: -1rem; margin-right: -1rem; }
.x_mx-6 { margin-left: -2rem; margin-right: -2rem; }
.x_mx-7 { margin-left: -4rem; margin-right: -4rem; }
.x_mx-8 { margin-left: -8rem; margin-right: -8rem; }
.x_mx-9 { margin-left: -999rem; margin-right: -999rem; }
.x_mx-a { margin-left: auto; margin-right: auto; }
.x_my0 { margin-top: 0; margin-bottom: 0; }
.x_my1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.x_my2 { margin-top: 0.125rem; margin-bottom: 0.125rem; }
.x_my3 { margin-top: 0.25rem; margin-bottom: 0.25rem; }
.x_my4 { margin-top: 0.5rem; margin-bottom: 0.5rem; }
.x_my5 { margin-top: 1rem; margin-bottom: 1rem; }
.x_my6 { margin-top: 2rem; margin-bottom: 2rem; }
.x_my7 { margin-top: 4rem; margin-bottom: 4rem; }
.x_my8 { margin-top: 8rem; margin-bottom: 8rem; }
.x_my9 { margin-top: 999rem; margin-bottom: 999rem; }
.x_my-1 { margin-top: 0.0625rem; margin-bottom: 0.0625rem; }
.x_my-2 { margin-top: -0.125rem; margin-bottom: -0.125rem; }
.x_my-3 { margin-top: -0.25rem; margin-bottom: -0.25rem; }
.x_my-4 { margin-top: -0.5rem; margin-bottom: -0.5rem; }
.x_my-5 { margin-top: -1rem; margin-bottom: -1rem; }
.x_my-6 { margin-top: -2rem; margin-bottom: -2rem; }
.x_my-7 { margin-top: -4rem; margin-bottom: -4rem; }
.x_my-8 { margin-top: -8rem; margin-bottom: -8rem; }
.x_my-9 { margin-top: -999rem; margin-bottom: -999rem; }
.x_my-a { margin-top: auto; margin-bottom: auto; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -