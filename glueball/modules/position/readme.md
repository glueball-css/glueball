# module: Position

Options








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.` |`position`|





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Values

Selector  | Value
--------- | ---------
`static` | `static`
`relative` | `relative`
`absolute` | `absolute`
`fixed` | `fixed`





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

.static { position: static; }
.relative { position: relative; }
.absolute { position: absolute; }
.fixed { position: fixed; }


@media (min-width: 36em) {
.s_static { position: static; }
.s_relative { position: relative; }
.s_absolute { position: absolute; }
.s_fixed { position: fixed; }
}


@media (min-width: 48em) {
.m_static { position: static; }
.m_relative { position: relative; }
.m_absolute { position: absolute; }
.m_fixed { position: fixed; }
}


@media (min-width: 62em) {
.l_static { position: static; }
.l_relative { position: relative; }
.l_absolute { position: absolute; }
.l_fixed { position: fixed; }
}


@media (min-width: 75em) {
.x_static { position: static; }
.x_relative { position: relative; }
.x_absolute { position: absolute; }
.x_fixed { position: fixed; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -