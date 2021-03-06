# module: Overflow

Modifiers








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.o` |`overflow`|
| `.ox` |`overflow-x`|
| `.oy` |`overflow-y`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`v` | `visible`
`h` | `hidden`
`s` | `scroll`
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

.o-v { overflow: visible; }
.o-h { overflow: hidden; }
.o-s { overflow: scroll; }
.o-a { overflow: auto; }
.ox-v { overflow-x: visible; }
.ox-h { overflow-x: hidden; }
.ox-s { overflow-x: scroll; }
.ox-a { overflow-x: auto; }
.oy-v { overflow-y: visible; }
.oy-h { overflow-y: hidden; }
.oy-s { overflow-y: scroll; }
.oy-a { overflow-y: auto; }


@media (min-width: 36em) {
.s_o-v { overflow: visible; }
.s_o-h { overflow: hidden; }
.s_o-s { overflow: scroll; }
.s_o-a { overflow: auto; }
.s_ox-v { overflow-x: visible; }
.s_ox-h { overflow-x: hidden; }
.s_ox-s { overflow-x: scroll; }
.s_ox-a { overflow-x: auto; }
.s_oy-v { overflow-y: visible; }
.s_oy-h { overflow-y: hidden; }
.s_oy-s { overflow-y: scroll; }
.s_oy-a { overflow-y: auto; }
}


@media (min-width: 48em) {
.m_o-v { overflow: visible; }
.m_o-h { overflow: hidden; }
.m_o-s { overflow: scroll; }
.m_o-a { overflow: auto; }
.m_ox-v { overflow-x: visible; }
.m_ox-h { overflow-x: hidden; }
.m_ox-s { overflow-x: scroll; }
.m_ox-a { overflow-x: auto; }
.m_oy-v { overflow-y: visible; }
.m_oy-h { overflow-y: hidden; }
.m_oy-s { overflow-y: scroll; }
.m_oy-a { overflow-y: auto; }
}


@media (min-width: 62em) {
.l_o-v { overflow: visible; }
.l_o-h { overflow: hidden; }
.l_o-s { overflow: scroll; }
.l_o-a { overflow: auto; }
.l_ox-v { overflow-x: visible; }
.l_ox-h { overflow-x: hidden; }
.l_ox-s { overflow-x: scroll; }
.l_ox-a { overflow-x: auto; }
.l_oy-v { overflow-y: visible; }
.l_oy-h { overflow-y: hidden; }
.l_oy-s { overflow-y: scroll; }
.l_oy-a { overflow-y: auto; }
}


@media (min-width: 75em) {
.x_o-v { overflow: visible; }
.x_o-h { overflow: hidden; }
.x_o-s { overflow: scroll; }
.x_o-a { overflow: auto; }
.x_ox-v { overflow-x: visible; }
.x_ox-h { overflow-x: hidden; }
.x_ox-s { overflow-x: scroll; }
.x_ox-a { overflow-x: auto; }
.x_oy-v { overflow-y: visible; }
.x_oy-h { overflow-y: hidden; }
.x_oy-s { overflow-y: scroll; }
.x_oy-a { overflow-y: auto; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -