# Daily Practice

Learning data structures and algorithms in Python, one problem a day, starting from zero.

- [ROADMAP.md](ROADMAP.md): 60 beginner problems in order, grouped by topic
- [PROGRESS.md](PROGRESS.md): what I've solved so far

## Layout

```
problems/
  2026-11-10-<problem-slug>/
    README.md      problem statement, my approach, complexity, what I learned
    solution.py    my accepted solution
```

## Daily routine

```bash
py new.py                 # set up the next roadmap problem
# solve it on leetcode.com, paste the accepted code into solution.py,
# fill in "My approach" and "What I learned" in the README
git add -A
git commit -m "Solve <problem name>"
git push
```

Other options: `py new.py --daily` uses LeetCode's daily problem, `py new.py two-sum` sets up a specific problem.
