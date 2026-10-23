# Exercise 20-3: Live Blog

## The exercise

Deploy the Blog project you've been working on to a live server. Make sure you set `DEBUG` to `False`, so users don't see the full Django error
pages when something goes wrong.

## Deploying is optional

This exercise has two parts. The first is required: making the Blog ready for a live server, which the build checks. The second, putting the Blog
online, is optional. You don't need to deploy it to complete the exercise, and the course doesn't depend on it.

If you do want to deploy, the steps are the same as chapter 20, step 5, with the Blog in place of the Learning Log. Note that a free PythonAnywhere
account has one web app. Deploying the Blog would replace your Learning Log site, unless you create a second free account for the Blog.

## What changed

The Blog's settings read the values that change on a live site from environment variables, as the Learning Log does:

```python
SECRET_KEY = os.environ.get("LL_SECRET_KEY", "django-insecure-blog-project-training-key-change-before-deploying")
DEBUG = os.environ.get("LL_DEBUG", "1") == "1"
ALLOWED_HOSTS = ["127.0.0.1", "localhost"] + [
    host.strip() for host in os.environ.get("LL_ALLOWED_HOSTS", "").split(",") if host.strip()
]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Locally the defaults apply, so nothing changes on your computer. A live site sets `LL_DEBUG` to `0`, which turns debug mode off, so visitors see
the friendly error pages instead of Django's detailed ones.

The error pages are `blogs/templates/404.html`, which uses the Blog's layout, and `blogs/templates/500.html`, which stands alone so it still works
when a request has failed.

## Running this exercise

In the runner, open **Ch20 · Styling and deploying**, then **Try it Yourself**, then **Exercise 20-3: Live Blog**, and click **Run**. The browser opens
at the home page, which works as before.

1. Go to `http://127.0.0.1:8000/no-such-page/`. Locally you see Django's debug page, because debug mode is on.
2. To see the friendly page, you'd need the live site, where `LL_DEBUG` is `0`. You don't need to deploy to complete the exercise.

## Testing this exercise

The three tests in `blogs/test_deploy.py` check that an unknown address uses the Blog's 404 page, that the page has its friendly message, and that
`STATIC_ROOT` is set. The build runs all 26 tests, and you should see `Ran 26 tests` and `OK`.

## Checking the settings

Django can check the settings for problems that matter on a live site. From the build folder, with the live settings set, run:

```pwsh
$env:LL_DEBUG = "0"
$env:LL_SECRET_KEY = "a-long-random-value-you-make-up"
python manage.py check --deploy
```

With `LL_DEBUG` set to `0`, the debug warning goes away. Any other warnings concern HTTPS and cookies, which the chapter 20, step 5 lesson covers.

## Output

None. This exercise changes the settings and error pages, and the tests show that they work.

## Changed files

- `blog_project/settings.py`: reads the key, debug mode and allowed addresses from the environment, and sets `STATIC_ROOT`
- `blogs/templates/404.html` (new): the Blog's friendly 404 page
- `blogs/templates/500.html` (new): the standalone error page
- `blogs/test_deploy.py` (new): tests for the error page and settings

---
