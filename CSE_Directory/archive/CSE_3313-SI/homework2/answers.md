# CSE 3313 - Homework #2 - Discrete linear Shift-Invariant Systems
- Name: Landon Moon
- ID: 1001906270

## <u>LINEARITY</u>

1.  We know that putting x<sub>1</sub> into a linear system results in the output y<sub>1</sub>; putting x<sub>2</sub> into the system results in the output y<sub>2</sub>; and putting x<sub>3</sub> into the system results in the output y<sub>3</sub>. What is the output of that linear system with the input below?

      ![Alt text](img/1.png)

      <u>ay<sub>1</sub> + by<sub>2</sub> + cy<sub>3</sub></u>

2. Test the following systems for **linearity** using the test procedure given in class and determine whether they ar elinear or non-linear.

    a. y[n] = 2x[n]+1

    1. y<sub>1</sub>[n] = 2x<sub>1</sub>[n]+1

       y<sub>2</sub>[n] = 2x<sub>2</sub>[n]+1

    2. x<sub>3</sub>[n] = ax<sub>1</sub>[n]+bx<sub>2</sub>[n]

    3. y<sub>3</sub>[n] = 2x<sub>3</sub>[n]+1

       y<sub>3</sub>[n] = 2(ax<sub>1</sub>[n]+bx<sub>2</sub>[n])+1 
       
       y<sub>3</sub>[n] = 2ax<sub>1</sub>[n] + 2bx<sub>2</sub>[n] + 1

    4. y<sub>3</sub>[n] = ay<sub>1</sub>[n]+by<sub>2</sub>[n] 

       y<sub>3</sub>[n] = a(2x<sub>1</sub>[n]+1)+b(2x<sub>2</sub>[n]+1) 

       y<sub>3</sub>[n] = 2ax<sub>1</sub>[n]+2bx<sub>2</sub>[n]+a+b

    5. 2ax<sub>1</sub>[n]+2bx<sub>2</sub>[n]+a+b  /=  2ax<sub>1</sub>[n] + 2bx<sub>2</sub>[n] + 1

       <u>NO, the system is not LINEAR</u>

    b. y[n] = (1/2)x[n] - (1/4)x[n-1]

    1. y<sub>1</sub>[n] = (1/2)x<sub>1</sub>[n] - (1/4)x<sub>1</sub>[n-1]

       y<sub>2</sub>[n] = (1/2)x<sub>2</sub>[n] - (1/4)x<sub>2</sub>[n-1]

    2. x<sub>3</sub>[n] = ax<sub>1</sub>[n]+bx<sub>2</sub>[n]

    3. y<sub>3</sub>[n] = (1/2)x<sub>3</sub>[n] - (1/4)x<sub>3</sub>[n-1]

       y<sub>3</sub>[n] = (1/2)(ax<sub>1</sub>[n]+bx<sub>2</sub>[n]) - (1/4)(ax<sub>1</sub>[n-1]+bx<sub>2</sub>[n-1])

    4. y<sub>3</sub>[n] = ay<sub>1</sub>[n] + by<sub>2</sub>[n] 

       y<sub>3</sub>[n] = a((1/2)x<sub>1</sub>[n]-(1/4)x<sub>1</sub>[n-1]) + b((1/2)x<sub>2</sub>[n] - (1/4)x<sub>2</sub>[n-1])

       y<sub>3</sub>[n] = (1/2)(ax<sub>1</sub>[n]+bx<sub>2</sub>[n]) - (1/4)(ax<sub>1</sub>[n-1]+bx<sub>2</sub>[n-1])

    5. (1/2)(ax<sub>1</sub>[n]+bx<sub>2</sub>[n]) - (1/4)(ax<sub>1</sub>[n-1]+bx<sub>2</sub>[n-1])  ==  (1/2)(ax<sub>1</sub>[n]+bx<sub>2</sub>[n]) - (1/4)(ax<sub>1</sub>[n-1]+bx<sub>2</sub>[n-1])

       <u>YES, the system is LINEAR</u>

    c. y[n] = x[2n]

    1. y<sub>1</sub>[n] = x<sub>1</sub>[2n]

       y<sub>2</sub>[n] = x<sub>2</sub>[2n]

    2. x<sub>3</sub>[n] = ax<sub>1</sub>[n]+bx<sub>2</sub>[n]

    3. y<sub>3</sub>[n] = x<sub>3</sub>[2n]

       y<sub>3</sub>[n] = ax<sub>1</sub>[2n]+bx<sub>2</sub>[2n]

    4. y<sub>3</sub>[n] = ay<sub>1</sub>[n]+by<sub>2</sub>[n] 

       y<sub>3</sub>[n] = ax<sub>1</sub>[2n]+bx<sub>2</sub>[2n]

    5. ax<sub>1</sub>[2n]+bx<sub>2</sub>[2n]  ==  ax<sub>1</sub>[2n]+bx<sub>2</sub>[2n]

       <u>YES, the system is LINEAR</u>


