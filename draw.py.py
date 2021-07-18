{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "194dcfc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9*1=9\n",
      "9*2=18\n",
      "9*3=27\n",
      "9*4=36\n",
      "9*5=45\n",
      "9*6=54\n",
      "9*7=63\n",
      "9*8=72\n",
      "9*9=81\n"
     ]
    }
   ],
   "source": [
    "a= 9\n",
    "b=1\n",
    "c=2\n",
    "d=3\n",
    "e=4\n",
    "f=5\n",
    "g=6\n",
    "h=7\n",
    "i=8\n",
    "j=9\n",
    "print('{0}*{1}={2}'.format(a,b,a*b))\n",
    "print('{0}*{1}={2}'.format(a,c,a*c))\n",
    "print('{0}*{1}={2}'.format(a,d,a*d))\n",
    "print('{0}*{1}={2}'.format(a,e,a*e))\n",
    "print('{0}*{1}={2}'.format(a,f,a*f))\n",
    "print('{0}*{1}={2}'.format(a,g,a*g))\n",
    "print('{0}*{1}={2}'.format(a,h,a*h))\n",
    "print('{0}*{1}={2}'.format(a,i,a*i))\n",
    "print('{0}*{1}={2}'.format(a,j,a*j))\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "15299731",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5X^2 + 3X + 7=0\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "b=3\n",
    "c=7\n",
    "\n",
    "print('{a}X^2 + {b}X + {c}=0'.format(a=a,b=b,c=c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "fda5edc9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nhap vao so thu nhat:5\n",
      "<class 'int'>\n",
      "Nhap vao so thu hai:1\n",
      "5+1=6\n",
      "5-1=4\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Nhap vao so thu nhat:\"))\n",
    "print(type(a))\n",
    "\n",
    "b=int(input(\"Nhap vao so thu hai:\"))\n",
    "\n",
    "sum=a+b\n",
    "sub=a-b\n",
    "\n",
    "print(\"{a}+{b}={c}\".format(a=a,b=b,c=sum))\n",
    "print(\"{a}-{b}={d}\".format(a=a,b=b,d=sub))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4898493",
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "t=turtle.Turtle()\n",
    "radius=int(input(\"ban kinh hinh tron=\"))\n",
    "color=input(\"mau cua vien hinh tron=\")\n",
    "\n",
    "t.pencolor(color)\n",
    "t.circle(radius)\n",
    "\n",
    "turtle.done"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b36193e6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
