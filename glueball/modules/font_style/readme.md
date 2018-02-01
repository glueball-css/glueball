# module: Font style

Normal or italic








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.` |`font-style`|





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Styles

Selector  | Value
--------- | ---------
`n` | `normal`
`i` | `italic`





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

.n { font-style: normal; }
.i { font-style: italic; }


@media (min-width: 36em) {
.s_n { font-style: normal; }
.s_i { font-style: italic; }
}


@media (min-width: 48em) {
.m_n { font-style: normal; }
.m_i { font-style: italic; }
}


@media (min-width: 62em) {
.l_n { font-style: normal; }
.l_i { font-style: italic; }
}


@media (min-width: 75em) {
.x_n { font-style: normal; }
.x_i { font-style: italic; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -