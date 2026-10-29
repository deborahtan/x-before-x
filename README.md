# x before x

My yearly list of things to do before my next birthday, live at
https://deborahtan.github.io/x-before-x/

## Each year, after my birthday

1. Archive last year's list: copy `index.html` into a folder named for that age,
   for example `31/index.html`. It stays online at `/x-before-x/31/`.
2. In `src/build.py`, change `AGE` and `BIRTHDAY` at the top, and replace the goals in `G`.
3. Run `python3 src/build.py`. That rebuilds `index.html`.
4. Commit and push. The main link stays the same.

## Updating a goal during the year

Edit its line in `G` in `src/build.py`. Each line is
`(status, category, goal, note, month)`, where status is `done`, `doing` or `todo`, and month is `YYYY-MM`.
Then run `python3 src/build.py` and push.
