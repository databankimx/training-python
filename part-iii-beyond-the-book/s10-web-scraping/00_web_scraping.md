## Web Scraping

> Source Credit
> 
> The lessons in this topic are based on the
> [Real Python Web Scraping Tutorial](https://realpython.com/python-web-scraping-practical-introduction/) and uses the practice 
> scraping site they provide at
> [http://olympus.realpython.org](http://olympus.realpython.org)

---

### What is web scraping?

In its simplest form, web scraping is the process of collecting data 
from the Internet and processing it to yield meaningful results.

Examples include:

* **Market Research**: For example, you might want to get comparative
  pricing for a competitor's products.
* **Content Aggregation**: You might be gathering headlines and links 
  from a variety of news sources in order to produce a search engine for
  topical articles.
* **User Sentiment Analysis**: Collecting feedback notes from Twitter,
  Reddit, or other sites can be useful to gauge user response to a
  marketing campaign.

---

### Is that ethical?

Web scraping (in general) lies in a bit of an ethical gray area. In
order to perform a web scrape, you are not only accumulating data that 
someone else assembled. You're also consuming resources on their web
server(s).

Many websites (including the ones developed by my team) include code
specifically meant to thwart web scraping bots.

It isn't illegal, and it is in high demand, but it's up to you as a 
developer to identify where you draw the line ethically.

Some folks are making their entire annual income delivering web scraping
projects. Others refuse to do it at all.

At the end of the day, I see web scraping as a skill set, wholly
distinct from the ethical questions arising from a specific 
implementation of it.

---

### Topics

We'll review three main topics in this section:

* Basic scraping using standard library tools
* HTML parsing using BeautifulSoup
* HTML interaction using MechanicalSoup

---
