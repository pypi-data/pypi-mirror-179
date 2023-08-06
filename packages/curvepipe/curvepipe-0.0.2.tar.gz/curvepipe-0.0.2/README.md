CurvePipe is designed to efficiently manipulate sets of curves without using Dataframes or Arrays.

You can transform curves in a Java stream-like syntax.

The following command 
- scales and adds an offset to the x-values of the curve 
- computes the logarithm for each y-value

```python
cpipe = CurvePipe(x=[0, 0.1, 0.2, 0.3, 0.4], y=[1, 2, 3, 3, 4])\
    .scale_x(2)\
    .offset_x(20.1) \
    .transform_y(lambda v: math.log(v))
```
The result is a CurvePipe-Object containing the transformed curve. You can acces the x- and y- values via the attributes x and y.
