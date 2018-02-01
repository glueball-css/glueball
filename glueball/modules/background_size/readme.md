# module: Background size

Contain or cover








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.` |`background-size`|





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Sizings

Selector  | Value
--------- | ---------
`contain` | `contain`
`cover` | `cover`





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

.contain { background-size: contain; }
.cover { background-size: cover; }


@media (min-width: 36em) {
.s_contain { background-size: contain; }
.s_cover { background-size: cover; }
}


@media (min-width: 48em) {
.m_contain { background-size: contain; }
.m_cover { background-size: cover; }
}


@media (min-width: 62em) {
.l_contain { background-size: contain; }
.l_cover { background-size: cover; }
}


@media (min-width: 75em) {
.x_contain { background-size: contain; }
.x_cover { background-size: cover; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -