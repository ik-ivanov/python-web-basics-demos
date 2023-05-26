## BLACK MAGIC (how to find and replace with regular expressions with back reference)
###### _Disclaimer: Generated with GPT4._

```regexp
RE for find: ="/static/([^"]+)"

RE for replace: ="{% static '$1' %}"
```

## Explanation

1. Regular expression pattern for "Find":

```
href="/staticfiles/([^"]+)"
```

- `href="`: This part of the pattern matches the exact string `href="`.
- `/staticfiles/`: This part matches the exact string `/staticfiles/`, which is the prefix of the paths you want to replace.
- `(` and `)`: These parentheses are used to define a capturing group. The content matched inside the parentheses will be captured and can be used in the replacement string.
- `[^"]`: This is a character class that matches any character except the double quote (`"`). The `^` inside the brackets negates the character class, so it matches anything but the specified character.
- `+`: This is a quantifier that means "one or more" of the preceding element. In this case, it means one or more characters that are not double quotes.
- `"`: This part of the pattern matches the closing double quote.

So, the pattern matches an `href` attribute that starts with `/staticfiles/` and captures the rest of the path until the closing double quote.

2. Replacement string:

```
href="{% static '$1' %}"
```

- `href="{% static '`: This part of the replacement string is a fixed text that will replace the matched `href="/staticfiles/` part.
- `$1`: This is a backreference to the first capturing group in the regular expression pattern. It will be replaced with the content captured by the group (i.e., the rest of the path after `/staticfiles/`).
- `' %}`: This part of the replacement string is a fixed text that will be added after the backreference, closing the `{% static %}` tag.

The replacement string uses the captured group from the regular expression pattern to construct the new `href` attribute with the desired format.