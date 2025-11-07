### Algorithm
Given an array $M$ of length $m$, and $k$ independent hash functions $h_1,\ldots,h_k:U\to\{1,\ldots,m\}$:
```
proc init(M):
	for i in (1, m):
		M[i] = 0

proc add(M, x):
    for i in (1, k):
        M[h_i(x)] = 1

proc query(M, x):
    for i in (i, k):
        if M[h_i(x)] == 0
            return FALSE
    
    return TRUE
```
-----------------------------------------------------------------------
### Correctness
$P[\text{query}(L, x)=\text{TRUE}\ |\ x\in X]=1$
$P[\text{query}(L,x)=\text{TRUE}\ |\ x\notin L]\ge0$
$P[\text{query}(L,x)=\text{FALSE}\ |\ x\in L]=0$
$P[\text{query}(L, x)=\text{FALSE}\ |\ x\notin L]\ge0$
- - -
### Time Complexity
add:    O(k)
query:  O(k)
- - -
### Space complexity
To minimize the chance of false positive:
$$k=k_\text{min}=\dfrac mn\ln(2)$$
which gives space complexity of:
$$n\log_2(e)\log_2\left(\dfrac1\epsilon\right)$$
where:
$$\epsilon=\left(\dfrac12\right)^{k_\min}$$
```ad-Dimostrazione
title: Minimize false positive chance/rate
Define $\rho$ as the fraction of bits of $M$ that are $=0$.

$$\begin{align}
P[M[h_i(x)]=1]&=1-P[M[h_i(x)]=0]=\\
&=1-\rho\quad\forall i
\end{align}$$

Using independence:

$$P[M[h_1(x)]=1,\ldots M[h_k(x)]=1]=(1-\rho)^k$$

We also define the probability that a specific element of $M$ is $0$, given $k$ hash functions and $n$ values inserted in $M$:

$$P[M[j]=0]=p'=\left(1-\dfrac1m\right)^{kn}$$

Since $E[\rho]=p'$:

$$\begin{align}
(1-p)^k\approx(1-p')^k&=\left(1-\left(1-\dfrac1m\right)^{kn}\right)^k=\\
&=\left(1-\left(e^{-\frac1m}\right)^{kn}\right)^k=\\
&=\left(1-e^{-\frac{kn}m}\right)^k)=\\
&=e^{k\ln(1-e^{-\frac{kn}m})}
\end{align}$$

Which gives:

$$\begin{align}
k_\min=\dfrac mn\ln(2)\implies f(k_\min)&=\left(\dfrac12\right)^{k_\min}=\\
&=2^{-\frac mn\ln(2)}=\\
&=(2^{\ln(2)})^{-\frac mn}\approx 0.6185^{\frac mn}
\end{align}$$
```

Are there significantly more space-efficient data structure than the bloom filter? Let's see what's the best we can hope for:
```ad-Dimostrazione
title: Lower bound
Assume a generic data structure with $m$ bit representation.

Let $Y(M)$ be the set of elements of $U$ such that $M$ answers YES to:

$$Y(M)=\{u\in U:M[u]=\text{YES}\}$$ 

For any $X$ represented by $M$, $X\subseteq Y(M)$, because there are no false negatives.
We allow for at most for a false positive rate $\epsilon$ for elements in $U\smallsetminus X$.
Thus, $Y(M)$ contains at most $\epsilon(u-n)$ elements more than $X$.

![[]]

In conclusion:
$$|Y(M)|\le n+\epsilon(u-n)$$

Also, $M$ can not represent more than $\dbinom{n+\epsilon(u-n)}n$ subsets $X$ since they all need to be contained in $Y(M)$.
There are also $2^m$ choices of $m$-length bit string $M$ and each represents at most $\dbinom{n+\epsilon(u-n)}n$ sets $X$.

So, the data structure cannot represent more sets than
$$2^m\dbinom{n+\epsilon(u-n)}n$$
But it needs to represent all of the $dbinom un$ sets $X$, so:
$$2^m\dbinom{n+\epsilon(u-n)}n\ge\dbinom un$$

$$\begin{align}
m&\ge\log_2\left(\dfrac{\dbinom un}{\dbinom{n+\epsilon(u-n)}n}\right)\approx\\
&\approx\log_2\left(\dfrac{\dbinom un}{\dbinom{\epsilon u}n}\right)\approx\\
&\approx\log_2\left(\dfrac{\dfrac{u^n}{n!}}{\dfrac{(\epsilon u)^n}{n!}}\right)=\log_2\left(\left(\dfrac1\epsilon\right)^n\right)=n\log_2\left(\dfrac1\epsilon\right)
\end{align}$$
```
Since the Bloom filter requires
$$n\log_2(e)\log_2\left(\dfrac1\epsilon\right)$$
We see that it's only a factor of $\log_2(e)\approx1.44$ of the lower bound.
- - -