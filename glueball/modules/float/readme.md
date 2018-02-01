# module: Float

Float left, right or none








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.float` |`float`|





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Values

Selector  | Value
--------- | ---------
`l` | `left`
`r` | `right`
`n` | `none`





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

.float-l { float: left; }
.float-r { float: right; }
.float-n { float: none; }


@media (min-width: 36em) {
.s_float-l { float: left; }
.s_float-r { float: right; }
.s_float-n { float: none; }
}


@media (min-width: 48em) {
.m_float-l { float: left; }
.m_float-r { float: right; }
.m_float-n { float: none; }
}


@media (min-width: 62em) {
.l_float-l { float: left; }
.l_float-r { float: right; }
.l_float-n { float: none; }
}


@media (min-width: 75em) {
.x_float-l { float: left; }
.x_float-r { float: right; }
.x_float-n { float: none; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -