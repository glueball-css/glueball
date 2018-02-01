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

### hover
The pseudo selector `hover` has the following media queries available:



| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|



### focus
The pseudo selector `focus` has the following media queries available:



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

.hover_size1:hover { font-size: .75rem; }
.hover_size2:hover { font-size: .875rem; }
.hover_size3:hover { font-size: 1rem; }
.hover_size4:hover { font-size: 1.25rem; }
.hover_size5:hover { font-size: 1.5rem; }
.hover_size6:hover { font-size: 2rem; }
.hover_size7:hover { font-size: 2.75rem; }
.hover_size8:hover { font-size: 3.75rem; }
.hover_size9:hover { font-size: 5rem; }


@media (min-width: 36em) {
.s_hover_size1:hover { font-size: .75rem; }
.s_hover_size2:hover { font-size: .875rem; }
.s_hover_size3:hover { font-size: 1rem; }
.s_hover_size4:hover { font-size: 1.25rem; }
.s_hover_size5:hover { font-size: 1.5rem; }
.s_hover_size6:hover { font-size: 2rem; }
.s_hover_size7:hover { font-size: 2.75rem; }
.s_hover_size8:hover { font-size: 3.75rem; }
.s_hover_size9:hover { font-size: 5rem; }
}


@media (min-width: 48em) {
.m_hover_size1:hover { font-size: .75rem; }
.m_hover_size2:hover { font-size: .875rem; }
.m_hover_size3:hover { font-size: 1rem; }
.m_hover_size4:hover { font-size: 1.25rem; }
.m_hover_size5:hover { font-size: 1.5rem; }
.m_hover_size6:hover { font-size: 2rem; }
.m_hover_size7:hover { font-size: 2.75rem; }
.m_hover_size8:hover { font-size: 3.75rem; }
.m_hover_size9:hover { font-size: 5rem; }
}


@media (min-width: 62em) {
.l_hover_size1:hover { font-size: .75rem; }
.l_hover_size2:hover { font-size: .875rem; }
.l_hover_size3:hover { font-size: 1rem; }
.l_hover_size4:hover { font-size: 1.25rem; }
.l_hover_size5:hover { font-size: 1.5rem; }
.l_hover_size6:hover { font-size: 2rem; }
.l_hover_size7:hover { font-size: 2.75rem; }
.l_hover_size8:hover { font-size: 3.75rem; }
.l_hover_size9:hover { font-size: 5rem; }
}


@media (min-width: 75em) {
.x_hover_size1:hover { font-size: .75rem; }
.x_hover_size2:hover { font-size: .875rem; }
.x_hover_size3:hover { font-size: 1rem; }
.x_hover_size4:hover { font-size: 1.25rem; }
.x_hover_size5:hover { font-size: 1.5rem; }
.x_hover_size6:hover { font-size: 2rem; }
.x_hover_size7:hover { font-size: 2.75rem; }
.x_hover_size8:hover { font-size: 3.75rem; }
.x_hover_size9:hover { font-size: 5rem; }
}

.focus_size1:focus { font-size: .75rem; }
.focus_size2:focus { font-size: .875rem; }
.focus_size3:focus { font-size: 1rem; }
.focus_size4:focus { font-size: 1.25rem; }
.focus_size5:focus { font-size: 1.5rem; }
.focus_size6:focus { font-size: 2rem; }
.focus_size7:focus { font-size: 2.75rem; }
.focus_size8:focus { font-size: 3.75rem; }
.focus_size9:focus { font-size: 5rem; }


@media (min-width: 36em) {
.s_focus_size1:focus { font-size: .75rem; }
.s_focus_size2:focus { font-size: .875rem; }
.s_focus_size3:focus { font-size: 1rem; }
.s_focus_size4:focus { font-size: 1.25rem; }
.s_focus_size5:focus { font-size: 1.5rem; }
.s_focus_size6:focus { font-size: 2rem; }
.s_focus_size7:focus { font-size: 2.75rem; }
.s_focus_size8:focus { font-size: 3.75rem; }
.s_focus_size9:focus { font-size: 5rem; }
}


@media (min-width: 48em) {
.m_focus_size1:focus { font-size: .75rem; }
.m_focus_size2:focus { font-size: .875rem; }
.m_focus_size3:focus { font-size: 1rem; }
.m_focus_size4:focus { font-size: 1.25rem; }
.m_focus_size5:focus { font-size: 1.5rem; }
.m_focus_size6:focus { font-size: 2rem; }
.m_focus_size7:focus { font-size: 2.75rem; }
.m_focus_size8:focus { font-size: 3.75rem; }
.m_focus_size9:focus { font-size: 5rem; }
}


@media (min-width: 62em) {
.l_focus_size1:focus { font-size: .75rem; }
.l_focus_size2:focus { font-size: .875rem; }
.l_focus_size3:focus { font-size: 1rem; }
.l_focus_size4:focus { font-size: 1.25rem; }
.l_focus_size5:focus { font-size: 1.5rem; }
.l_focus_size6:focus { font-size: 2rem; }
.l_focus_size7:focus { font-size: 2.75rem; }
.l_focus_size8:focus { font-size: 3.75rem; }
.l_focus_size9:focus { font-size: 5rem; }
}


@media (min-width: 75em) {
.x_focus_size1:focus { font-size: .75rem; }
.x_focus_size2:focus { font-size: .875rem; }
.x_focus_size3:focus { font-size: 1rem; }
.x_focus_size4:focus { font-size: 1.25rem; }
.x_focus_size5:focus { font-size: 1.5rem; }
.x_focus_size6:focus { font-size: 2rem; }
.x_focus_size7:focus { font-size: 2.75rem; }
.x_focus_size8:focus { font-size: 3.75rem; }
.x_focus_size9:focus { font-size: 5rem; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -