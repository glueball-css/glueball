# module: Justify content

Defines the alignment along the main axis.
It distributes extra free space leftover when the flex items on a line are inflexible,
or have reached their maximum size.








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.jc` |`justify-content`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`fs` | `flex-start`
`fe` | `flex-end`
`c` | `center`
`sb` | `space-between`
`sa` | `space-around`
`se` | `space-evenly`




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

.jc-fs { justify-content: flex-start; }
.jc-fe { justify-content: flex-end; }
.jc-c { justify-content: center; }
.jc-sb { justify-content: space-between; }
.jc-sa { justify-content: space-around; }
.jc-se { justify-content: space-evenly; }


@media (min-width: 36em) {
.s_jc-fs { justify-content: flex-start; }
.s_jc-fe { justify-content: flex-end; }
.s_jc-c { justify-content: center; }
.s_jc-sb { justify-content: space-between; }
.s_jc-sa { justify-content: space-around; }
.s_jc-se { justify-content: space-evenly; }
}


@media (min-width: 48em) {
.m_jc-fs { justify-content: flex-start; }
.m_jc-fe { justify-content: flex-end; }
.m_jc-c { justify-content: center; }
.m_jc-sb { justify-content: space-between; }
.m_jc-sa { justify-content: space-around; }
.m_jc-se { justify-content: space-evenly; }
}


@media (min-width: 62em) {
.l_jc-fs { justify-content: flex-start; }
.l_jc-fe { justify-content: flex-end; }
.l_jc-c { justify-content: center; }
.l_jc-sb { justify-content: space-between; }
.l_jc-sa { justify-content: space-around; }
.l_jc-se { justify-content: space-evenly; }
}


@media (min-width: 75em) {
.x_jc-fs { justify-content: flex-start; }
.x_jc-fe { justify-content: flex-end; }
.x_jc-c { justify-content: center; }
.x_jc-sb { justify-content: space-between; }
.x_jc-sa { justify-content: space-around; }
.x_jc-se { justify-content: space-evenly; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -