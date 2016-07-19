# 4 - Positioning And Layout With CSS
============
## Positioning
* **Static**
	```css
	position: static;
	```
* **Relative**
CSS:
 * **Absolute**
	```css
	position: absolute;
	```
* **Fixed**
This stays in place regardless of scrolling
	```css
	position: fixed;
	```
## Other CSS traits
These specify the offsets:

	```css
	element{
	    left|right|top|bottom: 25px;
	    float: left|right;
	    clear: left|right|both;
	    }
	```

_This makes the float reserve the specified zone instead of sharing._

## Layering
`z-index: [NUM];`
_This specifies which layer it should be sorted as_

==============

# 5 - Links
===========

## Page Anchors

===========

## E-mail Links
Directly open default email client
```html
<a href="maito:adam@mail.com?subject=Web mail">Email us!</a>
```

============

## Styling Links
```css
	a:link {
	    color: green;
	    }
	a:visited {
	    /* This is visited */
	    }
	a:hover {
	    /* This is mouse-over */
	    }
	a:active {
	    /* This is when held or loading */
	    }       
```

===========

## Adding Images

```html
<img src="http://purple.com/sample.png" Alt="A sample image from purple.com">
```

============

## Image Maps
```html
<img src="folder/image.png" width="200" height="150" usemap="#Image ID">
<map name="Image ID" id="Image ID">
<area title="Access Google." shape="rect" coords="x,y,x,y" href="http://google.com">
<area title="Access Yahoo." shape="rect" coords="x,y,x,y" href="http://yahoo.com">
<area title="Access Bing." shape="circle" coords="x,y,r" href="http://bing.com">
</map>
```

============

# 6 - Tables

**border-style**:

* dashed
* dotted
* double
* groove
* hidden
* inset
* outset
* solid
* ridge

```css
table {
	border: solid 2px #000;
	}
```

**border-collapse** : remove border-caused spacing
**border-spacing** : (measured in px)


**Alternating styles**:
```css
tr:nth:even {
	backgound: grey;
	}
```

============

# 7 - Forms
```html
<form action="scripts/sample.py" method="POST" name="moo" ID="mmoooo">
 </form>
```
***method**\* either ***GET**\* or ***POST***
The ***GET*** method appends a url-encoded string to the target url to send the data

The ***POST*** method uses an encoded string sent in the header

* More secure
* Enctype=multitype(or plaintext)

***<label>***
***<fieldset>***
***remember that we access via***
http://sftweb01/Lastname/Pacific
aka
http://sftweb01/Randall/Pacific
## Form Controls
[Input][1]
<input value="Input"></input>
<input type="password"></input>
<input type="file"></input>
<input type="button" value="exec script"></input>
<input type="checkbox" name="colors" value="blue" checked> Blue!</input>
<input type="checkbox" name="colors" value="green"> Green!</input>
<input type="radio" name="pets" value="cats" checked> Cats!</input>
<input type="radio" name="pets" value="dogs"> Dogs!</input>

<button>Button</button>

<select selected="Kitty">
<option value="meow">Kitty</option>
<option value="bark">Doggie</option>
</select>

[TextArea][2]
<textarea>TextArea</textarea>

***Attributes:***

* type
* name
* value
* ID (Optional)

### Form Controls: Input
***Attributes:***

* size (# of chars)
* maxlength (# of chars)
* value (set the default)
* autofocus
* autocomplete
* placeholder
* required
* accesskey (hotkey)
* tabindex
* ID (Optional)
* type (text,password,file,submit,reset)
* New types in HTML5
	* color
	* date
	* time
	* month
	* email
	* url
	* tel
	* search
* pattern (a regex pattern of what is allowed)
* datalist

### Form Controls: TextArea
***Attributes:***

* value (set the default)
* cols (when to wordwrap)
* rows
* tabindex
* ID (Optional)

[1]:	#form-controls:-input
[2]:	#form-controls:-textarea
