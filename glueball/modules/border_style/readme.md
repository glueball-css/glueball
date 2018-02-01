# module: Border style

Style for all borders and individual borders








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.bs` |`border-style`|
| `.bts` |`border-top-style`|
| `.brs` |`border-right-style`|
| `.bbs` |`border-bottom-style`|
| `.bls` |`border-left-style`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`n` | `none`
`dash` | `dashed`
`dot` | `dotted`
`s` | `   solid`




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

.bs-n { border-style: none; }
.bs-dash { border-style: dashed; }
.bs-dot { border-style: dotted; }
.bs-s { border-style:    solid; }
.bts-n { border-top-style: none; }
.bts-dash { border-top-style: dashed; }
.bts-dot { border-top-style: dotted; }
.bts-s { border-top-style:    solid; }
.brs-n { border-right-style: none; }
.brs-dash { border-right-style: dashed; }
.brs-dot { border-right-style: dotted; }
.brs-s { border-right-style:    solid; }
.bbs-n { border-bottom-style: none; }
.bbs-dash { border-bottom-style: dashed; }
.bbs-dot { border-bottom-style: dotted; }
.bbs-s { border-bottom-style:    solid; }
.bls-n { border-left-style: none; }
.bls-dash { border-left-style: dashed; }
.bls-dot { border-left-style: dotted; }
.bls-s { border-left-style:    solid; }


@media (min-width: 36em) {
.s_bs-n { border-style: none; }
.s_bs-dash { border-style: dashed; }
.s_bs-dot { border-style: dotted; }
.s_bs-s { border-style:    solid; }
.s_bts-n { border-top-style: none; }
.s_bts-dash { border-top-style: dashed; }
.s_bts-dot { border-top-style: dotted; }
.s_bts-s { border-top-style:    solid; }
.s_brs-n { border-right-style: none; }
.s_brs-dash { border-right-style: dashed; }
.s_brs-dot { border-right-style: dotted; }
.s_brs-s { border-right-style:    solid; }
.s_bbs-n { border-bottom-style: none; }
.s_bbs-dash { border-bottom-style: dashed; }
.s_bbs-dot { border-bottom-style: dotted; }
.s_bbs-s { border-bottom-style:    solid; }
.s_bls-n { border-left-style: none; }
.s_bls-dash { border-left-style: dashed; }
.s_bls-dot { border-left-style: dotted; }
.s_bls-s { border-left-style:    solid; }
}


@media (min-width: 48em) {
.m_bs-n { border-style: none; }
.m_bs-dash { border-style: dashed; }
.m_bs-dot { border-style: dotted; }
.m_bs-s { border-style:    solid; }
.m_bts-n { border-top-style: none; }
.m_bts-dash { border-top-style: dashed; }
.m_bts-dot { border-top-style: dotted; }
.m_bts-s { border-top-style:    solid; }
.m_brs-n { border-right-style: none; }
.m_brs-dash { border-right-style: dashed; }
.m_brs-dot { border-right-style: dotted; }
.m_brs-s { border-right-style:    solid; }
.m_bbs-n { border-bottom-style: none; }
.m_bbs-dash { border-bottom-style: dashed; }
.m_bbs-dot { border-bottom-style: dotted; }
.m_bbs-s { border-bottom-style:    solid; }
.m_bls-n { border-left-style: none; }
.m_bls-dash { border-left-style: dashed; }
.m_bls-dot { border-left-style: dotted; }
.m_bls-s { border-left-style:    solid; }
}


@media (min-width: 62em) {
.l_bs-n { border-style: none; }
.l_bs-dash { border-style: dashed; }
.l_bs-dot { border-style: dotted; }
.l_bs-s { border-style:    solid; }
.l_bts-n { border-top-style: none; }
.l_bts-dash { border-top-style: dashed; }
.l_bts-dot { border-top-style: dotted; }
.l_bts-s { border-top-style:    solid; }
.l_brs-n { border-right-style: none; }
.l_brs-dash { border-right-style: dashed; }
.l_brs-dot { border-right-style: dotted; }
.l_brs-s { border-right-style:    solid; }
.l_bbs-n { border-bottom-style: none; }
.l_bbs-dash { border-bottom-style: dashed; }
.l_bbs-dot { border-bottom-style: dotted; }
.l_bbs-s { border-bottom-style:    solid; }
.l_bls-n { border-left-style: none; }
.l_bls-dash { border-left-style: dashed; }
.l_bls-dot { border-left-style: dotted; }
.l_bls-s { border-left-style:    solid; }
}


@media (min-width: 75em) {
.x_bs-n { border-style: none; }
.x_bs-dash { border-style: dashed; }
.x_bs-dot { border-style: dotted; }
.x_bs-s { border-style:    solid; }
.x_bts-n { border-top-style: none; }
.x_bts-dash { border-top-style: dashed; }
.x_bts-dot { border-top-style: dotted; }
.x_bts-s { border-top-style:    solid; }
.x_brs-n { border-right-style: none; }
.x_brs-dash { border-right-style: dashed; }
.x_brs-dot { border-right-style: dotted; }
.x_brs-s { border-right-style:    solid; }
.x_bbs-n { border-bottom-style: none; }
.x_bbs-dash { border-bottom-style: dashed; }
.x_bbs-dot { border-bottom-style: dotted; }
.x_bbs-s { border-bottom-style:    solid; }
.x_bls-n { border-left-style: none; }
.x_bls-dash { border-left-style: dashed; }
.x_bls-dot { border-left-style: dotted; }
.x_bls-s { border-left-style:    solid; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -