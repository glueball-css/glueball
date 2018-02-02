# module: Font size

Progressively larger font sizes.








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.size` |`font-size`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`1` | `.75rem`
`2` | `.875rem`
`3` | `1rem`
`4` | `1.25rem`
`5` | `1.5rem`
`6` | `2rem`
`7` | `2.75rem`
`8` | `3.75rem`
`9` | `5rem`




## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|




## Pseudo selectors
The following pseudo selectors are available:

### hvr
The pseudo selector `hvr` has the following media queries available:



| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|



### fcs
The pseudo selector `fcs` has the following media queries available:



| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|






## CSS rules
```css

.size1 { font-size: .75rem; }
.size2 { font-size: .875rem; }
.size3 { font-size: 1rem; }
.size4 { font-size: 1.25rem; }
.size5 { font-size: 1.5rem; }
.size6 { font-size: 2rem; }
.size7 { font-size: 2.75rem; }
.size8 { font-size: 3.75rem; }
.size9 { font-size: 5rem; }


@media (min-width: 36em) {
.s_size1 { font-size: .75rem; }
.s_size2 { font-size: .875rem; }
.s_size3 { font-size: 1rem; }
.s_size4 { font-size: 1.25rem; }
.s_size5 { font-size: 1.5rem; }
.s_size6 { font-size: 2rem; }
.s_size7 { font-size: 2.75rem; }
.s_size8 { font-size: 3.75rem; }
.s_size9 { font-size: 5rem; }
}


@media (min-width: 48em) {
.m_size1 { font-size: .75rem; }
.m_size2 { font-size: .875rem; }
.m_size3 { font-size: 1rem; }
.m_size4 { font-size: 1.25rem; }
.m_size5 { font-size: 1.5rem; }
.m_size6 { font-size: 2rem; }
.m_size7 { font-size: 2.75rem; }
.m_size8 { font-size: 3.75rem; }
.m_size9 { font-size: 5rem; }
}


@media (min-width: 62em) {
.l_size1 { font-size: .75rem; }
.l_size2 { font-size: .875rem; }
.l_size3 { font-size: 1rem; }
.l_size4 { font-size: 1.25rem; }
.l_size5 { font-size: 1.5rem; }
.l_size6 { font-size: 2rem; }
.l_size7 { font-size: 2.75rem; }
.l_size8 { font-size: 3.75rem; }
.l_size9 { font-size: 5rem; }
}


@media (min-width: 75em) {
.x_size1 { font-size: .75rem; }
.x_size2 { font-size: .875rem; }
.x_size3 { font-size: 1rem; }
.x_size4 { font-size: 1.25rem; }
.x_size5 { font-size: 1.5rem; }
.x_size6 { font-size: 2rem; }
.x_size7 { font-size: 2.75rem; }
.x_size8 { font-size: 3.75rem; }
.x_size9 { font-size: 5rem; }
}

.hvr_size1:hover { font-size: .75rem; }
.hvr_size2:hover { font-size: .875rem; }
.hvr_size3:hover { font-size: 1rem; }
.hvr_size4:hover { font-size: 1.25rem; }
.hvr_size5:hover { font-size: 1.5rem; }
.hvr_size6:hover { font-size: 2rem; }
.hvr_size7:hover { font-size: 2.75rem; }
.hvr_size8:hover { font-size: 3.75rem; }
.hvr_size9:hover { font-size: 5rem; }


@media (min-width: 36em) {
.s_hvr_size1:hover { font-size: .75rem; }
.s_hvr_size2:hover { font-size: .875rem; }
.s_hvr_size3:hover { font-size: 1rem; }
.s_hvr_size4:hover { font-size: 1.25rem; }
.s_hvr_size5:hover { font-size: 1.5rem; }
.s_hvr_size6:hover { font-size: 2rem; }
.s_hvr_size7:hover { font-size: 2.75rem; }
.s_hvr_size8:hover { font-size: 3.75rem; }
.s_hvr_size9:hover { font-size: 5rem; }
}


@media (min-width: 48em) {
.m_hvr_size1:hover { font-size: .75rem; }
.m_hvr_size2:hover { font-size: .875rem; }
.m_hvr_size3:hover { font-size: 1rem; }
.m_hvr_size4:hover { font-size: 1.25rem; }
.m_hvr_size5:hover { font-size: 1.5rem; }
.m_hvr_size6:hover { font-size: 2rem; }
.m_hvr_size7:hover { font-size: 2.75rem; }
.m_hvr_size8:hover { font-size: 3.75rem; }
.m_hvr_size9:hover { font-size: 5rem; }
}


@media (min-width: 62em) {
.l_hvr_size1:hover { font-size: .75rem; }
.l_hvr_size2:hover { font-size: .875rem; }
.l_hvr_size3:hover { font-size: 1rem; }
.l_hvr_size4:hover { font-size: 1.25rem; }
.l_hvr_size5:hover { font-size: 1.5rem; }
.l_hvr_size6:hover { font-size: 2rem; }
.l_hvr_size7:hover { font-size: 2.75rem; }
.l_hvr_size8:hover { font-size: 3.75rem; }
.l_hvr_size9:hover { font-size: 5rem; }
}


@media (min-width: 75em) {
.x_hvr_size1:hover { font-size: .75rem; }
.x_hvr_size2:hover { font-size: .875rem; }
.x_hvr_size3:hover { font-size: 1rem; }
.x_hvr_size4:hover { font-size: 1.25rem; }
.x_hvr_size5:hover { font-size: 1.5rem; }
.x_hvr_size6:hover { font-size: 2rem; }
.x_hvr_size7:hover { font-size: 2.75rem; }
.x_hvr_size8:hover { font-size: 3.75rem; }
.x_hvr_size9:hover { font-size: 5rem; }
}

.fcs_size1:focus { font-size: .75rem; }
.fcs_size2:focus { font-size: .875rem; }
.fcs_size3:focus { font-size: 1rem; }
.fcs_size4:focus { font-size: 1.25rem; }
.fcs_size5:focus { font-size: 1.5rem; }
.fcs_size6:focus { font-size: 2rem; }
.fcs_size7:focus { font-size: 2.75rem; }
.fcs_size8:focus { font-size: 3.75rem; }
.fcs_size9:focus { font-size: 5rem; }


@media (min-width: 36em) {
.s_fcs_size1:focus { font-size: .75rem; }
.s_fcs_size2:focus { font-size: .875rem; }
.s_fcs_size3:focus { font-size: 1rem; }
.s_fcs_size4:focus { font-size: 1.25rem; }
.s_fcs_size5:focus { font-size: 1.5rem; }
.s_fcs_size6:focus { font-size: 2rem; }
.s_fcs_size7:focus { font-size: 2.75rem; }
.s_fcs_size8:focus { font-size: 3.75rem; }
.s_fcs_size9:focus { font-size: 5rem; }
}


@media (min-width: 48em) {
.m_fcs_size1:focus { font-size: .75rem; }
.m_fcs_size2:focus { font-size: .875rem; }
.m_fcs_size3:focus { font-size: 1rem; }
.m_fcs_size4:focus { font-size: 1.25rem; }
.m_fcs_size5:focus { font-size: 1.5rem; }
.m_fcs_size6:focus { font-size: 2rem; }
.m_fcs_size7:focus { font-size: 2.75rem; }
.m_fcs_size8:focus { font-size: 3.75rem; }
.m_fcs_size9:focus { font-size: 5rem; }
}


@media (min-width: 62em) {
.l_fcs_size1:focus { font-size: .75rem; }
.l_fcs_size2:focus { font-size: .875rem; }
.l_fcs_size3:focus { font-size: 1rem; }
.l_fcs_size4:focus { font-size: 1.25rem; }
.l_fcs_size5:focus { font-size: 1.5rem; }
.l_fcs_size6:focus { font-size: 2rem; }
.l_fcs_size7:focus { font-size: 2.75rem; }
.l_fcs_size8:focus { font-size: 3.75rem; }
.l_fcs_size9:focus { font-size: 5rem; }
}


@media (min-width: 75em) {
.x_fcs_size1:focus { font-size: .75rem; }
.x_fcs_size2:focus { font-size: .875rem; }
.x_fcs_size3:focus { font-size: 1rem; }
.x_fcs_size4:focus { font-size: 1.25rem; }
.x_fcs_size5:focus { font-size: 1.5rem; }
.x_fcs_size6:focus { font-size: 2rem; }
.x_fcs_size7:focus { font-size: 2.75rem; }
.x_fcs_size8:focus { font-size: 3.75rem; }
.x_fcs_size9:focus { font-size: 5rem; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -