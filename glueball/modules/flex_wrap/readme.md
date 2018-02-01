# module: Flex wrap

Defines whether the flex items are forced in a single line or can be flowed into multiple lines.
If set to multiple lines, it also defines the cross-axis which determines the direction new lines are stacked in.








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.fw` |`flex-wrap`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`n` | `nowrap`
`w` | `wrap`
`wr` | `wrap-reverse`




## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|






## CSS rules
```css

.fw-n { flex-wrap: nowrap; }
.fw-w { flex-wrap: wrap; }
.fw-wr { flex-wrap: wrap-reverse; }

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -