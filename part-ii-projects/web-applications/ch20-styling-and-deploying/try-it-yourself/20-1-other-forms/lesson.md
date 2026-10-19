# Exercise 20-1: Other Forms

## The exercise

We applied Bootstrap's styles to the login page. Make similar changes to the rest of the form-based pages, including `new_topic`, `new_entry`,
`edit_entry`, and `register`.

## About this exercise

In the course project, these pages are already styled. Chapter 20, step 3 (Styled Pages) made the change to all four, using `bootstrap_form`
and `bootstrap_button`. The lesson for that step shows the code, and this exercise points there so you can compare your version against it.

The pattern is the same on every form:

```html
{% load django_bootstrap5 %}

<form method="post" action="{% url 'learning_logs:new_topic' %}">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% bootstrap_button button_type="submit" content="Add topic" %}
</form>
```

`bootstrap_form` draws every field in Bootstrap's style, including its error messages. `bootstrap_button` draws the submit button. The
`{% csrf_token %}` line is still needed, because it protects the form from forged requests.

## Running this exercise

1. Open the step 3 lesson, "Styled Pages", and look at the templates it lists: `new_topic.html`, `new_entry.html`, `edit_entry.html`, and the
   `register.html` template in the accounts app.
2. Run **Ch20 · Styling and deploying → Styled Pages → Run**, sign in, and open each form. Each should look like the login page: Bootstrap
   fields, and a primary button.
3. To check your own version, make a change to a form template, such as the button's text, and reload the page to see the change.

## Solution

There's no separate code for this exercise. The solution is the four templates from chapter 20, step 3, which are in the course project.

## Output

None. This exercise changes the templates, which the step 3 lesson already shows.
