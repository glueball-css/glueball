# module: White space

White space is used to control how whitespace is rendered.








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.ws` |`white-space`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`n` | `normal`
`nw` | `nowrap`
`p` | `pre`




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

.ws-n { white-space: normal; }
.ws-nw { white-space: nowrap; }
.ws-p { white-space: pre; }


@media (min-width: 36em) {
.s_ws-n { white-space: normal; }
.s_ws-nw { white-space: nowrap; }
.s_ws-p { white-space: pre; }
}


@media (min-width: 48em) {
.m_ws-n { white-space: normal; }
.m_ws-nw { white-space: nowrap; }
.m_ws-p { white-space: pre; }
}


@media (min-width: 62em) {
.l_ws-n { white-space: normal; }
.l_ws-nw { white-space: nowrap; }
.l_ws-p { white-space: pre; }
}


@media (min-width: 75em) {
.x_ws-n { white-space: normal; }
.x_ws-nw { white-space: nowrap; }
.x_ws-p { white-space: pre; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -