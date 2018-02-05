# module: Table

Captions, border collapse, table layout, empty cells and table border spacing



## Basic styles

The basic styles do not depend on the provided values.
They do however adhere to the breakpoints and pseudo selectors.

```css

.tcs-t { caption-side: top; }

.tcs-b { caption-side: bottom; }

.separate { border-collapse: separate; }

.collapse { border-collapse: collapse; }

.tl-a { table-layout: auto; }

.tl-f { table-layout: fixed; }

.tec-s { empty-cells: show; }

.tec-h { empty-cells: hide; }

.odd_striped-gray-95:nth-child(odd) { background-color: hsl(0, 0%, 98%); }

.odd_striped-gray-90:nth-child(odd) { background-color: hsl(0, 0%, 95%); }

.even_striped-gray-95:nth-child(even) { background-color: hsl(0, 0%, 98%); }

.even_striped-gray-90:nth-child(even) { background-color: hsl(0, 0%, 95%); }

```






## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.tbs` |`border-spacing`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`0` | `0`
`1` | `0.0625rem`
`2` | `0.125rem`
`3` | `0.25rem`
`4` | `0.5rem`
`5` | `1rem`
`6` | `2rem`
`7` | `4rem`
`8` | `8rem`
`9` | `999rem`




## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|






## CSS rules
```css

.tcs-t { caption-side: top; }
.tcs-b { caption-side: bottom; }
.separate { border-collapse: separate; }
.collapse { border-collapse: collapse; }
.tl-a { table-layout: auto; }
.tl-f { table-layout: fixed; }
.tec-s { empty-cells: show; }
.tec-h { empty-cells: hide; }
.odd_striped-gray-95:nth-child(odd) { background-color: hsl(0, 0%, 98%); }
.odd_striped-gray-90:nth-child(odd) { background-color: hsl(0, 0%, 95%); }
.even_striped-gray-95:nth-child(even) { background-color: hsl(0, 0%, 98%); }
.even_striped-gray-90:nth-child(even) { background-color: hsl(0, 0%, 95%); }
.tbs0 { border-spacing: 0; }
.tbs1 { border-spacing: 0.0625rem; }
.tbs2 { border-spacing: 0.125rem; }
.tbs3 { border-spacing: 0.25rem; }
.tbs4 { border-spacing: 0.5rem; }
.tbs5 { border-spacing: 1rem; }
.tbs6 { border-spacing: 2rem; }
.tbs7 { border-spacing: 4rem; }
.tbs8 { border-spacing: 8rem; }
.tbs9 { border-spacing: 999rem; }

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -