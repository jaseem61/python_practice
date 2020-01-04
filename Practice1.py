{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FIFO page replacement algorithm\n",
      "Enter the number of pages:8\n",
      "Enter the frame size:3\n",
      "Enter the page00\n",
      "Enter the page11\n",
      "Enter the page22\n",
      "Enter the page33\n",
      "Enter the page44\n",
      "Enter the page55\n",
      "Enter the page66\n",
      "Enter the page77\n",
      "The frames in each stage is as shown below:\n",
      "[-1. -1. -1.]\n",
      "[ 0. -1. -1.]\n",
      "[ 0.  1. -1.]\n",
      "[0. 1. 2.]\n",
      "[3. 1. 2.]\n",
      "[3. 4. 2.]\n",
      "[3. 4. 5.]\n",
      "[6. 4. 5.]\n",
      "The number of page fault is:14\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "print(\"FIFO page replacement algorithm\")\n",
    "p=input(\"Enter the number of pages:\")\n",
    "nf=input(\"Enter the frame size:\")\n",
    "p=int(p)\n",
    "nf=int(nf)\n",
    "fault=0\n",
    "n=0\n",
    "page=np.ones((p))\n",
    "frame=np.ones((nf))\n",
    "for x in range(nf):\n",
    "    frame[x]=-1\n",
    "for x in range(0,p):\n",
    "    page[x]=input(\"Enter the page\"+str(x))\n",
    "print(\"The frames in each stage is as shown below:\")\n",
    "for x in range(p):\n",
    "    print(frame,sep='/n')\n",
    "    for y in range(nf):\n",
    "        if(frame[y]==page[x]):\n",
    "            break\n",
    "        elif(frame[y]==-1):\n",
    "            frame[y]=page[x]\n",
    "            fault+=1\n",
    "            break\n",
    "        else:\n",
    "            frame[x%3]=page[x]\n",
    "            fault+=1\n",
    "        \n",
    "print(\"The number of page fault is:\"+str(fault))\n",
    "            \n",
    "            \n",
    "            \n",
    "            \n",
    "        \n",
    "                  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
