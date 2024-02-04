# CSE 3313 - Homework #1 - Sampling and Nyquist
- Name: Landon Moon
- ID: 1001906270

## A
Determine the Sampling Frequency (f<sub>s</sub>) from the Sampling Period


1.  - T<sub>s</sub> = 2 sec
    - f<sub>s</sub> = <u>0.5 samples/sec</u>

<br>

2.  - T<sub>s</sub> = 0.1 sec
    - f<sub>s</sub> = <u>10 samples/sec</u>
    
<br>

3.  - T<sub>s</sub> = 1 msec
    - f<sub>s</sub> = <u>1,000 samples/sec</u>
    
<br>

4.  - T<sub>s</sub> = 5 μsec
    - f<sub>s</sub> = <u>200,000 samples/sec</u>

<div style="page-break-after: always"></div>

## B & C
B: Determine the bandwidth of the following real signals from their frequency spectrum?

C: What are the Nyquist Sampling Frequencies for the three signal spectra in part B?

1. 
![Alt text](img/B1.png)

B. Bandwidth = <u>10Hz</u>

C. Nyquist Sampling Frequency = <u>20Hz</u>

2. 
![Alt text](img/B2.png)

B. Bandwidth = <u>5Hz</u>

C. Nyquist Sampling Frequency = <u>10Hz</u>

3. 
![Alt text](img/B3.png)

B. Bandwidth = <u>1kHz</u>

C. Nyquist Sampling Frequency = <u>2kHz</u>


## D
You have a system that can sample an analog signal into discrete samples at a sampling frequency of 100 kHz.

1.  - Q: What is the maximum signal bandwidth you can sample without loss of signal information and allow for perfect signal reconstruction?
    - A: <u>The maximum signal bandwidth allowed would be 50 kHz. This is because the Nyquist-Shannon Sampling Theorem says that a signal can be completely reconstructed if the sample frequency is twice the bandwidth. 50 kHz * 2 = 100 kHz.</u>

<br>

2.  - Q: If the signal is real and has a minimum frequency of 0 Hz, what is the largest frequency component that the signal can contain and still meet the Nyquist sampling criteria?
    - A: <u>Similar to the answer above, the largest frequency component can be up to 50 kHz. With a minimum of 0 Hz and a maximum of 50 kHz the bandwidth would be 50 kHz which implies a minimum Nyquist Sampling Frequency of 100 kHz.</u>
