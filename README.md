# Efficient Algorithms — Exam Trainer

A self-study flashcard app for the **TUM INHN0008 "Fundamentals of Algorithms and Data Structures"** bonus tests (Bonus Tests 1–4). Every exam problem is a flip-card: the original exam **question** on the front, the **sample solution** on the back.

## Features

- **Authentic exam images** — questions cropped from the actual question sheets; solutions from the sample-solution PDFs (real notation, red-black trees, heaps, MST graphs, DP tables).
- **Version A / Version B** split into separate cards.
- **Multiple-choice & matching** split into one card per sub-question; the full question (statement + option boxes) is shown, with the answer on the back.
- **Filter** by test, question type (design & analyse / construction & trace / multiple choice / matching), and topic.
- **Progress tracking** (known / review) saved in the browser, shuffle, list view, light/dark themes, keyboard shortcuts.

## Run it

### Plain browser
Open `algorithms-study-app.html` directly — it works offline (keep the `img/` folder beside it). Needs internet only for the web fonts.

### Docker
```bash
docker compose up -d --build
```
Then open **http://localhost:8080**. Change the port via the `"8080:80"` line in `docker-compose.yml`.

```bash
docker compose stop     # pause
docker compose down     # stop & remove
```

## Structure

```
algorithms-study-app.html   # the whole app (HTML/CSS/JS in one file)
img/                        # cropped question & solution images
Dockerfile / default.conf   # nginx static hosting
docker-compose.yml
```

## Notes

- Card data (answers, topics, types) lives in the `IMG` and `MCQ` arrays inside the HTML.
- Image URLs carry a `?v=N` cache-busting param (`IMGV` in the script) — bump it when regenerating images.
