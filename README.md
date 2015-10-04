# ps.py

A simple example in Python about how to read /proc filesystem and create a very simple process list.

Sample Output :
```
[root@fdea24ee5ada ~]# ./processList.py
  > [0] init  (Childs: 2)
    > [1] (bash)  (Childs: 1)
      > [26] (bash)  (Childs: 1)
        > [81] (bash)  (Childs: 1)
          > [94] (bash)  (Childs: 2)
            > [186] (login)  (Childs: 0)
            > [250] (login)  (Childs: 1)
              > [251] (bash)  (Childs: 1)
                > [271] (ping)  (Childs: 0)
    > [327] (bash)  (Childs: 1)
      > [349] (processList.py)  (Childs: 0)
```

This script is just for educational purpose. Normally you wouldn't this kind of an application in a running Linux environment unless you delete ```ps``` accidentally.