<div style="page-break-after: always"></div>

## <u>SHIFT-INVARIANCE</u>

3. We know that putting x into a shift-invarient system results in the output y. What is the output of that shift-invariant system with the input given below?

    ![alt text](img/3.png)

    <u>The result is y[n-2]. This is due to the shift invarience condition where if x[n]->y[n] then x[n-n<sub>0</sub>]->y[n-n<sub>0</sub>]</u>

4. Test the above systems in problems 2z, 2b, 2c for shift-invariance using the test procedure given in class and determine whether they are shift-invarient or not shift-invarient

    a. y[n] = 2x[n]+1

    1. y[n - n<sub>0</sub>] = 2x[n - n<sub>0</sub>]+1

    2. y<sub>1</sub>[n - n<sub>0</sub>] = 2x[n - n<sub>0</sub>]+1

    3. 2x[n - n<sub>0</sub>]+1  ==  2x[n - n<sub>0</sub>]+1

       <u>YES, the system is SHIFT-INVARIENT</u>

    b. y[n] = (1/2)x[n] - (1/4)x[n-1]

    1. y[n - n<sub>0</sub>] = (1/2)x[n - n<sub>0</sub>] - (1/4)x[n-1 - n<sub>0</sub>]

    2. y[n - n<sub>0</sub>] = (1/2)x[n - n<sub>0</sub>] - (1/4)x[n-n<sub>0</sub> - 1]

    3. (1/2)x[n - n<sub>0</sub>] - (1/4)x[n-1 - n<sub>0</sub>]  ==  (1/2)x[n - n<sub>0</sub>] - (1/4)x[n-n<sub>0</sub> - 1]

       <u>YES, the system is SHIFT-INVARIENT</u>

    c. y[n] = x[2n]

    1. y[n - n<sub>0</sub>] = x[2n - n<sub>0</sub>]

    2. y[n - n<sub>0</sub>] = x[2(n-n<sub>0</sub>)]

       y[n - n<sub>0</sub>] = x[2n - 2n<sub>0</sub>]

    3. x[2n - n<sub>0</sub>]  /=  x[2n - 2n<sub>0</sub>]

       <u>NO, the system is not SHIFT-INVARIENT</u>

<div style="page-break-after: always"></div>

## <u>LINEAR SHIFT-INVARIENT SYSTEMS</u>

5. If we know that x into the sytem results in an output of y, what is the output of the linear shift-invariant (LSI) system below with the given input?

    ![alt text](img/5.png)

    <u>ay[n-2] + by[n+5]</u>

6. If we know that a delta function (𝛿[𝑛]) as an input to an LSI system results in an output of h[n], what is the output of the following LSI system?

    ![alt text](img/6.png)

    <u>a<sub>0</sub>h[𝑛] + a<sub>1</sub>h[𝑛-1] + a<sub>2</sub>h[𝑛-2]</u>

7. If we know that a delta function (𝛿[𝑛]) as an input to an LSI system results in an output of h[n], what is the output of the following LSI system?

    ![alt text](img/7.png)

    <u>a<sub>0</sub>h[n-0] + a<sub>1</sub>h[n-1] + a<sub>2</sub>h[n-2]</u>

8. If we know that a delta function (𝛿[𝑛]) as an input to an LSI system results in an output of h[n], what is the output of the following LSI system?

    ![alt text](img/8.png)

    <u>a<sub>-∞</sub>h[n - (-∞)] + a<sub>-∞+1</sub>h[n - (-∞+1)] + ... + a<sub>∞-1</sub>h[n - (∞-1)] + a<sub>∞</sub>h[n - (∞)]</u>

     or <u>Σ<sup>∞</sup><sub>k=-∞</sub> a<sub>k</sub>h[n - k]</u>

9. Write the decomposition of a infinitely long general sequence x[n] into a sum of weighted and shifted delta functions (𝛿[𝑛]).

    <u>x[n]</u>

10. If we know that a delta function ( 𝛿[𝑛] ) as an input to an LSI system results in an output of ℎ[𝑛],what is the output of an LSI system with your decomposed general sequence from question 9 as the input?

    <u>TODO</u>
