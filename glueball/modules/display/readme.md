# module: Display

Controls display property








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.d` |`display`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`n` | `none`
`i` | `inline`
`b` | `block`
`ib` | `inline-block`
`it` | `inline-table`
`t` | `table`
`tcell` | `table-cell`
`trow` | `table-row`
`trowg` | `table-row-group`
`tcol` | `table-column`
`tcolg` | `table-column-group`
`f` | `flex`
`if` | `inline-flex`




## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|
|  `tl`  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒||
|  `tm`  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|||
|  `ts`  |▒▒▒▒▒|▒▒▒▒▒||||
|  `tt`  |▒▒▒▒▒|||||






## CSS rules
```css

.d-n { display: none; }
.d-i { display: inline; }
.d-b { display: block; }
.d-ib { display: inline-block; }
.d-it { display: inline-table; }
.d-t { display: table; }
.d-tcell { display: table-cell; }
.d-trow { display: table-row; }
.d-trowg { display: table-row-group; }
.d-tcol { display: table-column; }
.d-tcolg { display: table-column-group; }
.d-f { display: flex; }
.d-if { display: inline-flex; }


@media (min-width: 36em) {
.s_d-n { display: none; }
.s_d-i { display: inline; }
.s_d-b { display: block; }
.s_d-ib { display: inline-block; }
.s_d-it { display: inline-table; }
.s_d-t { display: table; }
.s_d-tcell { display: table-cell; }
.s_d-trow { display: table-row; }
.s_d-trowg { display: table-row-group; }
.s_d-tcol { display: table-column; }
.s_d-tcolg { display: table-column-group; }
.s_d-f { display: flex; }
.s_d-if { display: inline-flex; }
}


@media (min-width: 48em) {
.m_d-n { display: none; }
.m_d-i { display: inline; }
.m_d-b { display: block; }
.m_d-ib { display: inline-block; }
.m_d-it { display: inline-table; }
.m_d-t { display: table; }
.m_d-tcell { display: table-cell; }
.m_d-trow { display: table-row; }
.m_d-trowg { display: table-row-group; }
.m_d-tcol { display: table-column; }
.m_d-tcolg { display: table-column-group; }
.m_d-f { display: flex; }
.m_d-if { display: inline-flex; }
}


@media (min-width: 62em) {
.l_d-n { display: none; }
.l_d-i { display: inline; }
.l_d-b { display: block; }
.l_d-ib { display: inline-block; }
.l_d-it { display: inline-table; }
.l_d-t { display: table; }
.l_d-tcell { display: table-cell; }
.l_d-trow { display: table-row; }
.l_d-trowg { display: table-row-group; }
.l_d-tcol { display: table-column; }
.l_d-tcolg { display: table-column-group; }
.l_d-f { display: flex; }
.l_d-if { display: inline-flex; }
}


@media (min-width: 75em) {
.x_d-n { display: none; }
.x_d-i { display: inline; }
.x_d-b { display: block; }
.x_d-ib { display: inline-block; }
.x_d-it { display: inline-table; }
.x_d-t { display: table; }
.x_d-tcell { display: table-cell; }
.x_d-trow { display: table-row; }
.x_d-trowg { display: table-row-group; }
.x_d-tcol { display: table-column; }
.x_d-tcolg { display: table-column-group; }
.x_d-f { display: flex; }
.x_d-if { display: inline-flex; }
}


@media (max-width: 74.99em) {
.tl_d-n { display: none; }
.tl_d-i { display: inline; }
.tl_d-b { display: block; }
.tl_d-ib { display: inline-block; }
.tl_d-it { display: inline-table; }
.tl_d-t { display: table; }
.tl_d-tcell { display: table-cell; }
.tl_d-trow { display: table-row; }
.tl_d-trowg { display: table-row-group; }
.tl_d-tcol { display: table-column; }
.tl_d-tcolg { display: table-column-group; }
.tl_d-f { display: flex; }
.tl_d-if { display: inline-flex; }
}


@media (max-width: 61.99em) {
.tm_d-n { display: none; }
.tm_d-i { display: inline; }
.tm_d-b { display: block; }
.tm_d-ib { display: inline-block; }
.tm_d-it { display: inline-table; }
.tm_d-t { display: table; }
.tm_d-tcell { display: table-cell; }
.tm_d-trow { display: table-row; }
.tm_d-trowg { display: table-row-group; }
.tm_d-tcol { display: table-column; }
.tm_d-tcolg { display: table-column-group; }
.tm_d-f { display: flex; }
.tm_d-if { display: inline-flex; }
}


@media (max-width: 47.99em) {
.ts_d-n { display: none; }
.ts_d-i { display: inline; }
.ts_d-b { display: block; }
.ts_d-ib { display: inline-block; }
.ts_d-it { display: inline-table; }
.ts_d-t { display: table; }
.ts_d-tcell { display: table-cell; }
.ts_d-trow { display: table-row; }
.ts_d-trowg { display: table-row-group; }
.ts_d-tcol { display: table-column; }
.ts_d-tcolg { display: table-column-group; }
.ts_d-f { display: flex; }
.ts_d-if { display: inline-flex; }
}


@media (max-width: 35.99em) {
.tt_d-n { display: none; }
.tt_d-i { display: inline; }
.tt_d-b { display: block; }
.tt_d-ib { display: inline-block; }
.tt_d-it { display: inline-table; }
.tt_d-t { display: table; }
.tt_d-tcell { display: table-cell; }
.tt_d-trow { display: table-row; }
.tt_d-trowg { display: table-row-group; }
.tt_d-tcol { display: table-column; }
.tt_d-tcolg { display: table-column-group; }
.tt_d-f { display: flex; }
.tt_d-if { display: inline-flex; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -