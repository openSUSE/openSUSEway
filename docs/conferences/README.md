# Conference Talks

These directories contain sources for the openSUSEwa presentations.

Presentations use: [reveal.js](https://revealjs.com/) is an open source HTML presentation framework.

You can reproduce presentations:

```sh
git clone https://github.com/hakimel/reveal.js

# copy needed md file to the reveal.js dir
cp oSC24/openSUSEway.md reveal.js/

```

Change `index.html` to use needed Markdown file:

```js
		<div class="reveal">
			<div class="slides">
				<section data-markdown="openSUSEway.md"
					data-separator="^\n\n\n"
					data-separator-vertical="^\n\n"
					data-separator-notes="^Note:"
					data-charset="iso-8859-15">
				</section>
			</div>
		</div>
```

Run reveal.js locally and see/present:

```sh
cd reveal.js

npm install
npm start
```

## Themes

There is an old (and gold) openSUSE theme for the reveal.js:

```sh
git clone git@github.com:krig/opensuse-presentation-template.git
cp -R -n opensuse-presentation-template/* reveal.js/
```

Add theme to the `index.html`:

```js
		<link rel="stylesheet" href="dist/reset.css">
		<link rel="stylesheet" href="dist/reveal.css">
		<link rel="stylesheet" href="dist/theme/black.css">
		<link rel="stylesheet" href="css/theme/opensuse.css">
    	<link rel="stylesheet" href="lib/css/github.css">
```

## Export to pdf

See [PDF Export](https://revealjs.com/pdf-export/)