# Daily Practice

One problem a day: my solutions, approach and notes. Progress log: [PROGRESS.md](PROGRESS.md).

## Layout

```
problems/
  2026-11-10-<problem-slug>/
    README.md      problem statement, my approach, complexity, what I learned
    solution.py    my accepted solution
```

## Daily routine

```bash
py new.py                 # scaffold today's LeetCode daily problem
# solve it on leetcode.com, paste the accepted code into the solution file,
# fill in "My approach" and "Complexity" in the README
git add -A
git commit -m "Solve <problem name>"
git push
```

Other options: `py new.py two-sum` scaffolds a specific problem, and `--lang java|cpp|js` picks the language.
