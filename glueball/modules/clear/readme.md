# module: Clear

Options for repeating background images



## Basic styles

The basic styles do not depend on the provided values.
They do however adhere to the breakpoints and pseudo selectors.

```css

.clear-fix { *zoom: 1; }

.clear-fix:before, .c-fix:after { content: " "; display: table; }

.clear-fix:after { clear: both; }

```






## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.clear` |`clear`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`l` | `left`
`r` | `right`
`b` | `bottom`
`n` | `none`




## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|






## CSS rules
```css

.clear-fix { *zoom: 1; }
.clear-fix:before, .c-fix:after { content: " "; display: table; }
.clear-fix:after { clear: both; }
.clear-l { clear: left; }
.clear-r { clear: right; }
.clear-b { clear: bottom; }
.clear-n { clear: none; }

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -