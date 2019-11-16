{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "x = 'radar'\n",
    "p = ''\n",
    "\n",
    "for i in x:\n",
    "    p = i + p\n",
    "    if x==p:\n",
    "        print('True')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "17 is a prime number\n"
     ]
    }
   ],
   "source": [
    "num = 17\n",
    "\n",
    "if num > 1:\n",
    "    for i in range(2, num//2):\n",
    "        if num % i == 0:\n",
    "            print(num, 'is not a prime number')\n",
    "            break\n",
    "    else:\n",
    "        print(num, 'is a prime number')\n",
    "else:\n",
    "    print(num, 'is not a prime number')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Prime number checker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "142913828922"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def Primes(n):\n",
    "    sum = 0\n",
    "    sieve = [True] * (n+1)\n",
    "    for p in range(2, n):\n",
    "        if sieve[p]:\n",
    "            sum += p \n",
    "            for i in range(p*p, n, p):\n",
    "                sieve[i] = False\n",
    "    return sum\n",
    "\n",
    "Primes(2000000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0\n",
      "31875000.0\n"
     ]
    }
   ],
   "source": [
    "for a in range(1000):\n",
    "    for b in range(a+1, 999):\n",
    "        c = math.sqrt(a*a + b*b)    \n",
    "        if a + b + c == 1000:\n",
    "            product = a*b*c\n",
    "            print(product)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Problem 11"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# (a) Penguins (65 to 75cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1440.0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = (.34 + .14) * 3000\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (b) P(height<60cm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.16"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P = (.16*3000)/3000\n",
    "P"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
